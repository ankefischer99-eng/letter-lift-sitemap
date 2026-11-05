from kit_lib import *

FILE = "Prompt-Bibliothek.docx"

# (Titel, Zweck, Prompt, Hinweis)
CATS = [
    ("Verwaltung", [
        ("Besprechungsprotokoll aus Stichpunkten", "Aus eigenen Notizen ein sauberes Protokoll machen.",
         "Du bist Assistenz der Geschäftsführung. Erstelle aus den folgenden Stichpunkten ein Besprechungsprotokoll mit den Abschnitten: Teilnehmende (nur Kürzel), Beschlüsse, Aufgaben (wer, was, bis wann), offene Punkte. Erfinde nichts; wenn Angaben fehlen, schreibe „[unklar]“.\n\nStichpunkte:\n[ANONYMISIERTE NOTIZEN]",
         "Namen durch Kürzel ersetzen. Aufgaben und Fristen anschließend mit den echten Notizen abgleichen."),
        ("E-Mail professionell umformulieren", "Einen eigenen Entwurf klarer und höflicher machen.",
         "Formuliere den folgenden E-Mail-Entwurf professionell, freundlich und kurz (maximal [120] Wörter). Behalte alle Inhalte und Zahlen unverändert bei und ergänze nichts. Ton: [sachlich/herzlich].\n\nEntwurf:\n[TEXT OHNE PERSONENDATEN]",
         "Namen, Nummern und Adressen vor dem Einfügen entfernen und danach selbst wieder einsetzen."),
        ("Langen Text zusammenfassen", "Schneller verstehen, worum es geht – bei nicht vertraulichen Texten.",
         "Fasse den folgenden Text in [5] Stichpunkten und einem Satz Gesamtfazit zusammen. Trenne klar zwischen dem, was im Text steht, und deiner Einschätzung. Markiere Stellen, bei denen du unsicher bist.\n\nText:\n[ÖFFENTLICHER ODER FREIGEGEBENER TEXT]",
         "Nur grüne (oder für das Tool freigegebene gelbe) Texte. Zusammenfassungen können Wichtiges weglassen – bei wichtigen Entscheidungen Original lesen."),
        ("Checkliste oder Ablauf erstellen", "Eine wiederkehrende Aufgabe als Checkliste festhalten.",
         "Erstelle eine Checkliste für den Ablauf „[AUFGABE, z. B. Neue Mitarbeiterin einrichten]“ in einem kleinen Betrieb mit [ANZAHL] Personen. Gliedere nach Phasen (vorher, am Tag, danach), nenne für jeden Schritt eine verantwortliche Rolle (keine Namen) und markiere Schritte, die mit Datenschutz zu tun haben, mit „(Datenschutz prüfen)“.",
         "Ergebnis mit den tatsächlichen Abläufen im Betrieb abgleichen; die KI kennt sie nicht."),
        ("Agenda für eine Besprechung", "Eine Besprechung vorbereiten.",
         "Erstelle eine Agenda für eine Besprechung von [60] Minuten zum Thema „[THEMA]“. Teilnehmende: [ROLLEN]. Ziel: [ZIEL]. Gib pro Punkt Dauer, Ziel (informieren/entscheiden/ideen sammeln) und Vorbereitungsaufgabe an. Plane 10 % Puffer ein.",
         "Zeiten realistisch nachprüfen. Keine internen Details, wenn das Tool nicht freigegeben ist."),
        ("Tabellenformel erklären oder bauen", "Excel/Google-Sheets-Formeln ohne echte Daten.",
         "Ich arbeite mit [Excel/Google Sheets]. Spalte A enthält [BESCHREIBUNG, z. B. Datum], Spalte B [BESCHREIBUNG]. Ich möchte [ZIEL, z. B. die Summe je Monat berechnen]. Schlage eine Formel vor, erkläre sie in einfachen Worten und nenne zwei Fälle, in denen sie falsche Ergebnisse liefern könnte. Nutze nur erfundene Beispieldaten.",
         "Formel an einer kleinen Testtabelle ausprobieren. Keine echten Daten einfügen."),
    ]),
    ("Vertrieb", [
        ("Begleitschreiben zum Angebot", "Einen Angebotsbegleittext entwerfen.",
         "Du bist Vertriebsmitarbeiter/in in einem kleinen Unternehmen der Branche [BRANCHE]. Schreibe ein kurzes Begleitschreiben (maximal [150] Wörter) zu einem Angebot über [LEISTUNG]. Betone den Nutzen: [NUTZEN 1], [NUTZEN 2]. Nenne keine Preise, Fristen oder Garantien, die ich nicht angegeben habe. Ende mit einem klaren nächsten Schritt: [SCHRITT].",
         "Preise, Fristen und Zusagen selbst eintragen und prüfen. Kundennamen erst im fertigen Dokument einsetzen."),
        ("Nachfassmail an Bestandskontakte", "Eine freundliche Erinnerung nach einem Angebot.",
         "Schreibe eine kurze, freundliche Nachfassmail (maximal [100] Wörter) zu einem Angebot, das vor [ZEITRAUM] verschickt wurde. Kein Druck, keine Übertreibung. Biete [HILFE, z. B. Rückfragen klären] an. Ton: [TON].",
         "Nur an Kontakte, mit denen eine Geschäftsbeziehung besteht oder die zugestimmt haben. Regeln zu Werbung im Zweifel mit Rechtsberatung klären."),
        ("Einwände vorbereiten", "Auf typische Einwände vorbereitet sein.",
         "Unsere Leistung: [BESCHREIBUNG]. Zielgruppe: [ZIELGRUPPE]. Nenne die 8 häufigsten Einwände, die Interessenten haben könnten (z. B. Preis, Zeit, Vertrauen). Formuliere zu jedem eine ehrliche, kurze Antwort ohne Übertreibung und eine Rückfrage, die das Gespräch öffnet. Erfinde keine Kundenzahlen oder Referenzen.",
         "Antworten mit echten Erfahrungen abgleichen. Referenzen und Zahlen ausschließlich selbst ergänzen."),
        ("Gesprächsvorbereitung aus öffentlichen Infos", "Sich auf ein Erstgespräch vorbereiten.",
         "Ich bereite ein Erstgespräch mit einem Unternehmen der Branche [BRANCHE] vor. Hier ist öffentlich verfügbare Information: [TEXT AUS WEBSEITE/PRESSE, öffentlich]. Erstelle: 1) was wir daraus ableiten können, 2) fünf offene Fragen, die ich stellen sollte, 3) eine mögliche Gesprächsstruktur. Trenne klar zwischen Fakten aus dem Text und Vermutungen.",
         "Nur öffentliche Informationen verwenden. Keine Daten aus dem Kundenmanagement-System."),
        ("Nutzen statt Merkmale", "Produktmerkmale in Kundennutzen übersetzen.",
         "Hier sind die Merkmale unseres Angebots: [MERKMALE]. Übersetze jedes Merkmal in einen konkreten Nutzen für [ZIELGRUPPE] nach dem Muster „Merkmal → Was bedeutet das im Alltag? → Warum ist das für Sie wichtig?“. Verwende einfache Sprache und keine Superlative.",
         "Prüfen, ob jeder Nutzen belegbar ist. Streichen, was wir nicht halten können."),
        ("Leitfaden für das Erstgespräch", "Ein Gespräch strukturieren.",
         "Erstelle einen Leitfaden für ein 20-minütiges Erstgespräch mit [ZIELGRUPPE] zu [THEMA]. Struktur: Einstieg, Bedarf klären (6 offene Fragen), Lösung kurz vorstellen, Einwände, Abschluss mit nächstem Schritt. Formuliere ehrlich und ohne Drucktechniken.",
         "Leitfaden zu Ihrem Stil anpassen und ausprobieren."),
    ]),
    ("Kundenservice", [
        ("Antwortentwurf auf eine Kundenanfrage", "Antworten schneller und freundlicher formulieren.",
         "Du bist Kundenservice-Mitarbeiter/in. Schreibe eine Antwort auf die folgende Kundenanfrage. Ton: freundlich, klar, lösungsorientiert. Länge: maximal [120] Wörter. Gib keine Zusagen zu Erstattung, Fristen oder Kulanz, die nicht in den unten genannten Regeln stehen.\n\nRegeln: [UNSERE REGELN IN STICHPUNKTEN]\nAnfrage (anonymisiert): [ANFRAGE OHNE NAMEN/NUMMERN]",
         "Name, Bestellnummer, Adresse weglassen und im Ergebnis wieder einsetzen. Zusagen vor dem Senden prüfen."),
        ("Beschwerde deeskalierend beantworten", "Eine verärgerte Nachricht ruhig beantworten.",
         "Die folgende Kundenbeschwerde ist emotional. Schreibe eine Antwort, die 1) das Anliegen in einem Satz zusammenfasst, 2) Verständnis zeigt, ohne Schuld zu erfinden, 3) einen konkreten nächsten Schritt nennt: [SCHRITT], 4) mit einem freundlichen Abschluss endet. Keine Floskeln, keine Rechtfertigungen.\n\nBeschwerde (anonymisiert): [TEXT]",
         "Keine Schuldanerkenntnisse oder Zusagen ohne Rücksprache. Bei rechtlichen Drohungen: [NAME/Funktion] einbinden."),
        ("FAQ-Entwurf", "Aus häufigen Fragen eine FAQ-Liste entwickeln.",
         "Hier sind häufige Kundenfragen (ohne Personendaten): [LISTE]. Formuliere zu jeder eine kurze, klare Antwort in [2–3] Sätzen. Wo du die Antwort nicht aus meinen Angaben kennst, schreibe „[Antwort ergänzen]“. Gruppiere nach Themen.",
         "Antworten mit den tatsächlichen Regeln abgleichen; die KI darf keine Lücken füllen."),
        ("Tonalitäts-Check", "Eigene Texte auf Wirkung prüfen.",
         "Prüfe den folgenden Text auf Wirkung beim Kunden: Wirkt er freundlich, klar, respektvoll? Nenne drei Stellen, die missverständlich oder schroff sein könnten, und schlage Alternativen vor. Verändere keine Inhalte.\n\nText:\n[TEXT OHNE PERSONENDATEN]",
         "Die KI beurteilt Wirkung nur ungefähr. Im Zweifel eine Kollegin oder einen Kollegen lesen lassen."),
        ("Anfragen sortieren", "Beispielanfragen in Kategorien einteilen.",
         "Ordne die folgenden anonymisierten Beispielanfragen in Kategorien (z. B. Lieferung, Rechnung, Reklamation, Technik, Sonstiges). Gib eine Tabelle mit Nummer, Kategorie, Dringlichkeit (hoch/mittel/niedrig) und einer Begründung in einem Satz aus.\n\nAnfragen:\n[NUMMERIERTE, ANONYMISIERTE BEISPIELE]",
         "Nur anonymisierte Beispiele. Die Zuordnung ist ein Vorschlag; Dringlichkeit entscheidet ein Mensch."),
        ("Textbausteine für Standardfälle", "Eine Sammlung wiederverwendbarer Antworten aufbauen.",
         "Erstelle fünf Textbausteine für folgende Standardsituationen: [SITUATIONEN, z. B. Lieferverzögerung, Terminbestätigung, Reklamation eingegangen]. Jeder Baustein: maximal [80] Wörter, mit Platzhaltern in eckigen Klammern für Name, Datum und Details. Keine Zusagen, die ich nicht genannt habe.",
         "Bausteine rechtlich unkritisch halten; keine Garantien oder Fristen formulieren, die Sie nicht prüfen konnten."),
    ]),
    ("Marketing", [
        ("Ideen für Social-Media-Beiträge", "Themen für einen Monat sammeln.",
         "Wir sind ein kleines Unternehmen in der Branche [BRANCHE] für [ZIELGRUPPE]. Schlage 12 Themen für Beiträge auf [KANAL] vor. Pro Thema: Kernbotschaft, Format (Text/Bild/Video) und ein Beispiel für die erste Zeile. Keine erfundenen Zahlen, keine Kundenbeispiele, keine Heilversprechen.",
         "Auswahl selbst treffen. Werbung muss als solche erkennbar sein; Bildrechte klären."),
        ("Newsletter-Entwurf", "Einen Newsletter strukturieren.",
         "Schreibe den Entwurf eines Newsletters (maximal [250] Wörter) für [ZIELGRUPPE] zum Thema „[THEMA]“. Struktur: Betreff (3 Varianten), Einstieg, drei Abschnitte mit Zwischenüberschriften, Handlungsaufforderung: [CTA]. Ton: [TON]. Erfinde keine Fakten, Zitate oder Statistiken.",
         "Fakten prüfen. Versand nur an Personen, die zugestimmt haben; Pflichtangaben und Abmeldelink nicht vergessen."),
        ("Produktbeschreibung", "Einen Beschreibungstext entwerfen.",
         "Schreibe eine Produktbeschreibung (maximal [100] Wörter) für [PRODUKT]. Eigenschaften: [LISTE]. Zielgruppe: [ZIELGRUPPE]. Verwende nur die genannten Eigenschaften, keine Superlative und keine Wirkversprechen.",
         "Technische Angaben mit dem Datenblatt abgleichen."),
        ("Blogartikel-Gliederung", "Ein Thema strukturieren.",
         "Erstelle die Gliederung eines Blogartikels zum Thema „[THEMA]“ für [ZIELGRUPPE]: Arbeitstitel (3 Varianten), Einleitung (Problem), 4–6 Zwischenüberschriften mit je 2 Stichpunkten, Fazit, 3 Fragen für einen FAQ-Abschnitt. Markiere Stellen, wo wir eigene Erfahrung oder belegte Zahlen ergänzen müssen, mit „[Beleg ergänzen]“.",
         "Fachliche Aussagen selbst belegen. Keine Quellen von der KI übernehmen, ohne sie zu öffnen."),
        ("Website-Text verständlicher machen", "Text kürzen und vereinfachen.",
         "Vereinfache den folgenden Webseitentext auf Sprachniveau [B1], kürze ihn um etwa [30 %] und behalte alle sachlichen Aussagen. Markiere Stellen, an denen Inhalt wegfiel.\n\nText:\n[ÖFFENTLICHER TEXT]",
         "Ergebnis mit dem Original abgleichen; rechtliche Pflichtangaben nie von der KI ändern lassen."),
        ("Redaktionsplan", "Inhalte planen.",
         "Erstelle einen Redaktionsplan für 4 Wochen als Tabelle (Woche, Kanal, Thema, Format, Ziel, Verantwortlich als Rolle). Kontext: [BRANCHE], [ZIELGRUPPE], verfügbare Zeit: [STUNDEN] pro Woche. Plane realistisch und kennzeichne optionale Beiträge.",
         "Mit den tatsächlichen Kapazitäten abgleichen."),
    ]),
    ("Personal", [
        ("Stellenanzeige entwerfen", "Eine Anzeige formulieren.",
         "Schreibe den Entwurf einer Stellenanzeige für [POSITION] in einem Betrieb mit [ANZAHL] Beschäftigten in [ORT/REMOTE]. Aufgaben: [LISTE]. Anforderungen (nur wirklich nötige): [LISTE]. Wir bieten: [LISTE]. Formuliere inklusiv und diskriminierungsfrei, ohne Altersangaben, ohne Geschlechtsfestlegung, und gib keine Gehaltsversprechen, die ich nicht genannt habe.",
         "Vor Veröffentlichung auf Rechtskonformität prüfen (z. B. Gleichbehandlung, Gehaltsangaben). Keine Daten von Bewerbenden einfügen."),
        ("Onboarding-Checkliste", "Neue Kolleginnen und Kollegen strukturiert einführen.",
         "Erstelle eine Onboarding-Checkliste für [POSITION] mit Abschnitten: vor dem ersten Tag, erster Tag, erste Woche, erster Monat. Pro Punkt: Verantwortliche Rolle und Hinweis. Berücksichtige Zugänge, Datenschutz- und KI-Schulung, Ansprechpersonen und Feedbackgespräche.",
         "An Ihre tatsächlichen Systeme und Abläufe anpassen."),
        ("Interviewleitfaden", "Strukturierte Fragen vorbereiten.",
         "Erstelle einen Interviewleitfaden für [POSITION] mit 8 verhaltensbasierten Fragen (z. B. „Erzählen Sie von einer Situation, in der …“), je einem Hinweis, worauf wir achten, und einer Bewertungsskala von 1 bis 5 mit Kriterien. Keine Fragen zu geschützten persönlichen Merkmalen wie Familienplanung, Religion, Herkunft oder Gesundheit.",
         "Die KI trifft keine Auswahlentscheidung. Keine Bewerbungsunterlagen hochladen. Fragen vorab prüfen."),
        ("Feedbackgespräch vorbereiten", "Ein Gespräch gut strukturieren – ohne Personendaten.",
         "Ich bereite ein Feedbackgespräch mit einer Mitarbeiterin/einem Mitarbeiter in der Rolle [ROLLE] vor. Situation (allgemein, ohne Namen): [BESCHREIBUNG]. Erstelle: eine Gesprächsstruktur mit Einstieg, konkretem Feedback nach dem Muster Beobachtung–Wirkung–Wunsch, vier offenen Fragen und einem Abschluss mit Vereinbarungen. Bleibe sachlich und wertschätzend.",
         "Keine Namen, Gesundheitsdaten oder Leistungsdaten eingeben. Die Bewertung der Person bleibt Sache der Führungskraft."),
        ("Lerneinheit oder Schulungsplan", "Interne Weiterbildung planen.",
         "Erstelle einen Plan für eine Lerneinheit von [45] Minuten zum Thema „[THEMA]“ für [ZIELGRUPPE] ohne Vorkenntnisse. Struktur: Ziel, Einstieg, zwei Erklärblöcke, eine Übung, Wissenscheck mit 3 Fragen. Nenne den Zeitbedarf je Block.",
         "Inhalte fachlich prüfen und an Ihren Betrieb anpassen."),
        ("Rundschreiben zur Regeländerung", "Eine interne Mitteilung verständlich formulieren.",
         "Formuliere eine interne Mitteilung (maximal [150] Wörter) an alle Beschäftigten: Was ändert sich ([ÄNDERUNG])? Ab wann ([DATUM])? Warum? Was müssen die Beschäftigten tun? Wer hilft bei Fragen ([KONTAKT])? Ton: klar und respektvoll, ohne Behördendeutsch.",
         "Inhalt und Datum vor dem Versand prüfen; Beteiligungsrechte (z. B. Betriebsrat) bei Bedarf klären."),
    ]),
]


def build(outdir):
    D = Doc("Prompt-Bibliothek", "30 Vorlagen für den Arbeitsalltag in kleinen Unternehmen", "Prompt-Bibliothek")
    D.disclaimer_box()
    D.h1("So nutzen Sie diese Bibliothek")
    D.numbered(
        [
            "**Tool wählen:** Nur ein von Ihrem Betrieb freigegebenes KI-Tool verwenden.",
            "**Datenampel prüfen:** Gehört das, was Sie eingeben wollen, zu grün, gelb oder rot? Rote Daten nur anonymisiert oder im dafür freigegebenen Tool.",
            "**Platzhalter ersetzen:** Alles in [ECKIGEN KLAMMERN] durch Ihre Angaben ersetzen – ohne echte Namen, Nummern oder vertrauliche Details.",
            "**Prompt einfügen** und das Ergebnis als Entwurf behandeln.",
            "**Prüfen:** Fakten, Zahlen/Quellen, Namen/Anrede, Ton/Zusagen, Vertraulichkeit/Rechte. Erst dann verwenden.",
        ]
    )
    D.callout(
        "Aufbau eines guten Prompts",
        [
            "**Rolle** („Du bist …“) · **Aufgabe** (was genau?) · **Kontext** (Zielgruppe, Zweck, Ton) · **Format** (Länge, Gliederung) · **Grenzen** („Erfinde nichts. Markiere Unsicheres.“).",
            "Bitten Sie die KI nie darum, Quellen, Paragraphen oder Urteile zu nennen und zu übernehmen – sie kann sie erfinden. Wenn Sie Quellen brauchen, suchen Sie sie selbst und prüfen Sie sie.",
        ],
    )
    D.callout(
        "Vor dem ersten Einsatz",
        ["Alle Beispiele sind Vorlagen und keine Garantie für ein gutes Ergebnis. Je nach Tool fallen Antworten unterschiedlich aus. Probieren Sie Prompts mit unkritischen Beispielen aus, bevor Sie sie im Alltag nutzen."],
        fill=SOFT_FILL,
    )
    n = 0
    for cat, prompts in CATS:
        D.page_break()
        D.h1(f"{cat}")
        for title, zweck, prompt, hint in prompts:
            n += 1
            t = D.table(
                [f"{n}. {title}", ""],
                [
                    ["Zweck", zweck],
                    ["Prompt\n(kopieren)", prompt],
                    ["Hinweis", hint],
                ],
                widths=[2.8, 13.6],
                size=10,
            )
            m = t.rows[0].cells[0].merge(t.rows[0].cells[1])
            for extra in m.paragraphs[1:]:
                extra._element.getparent().remove(extra._element)
    assert n == 30, n
    D.save(f"{outdir}/{FILE}")
    return FILE
