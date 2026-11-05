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
