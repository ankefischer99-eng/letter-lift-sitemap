# QA-Protokoll — KI-Starterkit v1

Erstellt: 2026-11-05 · Erzeugt mit `build/build_kit.py`, geprüft mit `build/verify_kit.py` (Ausführung: 2026-11-05 15:25).
Automatische Prüfungen: **84 von 84 bestanden**

## 1. Automatische Prüfungen (Skript, reproduzierbar)

| Datei | Prüfung | Ergebnis | OK |
|---|---|---|---|
| KI-Nutzungsrichtlinie.docx | Öffnen mit python-docx; PDF-Export mit LibreOffice; Seitenzahl | 7 Seiten (Soll 6–8); 112 Absätze, 10 Tabellen | ja |
| KI-Nutzungsrichtlinie.docx | Hinweis „ersetzt keine Rechtsberatung“ | vorhanden (2×, inkl. Fußzeile) | ja |
| Wissenstest-und-Nachweis.docx | Öffnen mit python-docx; PDF-Export mit LibreOffice; Seitenzahl | 6 Seiten; 92 Absätze, 7 Tabellen | ja |
| Wissenstest-und-Nachweis.docx | Hinweis „ersetzt keine Rechtsberatung“ | vorhanden (2×, inkl. Fußzeile) | ja |
| Prompt-Bibliothek.docx | Öffnen mit python-docx; PDF-Export mit LibreOffice; Seitenzahl | 14 Seiten; 61 Absätze, 38 Tabellen | ja |
| Prompt-Bibliothek.docx | Hinweis „ersetzt keine Rechtsberatung“ | vorhanden (2×, inkl. Fußzeile) | ja |
| Anpassungs-Prompt.docx | Öffnen mit python-docx; PDF-Export mit LibreOffice; Seitenzahl | 5 Seiten; 44 Absätze, 9 Tabellen | ja |
| Anpassungs-Prompt.docx | Hinweis „ersetzt keine Rechtsberatung“ | vorhanden (3×, inkl. Fußzeile) | ja |
| Kurzanleitung-In-einer-Woche-eingefuehrt.docx | Öffnen mit python-docx; PDF-Export mit LibreOffice; Seitenzahl | 1 Seiten (Soll 1–2); 19 Absätze, 1 Tabellen | ja |
| Kurzanleitung-In-einer-Woche-eingefuehrt.docx | Hinweis „ersetzt keine Rechtsberatung“ | vorhanden (2×, inkl. Fußzeile) | ja |
| Aha-Uebungen-Arbeitsblatt.docx | Öffnen mit python-docx; PDF-Export mit LibreOffice; Seitenzahl | 7 Seiten; 67 Absätze, 25 Tabellen | ja |
| Aha-Uebungen-Arbeitsblatt.docx | Hinweis „ersetzt keine Rechtsberatung“ | vorhanden (2×, inkl. Fußzeile) | ja |
| Grundbegriffe-in-einfacher-Sprache.docx | Öffnen mit python-docx; PDF-Export mit LibreOffice; Seitenzahl | 3 Seiten (Soll 2–3); 35 Absätze, 5 Tabellen | ja |
| Grundbegriffe-in-einfacher-Sprache.docx | Hinweis „ersetzt keine Rechtsberatung“ | vorhanden (2×, inkl. Fußzeile) | ja |
| KI-Schulung.pptx | Öffnen mit python-pptx; Folienzahl | 24 Folien (Soll 18–24) | ja |
| KI-Schulung.pptx | Sprechernotiz auf jeder Folie | 24/24 Folien mit Notiz > 40 Zeichen; kürzeste 217 Zeichen | ja |
| KI-Schulung.pptx | Zwei Praxisübungen | Folien [12, 17] | ja |
| KI-Schulung.pptx | Aha-Übung 1 (2 Folien: Anleitung + Auswertung) und Folie „Weitere Aha-Übungen“ | Folien [3, 4, 16] | ja |
| KI-Schulung.pptx | Kapitel Grundbegriffe (Soll 3–5 Folien) | Folien [20, 21, 22] | ja |
| KI-Schulung.pptx | Hinweis „ersetzt keine Rechtsberatung“ | auf 24/24 Folien (Fußzeile) | ja |
| KI-Schulung.pptx | PDF-Export mit LibreOffice (Rendern möglich) | 24 Seiten | ja |
| KI-Schulung.pptx | Text-Überlauf-Heuristik (> 700 Zeichen/Folie) | Folien mit viel Text: keine | ja |
| Datenschutz-Checkliste-und-Tool-Freigabe.xlsx | Öffnen mit openpyxl; Blätter | Anleitung, Checkliste, Tool-Bewertung, Tool-Register, Datenampel | ja |
| Datenschutz-Checkliste-und-Tool-Freigabe.xlsx | Hinweis „ersetzt keine Rechtsberatung“ | vorhanden | ja |
| Datenschutz-Checkliste-und-Tool-Freigabe.xlsx | Formeltest Tool-Bewertung: alle Ja, Punkte 2,1,2,1,1,1,2 (Beispielzeile, 20/28 = 71 %) | Empfehlung „Freigabe mit Auflagen“ (erwartet „Freigabe mit Auflagen“); Punkte 20/28, Anteil 0.714 | ja |
| Datenschutz-Checkliste-und-Tool-Freigabe.xlsx | Formeltest Tool-Bewertung: alle Ja, überall 2 (100 %) | Empfehlung „Freigabe empfohlen“ (erwartet „Freigabe empfohlen“); Punkte 28/28, Anteil 1 | ja |
| Datenschutz-Checkliste-und-Tool-Freigabe.xlsx | Formeltest Tool-Bewertung: alle Ja, überall 1 (genau 50 % = Grenzwert) | Empfehlung „Freigabe mit Auflagen“ (erwartet „Freigabe mit Auflagen“); Punkte 14/28, Anteil 0.5 | ja |
| Datenschutz-Checkliste-und-Tool-Freigabe.xlsx | Formeltest Tool-Bewertung: alle Ja, Punkte 0 | Empfehlung „Nicht freigeben“ (erwartet „Nicht freigeben“); Punkte 0/28, Anteil 0 | ja |
| Datenschutz-Checkliste-und-Tool-Freigabe.xlsx | Formeltest Tool-Bewertung: K2 = Nein, sonst gute Punkte | Empfehlung „Nur grüne Daten (Stufe 1)“ (erwartet „Nur grüne Daten (Stufe 1)“); Punkte 28/28, Anteil 1 | ja |
| Datenschutz-Checkliste-und-Tool-Freigabe.xlsx | Formeltest Tool-Bewertung: K1 = Unklar | Empfehlung „Erst klären“ (erwartet „Erst klären“); Punkte 28/28, Anteil 1 | ja |
| Datenschutz-Checkliste-und-Tool-Freigabe.xlsx | Formeltest Tool-Bewertung: K.-o. nur teilweise ausgefüllt | Empfehlung „K.-o.-Fragen ausfüllen“ (erwartet „K.-o.-Fragen ausfüllen“); Punkte 28/28, Anteil 1 | ja |
| Datenschutz-Checkliste-und-Tool-Freigabe.xlsx | Formeltest Tool-Bewertung: Kriterien unvollständig | Empfehlung „Kriterien bewerten“ (erwartet „Kriterien bewerten“); Punkte 12/28, Anteil 0.429 | ja |
| Datenschutz-Checkliste-und-Tool-Freigabe.xlsx | Formeltest Tool-Register (Neuprüfung fällig?) | Datum 2020 → „FÄLLIG“, Datum 2099 → „ok“ | ja |
| Datenschutz-Checkliste-und-Tool-Freigabe.xlsx | Formeltest Checkliste (Zähler) | Erledigt=4, Offen=15, Nicht zutreffend=1, Fortschritt=0.211, Alle erledigt?=Nein | ja |
| Datenschutz-Checkliste-und-Tool-Freigabe.xlsx | Keine Formelfehler (#WERT!, #NAME? …) nach Neuberechnung | keine | ja |
| Datenschutz-Checkliste-und-Tool-Freigabe.xlsx | Anzahl Formeln in der gelieferten Datei | 66 | ja |
| Datenschutz-Checkliste-und-Tool-Freigabe.xlsx | Dropdown-Listen (Datenvalidierung) | 4 Regeln | ja |
| Prompt-Bibliothek.docx | Anzahl Prompts (Tabellen mit Nr.) | 34 (Soll 34 = 5 Bereiche × 6 + 4 Excel); je Bereich {'Verwaltung': 6, 'Vertrieb': 6, 'Kundenservice': 6, 'Marketing': 6, 'Personal': 6, 'Excel und Auswertung (mit Plausibilitätscheck)': 4} | ja |
| Prompt-Bibliothek.docx | Jeder Prompt hat Zweck, Prompt-Text und Hinweis | ja | ja |
| Prompt-Bibliothek.docx | Kontext-Baukasten sichtbar: jeder Prompt hat ROLLE/ZIEL/ZIELGRUPPE/TON/BEISPIEL/FORMAT/GRENZEN/MATERIAL | ja | ja |
| Prompt-Bibliothek.docx | Excel-/Auswertungs-Prompts mit Plausibilitätscheck (Soll ≥ 3) | 4 | ja |
| Wissenstest-und-Nachweis.docx | 12 Fragen mit je 4 Antworten und Lösung | 12 Fragen; Verteilung richtiger Antworten {'A': 3, 'B': 3, 'C': 3, 'D': 3} | ja |
| KI-Nutzungsrichtlinie.docx | „Stand: November 2026“ vorhanden | ja | ja |
| Wissenstest-und-Nachweis.docx | „Stand: November 2026“ vorhanden | ja | ja |
| Prompt-Bibliothek.docx | „Stand: November 2026“ vorhanden | ja | ja |
| Anpassungs-Prompt.docx | „Stand: November 2026“ vorhanden | ja | ja |
| Kurzanleitung-In-einer-Woche-eingefuehrt.docx | „Stand: November 2026“ vorhanden | ja | ja |
| Aha-Uebungen-Arbeitsblatt.docx | „Stand: November 2026“ vorhanden | ja | ja |
| Grundbegriffe-in-einfacher-Sprache.docx | „Stand: November 2026“ vorhanden | ja | ja |
| KI-Schulung.pptx | „Stand: November 2026“ vorhanden | ja | ja |
| Datenschutz-Checkliste-und-Tool-Freigabe.xlsx | „Stand: November 2026“ vorhanden | ja | ja |
| alle 9 Dateien | Verbotsliste: Verbotsbegriff 1 (rechts-sicher) | 0 Treffer | ja |
| alle 9 Dateien | Verbotsliste: Verbotsbegriff 2 (erfüllt … AI Act) | 0 Treffer | ja |
| alle 9 Dateien | Verbotsliste: Verbotsbegriff 3 (zertifiziert) | 0 Treffer | ja |
| alle 9 Dateien | Verbotsliste: Paragraphenzeichen § | 0 Treffer | ja |
| alle 9 Dateien | Verbotsliste: Artikelzitat 'Art. <Zahl>' | 0 Treffer | ja |
| alle 9 Dateien | Verbotsliste: 'AI Act' (irgendwo) | 0 Treffer | ja |
| KI-Nutzungsrichtlinie.docx | Rechtschreib-Heuristik (Wörterbuch, unbekannte Wörter ≥ 4 Buchstaben) | 72 unbekannte Wörter: angebotstext, ansprechperson, anwendungsfall, anwendungsfälle, audio, audiogeneratoren, auftragsverarbeitung, bewerbungsauswahl, bewertungsmatrix, chatbot, datenabfluss, datenampel, datenschutzhinweise, datenschutzpanne, datenschutzpannen, datenschutzprüfung, datenschutzrecht, dokumentinfo, dsgvo, entscheidungsvorschläge, erstfassung, firmenbezug, freigabeliste, freigabestufe, freigabestufen, gesundheitsangaben, gesundheitsaussagen, gesundheitsdaten, grundverordnung, hochgeladene, hochladen, hochzuladen, ideensammlung, kundennummer, meldefristen, metadaten, mitarbeiterbewertung, nachschulen, neuprüfung, nutzungsbedingungen, nutzungsrichtlinie, personenbezug, personendaten, plug, preiskalkulationen, produktivsysteme, protokollwerkzeuge, prüfpflicht, rechtsberatung, rohentwurf, routinearbeit, schulungsfolien, selbstprüfung, skripte, social, sprachmodelle, starterkit, tabellenformeln, teilnahmeliste, transkriptions, transparenzvorgaben, verarbeitungstätigkeiten, videokonferenzen, webseitentexte, wissenstest, xlsx, zahlungsdaten, zugangsdaten, zurückgibt, änderungsprotokoll, übersetzungsdiensten, übungsbeispiele | ja |
| Wissenstest-und-Nachweis.docx | Rechtschreib-Heuristik (Wörterbuch, unbekannte Wörter ≥ 4 Buchstaben) | 32 unbekannte Wörter: anwendungsfall, arbeitsalltag, aufbewahrungsfrist, bearbeitungszeit, bestehensgrenze, chatbot, datenampel, datenschutzgründen, einzelblatt, freigabeliste, gesundheitsaussagen, gliederungsentwurf, ideensammlung, kundenbeschwerde, kundentexte, lösungsblatt, meldefristen, newsletter, personenbezug, praxisübungen, prompts, rechtsaussagen, rechtsberatung, schulungsleitung, schulungsnachweis, starterkit, teilnahmeliste, teilnahmelisten, webseitentext, wissenstest, zugangsdaten, übersetzungsvorschläge | ja |
| Prompt-Bibliothek.docx | Rechtschreib-Heuristik (Wörterbuch, unbekannte Wörter ≥ 4 Buchstaben) | 106 unbekannte Wörter: abmeldelink, aggregierte, altersangaben, angebotsbegleittext, ansprechpersonen, antwortentwurf, arbeitsalltag, arbeitsblatt, arbeitstitel, auswahlentscheidung, beispielanfragen, beispieldaten, bestandskontakte, bewertungsskala, bildrechte, blogartikel, blogartikels, content, controlling, datenampel, datenpfleger, erklärblöcke, erstgespräch, fachjargon, fachredakteur, feedbackgespräch, feedbackgespräche, führungskräftecoach, gegengerechnet, gegenrechnest, gehaltsangaben, gehaltsversprechen, gesamtfazit, geschäftskontakt, geschäftskorrespondenz, gesprächsstruktur, gesprächsvorbereitung, gesundheits, gesundheitsdaten, gleichbehandlung, handlungsaufforderung, heilversprechen, hinzuerfinden, hochladen, inklusiv, interviewleitfaden, kernbotschaft, kommunikationstrainerin, kundenanfrage, kundenbeispiele, kundeninformation, kundenmanagement, kundennamen, kundennutzen, kundenzahlen, kurzfazit, lerneinheit, lösungsorientiert, nachfassmail, newsletter, onboarding, organisationsberater, personalentwickler, personalreferent, personenbezug, personendaten, pflichtangaben, plausibilitätsblatt, plausibilitätscheck, produktmerkmale, produkttexter, programmierkenntnisse, prompts, prüfblatt, rechtsberatung, rechtskonformität, redaktionsplan, regeländerung, schuldanerkenntnisse, schulungsplan, servicekoordinator, servicekraft, servicetexter, sheets, social, sprachniveau, standardfälle, starterkit, summentabelle, tabellenformel, tabellenkalkulations, tabellenkenntnisse, teamleitungen, testtabelle, tonalitäts, verhaltensbasierte, vertriebsanalyst, vertriebsmitarbeiter, vertriebsmitarbeiterin, vertriebstrainer, vertriebstrainerin, wirkversprechen, wissenscheck, zeitbewusst, zwischenüberschriften, änderungsprotokoll | ja |
| Anpassungs-Prompt.docx | Rechtschreib-Heuristik (Wörterbuch, unbekannte Wörter ≥ 4 Buchstaben) | 38 unbekannte Wörter: alltagsbeispiele, anpassungs, ansprechperson, antwortmöglichkeiten, aufbewahrungsfristen, branchenregeln, datenampel, datenarten, docx, firmenangaben, firmenbezug, firmenname, firmenregeln, freigabeliste, gesetzesverweise, gesetzeszitate, juristendeutsch, kapitelnummern, kapiteltext, kapitelweise, kontaktdaten, lösungsblatt, nutzungsrichtlinie, paragraphenverweise, powerpoint, privatname, produktnamen, prüfungsfragen, rechtsberatung, schulungsfolie, schulungsfolien, sprechernotiz, starterkit, verschwiegenheitspflichten, versionsdatum, weglässt, wissenstest, zugangsdaten | ja |
| Kurzanleitung-In-einer-Woche-eingefuehrt.docx | Rechtschreib-Heuristik (Wörterbuch, unbekannte Wörter ≥ 4 Buchstaben) | 18 unbekannte Wörter: anpassungs, arbeitsblatt, freigabeliste, meldeweg, nutzungsrichtlinie, powerpoint, pptx, rechtsberatung, schulungstag, skills, starterkit, stolpersteine, tabellenauswertungen, teilnahmeliste, uebungen, videokonferenz, wissenstest, xlsx | ja |
| Aha-Uebungen-Arbeitsblatt.docx | Rechtschreib-Heuristik (Wörterbuch, unbekannte Wörter ≥ 4 Buchstaben) | 22 unbekannte Wörter: arbeitsalltag, arbeitsblatt, ausgabeform, beispieltexte, beispielton, erscheinungsjahr, fahrradladen, fahrradladens, imkereibetrieben, konkretheit, kundenbeschwerde, marketingassistenz, mitarbeiterdaten, newsletter, rechtsberatung, reflexionsfrage, schulungsleitung, startauftrag, starterkit, vergleichsfragen, websuche, wintercheck | ja |
| Grundbegriffe-in-einfacher-Sprache.docx | Rechtschreib-Heuristik (Wörterbuch, unbekannte Wörter ≥ 4 Buchstaben) | 20 unbekannte Wörter: datenampel, diagrammtext, fachchinesisch, flowchart, markdown, merkbild, mermaid, modellwahl, nachfassen, nachschlägt, produktinfos, prompts, rechtsberatung, skill, skills, standardantworten, starterkit, tarifbeschreibung, textsprache, tonvorgaben | ja |
| KI-Schulung.pptx | Rechtschreib-Heuristik (Wörterbuch, unbekannte Wörter ≥ 4 Buchstaben) | 64 unbekannte Wörter: ablaufentwurf, annika, ansprechperson, arbeitsalltag, arbeitsblatt, autovervollständigung, beispielprompt, bestehensgrenze, bewerbungs, bewerbungsdaten, bewertungsmatrix, chatbot, chatleiste, datenampel, datenschutzpannen, diagrammtext, einzelauskünfte, fachchinesisch, faktenprüfen, fehlertypen, flipchart, freigabeliste, hochladen, klärungsbedarf, kundenbeschwerde, kundenmail, kundennummer, markdown, meldekultur, mermaid, metadaten, modellwahl, nachschlägt, nachschärfen, neuprüfung, newsletter, notizfeldern, personenbezug, praxisübung, praxisübungen, preiskalkulation, prompts, prüfpflicht, prüfroutinen, rechtsaussagen, rechtsberatung, reflexionsfrage, schlusshinweis, skill, skills, sprachmodelle, starterkit, teilnahmeliste, themenspeicher, transparenzvorgaben, urlaubsantrag, verschwiegenheitspflichten, webseitentext, websuche, wissenstest, zugangsdaten, zugibt, änderungsverfolgung, übungstext | ja |
| Datenschutz-Checkliste-und-Tool-Freigabe.xlsx | Rechtschreib-Heuristik (Wörterbuch, unbekannte Wörter ≥ 4 Buchstaben) | 53 unbekannte Wörter: ablaufbeschreibung, admin, anbieterangaben, angebotskalkulation, anmeldesicherheit, anonymisierung, aufbewahrungsdauer, auftragsverarbeitung, ausschließbar, beispieleinträge, beschäftigtendaten, betroffenenrechte, bewerbungs, bewertungsentscheidungen, bewertungsmatrix, bewertungsskala, datenampel, datenart, datenarten, datenschutzberatung, datenschutzerklärung, datenschutzhinweise, datenschutzprüfung, datenstufen, einsatzzweck, firmenkonto, freigabeliste, konzeptentwurf, krankmeldung, kundenanfrage, kundenmail, metadaten, neuprüfung, neuprüfungsdatum, newsletter, nutzerkreis, nutzerverwaltung, nutzungsbedingungen, personaldaten, personenbezug, personendaten, personennamen, pivot, rechteverwaltung, rechtsberatung, starterkit, urlaubsantrag, verarbeitungstätigkeiten, vorausgefüllt, webseitentext, wissenstest, zugangsdaten, zugriffsschutz | ja |
| KI-Nutzungsrichtlinie.docx | Platzhalter in [ECKIGEN KLAMMERN] | 74 | ja |
| Wissenstest-und-Nachweis.docx | Platzhalter in [ECKIGEN KLAMMERN] | 15 | ja |
| Prompt-Bibliothek.docx | Platzhalter in [ECKIGEN KLAMMERN] | 145 | ja |
| Anpassungs-Prompt.docx | Platzhalter in [ECKIGEN KLAMMERN] | 13 | ja |
| Kurzanleitung-In-einer-Woche-eingefuehrt.docx | Platzhalter in [ECKIGEN KLAMMERN] | 1 | ja |
| Aha-Uebungen-Arbeitsblatt.docx | Platzhalter in [ECKIGEN KLAMMERN] | 9 | ja |
| Grundbegriffe-in-einfacher-Sprache.docx | Platzhalter in [ECKIGEN KLAMMERN] | 7 | ja |
| KI-Schulung.pptx | Platzhalter in [ECKIGEN KLAMMERN] | 22 | ja |
| Datenschutz-Checkliste-und-Tool-Freigabe.xlsx | Platzhalter in [ECKIGEN KLAMMERN] | 11 | ja |
| KI-Nutzungsrichtlinie.docx | ZIP-/OOXML-Integrität (testzip) | ok | ja |
| Wissenstest-und-Nachweis.docx | ZIP-/OOXML-Integrität (testzip) | ok | ja |
| Prompt-Bibliothek.docx | ZIP-/OOXML-Integrität (testzip) | ok | ja |
| Anpassungs-Prompt.docx | ZIP-/OOXML-Integrität (testzip) | ok | ja |
| Kurzanleitung-In-einer-Woche-eingefuehrt.docx | ZIP-/OOXML-Integrität (testzip) | ok | ja |
| Aha-Uebungen-Arbeitsblatt.docx | ZIP-/OOXML-Integrität (testzip) | ok | ja |
| Grundbegriffe-in-einfacher-Sprache.docx | ZIP-/OOXML-Integrität (testzip) | ok | ja |
| KI-Schulung.pptx | ZIP-/OOXML-Integrität (testzip) | ok | ja |
| Datenschutz-Checkliste-und-Tool-Freigabe.xlsx | ZIP-/OOXML-Integrität (testzip) | ok | ja |

Methode: Seitenzahlen = PDF-Export mit LibreOffice (Word kann je nach Schrift ±1 Seite abweichen). Formeln = Neuberechnung in LibreOffice auf einer Testkopie mit 7 Szenarien; die gelieferte Datei enthält nur das fiktive Beispiel.

## 2. Anforderungen aus STATE.md (abgehakt)

| # | Anforderung | Stand |
|---|---|---|
| 1 | `KI-Nutzungsrichtlinie.docx`: 6–8 Seiten, Platzhalter in [ECKIGEN KLAMMERN], 12 geforderte Kapitel (Zweck, Geltung, erlaubte/verbotene Nutzung, Daten & Vertraulichkeit, DSGVO, Tool-Freigabe, Kennzeichnung, Prüfpflicht/Halluzinationen, Verantwortlichkeiten, Schulung, Verstöße, Überprüfung) | erfüllt (Kapitel 1–13 + Anhänge, Zählung siehe oben) |
| 2 | `KI-Schulung.pptx`: 18–24 Folien, Sprechernotizen auf jeder Folie, schlichtes Layout, 2 Praxisübungen | erfüllt (Zahlen oben); Layout nur per LibreOffice-Rendering gesichtet, nicht in PowerPoint |
| 3 | `Wissenstest-und-Nachweis.docx`: 12 Fragen mit Lösungsblatt + Teilnahmeliste/Nachweisvorlage | erfüllt |
| 4 | `Datenschutz-Checkliste-und-Tool-Freigabe.xlsx`: Checkliste + Bewertungsmatrix | erfüllt (20 Prüfpunkte, 7 Kriterien + 3 K.-o.-Fragen, Register, Datenampel) |
| 5 | `Prompt-Bibliothek.docx`: Prompts nach Abteilung, je Zweck + Prompt + Hinweis | erfüllt: 34 Prompts (30 in den 5 Pflichtbereichen + 4 Excel-/Auswertungs-Prompts, D19); alle im Kontext-Baukasten (D18) |
| 6 | `Anpassungs-Prompt.docx`: Schritt für Schritt, deutliche Warnung vor vertraulichen/personenbezogenen Daten in öffentlichen KI-Tools, Anonymisierung | erfüllt (Warnkasten direkt am Anfang, wiederholt in Schritt 2) |
| 7 | `Kurzanleitung-In-einer-Woche-eingefuehrt.docx`: 1–2 Seiten | erfüllt (Zahl oben) |
| 8 | `Aha-Uebungen-Arbeitsblatt.docx` (D18): Kernübung „gleicher Prompt ohne/mit Kontext“ + 2–3 weitere Aha-Übungen, Notizfelder, Reflexionsfrage je Übung | erfüllt: 4 Übungen (1 Pflicht + 3 weitere), siehe Abschnitt 3a |
| 9 | `Grundbegriffe-in-einfacher-Sprache.docx` (D19): Chat vs. Agent, Skill, Markdown/.md, Modellwahl, Mermaid; 2–3 Seiten | erfüllt (Seitenzahl oben), tool-neutral, ohne Herstellernamen/Preise/Ranglisten |
| 10 | `QA.md` | diese Datei |
| – | Hinweis „Diese Vorlage ersetzt keine Rechtsberatung.“ in jedem Dokument | erfüllt (Fußzeile/Fußzeilen-Textfeld/Tabellenblatt, zusätzlich Hinweis-Kasten am Anfang) |
| – | Verbotsliste (3 Begriffe) + keine Paragraphen-/Artikelzitate | 0 Treffer (Skript, siehe oben); inhaltlich bleiben Rechtsaussagen allgemein („Datenschutzrecht“, „gesetzliche Meldefristen“, „Transparenzvorgaben“) |
| – | Keine erfundenen Statistiken | Das Kit enthält keine Marktzahlen/Statistiken. Prozentangaben im Kit sind nur Bewertungsschwellen (75 %/50 %), Kürzungsziele in Prompts und die Bestehensgrenze (9 von 12), jeweils als Vorschlag/Platzhalter |
| – | Keine echten Kunden-/Personendaten | Beispiele erfunden und markiert („Übungstext, frei erfunden“, „BEISPIEL (fiktives Tool …)“) |

## 3. Manuelle Prüfung (Lieferagent, Textdurchsicht)

- **Rechtschreibung:** ausgeführt. Eine Wörterbuch-Heuristik (deutsch, pyspellchecker) wurde über den gesamten Text gelegt; die unbekannten Wörter stehen in der Tabelle oben und wurden durchgesehen (es handelt sich um Fachwörter, Komposita, Eigennamen und Platzhalter-Fragmente; Tippfehler, die ein reales Wort ergeben, findet die Heuristik nicht). Grammatik und Stil wurden **nicht** maschinell geprüft. → Ankes Endabnahme sollte jede Datei einmal lesen.
- **Wissenstest:** Lösungen mit den Erklärungen in Richtlinie/Folien abgeglichen; richtige Antworten gleichmäßig auf A–D verteilt.
- **Konsistenz:** Datenampel (grün/gelb/rot) und Freigabestufen 1/2/3 sind in Richtlinie, Folien, Test, Excel und Prompt-Bibliothek gleich definiert; Prüfverfahren „5-Punkte-Prüfung“ überall identisch.
- **Praxisübung 2 (Folie 17):** Der Übungstext ist frei erfunden und enthält absichtlich Fehler; Aktenzeichen ist als „[erfunden]“ gekennzeichnet.

## 3a. Umsetzung der Aha-Übungen (D18) und Ergänzungen (D19)

- **Prinzip „Erleben vor Erklären“:** In `KI-Schulung.pptx` folgen Aha-Übung 1 (Folie 3 Anleitung, Folie 4 Auswertung/Vergleichsfragen) direkt auf die Zielfolie, **vor** jeder Erklärung. Erst danach kommt der Kontext-Baukasten (Folie 14), der erklärt, was die Gruppe selbst erlebt hat. Die Sprechernotizen verbieten der Schulungsleitung ausdrücklich, vorher zu erklären.
- **Aha-Übung 1 (Pflicht):** gleicher Auftrag zweimal an das KI-Tool: erst nackt („Schreib eine Antwort auf diese Kundenbeschwerde“), dann mit Baukasten (Rolle, Ziel, Zielgruppe, Ton, Beispiel, Format, Grenzen). Erfundene Beschwerde im Arbeitsblatt, Vergleichstabelle mit 5 Kriterien, 3 Vergleichsfragen, Reflexionsfrage, Notizfelder.
- **Weitere Übungen (Arbeitsblatt, 1 Folie als Überblick):** (2) Halluzination provozieren und entlarven: nach Fachbüchern zu einem erfundenen Nischenthema fragen, jedes Buch selbst nachsuchen, dann „Bist du sicher?“ und eine Variante mit Grenzen; (3) schlechten Prompt in vier Runden verbessern; (4) Aufgabe mit und ohne Beispiel. Alle ohne Fachwissen, mit erfundenen oder öffentlichen Beispielen, ohne vertrauliche Daten.
- **Prompt-Bibliothek:** jeder der 34 Prompts besteht aus den Feldern ROLLE/ZIEL/ZIELGRUPPE/TON/BEISPIEL/FORMAT/GRENZEN/MATERIAL (automatisch geprüft, siehe Tabelle); die Baukasten-Erklärung steht am Anfang.
- **Plausibilitätscheck (D19):** 4 Excel-/Auswertungs-Prompts fordern alle ein Blatt „Plausibilität“ (Gegenrechnen von Summen, Stichproben, Ausreißern); ein Satz erklärt warum („KI kann sich verrechnen, der Plausibilitätscheck macht Fehler sichtbar“).
- **Änderungen an v1 durch die Ergänzungen:** Schulungsdauer von 75 auf ca. 90 Minuten (bis 120 mit allen Aha-Übungen) – Schätzung, nicht gemessen. Um bei 24 Folien zu bleiben, wurden vier Foliengruppen zusammengelegt (KI-Grundlagen, Richtlinie/erlaubt/verboten, personenbezogene/vertrauliche Daten, Kennzeichnung/Melden); die Inhalte stehen weiter in Folien und Sprechernotizen, die Folien sind dadurch dichter. Grundbegriffe: Folien 20–22 plus eigenes Dokument. „Nächster Schritt“ (ohne Werbung) in der Kurzanleitung; Aufbauthemen (Präsentations-, Formular-, Excel-Workflows, eigene Skills) sind nicht enthalten.
- **Aha-Wirkung nicht getestet:** Ob die Übungen bei echten Teilnehmenden den erhofften Aha-Effekt auslösen, ist unbelegt; die Ergebnisse hängen vom Tool ab (Übung 2 besonders: Tools mit Websuche können korrekte Quellen liefern, das Arbeitsblatt weist darauf hin).

## 4. Bekannte Grenzen (ehrlich)

1. **Nicht in Microsoft Office geöffnet.** Geprüft wurde mit python-docx/-pptx/openpyxl und LibreOffice. Seitenumbrüche und Folienlayout können in Word/PowerPoint minimal abweichen. Bitte einmal in Word/PowerPoint/Excel öffnen und Seitenzahlen sowie die Folien 3, 8, 10, 12, 17 und 19 (viel Text; Layout nur im LibreOffice-Rendering geprüft) ansehen.
2. **Keine Rechtsprüfung.** Kein Jurist hat die Texte gesehen. Rechtliche Aussagen sind absichtlich allgemein gehalten; ob und wie die Vorlage zu einem konkreten Betrieb, Tarif- oder Betriebsratsfall passt, ist offen. Zur EU-KI-Verordnung und zur Rechtslage enthält das Kit bewusst keine Detailaussagen und keine Zitate (Scout-A-Quellen waren nur Suchsnippets, D17).
3. **Nicht an echten Nutzerinnen/Nutzern getestet.** Dass die Zielperson das Kit „in einer Woche“ einsetzen kann, ist eine Planungsannahme (Zeitschätzung in der Kurzanleitung: ca. 8–10 Stunden, **Schätzung, nicht gemessen**). Test mit 1–2 Personen aus Ankes Umfeld oder bezahlten Erstkäufern wäre der erste Beleg.
4. **Die KI-Anpassungsprompts (A–D) wurden nicht gegen ein KI-Tool ausgeführt** (kein Tool-Zugriff vorgesehen). Ihre Wirkung ist unerprobt; die Schutzregeln im Prompt (nichts erfinden, keine Zitate, Änderungen markieren) sind Absicht, keine Garantie.
5. **Keine Tool-Bewertungen realer Produkte.** Die Excel-Matrix enthält nur ein fiktives Beispiel. Schwellen (75 %/50 %) und Gewichte sind Vorschläge ohne empirische Grundlage.
6. **Schulung:** Zeitbedarf (90 Min.) und Übungsdauer (je 10 Min.) sind Schätzungen. Folie 6 beschreibt das Halluzinations-Muster allgemein; es werden bewusst keine konkreten Vorfälle genannt (nicht belegt).
7. **Marktbezug:** Das Kit sagt nichts über gesetzliche Pflichten zur Schulung. Der Stand der Rechtslage (Scout A, Sekundärquellen) ist ungeprüft; Marketingtexte (Vertrieb) dürfen daraus keine Pflicht ableiten.
8. **Nutzungsrechte/Lizenz:** Das Kit enthält keine Lizenz- oder Nutzungsbedingungen und keinen Anbieter-/Impressumshinweis. Das ist eine Entscheidung für Anke (Digistore24/Fiverr-AGB, Weitergabe, Branding). Bewusst nicht erfunden.
9. **Barrierefreiheit:** Kontrast/Struktur sind schlicht gehalten, aber nicht mit einem Prüfwerkzeug getestet. Alt-Texte entfallen, da keine Bilder enthalten sind.
10. **Rechtschreibprüfung:** nur Wörterbuch-Heuristik (siehe oben), kein Duden-/Grammatik-Check.

## 5. Reproduktion

```
cd company/deliveries/produkt-ki-starterkit-v1
pip install python-docx python-pptx openpyxl pypdf pyspellchecker
python3 build/build_kit.py     # erzeugt die 9 Office-Dateien
python3 build/verify_kit.py    # prüft und schreibt QA.md neu
```
Varianten (Englisch, Branchen): Texte in `build/b1_…b7_*.py` ersetzen, Layout steckt in `build/kit_lib.py`. `KIT_OUT=<Ordner>` leitet die Ausgabe um.
