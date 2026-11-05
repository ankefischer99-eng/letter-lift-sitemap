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

## D10 · 2026-11-05 · H2 (Ankes Expertise) wird Hauptlinie, H1 (Marktplatz) wird Rückfallebene
Begründung: Scout-Lauf 1 zeigt Medianpreise von ca. $50 auf einer US-Plattform mit Gebühren, neuem Profil ohne Bewertungen und englischer Kommunikation (D9). Bei 10 h/Woche ist Ankes Stunde zu wertvoll für $30-Aufträge. H2 bietet höhere Preise, DACH, Deutsch und Glaubwürdigkeit.
Bedingung bleibt: H2 startet erst nach T2 (Arbeitsvertrag) und T7.
H1 bleibt nur für Typ D (Tabellen/Daten/Präsentationen) als Rückfallebene, falls H2 rechtlich nicht geht.
Überprüfen: nach T2 und Scout-Lauf 2.

## D11 · 2026-11-05 · Rechtlicher Rahmen geklärt, Suchraum geöffnet
Anke hat Nebentätigkeit angemeldet, Gewerbe, Kleinunternehmerregelung, USt-ID. Firma darf jedes legale Geschäft prüfen; Graubereiche (nicht illegal) werden vor Start mit Anke als Advisor diskutiert und in DECISIONS dokumentiert.
Restgrenze: Angebote für den Kundenservice der Energiewirtschaft vorher mit Anke abklären (Wettbewerb zum Arbeitgeber).

## D12 · 2026-11-05 · Portfolio für Woche 1: zwei Wetten, eine Rückfallebene
Auswahlkriterien: (1) belegte, bezahlte Nachfrage existiert schon, (2) Agenten liefern in hoher Qualität, (3) wenig Anke-Zeit pro Euro, (4) wiederholbar/automatisierbar, (5) erreichbar ohne eigene Reichweite.
- **Wette A — KI-Kompetenz/AI Enablement für Kleinbetriebe (DACH).** Hypothese: Seit 2. Feb. 2025 verlangt Art. 4 EU AI Act, dass Betreiber von KI-Systemen für ausreichende KI-Kompetenz ihres Personals sorgen. Das erzeugt Nachfrage nach Schulung + Nachweis. Anke ist im Hauptberuf für AI Enablement und Training verantwortlich (Glaubwürdigkeit). Produkt: standardisiertes Schulungs- und Nachweispaket, von Agenten produziert, optional Live-Session durch Anke. **Unsicherheit:** Die EU hat 2025 Änderungen an Art. 4 diskutiert (Digital Omnibus). Ob und wie die Pflicht im Nov. 2026 gilt, ist nicht geprüft → Scout A klärt das zuerst. Ohne Pflicht schwächere, aber nicht tote Nachfrage.
- **Wette B — Deutschsprachige digitale Vorlagen auf Marktplätzen mit eigener Suchnachfrage** (z. B. Etsy, Digistore24). Hypothese: Marktplätze liefern Käufer ohne eigene Reichweite; Agenten produzieren Vorlagen; Anke lädt hoch. Vollständig skalierbar, Grenzkosten ≈ 0. Risiko: Sättigung, niedrige Preise. Ausgeschlossen: Vorlagen, die Rechtsberatung ersetzen sollen (Verträge u. Ä.) ohne gesonderte Diskussion.
- **Rückfallebene — H1 Typ D** (Tabellen/Daten auf Marktplätzen).
Abbruch: Wette A stirbt, wenn Scout A weder Rechtspflicht noch bezahlte Nachfrage im Kleinbetriebssegment belegt. Wette B stirbt, wenn Scout B keine 5 Nischen mit belegten Verkäufen und < 50 Wettbewerbern findet.
Verworfen (vorerst): Affiliate (Reichweite nötig), Arbitrage/Reselling (Kapitalbindung), eigene SaaS (F1), Werbung (kein Konversionsbeleg).

## D13 · 2026-11-05 · TikTok „Revelations" ist das einzige echte Reichweiten-Asset
> 1.000 Follower mit KI-Themen = bestehendes, thematisch passendes Publikum. Substack (6–7) ist vorerst kein Kanal.
Nutzung: (1) Vertriebskanal für eigene Produkte aus Wette A, (2) Affiliate für KI-/Tech-Tools als Zusatz.
Ehrliche Erwartung Affiliate: bei ~1.000 Followern Einnahmen im einstelligen bis niedrigen zweistelligen €-Bereich pro Monat (ANNAHME, abhängig von Views und Klickrate; wird gemessen, nicht geglaubt). Pflicht: Werbekennzeichnung („Anzeige"/Affiliate-Hinweis).
Entscheidung über Affiliate erst nach Analytics (T9): Land, Alter, Ø-Views.

## D14 · 2026-11-05 · Wette A bekommt Produktform: „KI-Starterpaket für Unternehmen"
Ankes Idee übernommen und geschärft. Bausteine: Präsentation (Live-Schulung), E-Learning-Modul, Wissenstest, Teilnahmenachweis, Muster-KI-Nutzungsrichtlinie, Datenschutz-Kapitel (DSGVO, keine Personendaten in öffentliche KI-Tools, Freigabeprozess).
Agenten-Hebel: **Anpassung an die Richtlinien des Kunden** — Kunde liefert seine Regeln, Lieferagent baut das Paket darauf um. Das ist Arbeit, die Agenten schnell und gut können und Menschen teuer ist.
Grenzen: keine Garantie „erfüllt Art. 4 AI Act" oder „rechtssicher" (keine Rechtsberatung, RDG); stattdessen „unterstützt beim Aufbau von KI-Kompetenz und dokumentiert die Schulung".
Preise und Stufen erst nach Scout-A-Daten (Wettbewerbspreise). Kein Bau vor Auswertung.

## D15 · 2026-11-05 · Wechsel von Recherche zu Verkaufstest; Wette A als Live-Paket testen, Wette B pausiert
Begründung: F4. Der günstigste Weg zu einem Nachfragebeleg ist jetzt ein echtes Angebot an echte Menschen, nicht ein vierter Recherchelauf.
- **Wette A → Experiment E4 „KI-Starter für Teams"**: Live-Online-Workshop 90 Min für Teams bis 10 Personen + an die eigenen Regeln angepasste KI-Nutzungsrichtlinie + Teilnahmedokumentation. **Testpreis 390 € Pauschale** (Kleinunternehmerin, keine USt).
  Preislogik: Wettbewerb rechnet pro Person (119–690 €/TN live); bei 4+ Teilnehmenden sind wir günstiger und liefern zusätzlich die Anpassung, die Agenten billig herstellen.
  Ankes Zeit: ca. 90 Min Workshop + 30 Min Abstimmung ≈ 2 h → ca. 195 €/h vor Steuer.
  Vertrieb ohne Produkt: Erst verkaufen, dann bauen. Material entsteht erst bei Zusage (Lieferagent, 3–5 Tage).
- **Wette B pausiert** bis echte Verkaufsdaten (T8 oder manuelle Stichprobe). Kein Bau.
- **Recherche pausiert** bis T8.
Graubereich bewusst ausgeschlossen: keine Aussagen wie „erfüllt Art. 4" oder „rechtssicher" (RDG, irreführende Werbung).
Überprüfen: E4-Abbruchkriterium.

## D16 · 2026-11-05 · E4 gestoppt; neue harte Randbedingung: Geschäft muss ohne Ankes Auftritt funktionieren
Anke tritt nicht live, nicht mit Gesicht und nicht öffentlich auf. Damit fallen: Workshops, Beratungsgespräche, persönliche Akquise über Ankes Netzwerk, alles mit Personenmarke.
Es bleiben: rein digitale Produkte und asynchrone, schriftliche Leistungen, die Agenten erstellen und Anke höchstens freigibt.
Vertriebsagent-Sitzung abgebrochen, Prüftermin gelöscht. Nächste Wette erst nach Klärung von Ankes Ja/Nein-Liste.

## D17 · 2026-11-05 · Produkt „KI-Starterkit für kleine Unternehmen" (DE), ein Produkt, drei Kanäle
Problem: In kleinen Firmen bekommt eine Person den Auftrag „KI-Regeln + Schulung" ohne Zeit und Vorlage. Markt (Scout A) bietet fast nur Kurse pro Person (10–690 €/TN), kein selbst einsetzbares, bearbeitbares Komplettpaket (Hinweis, nicht bewiesen).
Produkt (einmal bauen, beliebig verkaufen): Richtlinie (DOCX), Schulungsfolien mit Sprechernotizen (PPTX), Wissenstest + Schulungsnachweis, Datenschutz-Checkliste + Tool-Freigabematrix, 30 Prompts nach Abteilung, Anpassungs-Prompt zur Selbstanpassung an Firmenregeln, Kurzanleitung.
Kanäle: (1) Digistore24 Selbstbedienung + Affiliate-Marktplatz (fremde Reichweite gegen Provision), (2) Fiverr Gig mit agentenbasierter Anpassung (höherer Preis), (3) TikTok „Rebelaicious" als eigenes Publikum.
Skalierung: EN-Version (Fiverr global), Branchenvarianten.
Grenzen: kein „rechtssicher", kein „erfüllt AI Act", Hinweis „keine Rechtsberatung"; Anpassungs-Prompt warnt vor vertraulichen Daten in öffentlichen KI-Tools.
Preise: nach Bau, anhand Wettbewerb (Hypothese: Selbstbedienung 49–99 €, Fiverr angepasst 149–249 €).
Zu prüfen vor Start: Digistore24 als Wiederverkäufer (USt-Abwicklung), Fiverr-Fotopflicht.
Abbruch (E6): 30 Tage nach Listung 0 Verkäufe auf allen Kanälen → Produkt einstellen.

## D18 · 2026-11-05 · Didaktisches Kernprinzip des Kits: Erleben vor Erklären
Quelle: Ankes Praxiserfahrung (eigenes Know-how, kein Material des Arbeitgebers).
Pflicht: Aha-Übung „gleicher Prompt ohne/mit Kontext" + 2–3 weitere Aha-Übungen + Arbeitsblatt; Prompt-Bibliothek nutzt sichtbar den Kontext-Baukasten (Rolle, Ziel, Zielgruppe, Ton, Beispiel, Format).
Begründung: Gegen kostenlose Vorlagen und Kurse gewinnt das Kit nur, wenn es nachweislich besser wirkt. Ein Aha-Erlebnis ist zugleich das beste Verkaufsargument (Produktseite, TikTok).
Qualitätstor: Anke prüft v1 vor Veröffentlichung (Freigabe).

## D19 · 2026-11-05 · Produktleiter statt aufgeblähtes Kit
Ankes Praxisinhalte sind zu viel für ein Einsteigerkit und zu wertvoll zum Weglassen. Entscheidung:
- **Stufe 1 — KI-Starterkit (v1, im Bau):** Regeln, Schulung, Aha-Übungen + kurzes Kapitel „Grundbegriffe in einfacher Sprache" (Chat vs. Agent, Skill = Handbuch, .md, Modellwahl, Mermaid) + Plausibilitätscheck-Prompts für Excel.
- **Stufe 2 — KI-Praxispaket (nach Verkaufssignal für Stufe 1):** Schritt-für-Schritt-Workflows für Präsentationen, Formulare, Excel-Auswertungen mit Plausibilitätssheet, Markdown-Wissensbasis, eigene Skills/Handbücher bauen, Diagramme mit Mermaid.
- Später möglich: Bundle Stufe 1+2, Branchenvarianten, EN-Version, Update-Abo (KI-Inhalte veralten schnell; Pflege = Grund für wiederkehrenden Umsatz).
Begründung: Kleines Produkt wird fertig und testet den Markt; Stufe 2 ist das Upsell an bestehende Käufer (billigster Kunde ist ein bestehender). Kein Bau von Stufe 2 vor E6-Signal.
Regel: tool-neutral formulieren, „Stand: <Monat Jahr>" auf jedes Dokument, keine Preis-/Ranglisten von Modellen.

## D20 · 2026-11-05 · Kit v1 technisch abgenommen; Preise; Vertrieb erst nach Ankes Abnahme
- Technische Abnahme durch Koordinator (Stichprobe + Verbotsliste) bestanden. Fachliche Abnahme durch Anke (T14) ist das Qualitätstor.
- **Preise (Hypothesen, nach 30 Tagen prüfen):** Selbstbedienung (Digistore24) **79 €** für eine Betriebslizenz (ganzes Team, ein Betrieb). Fiverr „angepasst an deine Firma" **199 €**.
  Begründung: Kurse kosten 119–690 € pro Person (Scout A); wir verkaufen pro Betrieb und liefern Vorlagen zum Selbsteinsatz, also deutlich darunter, aber klar über Gratisvorlagen. 79 € liegt unter typischen Spontankauf-Hürden für Firmenausgaben (ANNAHME).
- **Vertriebsagent startet erst nach T14**, damit Texte nicht zweimal geschrieben werden und das Pro-Kontingent geschont wird. Konten (T12/T13) laufen parallel.
- Keine anwaltliche Prüfung vor Start (Budget); stattdessen minimale Werbeaussagen. Neu prüfen nach ersten Verkäufen.
- Nutzungsbedingungen (Betriebslizenz, keine Weitergabe, Haftungsausschluss) als Text für die Produktseite → Vertrieb nach T14.
- E4-Angebotskit (`opportunities/angebote-2026-11-05-ki-starter.md`) ist obsolet (D16), bleibt als Archiv.

## D21 · 2026-11-05 · Wette C: Selbstlernkurs „KI für Einsteiger" — angenommen, aber nach Kit-Start
Problem: Viele Berufstätige (v. a. 45+) haben Sorge um ihren Job und keinen Einstieg. Echter, großer Schmerz.
Warum gut: (1) Inhalte zu ca. 50 % schon im Kit (Grundbegriffe, Aha-Übungen, Kontext-Baukasten) → Kombinieren statt neu bauen. (2) Zwei Märkte mit einem Produkt: Privatkäufer (B2C) und Firmen, die den Kurs für ihre Belegschaft kaufen (Upsell zum Kit). (3) Komplett ohne Ankes Auftritt lieferbar.
Risiken: B2C-Markt voll mit Gratis-Videos und Kursen; Zielgruppe 45+ ist auf TikTok schwach vertreten; Preise niedrig (ANNAHME 19–49 €).
Kanal-Hypothese für 45+: **Amazon KDP (E-Book/Taschenbuch-Arbeitsbuch)** — Käufer suchen dort selbst, Zielgruppe kauft Bücher, Pseudonym möglich, KI-Inhalte müssen bei KDP angegeben werden. Zu prüfen (Wettbewerb „KI für Anfänger", Preise, Rezensionen).
Leitplanken: Ermutigen statt Angst machen (keine Angstwerbung, kein „Wer jetzt nicht lernt, verliert seinen Job"). Kein „Zertifikat", nur Teilnahmebescheinigung. Respektvolle Sprache, kein Herablassen; große Schrift, Bildsprache, ein Gedanke pro Seite.
Reihenfolge: Kit v1 an den Markt (Fokus). Parallel nur der kostenlose Realitätstest T16. Kein Bau vor Kit-Launch, außer T16 liefert starkes Signal.

## D22 · 2026-11-05 · Vertriebstexte jetzt vorbereiten (D20 teilweise revidiert); Scout prüft Plattformregeln + KDP
Anke ist einige Stunden abwesend → Pro-Kontingent ungenutzt. Zeit bis Markteintritt ist wertvoller als das Risiko, Texte nach T14 leicht anzupassen (Produktstruktur steht).
Revision zu D20: Vertrieb startet vor T14, Texte gelten als Entwurf bis zur Abnahme.
Scout klärt Fragen, die sonst Ankes Zeit kosten (Fiverr-Fotopflicht, Digistore24 als Wiederverkäufer/USt für Kleinunternehmer, KDP-Regeln) und den KDP-Wettbewerb für Wette C.

## D23 · 2026-11-05 · Lern-App mit Gamification → Backlog, Format wird billig vorgetestet
Idee: KI lernen wie eine Sprache, täglich 5 Minuten, Fortschritt, Serien, Abzeichen.
Bewertung: Format stark (kleine Häppchen passen genau zur Zielgruppe von Wette C). Als echte App aber das teuerste und riskanteste Produkt im Portfolio: Entwicklung, App-Store-Gebühren und -Prüfung, Pflege, und vor allem Nutzergewinnung ohne Werbebudget — das ist F1 (Nachhaker/SaaS) in neuer Verpackung.
Entscheidung: Keine App jetzt. Das Format wird zuerst ohne App getestet: Inhalte von Wette C als tägliche Mini-Lektionen (z. B. E-Mail-Kurs über Ankes Substack oder ein Arbeitsbuch mit 30 Tages-Lektionen). Zeigen Abschlussraten und Zahlungsbereitschaft Signal, folgt eine einfache Web-App (PWA, ohne App Store) aus denselben Inhalten.
Voraussetzung: Kit verkauft sich ODER Wette C zeigt Signal (T16, Scout C).

## D24 · 2026-11-05 · Fiverr: nur ein Paket „angepasst an Ihre Firma" (199 €)
Begründung: (1) Fiverr-Regel gegen identischen KI-Output an viele Kunden (Scout C) macht „Kit unverändert" riskant; unverändert verkauft Digistore24. (2) Ankes Kapazität (10 h/Woche) reicht nicht für drei Pakete mit Freigabe. Premium (299 €) erst bei Nachfrage. Teil D der Verkaufstexte entsprechend vor Veröffentlichung kürzen.

## D25 · 2026-11-05 · Wette C (Selbstlernkurs/KDP) herabgestuft
KDP-Wettbewerb dicht, Preise 8–26 € (unter D21-Hypothese 19–49 €), Arbeitsbücher mit Übungen existieren schon. Wette C wird nur gebaut, wenn T16 (Kollege) ein starkes Signal liefert (klares Klick-Erlebnis + nennt Zahlungsbereitschaft). Positionierungsidee „ermutigend, 45+ im Beruf" bleibt Hypothese.
Fokus bleibt: Kit v1 an den Markt (Digistore24 zuerst, Fiverr zweitens, TikTok begleitend).
