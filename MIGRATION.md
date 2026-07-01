# Umzug in ein eigenes Repo („nachhaker")

**Entscheidung:** Nachhaker bekommt ein eigenes, sauberes Repo — nicht das
Erbe des toten Projekts „letter-lift". Der Code ist bewusst portabel und hat
**keine Kopplung** an letter-lift; „letter-lift-sitemap" ist nur der Name der
aktuellen Hülle.

**Warum es (noch) hier liegt:** Diese Claude-Session ist von GitHub auf das
Repo `ankefischer99-eng/letter-lift-sitemap` beschränkt. `create_repository`
liefert `403 – Resource not accessible by integration`. Ein neues Repo kann in
dieser Session weder angelegt noch bepusht werden.

## Umzug in 3 Schritten (deine ~5 Minuten)

1. **Neues Repo anlegen:** github.com → New repository → Name `nachhaker`,
   public, **ohne** README/gitignore.
2. **Inhalte übertragen** (lokal, mit dem letter-lift-Klon):
   ```bash
   git clone https://github.com/ankefischer99-eng/letter-lift-sitemap.git nachhaker
   cd nachhaker
   git checkout claude/side-income-ideas-hx0vr1
   git remote set-url origin https://github.com/ankefischer99-eng/nachhaker.git
   git push -u origin claude/side-income-ideas-hx0vr1:main
   ```
   (Alternativ: die Dateien einfach ins neue Repo kopieren und committen.)
3. **Pages im neuen Repo aktivieren:** Settings → Pages → Deploy from branch →
   `main` → `/(root)`. Live unter
   `https://ankefischer99-eng.github.io/nachhaker/`.

Danach kann `letter-lift-sitemap` archiviert oder gelöscht werden.

## Was mitwandert (alles portabel)
```
index.html            – Produkt-Landing + Live-Demo + Warteliste
ratgeber/             – 6 SEO-Seiten (Traffic-Engine)
sitemap.xml, robots.txt
.github/workflows/    – Pages-Deploy (GitHub Actions)
backend/              – Cloudflare Worker + D1 (MVP: Warteliste, Rechnungen, Cron-Mahnungen)
BUSINESS.md           – Betriebsplan & Weg zu 20k
```
