# Nachhaker Backend (MVP)

Cloudflare Worker + D1. Nimmt Wartelisten-Anmeldungen entgegen, speichert
Rechnungen und verschickt per täglichem Cron die Eskalation
(Zahlungserinnerung → Mahnung). Läuft komplett im Gratis-Tier.

## Warum dieser Stack
- **Kosten:** Cloudflare Workers + D1 sind bis zu hohen Volumina kostenlos →
  keine Fixkosten, bis echter Umsatz da ist.
- **Skalierung:** global verteilt, kein Server-Management.
- **E-Mail:** Resend (Gratis-Tier 3.000 Mails/Monat) für den Versand.

## Deploy (die menschlichen Tore – einmalig, ~10 Min.)

```bash
npm install -g wrangler
wrangler login                          # (1) Cloudflare-Login  ← braucht dich

# (2) Datenbank anlegen und database_id in wrangler.toml eintragen
wrangler d1 create nachhaker
wrangler d1 execute nachhaker --file=./schema.sql

# (3) Secrets setzen
wrangler secret put API_KEY             # frei wählbarer Schlüssel für Schreib-Endpunkte
wrangler secret put RESEND_API_KEY      # von resend.com (Gratis)
wrangler secret put FROM_EMAIL          # verifizierte Absenderadresse

# (4) Deploy
wrangler deploy
```

Danach läuft der Worker unter `https://nachhaker.<dein-subdomain>.workers.dev`.
Diese URL im Frontend als `WAITLIST_ENDPOINT` eintragen (in `index.html`).

## Ohne Konfiguration
Ist kein `RESEND_API_KEY` gesetzt, läuft der Cron im **Dry-Run** (loggt nur,
verschickt nichts) – praktisch zum Testen der Logik ohne echten Mailversand.

## Endpunkte
| Methode | Pfad | Auth | Zweck |
|---|---|---|---|
| POST | `/api/waitlist` | – | Warteliste (E-Mail) |
| POST | `/api/invoices` | X-Api-Key | Rechnung anlegen |
| GET | `/api/invoices?owner=…` | X-Api-Key | Rechnungen listen |
| POST | `/api/invoices/:id/paid` | X-Api-Key | Als bezahlt markieren → Kette stoppt |
