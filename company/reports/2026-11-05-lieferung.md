# Report Lieferung 2026-11-05
Auftrag (aus STATE.md): Produkt „KI-Starterkit für kleine Unternehmen" v1 (D17) → `deliveries/produkt-ki-starterkit-v1/`, 8 Dateien, Verbotsliste einhalten, Skript für Varianten, QA.md.

Erledigt (alles in `company/deliveries/produkt-ki-starterkit-v1/`):
- `KI-Nutzungsrichtlinie.docx` — 7 Seiten, 13 Kapitel + Anhang A (Tool-Liste) + B (Kenntnisnahme), Platzhalter in [ECKIGEN KLAMMERN]
- `KI-Schulung.pptx` — 22 Folien, Sprechernotiz auf jeder Folie, 2 Praxisübungen (Folien 13 und 17, je mit Auflösung)
- `Wissenstest-und-Nachweis.docx` — 12 Fragen, Lösungsblatt, Teilnahmeliste, Einzelnachweis (6 Seiten)
- `Datenschutz-Checkliste-und-Tool-Freigabe.xlsx` — 5 Blätter (Anleitung, Checkliste 20 Punkte, Bewertungsmatrix mit 3 K.-o.-Fragen + 7 gewichteten Kriterien, Tool-Register, Datenampel), Formeln und Dropdowns
- `Prompt-Bibliothek.docx` — 30 Prompts (5 Bereiche × 6), je Zweck/Prompt/Hinweis (11 Seiten)
- `Anpassungs-Prompt.docx` — 7 Schritte, Warnkasten am Anfang, Fragebogen, 4 Prompts (A–D) (5 Seiten)
- `Kurzanleitung-In-einer-Woche-eingefuehrt.docx` — 1 Seite
- `QA.md` — Prüfprotokoll
- `build/` — `build_kit.py` (erzeugt alles), `kit_lib.py` (Layout), `b1…b7_*.py` (Inhalte je Datei), `verify_kit.py` (prüft + schreibt QA.md neu)

Ergebnis/Zahlen: 61 automatische Prüfungen, 61 bestanden (QA.md §1): alle Dateien öffnen sich (python-docx/-pptx/openpyxl, ZIP-Test), PDF-Export per LibreOffice, Seiten-/Folienzahlen im Soll, Excel-Formeln in 8 Szenarien per LibreOffice-Neuberechnung getestet (inkl. Grenzwert 50 %, K.-o.-Logik, Fälligkeit), Verbotsliste (3 Begriffe) + „§" + „Art. <Zahl>" + „AI Act": 0 Treffer. Folienlayout und zwei Dokumentseiten zusätzlich als Bild gesichtet. Eine Zwischenprüfung fand einen echten Fehler (Spaltenbreiten wurden in LibreOffice ignoriert) und zwei falsche Testerwartungen von mir; behoben.

Erkenntnisse: → Kandidat für LEARNINGS
- Bau des gesamten Kits ist skriptbar; Varianten (EN, Branche) kosten nur Textersatz in `b1…b7`, kein neues Layout.
- Die Excel-Empfehlungslogik und das Layout lassen sich ohne Microsoft Office testen (LibreOffice-Neuberechnung); Word-/PowerPoint-Darstellung bleibt trotzdem ungeprüft.

Fehlschläge: → Kandidat für FAILURES
- Keine. Ein Verstoß gegen die Verbotsliste war zwischenzeitlich im Anpassungs-Prompt (das verbotene Wort stand als Negativbeispiel im Text); vor Abgabe entfernt, jetzt automatisch geprüft.

Braucht Anke: → Kandidat für TICKETS
1. **Endabnahme (Schätzung, nicht gemessen): ca. 2,5–3,5 Std.** Jede Datei einmal lesen (Grammatik/Stil wurde nur per Wörterbuch-Heuristik geprüft), alle Dateien in Word/PowerPoint/Excel öffnen (dort wurde nicht getestet), Folien 13/17/18 ansehen.
2. **Entscheidung Rechtsprüfung:** Kein Jurist hat das Kit gesehen. Ob vor dem Verkauf eine anwaltliche Durchsicht (Richtlinie, Hinweistexte, Werbeaussagen) gewünscht ist, entscheidet Anke; die Kosten wären ein Budgetticket.
3. **Nutzungsbedingungen/Impressum/Branding:** Das Kit enthält bewusst keine Lizenz- oder Anbieterangaben (Weitergabe, Nutzung im eigenen Betrieb, Haftungsausschluss in den Verkaufs-AGB). Muss mit Digistore24/Fiverr-Vorgaben abgestimmt werden.
4. **Erster echter Test:** 1–2 Personen aus Ankes Umfeld, die das Kit nach der Kurzanleitung einsetzen. Erst das belegt „in einer Woche einsetzbar"; bisher ist es eine Planung (ca. 8–10 Std. in der Kurzanleitung geschätzt).
5. Bereits offen aus D17: Digistore24-Wiederverkäufer/USt, Fiverr-Fotopflicht.

Vorschlag an den Koordinator:
- Vertrieb (Produktseite, Fiverr-Gig, TikTok-Skripte) kann nach Ankes Endabnahme starten. Werbetexte dürfen aus dem Kit **keine** gesetzliche Pflicht und keine Rechtssicherheit ableiten; zulässige Aussagen: „bearbeitbare Vorlagen", „unterstützt beim Aufbau von KI-Kompetenz", „keine Rechtsberatung".
- Preise erst nach Ankes Abnahme festlegen; Aufwand für Variante EN ca. 1 Sitzung (Übersetzung der Texte b1…b7, Rechtsbezug auf DACH-Kontext prüfen/streichen).
- Die Anpassungs-Prompts A–D sind nicht gegen ein KI-Tool getestet; wenn ein „Fiverr-angepasst"-Gig verkauft wird, sollte ein Probelauf mit fiktiven Firmenangaben vorher stattfinden.

Geschätzter Aufwand dieser Sitzung: lang
