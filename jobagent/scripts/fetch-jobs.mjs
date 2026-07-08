#!/usr/bin/env node
/**
 * JobAgent – Aggregator
 *
 * Holt Remote-Stellen aus allen im Profil aktivierten Quellen, wendet den
 * HARTEN Remote/EU-Filter an (Pflicht: 100 % remote + aus der EU ausübbar),
 * filtert nach Keywords, dedupliziert und schreibt das Ergebnis als JSON.
 *
 * Aufruf:  node scripts/fetch-jobs.mjs [--profil profil.md] [--out daten/jobs.json]
 * Keine Dependencies – läuft mit purem Node ≥ 18 (fetch eingebaut).
 */
import { writeFileSync, mkdirSync } from "node:fs";
import { dirname } from "node:path";
import { parseProfil } from "./lib/profil.mjs";
import { hartFiltern, keywordFilter } from "./lib/filter.mjs";
import { dedupe } from "./lib/normalize.mjs";

import * as remotive from "./quellen/remotive.mjs";
import * as remoteok from "./quellen/remoteok.mjs";
import * as jobicy from "./quellen/jobicy.mjs";
import * as arbeitnow from "./quellen/arbeitnow.mjs";
import * as wwr from "./quellen/wwr.mjs";
import * as arbeitsagentur from "./quellen/arbeitsagentur.mjs";

const QUELLEN = { remotive, remoteok, jobicy, arbeitnow, wwr, arbeitsagentur };

function arg(name, fallback) {
  const i = process.argv.indexOf(`--${name}`);
  return i > -1 && process.argv[i + 1] ? process.argv[i + 1] : fallback;
}

const profilPfad = arg("profil", "profil.md");
const outPfad = arg("out", `daten/jobs-${new Date().toISOString().slice(0, 10)}.json`);

const conf = parseProfil(profilPfad);
console.log(`Profil: ${profilPfad} | Quellen: ${conf.quellen.join(", ")} | Keywords: ${conf.keywords.join(", ") || "(alle)"}`);

const quellenStatus = {};
let roh = [];

for (const qName of conf.quellen) {
  const q = QUELLEN[qName];
  if (!q) {
    quellenStatus[qName] = "unbekannte Quelle – übersprungen";
    continue;
  }
  try {
    const jobs = await q.holen(conf);
    quellenStatus[qName] = `ok, ${jobs.length} Stellen`;
    roh.push(...jobs);
  } catch (e) {
    quellenStatus[qName] = `FEHLER: ${e.message}`;
    console.error(`Quelle ${qName} fehlgeschlagen:`, e.message);
  }
}

const vorFilter = roh.length;
const { durch, raus } = hartFiltern(roh);
const passend = keywordFilter(durch, conf.keywords, conf.keywords_ausschluss);
const jobs = dedupe(passend).sort((a, b) => (b.veroeffentlicht || "").localeCompare(a.veroeffentlicht || ""));

const ergebnis = {
  erstellt: new Date().toISOString(),
  profil: { keywords: conf.keywords, match_schwelle: conf.match_schwelle, quellen: conf.quellen },
  statistik: {
    roh: vorFilter,
    nachRemoteEuFilter: durch.length,
    remoteEuAussortiert: raus.length,
    nachKeywords: passend.length,
    final: jobs.length,
  },
  quellenStatus,
  aussortiertBeispiele: raus.slice(0, 10),
  jobs,
};

mkdirSync(dirname(outPfad), { recursive: true });
writeFileSync(outPfad, JSON.stringify(ergebnis, null, 2));
console.log(
  `${jobs.length} Stellen → ${outPfad} (roh ${vorFilter}, Remote/EU-Filter entfernte ${raus.length}, Keywords ließen ${passend.length} durch)`
);
