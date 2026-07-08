/**
 * Harter Remote/EU-Filter — läuft VOR jedem Scoring.
 *
 * Regel (Ankes Pflicht-Kriterium): Eine Stelle kommt nur durch, wenn sie
 * 100 % remote ist UND aus der EU ausgeübt werden darf. Alle angebundenen
 * Boards sind Remote-Boards; entscheidend ist daher candidateLocation:
 *
 *  - EU-tauglich (worldwide/anywhere/europe/emea/EU-Land)  → PASS
 *  - explizit Nicht-EU-Region (US only, Americas, APAC …)  → DROP
 *  - unbekannt/leer → PASS mit standortUnsicher=true (wird beim Scoring
 *    gegen den Anzeigentext geprüft, statt still gute Stellen zu verlieren)
 */

const EU_TAUGLICH = [
  "worldwide", "anywhere", "global", "remote (any", "international",
  "europe", "emea", "european union", "eu ", "eu,", "eu-", "eu)",
  // EU-/EWR-Länder (englische + deutsche Schreibweise, Auswahl)
  "germany", "deutschland", "austria", "österreich", "netherlands", "niederlande",
  "france", "frankreich", "spain", "spanien", "portugal", "italy", "italien",
  "ireland", "irland", "belgium", "belgien", "poland", "polen", "sweden", "schweden",
  "denmark", "dänemark", "finland", "finnland", "czech", "tschechien", "greece",
  "romania", "rumänien", "hungary", "ungarn", "croatia", "kroatien", "bulgaria",
  "slovakia", "slovenia", "estonia", "estland", "latvia", "lettland", "lithuania",
  "litauen", "luxembourg", "luxemburg", "malta", "cyprus", "zypern",
  "cet", "cest", "utc+1", "utc+2", "utc-0", "utc+0", "gmt",
];

const NICHT_EU = [
  "us only", "usa only", "us-only", "united states only", "us citizens",
  "us based", "us-based", "usa.", "united states", "north america", "americas",
  "canada", "kanada", "latam", "latin america", "south america", "brazil",
  "apac", "asia", "australia", "australien", "new zealand", "africa only",
  "india", "philippines", "uk only", "united kingdom only",
];

function enthaelt(text, muster) {
  return muster.some((m) => text.includes(m));
}

/**
 * @returns {{ pass: boolean, grund: string, standortUnsicher: boolean }}
 */
export function remoteEuCheck(jobItem) {
  const loc = (jobItem.candidateLocation || "").toLowerCase().trim();

  if (!loc) {
    return { pass: true, grund: "Standort-Angabe fehlt – beim Scoring prüfen", standortUnsicher: true };
  }
  if (enthaelt(loc, EU_TAUGLICH)) {
    return { pass: true, grund: `EU-tauglich: „${jobItem.candidateLocation}"`, standortUnsicher: false };
  }
  if (enthaelt(loc, NICHT_EU)) {
    return { pass: false, grund: `Nicht aus der EU ausübbar: „${jobItem.candidateLocation}"`, standortUnsicher: false };
  }
  return { pass: true, grund: `Standort unklar: „${jobItem.candidateLocation}" – beim Scoring prüfen`, standortUnsicher: true };
}

/** Wendet den harten Filter auf eine Liste an; annotiert Durchkommer. */
export function hartFiltern(jobs) {
  const durch = [];
  const raus = [];
  for (const j of jobs) {
    const check = remoteEuCheck(j);
    if (check.pass) {
      durch.push({ ...j, standortUnsicher: check.standortUnsicher, standortGrund: check.grund });
    } else {
      raus.push({ id: j.id, titel: j.titel, firma: j.firma, grund: check.grund });
    }
  }
  return { durch, raus };
}

/** Keyword-Filter: Titel/Tags/Beschreibung muss mind. ein Keyword enthalten. */
export function keywordFilter(jobs, keywords, ausschluss = []) {
  const kws = keywords.map((k) => k.toLowerCase()).filter(Boolean);
  const neg = ausschluss.map((k) => k.toLowerCase()).filter(Boolean);
  return jobs.filter((j) => {
    const text = `${j.titel} ${j.tags.join(" ")} ${j.beschreibung}`.toLowerCase();
    if (neg.some((n) => text.includes(n))) return false;
    if (kws.length === 0) return true;
    return kws.some((k) => text.includes(k));
  });
}
