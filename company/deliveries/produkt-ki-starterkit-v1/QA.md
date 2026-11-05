# QA-Protokoll — KI-Starterkit v1

Erstellt: 2026-11-05 · Erzeugt mit `build/build_kit.py`, geprüft mit `build/verify_kit.py` (Ausführung: 2026-11-05 15:18).
Automatische Prüfungen: **61 von 61 bestanden**

## 1. Automatische Prüfungen (Skript, reproduzierbar)

| Datei | Prüfung | Ergebnis | OK |
|---|---|---|---|
| KI-Nutzungsrichtlinie.docx | Öffnen mit python-docx; PDF-Export mit LibreOffice; Seitenzahl | 7 Seiten (Soll 6–8); 112 Absätze, 10 Tabellen | ja |
| KI-Nutzungsrichtlinie.docx | Hinweis „ersetzt keine Rechtsberatung“ | vorhanden (2×, inkl. Fußzeile) | ja |
| Wissenstest-und-Nachweis.docx | Öffnen mit python-docx; PDF-Export mit LibreOffice; Seitenzahl | 6 Seiten; 92 Absätze, 7 Tabellen | ja |
| Wissenstest-und-Nachweis.docx | Hinweis „ersetzt keine Rechtsberatung“ | vorhanden (2×, inkl. Fußzeile) | ja |
| Prompt-Bibliothek.docx | Öffnen mit python-docx; PDF-Export mit LibreOffice; Seitenzahl | 11 Seiten; 52 Absätze, 33 Tabellen | ja |
| Prompt-Bibliothek.docx | Hinweis „ersetzt keine Rechtsberatung“ | vorhanden (2×, inkl. Fußzeile) | ja |
| Anpassungs-Prompt.docx | Öffnen mit python-docx; PDF-Export mit LibreOffice; Seitenzahl | 5 Seiten; 44 Absätze, 9 Tabellen | ja |
| Anpassungs-Prompt.docx | Hinweis „ersetzt keine Rechtsberatung“ | vorhanden (3×, inkl. Fußzeile) | ja |
| Kurzanleitung-In-einer-Woche-eingefuehrt.docx | Öffnen mit python-docx; PDF-Export mit LibreOffice; Seitenzahl | 1 Seiten (Soll 1–2); 17 Absätze, 1 Tabellen | ja |
| Kurzanleitung-In-einer-Woche-eingefuehrt.docx | Hinweis „ersetzt keine Rechtsberatung“ | vorhanden (2×, inkl. Fußzeile) | ja |
| KI-Schulung.pptx | Öffnen mit python-pptx; Folienzahl | 22 Folien (Soll 18–24) | ja |
| KI-Schulung.pptx | Sprechernotiz auf jeder Folie | 22/22 Folien mit Notiz > 40 Zeichen; kürzeste 217 Zeichen | ja |
| KI-Schulung.pptx | Zwei Praxisübungen | Folien [13, 17] | ja |
| KI-Schulung.pptx | Hinweis „ersetzt keine Rechtsberatung“ | auf 22/22 Folien (Fußzeile) | ja |
| KI-Schulung.pptx | PDF-Export mit LibreOffice (Rendern möglich) | 22 Seiten | ja |
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
| Prompt-Bibliothek.docx | Anzahl Prompts (Tabellen mit Nr.) | 30 (Soll 30); je Bereich {'Verwaltung': 6, 'Vertrieb': 6, 'Kundenservice': 6, 'Marketing': 6, 'Personal': 6} | ja |
| Prompt-Bibliothek.docx | Jeder Prompt hat Zweck, Prompt-Text und Hinweis | ja | ja |
| Wissenstest-und-Nachweis.docx | 12 Fragen mit je 4 Antworten und Lösung | 12 Fragen; Verteilung richtiger Antworten {'A': 3, 'B': 3, 'C': 3, 'D': 3} | ja |
| alle 7 Dateien | Verbotsliste: Verbotsbegriff 1 (rechts-sicher) | 0 Treffer | ja |
| alle 7 Dateien | Verbotsliste: Verbotsbegriff 2 (erfüllt … AI Act) | 0 Treffer | ja |
| alle 7 Dateien | Verbotsliste: Verbotsbegriff 3 (zertifiziert) | 0 Treffer | ja |
| alle 7 Dateien | Verbotsliste: Paragraphenzeichen § | 0 Treffer | ja |
| alle 7 Dateien | Verbotsliste: Artikelzitat 'Art. <Zahl>' | 0 Treffer | ja |
| alle 7 Dateien | Verbotsliste: 'AI Act' (irgendwo) | 0 Treffer | ja |
| KI-Nutzungsrichtlinie.docx | Rechtschreib-Heuristik (Wörterbuch, unbekannte Wörter ≥ 4 Buchstaben) | 72 unbekannte Wörter: angebotstext, ansprechperson, anwendungsfall, anwendungsfälle, audio, audiogeneratoren, auftragsverarbeitung, bewerbungsauswahl, bewertungsmatrix, chatbot, datenabfluss, datenampel, datenschutzhinweise, datenschutzpanne, datenschutzpannen, datenschutzprüfung, datenschutzrecht, dokumentinfo, dsgvo, entscheidungsvorschläge, erstfassung, firmenbezug, freigabeliste, freigabestufe, freigabestufen, gesundheitsangaben, gesundheitsaussagen, gesundheitsdaten, grundverordnung, hochgeladene, hochladen, hochzuladen, ideensammlung, kundennummer, meldefristen, metadaten, mitarbeiterbewertung, nachschulen, neuprüfung, nutzungsbedingungen, nutzungsrichtlinie, personenbezug, personendaten, plug, preiskalkulationen, produktivsysteme, protokollwerkzeuge, prüfpflicht, rechtsberatung, rohentwurf, routinearbeit, schulungsfolien, selbstprüfung, skripte, social, sprachmodelle, starterkit, tabellenformeln, teilnahmeliste, transkriptions, transparenzvorgaben, verarbeitungstätigkeiten, videokonferenzen, webseitentexte, wissenstest, xlsx, zahlungsdaten, zugangsdaten, zurückgibt, änderungsprotokoll, übersetzungsdiensten, übungsbeispiele | ja |
| Wissenstest-und-Nachweis.docx | Rechtschreib-Heuristik (Wörterbuch, unbekannte Wörter ≥ 4 Buchstaben) | 32 unbekannte Wörter: anwendungsfall, arbeitsalltag, aufbewahrungsfrist, bearbeitungszeit, bestehensgrenze, chatbot, datenampel, datenschutzgründen, einzelblatt, freigabeliste, gesundheitsaussagen, gliederungsentwurf, ideensammlung, kundenbeschwerde, kundentexte, lösungsblatt, meldefristen, newsletter, personenbezug, praxisübungen, prompts, rechtsaussagen, rechtsberatung, schulungsleitung, schulungsnachweis, starterkit, teilnahmeliste, teilnahmelisten, webseitentext, wissenstest, zugangsdaten, übersetzungsvorschläge | ja |
| Prompt-Bibliothek.docx | Rechtschreib-Heuristik (Wörterbuch, unbekannte Wörter ≥ 4 Buchstaben) | 73 unbekannte Wörter: abmeldelink, altersangaben, angebotsbegleittext, ansprechpersonen, antwortentwurf, arbeitsalltag, arbeitstitel, auswahlentscheidung, beispielanfragen, beispieldaten, bestandskontakte, bewertungsskala, bildrechte, blogartikel, blogartikels, datenampel, erklärblöcke, erstgespräch, feedbackgespräch, feedbackgespräche, gehaltsangaben, gehaltsversprechen, gesamtfazit, geschlechtsfestlegung, gesprächsstruktur, gesprächsvorbereitung, gesundheitsdaten, gleichbehandlung, handlungsaufforderung, heilversprechen, hochladen, inklusiv, interviewleitfaden, kernbotschaft, kundenanfrage, kundenbeispiele, kundenbeschwerde, kundenfragen, kundenmanagement, kundennamen, kundennutzen, kundenzahlen, lerneinheit, lösungsorientiert, nachfassmail, newsletter, newsletters, onboarding, personendaten, pflichtangaben, produktmerkmale, prompts, rechtsberatung, rechtskonformität, redaktionsplan, regeländerung, schuldanerkenntnisse, schulungsplan, sheets, social, sprachniveau, standardfälle, starterkit, tabellenformel, testtabelle, tonalitäts, verhaltensbasierten, vertriebsmitarbeiter, vorbereitungsaufgabe, webseitentext, wirkversprechen, wissenscheck, zwischenüberschriften | ja |
| Anpassungs-Prompt.docx | Rechtschreib-Heuristik (Wörterbuch, unbekannte Wörter ≥ 4 Buchstaben) | 38 unbekannte Wörter: alltagsbeispiele, anpassungs, ansprechperson, antwortmöglichkeiten, aufbewahrungsfristen, branchenregeln, datenampel, datenarten, docx, firmenangaben, firmenbezug, firmenname, firmenregeln, freigabeliste, gesetzesverweise, gesetzeszitate, juristendeutsch, kapitelnummern, kapiteltext, kapitelweise, kontaktdaten, lösungsblatt, nutzungsrichtlinie, paragraphenverweise, powerpoint, privatname, produktnamen, prüfungsfragen, rechtsberatung, schulungsfolie, schulungsfolien, sprechernotiz, starterkit, verschwiegenheitspflichten, versionsdatum, weglässt, wissenstest, zugangsdaten | ja |
| Kurzanleitung-In-einer-Woche-eingefuehrt.docx | Rechtschreib-Heuristik (Wörterbuch, unbekannte Wörter ≥ 4 Buchstaben) | 14 unbekannte Wörter: anpassungs, freigabeliste, meldeweg, nutzungsrichtlinie, powerpoint, pptx, rechtsberatung, schulungstag, starterkit, stolpersteine, teilnahmeliste, videokonferenz, wissenstest, xlsx | ja |
| KI-Schulung.pptx | Rechtschreib-Heuristik (Wörterbuch, unbekannte Wörter ≥ 4 Buchstaben) | 59 unbekannte Wörter: ablaufentwurf, annika, ansprechperson, arbeitsalltag, autovervollständigung, bestehensgrenze, bewerbungs, bewerbungsdaten, bewertungsmatrix, bildgeneratoren, chatbot, chatleiste, datenabfluss, datenampel, datenschutzpannen, einzelauskünfte, fachchinesisch, faktenprüfen, fehlertypen, firmendaten, flipchart, freigabeliste, hochladen, klärungsbedarf, krankmeldungen, kundenberaterin, kundenbeschwerde, kundenmail, kundennummer, meldekultur, metadaten, nachschärfen, neuprüfung, newsletter, personenbezug, praxisübung, preiskalkulation, preiskalkulationen, prompts, prüfpflicht, prüfroutinen, rechtsaussagen, rechtsberatung, schiefgeht, schlusshinweis, sprachmodell, sprachmodelle, starterkit, teilnahmeliste, themenspeicher, transparenzvorgaben, urlaubsantrag, verschwiegenheitspflichten, webseitentext, wissenstest, zugangsdaten, zugibt, änderungsverfolgung, übungstext | ja |
| Datenschutz-Checkliste-und-Tool-Freigabe.xlsx | Rechtschreib-Heuristik (Wörterbuch, unbekannte Wörter ≥ 4 Buchstaben) | 53 unbekannte Wörter: ablaufbeschreibung, admin, anbieterangaben, angebotskalkulation, anmeldesicherheit, anonymisierung, aufbewahrungsdauer, auftragsverarbeitung, ausschließbar, beispieleinträge, beschäftigtendaten, betroffenenrechte, bewerbungs, bewertungsentscheidungen, bewertungsmatrix, bewertungsskala, datenampel, datenart, datenarten, datenschutzberatung, datenschutzerklärung, datenschutzhinweise, datenschutzprüfung, datenstufen, einsatzzweck, firmenkonto, freigabeliste, konzeptentwurf, krankmeldung, kundenanfrage, kundenmail, metadaten, neuprüfung, neuprüfungsdatum, newsletter, nutzerkreis, nutzerverwaltung, nutzungsbedingungen, personaldaten, personenbezug, personendaten, personennamen, pivot, rechteverwaltung, rechtsberatung, starterkit, urlaubsantrag, verarbeitungstätigkeiten, vorausgefüllt, webseitentext, wissenstest, zugangsdaten, zugriffsschutz | ja |
| KI-Nutzungsrichtlinie.docx | Platzhalter in [ECKIGEN KLAMMERN] | 74 | ja |
| Wissenstest-und-Nachweis.docx | Platzhalter in [ECKIGEN KLAMMERN] | 15 | ja |
| Prompt-Bibliothek.docx | Platzhalter in [ECKIGEN KLAMMERN] | 87 | ja |
| Anpassungs-Prompt.docx | Platzhalter in [ECKIGEN KLAMMERN] | 13 | ja |
| Kurzanleitung-In-einer-Woche-eingefuehrt.docx | Platzhalter in [ECKIGEN KLAMMERN] | 1 | ja |
| KI-Schulung.pptx | Platzhalter in [ECKIGEN KLAMMERN] | 22 | ja |
| Datenschutz-Checkliste-und-Tool-Freigabe.xlsx | Platzhalter in [ECKIGEN KLAMMERN] | 11 | ja |
| KI-Nutzungsrichtlinie.docx | ZIP-/OOXML-Integrität (testzip) | ok | ja |
| Wissenstest-und-Nachweis.docx | ZIP-/OOXML-Integrität (testzip) | ok | ja |
| Prompt-Bibliothek.docx | ZIP-/OOXML-Integrität (testzip) | ok | ja |
| Anpassungs-Prompt.docx | ZIP-/OOXML-Integrität (testzip) | ok | ja |
| Kurzanleitung-In-einer-Woche-eingefuehrt.docx | ZIP-/OOXML-Integrität (testzip) | ok | ja |
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
| 5 | `Prompt-Bibliothek.docx`: 30 Prompts, 5 Bereiche, je Zweck + Prompt + Hinweis | erfüllt |
| 6 | `Anpassungs-Prompt.docx`: Schritt für Schritt, deutliche Warnung vor vertraulichen/personenbezogenen Daten in öffentlichen KI-Tools, Anonymisierung | erfüllt (Warnkasten direkt am Anfang, wiederholt in Schritt 2) |
| 7 | `Kurzanleitung-In-einer-Woche-eingefuehrt.docx`: 1–2 Seiten | erfüllt (Zahl oben) |
| 8 | `QA.md` | diese Datei |
| – | Hinweis „Diese Vorlage ersetzt keine Rechtsberatung.“ in jedem Dokument | erfüllt (Fußzeile/Fußzeilen-Textfeld/Tabellenblatt, zusätzlich Hinweis-Kasten am Anfang) |
| – | Verbotsliste (3 Begriffe) + keine Paragraphen-/Artikelzitate | 0 Treffer (Skript, siehe oben); inhaltlich bleiben Rechtsaussagen allgemein („Datenschutzrecht“, „gesetzliche Meldefristen“, „Transparenzvorgaben“) |
| – | Keine erfundenen Statistiken | Das Kit enthält keine Marktzahlen/Statistiken. Prozentangaben im Kit sind nur Bewertungsschwellen (75 %/50 %), Kürzungsziele in Prompts und die Bestehensgrenze (9 von 12), jeweils als Vorschlag/Platzhalter |
| – | Keine echten Kunden-/Personendaten | Beispiele erfunden und markiert („Übungstext, frei erfunden“, „BEISPIEL (fiktives Tool …)“) |

## 3. Manuelle Prüfung (Lieferagent, Textdurchsicht)

- **Rechtschreibung:** ausgeführt. Eine Wörterbuch-Heuristik (deutsch, pyspellchecker) wurde über den gesamten Text gelegt; die unbekannten Wörter stehen in der Tabelle oben und wurden durchgesehen (es handelt sich um Fachwörter, Komposita, Eigennamen und Platzhalter-Fragmente; Tippfehler, die ein reales Wort ergeben, findet die Heuristik nicht). Grammatik und Stil wurden **nicht** maschinell geprüft. → Ankes Endabnahme sollte jede Datei einmal lesen.
- **Wissenstest:** Lösungen mit den Erklärungen in Richtlinie/Folien abgeglichen; richtige Antworten gleichmäßig auf A–D verteilt.
- **Konsistenz:** Datenampel (grün/gelb/rot) und Freigabestufen 1/2/3 sind in Richtlinie, Folien, Test, Excel und Prompt-Bibliothek gleich definiert; Prüfverfahren „5-Punkte-Prüfung“ überall identisch.
- **Praxisübung 2 (Folie 17):** Der Übungstext ist frei erfunden und enthält absichtlich Fehler; Aktenzeichen ist als „[erfunden]“ gekennzeichnet.

## 4. Bekannte Grenzen (ehrlich)

1. **Nicht in Microsoft Office geöffnet.** Geprüft wurde mit python-docx/-pptx/openpyxl und LibreOffice. Seitenumbrüche und Folienlayout können in Word/PowerPoint minimal abweichen. Bitte einmal in Word/PowerPoint/Excel öffnen und Seitenzahlen sowie die Folien 13, 17 und 18 (viel Text; im LibreOffice-Rendering ohne Überlauf) ansehen.
2. **Keine Rechtsprüfung.** Kein Jurist hat die Texte gesehen. Rechtliche Aussagen sind absichtlich allgemein gehalten; ob und wie die Vorlage zu einem konkreten Betrieb, Tarif- oder Betriebsratsfall passt, ist offen. Zur EU-KI-Verordnung und zur Rechtslage enthält das Kit bewusst keine Detailaussagen und keine Zitate (Scout-A-Quellen waren nur Suchsnippets, D17).
3. **Nicht an echten Nutzerinnen/Nutzern getestet.** Dass die Zielperson das Kit „in einer Woche“ einsetzen kann, ist eine Planungsannahme (Zeitschätzung in der Kurzanleitung: ca. 8–10 Stunden, **Schätzung, nicht gemessen**). Test mit 1–2 Personen aus Ankes Umfeld oder bezahlten Erstkäufern wäre der erste Beleg.
4. **Die KI-Anpassungsprompts (A–D) wurden nicht gegen ein KI-Tool ausgeführt** (kein Tool-Zugriff vorgesehen). Ihre Wirkung ist unerprobt; die Schutzregeln im Prompt (nichts erfinden, keine Zitate, Änderungen markieren) sind Absicht, keine Garantie.
5. **Keine Tool-Bewertungen realer Produkte.** Die Excel-Matrix enthält nur ein fiktives Beispiel. Schwellen (75 %/50 %) und Gewichte sind Vorschläge ohne empirische Grundlage.
6. **Schulung:** Zeitbedarf (75 Min.) und Übungsdauer (je 10 Min.) sind Schätzungen. Folie 6 beschreibt das Halluzinations-Muster allgemein; es werden bewusst keine konkreten Vorfälle genannt (nicht belegt).
7. **Marktbezug:** Das Kit sagt nichts über gesetzliche Pflichten zur Schulung. Der Stand der Rechtslage (Scout A, Sekundärquellen) ist ungeprüft; Marketingtexte (Vertrieb) dürfen daraus keine Pflicht ableiten.
8. **Nutzungsrechte/Lizenz:** Das Kit enthält keine Lizenz- oder Nutzungsbedingungen und keinen Anbieter-/Impressumshinweis. Das ist eine Entscheidung für Anke (Digistore24/Fiverr-AGB, Weitergabe, Branding). Bewusst nicht erfunden.
9. **Barrierefreiheit:** Kontrast/Struktur sind schlicht gehalten, aber nicht mit einem Prüfwerkzeug getestet. Alt-Texte entfallen, da keine Bilder enthalten sind.
10. **Rechtschreibprüfung:** nur Wörterbuch-Heuristik (siehe oben), kein Duden-/Grammatik-Check.

## 5. Reproduktion

```
cd company/deliveries/produkt-ki-starterkit-v1
pip install python-docx python-pptx openpyxl pypdf pyspellchecker
python3 build/build_kit.py     # erzeugt die 7 Office-Dateien
python3 build/verify_kit.py    # prüft und schreibt QA.md neu
```
Varianten (Englisch, Branchen): Texte in `build/b1_…b7_*.py` ersetzen, Layout steckt in `build/kit_lib.py`. `KIT_OUT=<Ordner>` leitet die Ausgabe um.
