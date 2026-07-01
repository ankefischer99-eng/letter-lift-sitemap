# Nachhaker — Betriebsplan & Weg zu 20.000 €/Monat

> Ziel: legal & langfristig 20.000 €/Monat wiederkehrenden Umsatz (MRR).
> Dieses Dokument verantworte ich (Claude) als Betriebsplan. Es ist ehrlich —
> inkl. der Punkte, die nur die Inhaberin (Anke) freischalten kann.

## 1. Das Produkt

**Nachhaker** ist ein DACH-fokussiertes SaaS, das offenen Rechnungen von
Freelancern und Solo-Selbstständigen automatisch hinterherjagt: von der
freundlichen Zahlungserinnerung bis zur formellen Mahnung — im Ton der Nutzerin,
mit Zahllink, DSGVO-konform. Zahlung erkannt → Kette stoppt automatisch.

**Warum es eine Lücke gibt (recherchiert):**
- Selbstständige verlieren ~1 Arbeitstag/Monat mit dem Eintreiben von Geld.
- 71 % der Freelancer erleben verspätete Zahlungen; im Schnitt 9 offene
  Rechnungen gleichzeitig.
- Bestehende dedizierte „Chaser"-Tools (Landolio, Auto-Invoicer, InvoicifyAI)
  sind **alle englisch/US/UK**. Kein Anbieter bedient den DACH-Markt sauber mit
  korrekter Erinnerung→Mahnung-Eskalation und deutschem, rechtssicherem Ton.

## 2. Preismodell

| Plan     | Preis      | Zielgruppe                          |
|----------|------------|-------------------------------------|
| Solo     | 0 €/Monat  | Einstieg, bis 3 aktive Rechnungen   |
| Pro      | 9 €/Monat  | Solo-Selbstständige, Freelancer     |
| Business | 19 €/Monat | Kleine Agenturen, mehrere Absender  |

Geplante Erweiterungen für höheren ARPU: Jahresabo (−20 %), „Done-for-you"-
Onboarding, White-Label für Steuerberater/Agenturen (49 €+).

## 3. Rechnung bis 20.000 €/Monat (die ehrliche Mathematik)

Bei **blended ARPU ~12 €/Monat** (Mix aus Pro/Business/Jahresabos):

```
20.000 € / 12 € ≈ 1.670 zahlende Kunden
```

Zum Einordnen: In DE gibt es >4 Mio. Selbstständige/Freelancer.
1.670 Kunden = **0,04 %** der Zielgruppe. Klein, aber es braucht einen
verlässlichen, günstigen Kanal — kein bezahltes Wachstum um jeden Preis.

**Trichter-Annahmen (konservativ):**
- SEO-Content-Bibliothek → organischer Traffic (Vorlagen-Seiten ranken für
  „Zahlungserinnerung Vorlage", „Mahnung schreiben" etc.)
- Besucher → Free-Signup: 3 %
- Free → Paid: 8 %
- Nötiger Traffic für 1.670 Kunden: ~700.000 Besucher (kumuliert), also
  ~30–60k Besucher/Monat im eingeschwungenen Zustand bei gesunder Churn.

**Zeithorizont:** realistisch **18–36 Monate**. Das ist ein Aufbau, kein
Session-Ergebnis. Wer „20k in Wochen" verspricht, lügt.

## 4. Wachstums-Engine (das, was skaliert)

1. **Programmatische SEO** — Bibliothek nützlicher Gratis-Vorlagen/Ratgeber
   (`/ratgeber/`), die genau die zahlungsgeplagte Zielgruppe anziehen und in
   die Warteliste/Free-Version leiten. *→ wird bereits gebaut.*
2. **Product-led:** kostenlose Stufe + „Zahlung erkannt = Auto-Stopp" als
   Aha-Moment → Mundpropaganda in Freelancer-Communities.
3. **Integrations-Distribution:** Andocken an gängige Rechnungstools
   (Export/Import), Präsenz in deren Marktplätzen.
4. **Content/Community:** Reddit (r/selbststaendig, r/Finanzen), LinkedIn,
   Steuerberater-Kooperationen.

## 5. Was ich (der Agent) autonom baue/besitze

- [x] Produkt-Landingpage + Live-Demo (Sequenz-Generator)
- [x] Warteliste (E-Mail-Erfassung, konfigurierbarer Endpoint)
- [x] SEO-Content-Bibliothek (parallel via Sub-Agent)
- [x] Deploy-Pipeline (GitHub Pages, `.github/workflows/deploy.yml`)
- [x] Sitemap für Indexierung
- [ ] Backend/MVP (Rechnungen speichern, Mails zeitgesteuert senden) — nächster Bauabschnitt
- [ ] Zahlungs-Abgleich (der harte, wertentscheidende Teil)

## 6. Was NUR Anke freischalten kann (menschliche Tore)

Diese Schritte kann kein Agent legal für dich erledigen — sie brauchen deine
Identität, dein Geld oder deine Unterschrift:

1. **GitHub Pages aktivieren:** Repo → Settings → Pages → Source = „GitHub
   Actions". Danach ist die Seite live (URL erscheint im Actions-Deploy).
2. **Domain** kaufen (z.B. nachhaker.de) und mit Pages verbinden.
3. **Zahlungsanbieter:** Stripe-Konto (oder PayPal, ist schon angebunden) für
   echte Abos. Braucht deine Verifizierung.
4. **Rechtsform & Impressum:** Gewerbe/Kleinunternehmer, Impressum, DSGVO-
   Datenschutzerklärung, AVV mit E-Mail-Versender. (Steuerberater fragen.)
5. **E-Mail-Versand-Infra:** Domain-Verifizierung bei einem Versender
   (z.B. Postmark/Resend) — sonst landen Mahnungen im Spam.

## 7. Nächste Schritte (Priorität)

1. Anke aktiviert GitHub Pages → Seite ist live, Warteliste sammelt echte Leads.
2. Ich baue das Backend-MVP (Rechnung anlegen → geplanter Mailversand).
3. 20 echte Zielnutzer aus Ankes Umfeld/Communities auf die Warteliste holen
   und interviewen (Preisbereitschaft, größter Schmerz).
4. Erst bei Signal: Zahlungsabgleich + kostenpflichtige Abos scharf schalten.
