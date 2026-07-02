/**
 * Nachhaker – MVP-Backend (Cloudflare Worker + D1)
 *
 * HTTP-API:
 *   POST /api/waitlist            { email }                     – öffentlich
 *   POST /api/invoices            { ...invoice }                – API-Key
 *   GET  /api/invoices?owner=...                                – API-Key
 *   POST /api/invoices/:id/paid                                 – API-Key
 *
 * Cron (täglich): findet überfällige, offene Rechnungen, ermittelt die nächste
 * Eskalationsstufe und verschickt die passende deutsche E-Mail (Zahlungs-
 * mehrere freundliche Erinnerungen). Bei status = 'bezahlt' stoppt die Kette automatisch.
 */

const CORS = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Methods": "GET,POST,OPTIONS",
  "Access-Control-Allow-Headers": "Content-Type,X-Api-Key",
};

const json = (data, status = 200) =>
  new Response(JSON.stringify(data), {
    status,
    headers: { "Content-Type": "application/json", ...CORS },
  });

// --- Eskalationsstufen: Tage-nach-Fälligkeit + Textgenerator ---------------
const TONE = {
  freundlich: { gruss: "Hallo", close: "Ganz herzliche Grüße" },
  neutral: { gruss: "Guten Tag", close: "Freundliche Grüße" },
  bestimmt: { gruss: "Sehr geehrte Damen und Herren", close: "Mit freundlichen Grüßen" },
};

const STUFEN = [
  { nr: 1, label: "Zahlungserinnerung", nachTagen: 3 },
  { nr: 2, label: "2. Erinnerung", nachTagen: 7 },
  { nr: 3, label: "3. Erinnerung", nachTagen: 14 },
  { nr: 4, label: "Freundliche Nachfrage", nachTagen: 30 },
];

const euro = (cent) =>
  new Intl.NumberFormat("de-DE", { style: "currency", currency: "EUR" }).format((cent || 0) / 100);
const fmt = (iso) => {
  const d = new Date(iso);
  return d.toLocaleDateString("de-DE", { day: "2-digit", month: "2-digit", year: "numeric" });
};
const addDays = (iso, n) => {
  const d = new Date(iso);
  d.setDate(d.getDate() + n);
  return d.toISOString().slice(0, 10);
};

function buildMail(inv, stufeNr) {
  const t = TONE[inv.ton] || TONE.neutral;
  const b = euro(inv.betrag_cent);
  const link = inv.zahllink || "[Zahllink]";
  const nr = inv.rechnung_nr;
  const k = inv.kunde;
  const a = inv.owner_email;
  switch (stufeNr) {
    case 1:
      return {
        betreff: `Kurze Erinnerung zu Rechnung ${nr}`,
        body: `${t.gruss} ${k},\n\nvielleicht ist es im Alltag untergegangen – unsere Rechnung ${nr} über ${b} ist seit dem ${fmt(inv.faellig_am)} offen. Falls schon überwiesen: bitte ignorieren.\n\nDirekt zahlen: ${link}\n\n${t.close}\n${a}`,
      };
    case 2:
      return {
        betreff: `Zweite Erinnerung: Rechnung ${nr} noch offen`,
        body: `${t.gruss} ${k},\n\nzu Rechnung ${nr} über ${b} (fällig am ${fmt(inv.faellig_am)}) konnten wir noch keinen Zahlungseingang feststellen. Wir bitten um Ausgleich in den nächsten Tagen.\n\nSchnell zahlen: ${link}\n\n${t.close}\n${a}`,
      };
    case 3:
      return {
        betreff: `Erinnerung: Rechnung ${nr} weiterhin offen`,
        body: `${t.gruss} ${k},\n\ntrotz meiner Erinnerungen ist Rechnung ${nr} über ${b} noch offen. Ich würde mich freuen, wenn du den Betrag in den nächsten Tagen begleichen könntest.\n\nFalls die Zahlung schon unterwegs ist, ignoriere diese Nachricht bitte.\n\nZahlung: ${link}\n\n${t.close}\n${a}`,
      };
    default:
      return {
        betreff: `Kurze Nachfrage zu Rechnung ${nr}`,
        body: `${t.gruss} ${k},\n\ndie Rechnung ${nr} über ${b} ist leider immer noch offen. Falls etwas unklar ist oder es ein Problem gibt, melde dich gern – wir finden bestimmt eine Lösung.\n\nAnsonsten freue ich mich über den Ausgleich: ${link}\n\n${t.close}\n${a}`,
      };
  }
}

async function sendEmail(env, to, betreff, body) {
  if (!env.RESEND_API_KEY || !env.FROM_EMAIL) {
    // Kein Versender konfiguriert -> nur loggen (Dry-Run), damit der Cron trotzdem läuft.
    console.log(`[DRY-RUN] an ${to}: ${betreff}`);
    return { dryRun: true };
  }
  const res = await fetch("https://api.resend.com/emails", {
    method: "POST",
    headers: { Authorization: `Bearer ${env.RESEND_API_KEY}`, "Content-Type": "application/json" },
    body: JSON.stringify({ from: env.FROM_EMAIL, to, subject: betreff, text: body }),
  });
  return { ok: res.ok, status: res.status };
}

function daysBetween(iso) {
  const due = new Date(iso).getTime();
  return Math.floor((Date.now() - due) / 86400000);
}

// --- HTTP-Router ------------------------------------------------------------
async function handleRequest(req, env) {
  if (req.method === "OPTIONS") return new Response(null, { headers: CORS });
  const url = new URL(req.url);
  const p = url.pathname;

  if (req.method === "POST" && p === "/api/waitlist") {
    const { email, source } = await req.json().catch(() => ({}));
    if (!email || !/^\S+@\S+\.\S+$/.test(email)) return json({ error: "invalid email" }, 400);
    await env.DB.prepare("INSERT OR IGNORE INTO waitlist (email, source) VALUES (?, ?)")
      .bind(email.toLowerCase(), source || "web").run();
    return json({ ok: true });
  }

  // Ab hier: API-Key nötig
  const key = req.headers.get("X-Api-Key");
  if (!env.API_KEY || key !== env.API_KEY) return json({ error: "unauthorized" }, 401);

  if (req.method === "POST" && p === "/api/invoices") {
    const b = await req.json().catch(() => ({}));
    const req_fields = ["owner_email", "kunde", "kunde_email", "rechnung_nr", "betrag_cent", "faellig_am"];
    for (const f of req_fields) if (b[f] === undefined) return json({ error: `missing ${f}` }, 400);
    const r = await env.DB.prepare(
      `INSERT INTO invoices (owner_email,kunde,kunde_email,rechnung_nr,betrag_cent,faellig_am,ton,zahllink)
       VALUES (?,?,?,?,?,?,?,?)`
    ).bind(b.owner_email, b.kunde, b.kunde_email, b.rechnung_nr, b.betrag_cent, b.faellig_am,
           b.ton || "neutral", b.zahllink || null).run();
    return json({ ok: true, id: r.meta.last_row_id });
  }

  if (req.method === "GET" && p === "/api/invoices") {
    const owner = url.searchParams.get("owner");
    const q = owner
      ? env.DB.prepare("SELECT * FROM invoices WHERE owner_email = ? ORDER BY created_at DESC").bind(owner)
      : env.DB.prepare("SELECT * FROM invoices ORDER BY created_at DESC");
    const { results } = await q.all();
    return json({ invoices: results });
  }

  const paid = p.match(/^\/api\/invoices\/(\d+)\/paid$/);
  if (req.method === "POST" && paid) {
    await env.DB.prepare("UPDATE invoices SET status='bezahlt' WHERE id=?").bind(paid[1]).run();
    return json({ ok: true });
  }

  return json({ error: "not found" }, 404);
}

// --- Cron: Eskalation verschicken ------------------------------------------
async function runReminders(env) {
  const { results } = await env.DB.prepare(
    "SELECT * FROM invoices WHERE status='offen'"
  ).all();
  let sent = 0;
  for (const inv of results) {
    const overdue = daysBetween(inv.faellig_am);
    if (overdue < STUFEN[0].nachTagen) continue; // noch nicht fällig genug
    // höchste erreichte Stufe finden, die noch nicht gesendet wurde
    let next = null;
    for (const s of STUFEN) {
      if (overdue >= s.nachTagen && s.nr > inv.stufe) { next = s; break; }
    }
    if (!next) continue;
    const mail = buildMail(inv, next.nr);
    await sendEmail(env, inv.kunde_email, mail.betreff, mail.body);
    await env.DB.prepare("UPDATE invoices SET stufe=? WHERE id=?").bind(next.nr, inv.id).run();
    await env.DB.prepare("INSERT INTO reminders_log (invoice_id,stufe,betreff) VALUES (?,?,?)")
      .bind(inv.id, next.nr, mail.betreff).run();
    sent++;
  }
  console.log(`Nachhaker Cron: ${sent} Erinnerung(en) verschickt.`);
}

export default {
  async fetch(req, env) {
    try {
      return await handleRequest(req, env);
    } catch (e) {
      return json({ error: String(e) }, 500);
    }
  },
  async scheduled(_event, env, ctx) {
    ctx.waitUntil(runReminders(env));
  },
};
