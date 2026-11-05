from kit_lib import *

FILE = "Anpassungs-Prompt.docx"

PROMPT_A = """Du bist eine sorgfältige Redakteurin für betriebliche Richtlinien in einem kleinen Unternehmen in Deutschland. Deine Aufgabe: Passe den unten stehenden Entwurf einer KI-Nutzungsrichtlinie an die Angaben des Unternehmens an.

REGELN FÜR DICH:
1. Verwende ausschließlich die Angaben aus „FIRMENANGABEN“ und den Entwurf. Erfinde nichts.
2. Zitiere keine Gesetze, Paragraphen, Urteile oder Fristen. Wo der Entwurf rechtliche Punkte allgemein formuliert, lass sie allgemein.
3. Füge keine Zusicherungen hinzu, die Richtlinie decke gesetzliche Anforderungen ab oder sei rechtlich geprüft. Behalte den Hinweis „Diese Vorlage ersetzt keine Rechtsberatung.“ bei.
4. Wenn eine Angabe fehlt, lass den Platzhalter in [ECKIGEN KLAMMERN] stehen und liste ihn am Ende unter „Noch offen“ auf.
5. Behalte Gliederung und Kapitelnummern bei. Ändere die Sprache nicht ins Juristische: kurze Sätze, klare Wörter.
6. Markiere jede Stelle, die du gegenüber dem Entwurf inhaltlich verändert hast, am Zeilenende mit „(geändert)“.
7. Schlage am Ende „Rückfragen an die Geschäftsleitung“ vor (maximal 8).

FIRMENANGABEN:
[HIER DEN AUSGEFÜLLTEN FRAGENBOGEN EINFÜGEN – ANONYMISIERT]

ENTWURF:
[HIER DEN TEXT DER RICHTLINIE EINFÜGEN – KAPITEL FÜR KAPITEL]"""

PROMPT_B = """Du bist Trainerin für betriebliche Schulungen. Unten steht der Text einer Schulungsfolie (Titel, Stichpunkte, Sprechernotiz). Passe ihn an die FIRMENANGABEN an.

REGELN:
1. Nutze nur die Angaben aus „FIRMENANGABEN“. Erfinde keine Beispiele mit echten Personen, Kunden oder Fällen und keine Statistiken.
2. Keine Gesetzeszitate, keine Paragraphen. Rechtliches bleibt allgemein.
3. Maximal 5 Stichpunkte pro Folie, je höchstens 15 Wörter. Die Sprechernotiz darf bis zu 120 Wörter haben, in einfacher Sprache.
4. Gib das Ergebnis im selben Format aus: Titel / Stichpunkte / Sprechernotiz.

FIRMENANGABEN:
[ANONYMISIERTER FRAGENBOGEN]

FOLIE:
[TITEL, STICHPUNKTE UND SPRECHERNOTIZ DER FOLIE]"""

PROMPT_C = """Du erstellst Prüfungsfragen für eine kurze betriebliche Schulung. Passe die folgende Frage so an, dass sie zu den FIRMENANGABEN passt. Es bleibt bei 4 Antwortmöglichkeiten (A–D) mit genau einer richtigen Antwort. Gib zusätzlich eine Begründung in einem Satz aus. Erfinde keine rechtlichen Aussagen und keine Gesetzesverweise.

FIRMENANGABEN:
[ANONYMISIERTER FRAGENBOGEN]

FRAGE:
[FRAGE MIT ANTWORTEN]"""

PROMPT_D = """Prüfe den folgenden angepassten Text kritisch gegen den ursprünglichen Entwurf. Liste auf:
1. Alle Stellen, an denen sich die Bedeutung geändert hat.
2. Alle neu hinzugefügten Aussagen, Zahlen, Fristen, Gesetzes- oder Paragraphenverweise (diese bitte besonders deutlich).
3. Alle Stellen, die zu Datenschutz oder Vertraulichkeit weniger streng sind als der Entwurf.
Gib nur die Liste aus, ohne den Text neu zu schreiben.

ORIGINAL:
[ENTWURF]

ANGEPASSTER TEXT:
[ERGEBNIS AUS SCHRITT 4]"""

QUESTIONS = [
    ("Firmenname, Branche, Größe", "[z. B. Tischlerei, 14 Beschäftigte]"),
    ("Wer ist KI-Beauftragte/r (Funktion, kein Privatname nötig)?", ""),
    ("Welche KI-Tools sind bereits freigegeben oder im Gespräch? (Produktnamen genügen)", ""),
    ("Welche Datenarten verarbeiten Sie täglich? (Kunden, Lieferanten, Bewerber, Personal …)", ""),
    ("Welche Daten dürfen NIE in ein KI-Tool? (Ihre Regeln)", ""),
    ("Gibt es Verschwiegenheitspflichten gegenüber Kunden/Branchenregeln, die Sie beachten müssen?", ""),
    ("Gibt es eine/n Datenschutzbeauftragte/n (intern/extern)? Funktion genügt.", ""),
    ("Gibt es einen Betriebsrat?", "[ja/nein]"),
    ("Wer entscheidet über Tool-Freigaben, in welcher Frist?", ""),
    ("Dürfen private Konten genutzt werden? (Empfehlung der Vorlage: nein)", ""),
    ("Wie kennzeichnen Sie KI-Unterstützung intern/extern?", ""),
    ("Welche Texte/Entscheidungen brauchen eine fachliche Prüfung vor Verwendung?", ""),
    ("Wie oft soll geschult und die Richtlinie überprüft werden?", ""),
    ("Welche Folgen sollen Verstöße haben? (Verweis auf bestehende Regeln im Betrieb)", ""),
    ("Typische Alltagsbeispiele aus Ihrem Betrieb (für Schulungsfolien, ohne Namen)", ""),
]


def build(outdir):
    D = Doc("Anpassungs-Prompt", "Richtlinie, Folien und Test mit KI an Ihren Betrieb anpassen – Schritt für Schritt", "Anpassungs-Prompt")
    D.disclaimer_box()
    D.callout(
        "WARNUNG – bitte zuerst lesen",
        [
            "**Geben Sie keine vertraulichen oder personenbezogenen Daten in öffentliche KI-Tools ein.** Dazu gehören Namen von Kundinnen, Kunden und Beschäftigten, Kontaktdaten, Verträge, Kalkulationen, Zugangsdaten und Interna.",
            "Für diese Anpassung brauchen Sie solche Daten nicht. Beschreiben Sie Ihren Betrieb allgemein (z. B. „Tischlerei, 14 Beschäftigte“) und **anonymisieren Sie vorher**: Namen → Funktionen oder [Platzhalter].",
            "Nutzen Sie nur ein Tool, das Ihr Betrieb für diesen Zweck freigegeben hat. Geben Sie Zusammenhang und Firmenregeln in eigenen Worten ein – nicht aus vertraulichen Dokumenten kopiert.",
            "Die KI kann falsche Aussagen erfinden, auch Paragraphen. **Prüfen Sie jedes Ergebnis selbst** (Schritt 6).",
        ],
        fill=WARN_FILL,
    )
    D.h1("Überblick: 7 Schritte, ca. 2–3 Stunden")
    D.table(
        ["Schritt", "Was", "Dauer"],
        [
            ["1", "Fragebogen ausfüllen (eigene Regeln sammeln)", "30–45 Min."],
            ["2", "Anonymisieren und prüfen, was eingegeben werden darf", "15 Min."],
            ["3", "Tool wählen und vorbereiten", "10 Min."],
            ["4", "Richtlinie anpassen lassen (Prompt A)", "30–40 Min."],
            ["5", "Folien und Test anpassen lassen (Prompt B, C)", "40–60 Min."],
            ["6", "Ergebnis kritisch prüfen (Prompt D und eigene Prüfung)", "30–45 Min."],
            ["7", "Übertragen, freigeben lassen, Rechtsberatung für Offenes", "je nach Bedarf"],
        ],
        widths=[2.0, 11.4, 3.0],
    )

    D.h1("Schritt 1: Fragebogen ausfüllen")
    D.p("Schreiben Sie Ihre Antworten in Stichpunkten in eigenen Worten. Es geht um Ihre **Regeln und Entscheidungen**, nicht um Daten aus Ihrem Alltag.")
    D.table(["Frage", "Ihre Antwort"], [[q, a] for q, a in QUESTIONS], widths=[9.0, 7.4], size=10)

    D.h1("Schritt 2: Anonymisieren")
    D.bullets(
        [
            "Streichen Sie aus Ihren Antworten alle Namen von Personen, Kunden und Lieferanten sowie Adressen, Nummern und Beträge.",
            "Ersetzen Sie Namen durch Funktionen (z. B. „Geschäftsführerin“) oder Platzhalter ([Kunde A]).",
            "Lesen Sie den Text einmal als Außenstehender: Könnte man daraus einen Menschen oder ein vertrauliches Projekt erkennen? Dann weiter kürzen.",
            "Im Zweifel fragen Sie Ihre Datenschutz-Ansprechperson, bevor Sie etwas eingeben.",
        ]
    )

    D.h1("Schritt 3: Tool wählen")
    D.bullets(
        [
            "Nutzen Sie ein Tool aus Ihrer Freigabeliste. Gibt es noch keines: Nutzen Sie für diese Anpassung nur Texte, die nach der Datenampel grün sind (anonymisiert, allgemein).",
            "Öffnen Sie eine **neue Unterhaltung**, damit keine früheren Eingaben mitlaufen.",
            "Prüfen Sie in den Einstellungen des Tools, ob Verlauf/Training mit Ihren Eingaben abgeschaltet werden kann, und tun Sie es, falls möglich.",
        ]
    )

    D.h1("Schritt 4: Richtlinie anpassen – Prompt A")
    D.p("Kopieren Sie den Prompt. Ersetzen Sie die beiden Platzhalter am Ende (Fragebogen und Entwurf). Geben Sie die Richtlinie **kapitelweise** ein, wenn das Tool bei langen Texten Teile weglässt.")
    D.callout("Prompt A: Richtlinie anpassen", PROMPT_A.split("\n"), fill=SOFT_FILL)

    D.h1("Schritt 5: Folien und Wissenstest anpassen")
    D.p("Die KI bearbeitet Ihre PowerPoint-Datei nicht direkt. Kopieren Sie **Folie für Folie** den Text (Titel, Stichpunkte, Sprechernotiz) in den Prompt und übertragen Sie das Ergebnis danach in die Folie. Konzentrieren Sie sich auf Folien, die Firmenbezug haben: Folie 3 bis 8, 10 bis 13 und 18.")
    D.callout("Prompt B: Folie anpassen", PROMPT_B.split("\n"), fill=SOFT_FILL)
    D.callout("Prompt C: Testfrage anpassen", PROMPT_C.split("\n"), fill=SOFT_FILL)
    D.p("Passen Sie danach in der Datei „Wissenstest-und-Nachweis.docx“ das Lösungsblatt an. Die richtige Antwort darf sich dabei nicht unbemerkt ändern.")

    D.h1("Schritt 6: Ergebnis kritisch prüfen")
    D.p("Lassen Sie zuerst die KI die eigenen Änderungen auflisten (Prompt D), prüfen Sie dann selbst:")
    D.callout("Prompt D: Änderungen sichtbar machen", PROMPT_D.split("\n"), fill=SOFT_FILL)
    D.numbered(
        [
            "Hat die KI **Gesetze, Paragraphen, Urteile oder Fristen** eingefügt? Löschen Sie diese oder lassen Sie sie von einer fachkundigen Person prüfen.",
            "Hat die KI Zusicherungen eingefügt, die Richtlinie sei rechtlich geprüft oder erfülle gesetzliche Anforderungen? Streichen.",
            "Ist der Datenschutz **gleich streng oder strenger** geworden – nicht lockerer?",
            "Stimmen Namen, Funktionen, Fristen und Tool-Namen mit der Wirklichkeit in Ihrem Betrieb überein?",
            "Bleiben die Platzhalter, die Sie nicht beantwortet haben, sichtbar?",
            "Passt der Ton: klar, kurze Sätze, kein Juristendeutsch?",
            "Hat jemand außer Ihnen den Text gelesen (Vier-Augen-Prinzip)?",
        ]
    )

    D.h1("Schritt 7: Übertragen und freigeben")
    D.bullets(
        [
            "Übertragen Sie die geprüften Texte in die Dateien des Kits.",
            "Lassen Sie die Richtlinie von der Geschäftsleitung freigeben und – falls vorhanden – von Datenschutzbeauftragten und Betriebsrat prüfen.",
            "Offene rechtliche Fragen (z. B. Beteiligungsrechte, Aufbewahrungsfristen, Folgen von Verstößen) klären Sie mit einer Rechtsberatung.",
            "Tragen Sie Versionsdatum und Verantwortliche ein, und setzen Sie einen Termin zur Überprüfung.",
        ]
    )
    D.h2("Typische Probleme")
    D.table(
        ["Problem", "Was hilft"],
        [
            ["Die KI kürzt den Text oder lässt Kapitel weg.", "Kapitelweise eingeben; „Gib den vollständigen Kapiteltext aus“ ergänzen."],
            ["Die KI fügt juristische Formulierungen oder Paragraphen hinzu.", "Prompt A, Regel 2, wiederholen; Stellen löschen; Prompt D nutzen."],
            ["Das Ergebnis klingt allgemein.", "Konkretere Antworten im Fragebogen, mehr eigene Beispiele (anonymisiert)."],
            ["Unsicherheit, ob etwas eingegeben werden darf.", "Nicht eingeben. Ansprechperson fragen."],
        ],
        widths=[7.0, 9.4],
    )
    D.save(f"{outdir}/{FILE}")
    return FILE
