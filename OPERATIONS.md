# Cashflow-Experiment — Betriebsbuch

Stand: 2026-11-05 · Status: **Tag 0, kein Umsatz, keine Ausgaben.**

Dieses Dokument ist die einzige Wahrheit über Geld, Experimente und Entscheidungen.
Nichts wird hier eingetragen, was nicht belegt ist (Kontoauszug, Plattform-Abrechnung, Rechnung).

## 1. Ausgangslage (ehrlich)

- Projekt „Nachhaker" (dieses Repo): Landing, 10 SEO-Seiten, Backend-MVP gebaut — **seit 2026-07-02 keine Änderung**.
- `WAITLIST_ENDPOINT` in `index.html` ist leer, `database_id` in `backend/wrangler.toml` ist ein Platzhalter.
  → Die Warteliste konnte konstruktionsbedingt **keinen einzigen Lead** speichern.
- Ob die Seite überhaupt live ist, konnte aus dieser Session nicht geprüft werden (Netzwerk-Proxy).
- Echte Kunden: 0. Echter Umsatz: 0 €.

## 2. Strategie (Kurzform)

**Nachfrage mieten statt aufbauen.** Bezahlte Kleinaufträge auf Plattformen annehmen, auf denen Käufer
ihre Kaufabsicht bereits öffentlich posten. Lieferung: Agent. Konto, Kommunikation, Qualitätsfreigabe: Anke.
Wiederkehrende Auftragstypen werden zu Festpreis-Paketen, dann zu Werkzeugen standardisiert.
Nachhaker wird eingefroren (nicht gelöscht) und nur bei Nachfragesignal reaktiviert.

Experiment-Lanes (Woche 1):

| Lane | Angebot | Kanal | Preis-Hypothese |
|---|---|---|---|
| A | Excel/Google-Sheets-Formeln, kleine Automationen (Apps Script/Python) | Upwork, Fiverr | 40–150 € pro Paket |
| B | DE-Lokalisierung von Shop-/Produkttexten für Nicht-DACH-Händler, Muttersprachen-Check durch Anke | Upwork, Fiverr | 0,06–0,10 €/Wort oder 49–129 € Paket |
| C | Warmes Netzwerk: 20 direkte Nachrichten an bekannte Selbstständige/Kleinbetriebe | persönlich, mit Einwilligung | frei verhandelt |

## 3. Kassenbuch

| Datum | Vorgang | Experiment | Einnahme € | Ausgabe € | Gebühren € | Beleg |
|---|---|---|---|---|---|---|
| — | noch keine Buchung | — | 0,00 | 0,00 | 0,00 | — |

**Kassenregeln**
- Experimentbudget Woche 1: **max. 40 €**. Gewerbeanmeldung (Gebühr je nach Stadt ca. 15–65 €) zählt separat als Pflichtkosten.
- Geschützte Reserve: alles über dem Wochenbudget bleibt unangetastet, bis netto ≥ 300 € eingenommen sind.
- Steuerrücklage: 30 % jedes Netto-Überschusses sofort separieren (Schätzwert, Steuerberater bestätigt).
- Rückerstattungsrisiko: Plattformgeld gilt erst nach Freigabe/Auszahlung als „verfügbar".
- Danach Verteilung des Überschusses (nach Reserve + Steuer): 80 % Skalierung bewiesener Lane, 20 % neue Tests.

## 4. Abbruch- und Wechselkriterien

| Signal | Entscheidung |
|---|---|
| 25 Angebote/Proposals in einer Lane, < 2 Antworten | Profil/Kategorie/Text falsch → Lane umbauen oder streichen |
| ≥ 10 Antworten, 0 Aufträge | Preis oder Angebot falsch → Preis/Paket ändern |
| Experimentbudget verbraucht ohne Antwortsignal | Ausgaben stoppen, Hypothese neu |
| Nach 5 Aufträgen < 15 € netto pro Anke-Stunde | Nicht tragfähig → standardisieren oder abbrechen |
| Gleicher Auftragstyp ≥ 3× | Festpreis-Paket bauen, Lieferung automatisieren |
| ≥ 3 zahlende Kunden fragen nach Mahnwesen/Rechnungsnachverfolgung | Nachhaker reaktivieren |

## 5. Arbeitstickets für Anke

Format: Aufgabe · Begründung · Nutzen · Kosten/Risiken · Priorität · Konkrete Handlung

**T1 — Entscheidung Zeitbudget & Fähigkeiten** · Kritisch
Ohne Wissen, wie viele Stunden/Tag und welche eigenen Kompetenzen verfügbar sind, ist jede Lane-Wahl geraten.
Handlung: Stunden/Tag, eigene Fachgebiete, Englischniveau, Netzwerk (Branchen) mitteilen.

**T2 — Nebentätigkeit/Gewerbe prüfen** · Kritisch (vor erster Rechnung)
Gewerbeanmeldung ggf. nötig; bei Anstellung Nebentätigkeitsklausel prüfen; Kleinunternehmerregelung (§ 19 UStG) wählen.
Kosten: Gewerbeamt-Gebühr. Risiko: Bußgeld bei fehlender Anmeldung.
Handlung: Arbeitsvertrag prüfen, Gewerbe online anmelden, Fragebogen zur steuerlichen Erfassung ausfüllen.

**T3 — Plattformkonten** · Hoch
Upwork- und Fiverr-Profil auf Ankes Namen (Identitätsprüfung nur durch sie). Profiltexte liefert der Agent.
Risiko: Profil-Ablehnung in überlaufenen Kategorien; Kunden dürfen laut ToS nicht von der Plattform abgeworben werden.
KI-Einsatz wird gegenüber Kunden **nicht verschwiegen**, wenn gefragt oder relevant.
Handlung: Konten anlegen, verifizieren, Auszahlungsmethode hinterlegen, Agent-Texte einfügen.

**T4 — Upwork Connects kaufen** · Hoch, max. 15 €
Bewerbungen kosten Connects. Handlung: nach Profilfreigabe kleinstes Paket kaufen.

**T5 — 20 Warm-Nachrichten** · Hoch, 0 €
Schnellster Weg zum ersten Euro sind Menschen, die Anke bereits kennen. Kein Massenversand, keine Kaltakquise per E-Mail (UWG § 7).
Handlung: Agent-Entwurf personalisieren und an 20 bekannte Kontakte senden.

**T6 — Tägliche Session öffnen** · Kritisch
Der Agent arbeitet nicht im Hintergrund. Handlung: 1×/Tag eine Session starten und neue Jobanfragen/Antworten hineinkopieren.

## 6. Experiment-Log

| Datum | Lane | Aktion | Ergebnis | Entscheidung |
|---|---|---|---|---|
| 2026-11-05 | — | Strategie festgelegt, Betriebsbuch angelegt | — | Warten auf T1 |
