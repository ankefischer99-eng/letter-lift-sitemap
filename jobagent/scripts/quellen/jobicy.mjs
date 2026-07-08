import { job, plainText, fetchJson } from "../lib/normalize.mjs";

// https://jobicy.com/api/v2/remote-jobs — offene API mit Geo-Filter.
// Wir fragen gezielt EU-taugliche Geos ab; US-only-Stellen kommen so gar nicht erst an.
export const name = "jobicy";

export async function holen(conf) {
  const geos = ["europe", "anywhere", "emea"];
  const alle = [];
  for (const geo of geos) {
    try {
      const url = `https://jobicy.com/api/v2/remote-jobs?count=50&geo=${geo}`;
      const data = await fetchJson(url);
      for (const r of data.jobs || []) {
        alle.push(
          job({
            id: `jobicy-${r.id}`,
            quelle: name,
            titel: r.jobTitle || "",
            firma: r.companyName || "",
            url: r.url || "",
            candidateLocation: r.jobGeo || geo,
            beschreibung: plainText(r.jobExcerpt || r.jobDescription),
            tags: [r.jobIndustry, r.jobType].flat().filter(Boolean),
            gehalt: r.annualSalaryMin
              ? `${r.annualSalaryMin}–${r.annualSalaryMax || "?"} ${r.salaryCurrency || ""}`.trim()
              : "",
            veroeffentlicht: (r.pubDate || "").slice(0, 10),
          })
        );
      }
    } catch (e) {
      // einzelnes Geo darf ausfallen (Jobicy antwortet 404 bei leerem Ergebnis)
      if (!String(e).includes("404")) throw e;
    }
  }
  return alle;
}
