-- Nachhaker MVP – Datenbankschema (Cloudflare D1 / SQLite)
-- Anwenden mit:  wrangler d1 execute nachhaker --file=./schema.sql

CREATE TABLE IF NOT EXISTS waitlist (
  id         INTEGER PRIMARY KEY AUTOINCREMENT,
  email      TEXT NOT NULL UNIQUE,
  source     TEXT,
  created_at TEXT NOT NULL DEFAULT (datetime('now'))
);

CREATE TABLE IF NOT EXISTS invoices (
  id           INTEGER PRIMARY KEY AUTOINCREMENT,
  owner_email  TEXT NOT NULL,          -- wem gehört die Rechnung (der Nutzer)
  kunde        TEXT NOT NULL,
  kunde_email  TEXT NOT NULL,          -- an wen die Erinnerung geht
  rechnung_nr  TEXT NOT NULL,
  betrag_cent  INTEGER NOT NULL,
  faellig_am   TEXT NOT NULL,          -- ISO-Datum YYYY-MM-DD
  ton          TEXT NOT NULL DEFAULT 'neutral',  -- freundlich | neutral | bestimmt
  zahllink     TEXT,
  status       TEXT NOT NULL DEFAULT 'offen',    -- offen | bezahlt | storniert
  stufe        INTEGER NOT NULL DEFAULT 0,        -- welche Eskalationsstufe zuletzt gesendet
  created_at   TEXT NOT NULL DEFAULT (datetime('now'))
);

CREATE INDEX IF NOT EXISTS idx_invoices_status ON invoices(status, faellig_am);

CREATE TABLE IF NOT EXISTS reminders_log (
  id         INTEGER PRIMARY KEY AUTOINCREMENT,
  invoice_id INTEGER NOT NULL,
  stufe      INTEGER NOT NULL,
  betreff    TEXT,
  gesendet_at TEXT NOT NULL DEFAULT (datetime('now')),
  FOREIGN KEY (invoice_id) REFERENCES invoices(id)
);
