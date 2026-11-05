# FAILURES — Fehlschläge

Kein Schuldbuch, sondern Firmenvermögen. Format: was, warum, was es gekostet hat, was wir ändern.

## F1 · Nachhaker (2026-07 bis 2026-11)
- **Was:** Landing, 10 SEO-Seiten, Backend gebaut, 0 Kunden, 0 messbare Leads.
- **Warum:** Bau vor Validierung; Warteliste nie an ein Backend angeschlossen; Deploy hing an menschlichen Schritten, die nie als priorisierte Tickets verfolgt wurden.
- **Kosten:** Mehrere Agentensitzungen, 4 Monate Zeit, 0 €.
- **Änderung:** Jeder Bau braucht vorher ein belegtes Nachfragesignal. Menschliche Schritte werden Tickets mit Priorität und Nachverfolgung durch den Koordinator.

## F2 · Scout-Probelauf auf Opus gestartet (2026-11-05)
- **Was:** Erste Agentensession ohne Modellwahl gestartet → erbte das teuerste Modell.
- **Warum:** Koordinator hat den Modellparameter beim Start vergessen.
- **Kosten:** Mehr Pro-Kontingent als nötig für eine Sitzung.
- **Änderung:** D7; Modell wird bei jedem Agentenstart explizit gesetzt.

## F3 · Scout blind für deutsche Quellen (2026-11-05)
- **Was:** Webabruf auf reddit, freelancer.com, freelancermap.de, peopleperhour, guru, kleinanzeigen.de, hn.algolia gesperrt; alle 25 Funde nur aus Suchindex, keiner auf Originalseite geprüft.
- **Warum:** Netzwerkrichtlinie der Cloud-Umgebung.
- **Kosten:** DE-Hypothese nicht testbar; Funde nur Indizien.
- **Änderung:** Ticket T8 (Netzfreigabe). Bis dahin Funde als „Hinweis", nicht als „Nachfrage" werten.

## F4 · Drei Scout-Läufe ohne einen Nachfragebeleg (2026-11-05)
- **Was:** Scout 1, A, B lieferten 25 + 24 + 14 Funde, aber keinen einzigen Beleg zahlender Nachfrage im Zielsegment.
- **Warum:** Webabruf gesperrt (F3); Websuche zeigt Angebote, kaum Gesuche oder Verkaufszahlen.
- **Kosten:** 3 Agentensitzungen (1× Opus, 2× Sonnet), alle „mittel".
- **Änderung:** D15 — Recherche pausiert, Nachfrage wird mit einem echten Angebot gemessen.

## F5 · E4 auf einer falschen Annahme gebaut (2026-11-05)
- **Was:** Verkaufstest E4 (Live-Workshop mit Anke als Trainerin) beschlossen und Vertriebsagent gestartet.
- **Warum:** Koordinator hat „ich kann das Gesicht für deine Firma sein" als Bereitschaft zu Live-Auftritten gelesen, ohne nachzufragen. Anke meinte: rechtliche/administrative Inhaberin im Hintergrund.
- **Kosten:** 1 abgebrochene Vertriebssitzung (Sonnet), eine Planungsrunde.
- **Änderung:** Ankes Rolle steht ab jetzt als explizite Ja/Nein-Liste in README §2. Jede neue Wette wird vor dem Start gegen diese Liste geprüft.
