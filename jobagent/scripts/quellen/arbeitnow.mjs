import { job, plainText, fetchJson } from "../lib/normalize.mjs";

// https://www.arbeitnow.com/api/job-board-api — offene API, Europa-fokussiert.
// Nur Einträge mit remote=true werden übernommen (Ankes Pflicht-Kriterium).
export const name = "arbeitnow";

export async function holen() {
  const alle = [];
  for (let seite = 1; seite <= 3; seite++) {
    const data = await fetchJson(`https://www.arbeitnow.com/api/job-board-api?page=${seite}`);
    for (const r of data.data || []) {
      if (!r.remote) continue;
      alle.push(
        job({
          id: `arbeitnow-${r.slug}`,
          quelle: name,
          titel: r.title || "",
          firma: r.company_name || "",
          url: r.url || "",
          candidateLocation: r.location || "",
          ort: r.location || "",
          beschreibung: plainText(r.description),
          tags: [...(r.tags || []), ...(r.job_types || [])],
          veroeffentlicht: r.created_at ? new Date(r.created_at * 1000).toISOString().slice(0, 10) : "",
        })
      );
    }
    if (!data.links?.next) break;
  }
  return alle;
}
