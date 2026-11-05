# DECISIONS — Entscheidungslog

Format: Datum · Entscheidung · Begründung · Alternativen verworfen · Überprüfen wann

## D1 · 2026-11-05 · Nachhaker eingefroren
Begründung: 4 Monate ohne Änderung, Warteliste technisch nie angeschlossen (0 Leads möglich), SEO-SaaS braucht 18+ Monate bis zu relevantem Umsatz.
Verworfen: Weiterbauen. Überprüfen: falls ≥ 3 zahlende Kunden nach Mahnwesen fragen.

## D2 · 2026-11-05 · Firma als Multi-Agenten-Organisation mit Dateigedächtnis
Begründung: Auftrag der Inhaberin. Gedächtnis in Markdown im Repo, weil jeder Agent es ohne Zusatzinfrastruktur lesen/schreiben kann und Git alles versioniert.
Verworfen: Datenbank/Notion (Zusatzkosten, Zugriffsrechte). Überprüfen: wenn Merge-Konflikte oder Dateigröße stören.

## D3 · 2026-11-05 · Start mit 3 Agenten + Koordinator, Lieferung nur auf Auftrag
Begründung: Agenten sind Kosten. Ohne Umsatz wird nur gesucht und angeboten, nicht produziert.
Verworfen: separater Finanz-, Marketing-, Revisionsagent (vorerst im Koordinator gebündelt). Überprüfen: nach ersten 3 bezahlten Aufträgen.

## D4 · 2026-11-05 · Erste Geschäftshypothese: digitale Kleinaufträge über bestehende Marktplätze
Begründung: Käufer posten dort Kaufabsicht öffentlich → keine eigene Reichweite nötig. Rechenkosten pro Auftrag ≈ 1–2 $ bei Preisen von 50–150 €.
Risiko: neue Profile ohne Bewertungen, Plattformgebühren, Ankes Zeit als Engpass.
Überprüfen: nach Scout-Lauf 1 (Daten statt Bauchgefühl).

## D5 · 2026-11-05 · Vorerst kein API-Guthaben
Begründung: Pro ist bereits bezahlt; API-Ausgaben vor dem ersten Umsatz wären Geld für Agenten, die noch nichts verdient haben. Eigene Regel: max. 20 € Vorschuss.
Risiko: Pro-Limits (5-Stunden-Fenster) teilen sich Agenten und Ankes eigene Nutzung → Agententakt niedrig halten.
Überprüfen: sobald Limits den Betrieb zweimal blockieren ODER der erste Umsatz eingeht. Dann API mit hartem Ausgabelimit (Start 10 €).

## D6 · 2026-11-05 · Pro-Abo ist Fixkosten der Firma
Begründung: Strenge Rechnung statt Schönrechnen. Die Firma ist erst profitabel, wenn sie ihre eigene Laufzeit bezahlt.
Verworfen: Anteilige Zurechnung (würde den Break-even künstlich senken).

## D7 · 2026-11-05 · Agenten-Sessions laufen künftig auf Sonnet, nicht Opus
Begründung: Recherche/Entwürfe brauchen kein Spitzenmodell; Opus verbraucht das Pro-Kontingent schneller. Koordinator darf für Entscheidungen Opus nutzen.

## D8 · 2026-11-05 · Ankes Expertise wird zweite Geschäftshypothese (H2), nicht ignoriert
Begründung: Käufer kaufen bei Menschen mit Glaubwürdigkeit. Anke bringt nachweisbare Führungserfahrung in Kundenservice-Qualität, Training, Sales-Performance und AI Enablement mit. Agenten ohne diesen Hebel konkurrieren mit dem ganzen Internet um Excel-Kleinaufträge.
H2: Produkte/Leistungen für Kundenservice- und Vertriebsteams kleiner Firmen (z. B. QA-Scorecards, Coaching-Leitfäden, KI-Prompt-Kits für Servicemitarbeitende, Einführungsworkshops), DACH, deutschsprachig.
Bedingung: **nur nach T2** (keine Konkurrenz zum Arbeitgeber, keine Firmeninterna, kein Material des Arbeitgebers). H1 (Marktplatz-Kleinaufträge) läuft parallel weiter.
Überprüfen: nach T2/T7 und Scout-Lauf 2.

## D9 · 2026-11-05 · Markt: DACH, deutschsprachig
Begründung: Kundengespräche müssen auf Ankes Seite sicher laufen; Business-Englisch ist laut Anke schwach. Englische Texte darf der Vertrieb schreiben, aber Kundenbeziehungen mit Gesprächsbedarf nur auf Deutsch.
Kapazität: 10 h/Woche Anke → Engpass, also nur Angebote mit wenig Abstimmungsaufwand pro Euro.
