/**
 * Gemeinsames Job-Format für alle Quellen:
 * {
 *   id: string            – stabil, quelle + externe ID
 *   quelle: string        – z.B. "remotive"
 *   titel: string
 *   firma: string
 *   url: string           – Link zur Anzeige / Bewerbung
 *   candidateLocation: string – von wo darf gearbeitet werden ("" = unbekannt)
 *   ort: string           – Firmensitz/angegebener Ort (informativ)
 *   beschreibung: string  – Klartext, gekürzt
 *   tags: string[]
 *   gehalt: string
 *   veroeffentlicht: string – ISO-Datum, "" wenn unbekannt
 * }
 */

export function job(teil) {
  return {
    id: "",
    quelle: "",
    titel: "",
    firma: "",
    url: "",
    candidateLocation: "",
    ort: "",
    beschreibung: "",
    tags: [],
    gehalt: "",
    veroeffentlicht: "",
    ...teil,
  };
}

const ENTITIES = { amp: "&", lt: "<", gt: ">", quot: '"', apos: "'", nbsp: " ", "#39": "'", "#x27": "'" };

export function plainText(html, maxLen = 1200) {
  if (!html) return "";
  const text = String(html)
    .replace(/<(style|script)[\s\S]*?<\/\1>/gi, " ")
    .replace(/<br\s*\/?>/gi, "\n")
    .replace(/<\/(p|div|li|h[1-6])>/gi, "\n")
    .replace(/<[^>]+>/g, " ")
    .replace(/&([a-z0-9#x]+);/gi, (m, e) => ENTITIES[e.toLowerCase()] ?? " ")
    .replace(/[ \t]+/g, " ")
    .replace(/\n{3,}/g, "\n\n")
    .trim();
  return text.length > maxLen ? text.slice(0, maxLen) + "…" : text;
}

/** Dedupliziert über normalisierte firma+titel; erste Quelle gewinnt. */
export function dedupe(jobs) {
  const key = (j) => (j.firma + "::" + j.titel).toLowerCase().replace(/[^a-z0-9:äöüß]+/g, "");
  const seen = new Map();
  for (const j of jobs) if (!seen.has(key(j))) seen.set(key(j), j);
  return [...seen.values()];
}

export async function fetchJson(url, headers = {}) {
  const res = await fetch(url, { headers: { Accept: "application/json", ...headers } });
  if (!res.ok) throw new Error(`HTTP ${res.status} für ${url}`);
  return res.json();
}

export async function fetchText(url, headers = {}) {
  const res = await fetch(url, { headers });
  if (!res.ok) throw new Error(`HTTP ${res.status} für ${url}`);
  return res.text();
}
