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
