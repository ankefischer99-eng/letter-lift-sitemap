import { job, plainText, fetchJson } from "../lib/normalize.mjs";

// https://remotive.com/api/remote-jobs — offizielle öffentliche API.
// Liefert candidate_required_location, ideal für den EU-Filter.
export const name = "remotive";

export async function holen(conf) {
  const suchen = conf.keywords.length ? conf.keywords : [""];
  const alle = [];
  for (const kw of suchen.slice(0, 5)) {
    const url = `https://remotive.com/api/remote-jobs?limit=100${kw ? `&search=${encodeURIComponent(kw)}` : ""}`;
    const data = await fetchJson(url);
    for (const r of data.jobs || []) {
      alle.push(
        job({
          id: `remotive-${r.id}`,
          quelle: name,
          titel: r.title || "",
          firma: r.company_name || "",
          url: r.url || "",
          candidateLocation: r.candidate_required_location || "",
          beschreibung: plainText(r.description),
          tags: [r.category, r.job_type].filter(Boolean),
          gehalt: r.salary || "",
          veroeffentlicht: (r.publication_date || "").slice(0, 10),
        })
      );
    }
  }
  return alle;
}
