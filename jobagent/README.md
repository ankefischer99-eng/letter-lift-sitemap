# JobAgent — automatisiertes Bewerbungssystem

Findet täglich passende **Remote-Jobs (arbeitbar aus der EU — Pflichtfilter)**,
bewertet sie gegen das persönliche Profil, schreibt individuelle Anschreiben und
legt sie als fertige Gmail-Entwürfe ab. Termine und Nachfass-Erinnerungen landen
im Google Kalender.

## Architektur

```
┌─ privates Repo: jobagent-daten ──────────────────────────┐
│ profil.md          ← Suchkriterien, Match-Schwelle (DU)  │
│ cv/                ← Lebenslauf (DU)                     │
│ daten/jobs-*.json  ← täglicher Abruf (GitHub Actions)    │
│ daten/bewerbungen.json ← Pipeline-Tracking (Agent)       │
│ anschreiben/       ← Archiv aller Anschreiben (Agent)    │
└──────────────────────────────────────────────────────────┘
          ▲ Actions: 06:30 holt Jobs      ▲ Agent-Routine: ~07:00
          │                               │ bewertet, schreibt, trackt
   Job-Quellen (APIs)              Gmail-Entwürfe + Google Kalender
```

- **Dieser Ordner (`jobagent/`, öffentliches Repo):** generischer Code + Vorlagen.
  Keine persönlichen Daten.
- **Privates Repo `jobagent-daten`:** deine Daten. Dort läuft auch der tägliche
  Actions-Workflow, weil diese Umgebung externe Job-APIs nicht direkt erreicht.

## Job-Quellen (legale, offene APIs/Feeds)

| Quelle | Abdeckung | EU-Filter über |
|---|---|---|
| Remotive | international | `candidate_required_location` |
| RemoteOK | international, viele US-Firmen | `location` |
| Jobicy | international | Geo-Abfrage `europe`/`anywhere`/`emea` |
| Arbeitnow | Europa/DACH | `remote`-Flag + `location` |
| We Work Remotely | international | RSS `<region>` |
| Arbeitsagentur | DACH | Homeoffice-Filter (`arbeitszeit=ho`) |

Bewusst **nicht** dabei: Scraping von LinkedIn/Indeed/StepStone (verstößt gegen
deren Nutzungsbedingungen). Portal-only-Stellen bekommen stattdessen fertigen
Bewerbungstext + Link zum Selbst-Einreichen.

## Harter Remote/EU-Filter

Läuft vor jeder Bewertung (`scripts/lib/filter.mjs`):

- Standortangabe EU-tauglich (worldwide/anywhere/Europe/EMEA/EU-Land) → **durch**
- explizit Nicht-EU (US only, Americas, APAC …) → **raus**
- unklar/fehlend → durch mit Flag `standortUnsicher`; der Agent prüft es beim
  Scoring gegen den Anzeigentext, bevor eine Bewerbung entsteht

## Lokal testen

```bash
node scripts/fetch-jobs.mjs --profil templates/profil.md --out /tmp/jobs.json
```

(Braucht Internetzugang zu den Job-APIs; in der Agent-Umgebung übernimmt das
GitHub Actions im privaten Repo.)

## Was nur Anke kann (menschliche Tore)

- Lebenslauf bereitstellen, `profil.md` bestätigen/anpassen
- Gmail-Entwürfe prüfen und **senden** (der Gmail-Connector kann nur Entwürfe anlegen)
- Optional: eigene Versand-Infrastruktur (z. B. Resend) für echtes Auto-Senden
