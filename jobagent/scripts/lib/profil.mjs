import { readFileSync } from "node:fs";

/**
 * Liest die Konfiguration aus profil.md. Konfiguriert wird in einem
 * ```jobagent-Codeblock mit einfachen `schluessel: wert`-Zeilen —
 * bequem im GitHub-Web-Editor änderbar, ohne JSON-Fallen.
 */

const DEFAULTS = {
  keywords: [],
  keywords_ausschluss: [],
  sprachen: ["de", "en"],
  quellen: ["remotive", "remoteok", "jobicy", "arbeitnow", "wwr", "arbeitsagentur"],
  match_schwelle: "nur-top", // nur-top (>=85) | gut (>=70) | alle (>=50)
  max_pro_tag: 0, // 0 = kein Limit
  arbeitszeit: "egal", // vollzeit | teilzeit | egal
};

const LISTEN_FELDER = new Set(["keywords", "keywords_ausschluss", "sprachen", "quellen"]);

export function parseProfil(pfad) {
  const md = readFileSync(pfad, "utf8");
  const block = md.match(/```jobagent\n([\s\S]*?)```/);
  const conf = { ...DEFAULTS };
  if (block) {
    for (const zeile of block[1].split("\n")) {
      const m = zeile.match(/^\s*([a-z_]+)\s*:\s*(.+?)\s*$/i);
      if (!m) continue;
      const [, roh, wert] = m;
      const key = roh.toLowerCase();
      if (LISTEN_FELDER.has(key)) {
        conf[key] = wert.split(",").map((s) => s.trim()).filter(Boolean);
      } else if (key === "max_pro_tag") {
        conf[key] = parseInt(wert, 10) || 0;
      } else {
        conf[key] = wert.trim();
      }
    }
  }
  return conf;
}

export function schwelleAlsZahl(schwelle) {
  return { "nur-top": 85, gut: 70, alle: 50 }[schwelle] ?? 85;
}
