import { job, plainText, fetchJson } from "../lib/normalize.mjs";

// https://remoteok.com/api — offizieller JSON-Feed (erster Eintrag = Legal-Hinweis,
// Nutzung mit Verlinkung zur Original-Anzeige erlaubt; url zeigt dorthin).
export const name = "remoteok";

export async function holen() {
  const data = await fetchJson("https://remoteok.com/api", {
    "User-Agent": "JobAgent/1.0 (persoenlicher Bewerbungsassistent)",
  });
  const eintraege = Array.isArray(data) ? data.filter((e) => e && e.id) : [];
  return eintraege.map((r) =>
    job({
      id: `remoteok-${r.id}`,
      quelle: name,
      titel: r.position || "",
      firma: r.company || "",
      url: r.url || (r.slug ? `https://remoteok.com/remote-jobs/${r.slug}` : ""),
      candidateLocation: r.location || "",
      beschreibung: plainText(r.description),
      tags: r.tags || [],
      gehalt: r.salary_min ? `${r.salary_min}–${r.salary_max || "?"} USD` : "",
      veroeffentlicht: (r.date || "").slice(0, 10),
    })
  );
}
