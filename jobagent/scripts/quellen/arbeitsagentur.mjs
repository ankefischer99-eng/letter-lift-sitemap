import { job, fetchJson } from "../lib/normalize.mjs";

// Jobsuche-API der Bundesagentur für Arbeit (offen dokumentiert auf bund.dev).
// arbeitszeit=ho = Homeoffice-Stellen. DACH-Ergänzung zu den internationalen Boards;
// die Anzeigen sind oft "remote innerhalb DE" → candidateLocation = Deutschland.
export const name = "arbeitsagentur";

export async function holen(conf) {
  const suchen = conf.keywords.length ? conf.keywords : [""];
  const alle = [];
  for (const kw of suchen.slice(0, 5)) {
    const url =
      "https://rest.arbeitsagentur.de/jobboerse/jobsuche-service/pc/v4/jobs" +
      `?size=50&arbeitszeit=ho${kw ? `&was=${encodeURIComponent(kw)}` : ""}`;
    const data = await fetchJson(url, { "X-API-Key": "jobboerse-jobsuche" });
    for (const r of data.stellenangebote || []) {
      alle.push(
        job({
          id: `ba-${r.refnr}`,
          quelle: name,
          titel: r.titel || r.beruf || "",
          firma: r.arbeitgeber || "",
          url: r.externeUrl || `https://www.arbeitsagentur.de/jobsuche/jobdetail/${encodeURIComponent(r.refnr)}`,
          candidateLocation: "Deutschland (Homeoffice)",
          ort: r.arbeitsort?.ort || "",
          veroeffentlicht: (r.aktuelleVeroeffentlichungsdatum || "").slice(0, 10),
        })
      );
    }
  }
  return alle;
}
