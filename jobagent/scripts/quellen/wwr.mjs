import { job, plainText, fetchText } from "../lib/normalize.mjs";

// We Work Remotely — offizieller RSS-Feed. <region> enthält z.B.
// "Anywhere in the World" oder "Europe Only" → direkt EU-filterbar.
export const name = "wwr";

function tag(xml, t) {
  const m = xml.match(new RegExp(`<${t}[^>]*>([\\s\\S]*?)</${t}>`));
  return m ? m[1].replace(/<!\[CDATA\[([\s\S]*?)\]\]>/, "$1").trim() : "";
}

export async function holen() {
  const xml = await fetchText("https://weworkremotely.com/remote-jobs.rss", {
    "User-Agent": "JobAgent/1.0 (persoenlicher Bewerbungsassistent)",
  });
  const items = xml.match(/<item>[\s\S]*?<\/item>/g) || [];
  return items.map((item, i) => {
    const rohTitel = tag(item, "title"); // Format: "Firma: Stellentitel"
    const [firma, ...rest] = rohTitel.split(":");
    const link = tag(item, "link");
    return job({
      id: `wwr-${link.split("/").filter(Boolean).pop() || i}`,
      quelle: name,
      titel: rest.join(":").trim() || rohTitel,
      firma: rest.length ? firma.trim() : "",
      url: link,
      candidateLocation: tag(item, "region"),
      beschreibung: plainText(tag(item, "description")),
      tags: [tag(item, "category")].filter(Boolean),
      veroeffentlicht: tag(item, "pubDate") ? new Date(tag(item, "pubDate")).toISOString().slice(0, 10) : "",
    });
  });
}
