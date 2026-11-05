from kit_lib import *

FILE = "Prompt-Bibliothek.docx"

BSP = "[OPTIONAL, aber wirksam: ein kurzes, gelungenes Beispiel aus Ihrem Betrieb, anonymisiert]"
GRZ0 = "Erfinde nichts; markiere Unsicheres mit „[unklar]“."
PLAUS = ("Erstelle zusätzlich ein Blatt „Plausibilität“, in dem du jede Auswertung gegenrechnest (Summen, Stichproben, Ausreißer) "
         "und Auffälligkeiten markierst. Nenne ausdrücklich, was du nicht prüfen konntest.")

# Felder: (Titel, Zweck, ROLLE, ZIEL, ZIELGRUPPE, TON, BEISPIEL, FORMAT, GRENZEN, MATERIAL, Hinweis)
CATS = [
    ("Verwaltung", [
        ("Besprechungsprotokoll aus Stichpunkten", "Aus eigenen Notizen ein sauberes Protokoll machen.",
         "Assistenz der Geschäftsführung", "Ein Besprechungsprotokoll aus den Stichpunkten erstellen", "Teilnehmende und Abwesende, die nachlesen",
         "Sachlich, knapp", BSP, "Abschnitte: Teilnehmende (nur Kürzel), Beschlüsse, Aufgaben (wer, was, bis wann), offene Punkte", GRZ0,
         "[ANONYMISIERTE NOTIZEN]",
         "Namen durch Kürzel ersetzen. Aufgaben und Fristen mit den echten Notizen abgleichen."),
        ("E-Mail professionell umformulieren", "Einen eigenen Entwurf klarer und höflicher machen.",
         "Erfahrene Sachbearbeiterin für Geschäftskorrespondenz", "Den Entwurf klar, höflich und kurz formulieren, ohne Inhalte zu ändern", "[EMPFÄNGERGRUPPE, z. B. Geschäftspartner]",
         "[sachlich/herzlich]", BSP, "Maximal [120] Wörter, Betreff vorschlagen", "Alle Inhalte und Zahlen unverändert lassen, nichts hinzufügen",
         "[ENTWURF OHNE PERSONENDATEN]",
         "Namen, Nummern und Adressen vor dem Einfügen entfernen und danach selbst wieder einsetzen."),
        ("Langen Text zusammenfassen", "Schneller verstehen, worum es geht – nur bei nicht vertraulichen Texten.",
         "Aufmerksame Redakteurin", "Den Text für eine Entscheidung zusammenfassen", "[WER LIEST DIE ZUSAMMENFASSUNG?]",
         "Neutral", BSP, "[5] Stichpunkte plus ein Satz Gesamtfazit; getrennt: „Steht im Text“ und „Meine Einschätzung“", "Unsicheres markieren, nichts ergänzen, was nicht im Text steht",
         "[ÖFFENTLICHER ODER FREIGEGEBENER TEXT]",
         "Nur grüne (oder für das Tool freigegebene gelbe) Texte. Zusammenfassungen können Wichtiges weglassen: bei wichtigen Entscheidungen das Original lesen."),
        ("Checkliste oder Ablauf erstellen", "Eine wiederkehrende Aufgabe als Checkliste festhalten.",
         "Organisationsberater/in für Kleinbetriebe", "Eine Checkliste für den Ablauf „[AUFGABE]“ erstellen", "Beschäftigte eines Betriebs mit [ANZAHL] Personen",
         "Klar, handlungsorientiert", BSP, "Phasen (vorher, am Tag, danach); je Schritt eine Rolle (keine Namen); Datenschutz-Schritte mit „(Datenschutz prüfen)“ markieren", GRZ0,
         "[STICHPUNKTE ZUM ABLAUF]",
         "Mit den tatsächlichen Abläufen im Betrieb abgleichen; die KI kennt sie nicht."),
        ("Agenda für eine Besprechung", "Eine Besprechung vorbereiten.",
         "Moderator/in", "Eine Agenda für [60] Minuten zum Thema „[THEMA]“ erstellen; Ziel der Besprechung: [ZIEL]", "Teilnehmende: [ROLLEN]",
         "Strukturiert, zeitbewusst", BSP, "Tabelle: Punkt, Dauer, Ziel (informieren/entscheiden/Ideen sammeln), Vorbereitung; 10 % Puffer", "Keine Zeiten über die Gesamtdauer",
         "[THEMENLISTE]",
         "Zeiten realistisch nachprüfen. Keine internen Details, wenn das Tool nicht dafür freigegeben ist."),
        ("Tabellenformel erklären oder bauen", "Excel/Google-Sheets-Formeln ohne echte Daten.",
         "Geduldiger Tabellenkalkulations-Trainer", "Eine Formel für [ZIEL, z. B. Summe je Monat] vorschlagen und erklären", "Anwender ohne Programmierkenntnisse",
         "Einfach, mit Beispiel", BSP, "Formel, Erklärung in einfachen Worten, zwei Fälle, in denen sie falsche Ergebnisse liefern könnte", "Nur erfundene Beispieldaten verwenden",
         "Ich arbeite mit [Excel/Google Sheets]. Spalte A enthält [BESCHREIBUNG], Spalte B [BESCHREIBUNG].",
         "Formel an einer kleinen Testtabelle ausprobieren. Keine echten Daten einfügen."),
    ]),
    ("Vertrieb", [
        ("Begleitschreiben zum Angebot", "Einen Angebotsbegleittext entwerfen.",
         "Vertriebsmitarbeiter/in eines kleinen Unternehmens der Branche [BRANCHE]", "Ein Begleitschreiben zu einem Angebot über [LEISTUNG] verfassen, das zum nächsten Schritt „[SCHRITT]“ führt", "[ANSPRECHPARTNER-TYP, z. B. Geschäftsführung eines kleinen Betriebs]",
         "Freundlich, kompetent, nicht aufdringlich", BSP, "Maximal [150] Wörter; Nutzen: [NUTZEN 1], [NUTZEN 2]", "Keine Preise, Fristen oder Garantien nennen, die ich nicht angegeben habe",
         "[STICHPUNKTE ZUM ANGEBOT, ohne Personendaten]",
         "Preise, Fristen und Zusagen selbst eintragen und prüfen. Kundennamen erst im fertigen Dokument einsetzen."),
        ("Nachfassmail an Bestandskontakte", "Eine freundliche Erinnerung nach einem Angebot.",
         "Aufmerksame Vertriebsmitarbeiterin", "Nachfragen, ob das Angebot vom [ZEITRAUM] noch Fragen offenlässt", "Bestehender Geschäftskontakt",
         "[TON, z. B. freundlich, ohne Druck]", BSP, "Maximal [100] Wörter, ein Angebot zur Hilfe: [HILFE]", "Keine Übertreibung, kein künstlicher Zeitdruck",
         "[STICHPUNKTE ZUM ANGEBOT]",
         "Nur an Kontakte, mit denen eine Geschäftsbeziehung besteht oder die zugestimmt haben. Regeln zu Werbung im Zweifel mit Rechtsberatung klären."),
        ("Einwände vorbereiten", "Auf typische Einwände vorbereitet sein.",
         "Erfahrene Vertriebstrainerin", "Die 8 häufigsten Einwände sammeln und ehrliche Antworten samt Rückfrage formulieren", "Interessenten: [ZIELGRUPPE]",
         "Respektvoll, ehrlich", BSP, "Tabelle: Einwand, kurze Antwort, Rückfrage", "Keine Kundenzahlen, Referenzen oder Garantien erfinden",
         "Unsere Leistung: [BESCHREIBUNG]",
         "Antworten mit echten Erfahrungen abgleichen. Referenzen und Zahlen ausschließlich selbst ergänzen."),
        ("Gesprächsvorbereitung aus öffentlichen Infos", "Sich auf ein Erstgespräch vorbereiten.",
         "Vertriebsanalyst/in", "Aus den öffentlichen Informationen Fragen und eine Gesprächsstruktur ableiten", "Ich selbst (Vorbereitung)",
         "Sachlich", BSP, "1) Ableitungen, 2) fünf offene Fragen, 3) Gesprächsstruktur; Fakten aus dem Text und Vermutungen getrennt", "Nichts hinzuerfinden",
         "Öffentlich verfügbare Information: [TEXT AUS WEBSEITE/PRESSE]",
         "Nur öffentliche Informationen verwenden. Keine Daten aus dem Kundenmanagement-System."),
        ("Nutzen statt Merkmale", "Produktmerkmale in Kundennutzen übersetzen.",
         "Texter/in", "Jedes Merkmal in einen konkreten Nutzen übersetzen", "[ZIELGRUPPE]",
         "Einfach, ohne Superlative", BSP, "Je Merkmal: Merkmal → Was bedeutet das im Alltag? → Warum ist das wichtig?", "Keine Wirkversprechen, die wir nicht belegen können",
         "Merkmale: [LISTE]",
         "Prüfen, ob jeder Nutzen belegbar ist. Streichen, was wir nicht halten können."),
        ("Leitfaden für das Erstgespräch", "Ein Gespräch strukturieren.",
         "Vertriebstrainer/in", "Einen Leitfaden für ein 20-minütiges Erstgespräch zu [THEMA] erstellen", "Mitarbeitende im Vertrieb",
         "Ehrlich, ohne Drucktechniken", BSP, "Einstieg, Bedarf klären (6 offene Fragen), Lösung kurz vorstellen, Einwände, Abschluss mit nächstem Schritt", GRZ0,
         "Zielgruppe der Gespräche: [ZIELGRUPPE]",
         "Leitfaden zu Ihrem Stil anpassen und ausprobieren."),
    ]),
    ("Kundenservice", [
        ("Antwortentwurf auf eine Kundenanfrage", "Antworten schneller und freundlicher formulieren.",
         "Kundenservice-Mitarbeiter/in", "Eine hilfreiche Antwort auf die Anfrage schreiben", "Kundin/Kunde mit Anliegen",
         "Freundlich, klar, lösungsorientiert", BSP, "Maximal [120] Wörter, Anrede und Gruß", "Keine Zusagen zu Erstattung, Fristen oder Kulanz, die nicht in den Regeln stehen",
         "Regeln: [UNSERE REGELN IN STICHPUNKTEN]\nAnfrage (anonymisiert): [ANFRAGE OHNE NAMEN/NUMMERN]",
         "Name, Bestellnummer, Adresse weglassen und im Ergebnis wieder einsetzen. Zusagen vor dem Senden prüfen."),
        ("Beschwerde deeskalierend beantworten", "Eine verärgerte Nachricht ruhig beantworten.",
         "Erfahrene Servicekraft für Beschwerden", "Das Anliegen aufgreifen, Verständnis zeigen, nächsten Schritt „[SCHRITT]“ nennen", "Verärgerte Kundin/verärgerter Kunde",
         "Ruhig, respektvoll, ohne Floskeln", BSP, "Vier Teile: Anliegen in einem Satz, Verständnis, nächster Schritt, Abschluss", "Keine Schuld erfinden, keine Rechtfertigungen, keine Zusagen ohne Rücksprache",
         "Beschwerde (anonymisiert): [TEXT]",
         "Keine Schuldanerkenntnisse oder Zusagen ohne Rücksprache. Bei rechtlichen Drohungen [NAME/Funktion] einbinden."),
        ("FAQ-Entwurf", "Aus häufigen Fragen eine FAQ-Liste entwickeln.",
         "Redakteur/in für Kundeninformation", "Zu jeder Frage eine kurze, klare Antwort formulieren", "Kundinnen und Kunden auf unserer Webseite",
         "Einfach, freundlich", BSP, "[2–3] Sätze je Antwort, nach Themen gruppiert", "Wo die Antwort nicht aus meinen Angaben hervorgeht, „[Antwort ergänzen]“ schreiben",
         "Häufige Fragen (ohne Personendaten): [LISTE]",
         "Antworten mit den tatsächlichen Regeln abgleichen; die KI darf keine Lücken füllen."),
        ("Tonalitäts-Check", "Eigene Texte auf Wirkung prüfen.",
         "Kommunikationstrainerin", "Wirkung des Textes beim Kunden einschätzen", "Kundinnen und Kunden",
         "Konstruktiv", BSP, "Drei missverständliche oder schroffe Stellen mit Alternativvorschlag", "Keine Inhalte verändern",
         "Text: [TEXT OHNE PERSONENDATEN]",
         "Die KI beurteilt Wirkung nur ungefähr. Im Zweifel Kollegin oder Kollegen lesen lassen."),
        ("Anfragen sortieren", "Beispielanfragen in Kategorien einteilen.",
         "Servicekoordinator/in", "Anfragen nach Kategorie und Dringlichkeit einordnen", "Interne Weiterleitung",
         "Sachlich", BSP, "Tabelle: Nummer, Kategorie (z. B. Lieferung, Rechnung, Reklamation, Technik, Sonstiges), Dringlichkeit (hoch/mittel/niedrig), Begründung in einem Satz", GRZ0,
         "Anfragen: [NUMMERIERTE, ANONYMISIERTE BEISPIELE]",
         "Nur anonymisierte Beispiele. Die Zuordnung ist ein Vorschlag; Dringlichkeit entscheidet ein Mensch."),
        ("Textbausteine für Standardfälle", "Eine Sammlung wiederverwendbarer Antworten aufbauen.",
         "Servicetexter/in", "Fünf Textbausteine für diese Situationen schreiben: [SITUATIONEN]", "Kundinnen und Kunden",
         "Freundlich, klar", BSP, "Maximal [80] Wörter je Baustein; Platzhalter in eckigen Klammern für Name, Datum, Details", "Keine Zusagen oder Fristen, die ich nicht genannt habe",
         "[SITUATIONEN, z. B. Lieferverzögerung, Terminbestätigung]",
         "Rechtlich unkritisch halten; keine Garantien formulieren, die Sie nicht geprüft haben."),
    ]),
    ("Marketing", [
        ("Ideen für Social-Media-Beiträge", "Themen für einen Monat sammeln.",
         "Social-Media-Redakteur/in für die Branche [BRANCHE]", "12 Themen für Beiträge auf [KANAL] vorschlagen", "[ZIELGRUPPE]",
         "[TON, z. B. locker, kompetent]", BSP, "Tabelle: Thema, Kernbotschaft, Format (Text/Bild/Video), erste Zeile als Beispiel", "Keine erfundenen Zahlen, Kundenbeispiele oder Heilversprechen",
         "[STICHPUNKTE ZU UNSEREM ANGEBOT]",
         "Auswahl selbst treffen. Werbung muss als solche erkennbar sein; Bildrechte klären."),
        ("Newsletter-Entwurf", "Einen Newsletter strukturieren.",
         "Newsletter-Redakteur/in", "Einen Newsletter zum Thema „[THEMA]“ entwerfen mit Handlungsaufforderung: [CTA]", "[ZIELGRUPPE]",
         "[TON]", BSP, "Maximal [250] Wörter; Betreff (3 Varianten), Einstieg, drei Abschnitte mit Zwischenüberschriften", "Keine erfundenen Fakten, Zitate oder Statistiken",
         "[STICHPUNKTE]",
         "Fakten prüfen. Versand nur an Personen, die zugestimmt haben; Pflichtangaben und Abmeldelink nicht vergessen."),
        ("Produktbeschreibung", "Einen Beschreibungstext entwerfen.",
         "Produkttexter/in", "Eine Produktbeschreibung für [PRODUKT] verfassen", "[ZIELGRUPPE]",
         "Klar, ohne Superlative", BSP, "Maximal [100] Wörter", "Nur die genannten Eigenschaften verwenden, keine Wirkversprechen",
         "Eigenschaften: [LISTE]",
         "Technische Angaben mit dem Datenblatt abgleichen."),
        ("Blogartikel-Gliederung", "Ein Thema strukturieren.",
         "Fachredakteur/in", "Die Gliederung eines Blogartikels zum Thema „[THEMA]“ erstellen", "[ZIELGRUPPE]",
         "Verständlich, praxisnah", BSP, "Arbeitstitel (3 Varianten), Einleitung, 4–6 Zwischenüberschriften mit je 2 Stichpunkten, Fazit, 3 FAQ-Fragen", "Stellen, an denen eigene Erfahrung oder Belege nötig sind, mit „[Beleg ergänzen]“ markieren; keine Quellen nennen",
         "[STICHPUNKTE]",
         "Fachliche Aussagen selbst belegen. Keine Quellen von der KI übernehmen, ohne sie zu öffnen."),
        ("Website-Text verständlicher machen", "Text kürzen und vereinfachen.",
         "Lektor/in für einfache Sprache", "Den Text auf Sprachniveau [B1] vereinfachen und um etwa [30 %] kürzen", "Besucher unserer Webseite",
         "Freundlich, klar", BSP, "Gleiche Struktur, Stellen mit entfallenem Inhalt markieren", "Alle sachlichen Aussagen beibehalten",
         "[ÖFFENTLICHER TEXT]",
         "Ergebnis mit dem Original abgleichen; rechtliche Pflichtangaben nie von der KI ändern lassen."),
        ("Redaktionsplan", "Inhalte planen.",
         "Content-Planer/in", "Einen Redaktionsplan für 4 Wochen erstellen", "[ZIELGRUPPE], Branche [BRANCHE]",
         "Realistisch", BSP, "Tabelle: Woche, Kanal, Thema, Format, Ziel, Verantwortlich (Rolle); optionale Beiträge kennzeichnen", "Planen für höchstens [STUNDEN] pro Woche",
         "[STICHPUNKTE ZU THEMEN UND KANÄLEN]",
         "Mit den tatsächlichen Kapazitäten abgleichen."),
    ]),
    ("Personal", [
        ("Stellenanzeige entwerfen", "Eine Anzeige formulieren.",
         "Personalreferent/in", "Eine Stellenanzeige für [POSITION] in [ORT/REMOTE] entwerfen", "Potenzielle Bewerberinnen und Bewerber",
         "Einladend, ehrlich", BSP, "Aufgaben, Anforderungen (nur wirklich nötige), Wir bieten", "Inklusiv und diskriminierungsfrei, keine Altersangaben, keine Gehaltsversprechen",
         "Aufgaben: [LISTE]; Anforderungen: [LISTE]; Wir bieten: [LISTE]; Betrieb mit [ANZAHL] Beschäftigten",
         "Vor Veröffentlichung auf Rechtskonformität prüfen (z. B. Gleichbehandlung, Gehaltsangaben). Keine Daten von Bewerbenden einfügen."),
        ("Onboarding-Checkliste", "Neue Kolleginnen und Kollegen strukturiert einführen.",
         "Personalentwickler/in", "Eine Onboarding-Checkliste für [POSITION] erstellen", "Führungskraft und neue Mitarbeitende",
         "Praktisch", BSP, "Abschnitte: vor dem ersten Tag, erster Tag, erste Woche, erster Monat; je Punkt Rolle und Hinweis", "Berücksichtigen: Zugänge, Datenschutz- und KI-Schulung, Ansprechpersonen, Feedbackgespräche; nichts erfinden",
         "[UNSERE SYSTEME UND ABLÄUFE IN STICHPUNKTEN]",
         "An Ihre tatsächlichen Systeme und Abläufe anpassen."),
        ("Interviewleitfaden", "Strukturierte Fragen vorbereiten.",
         "Erfahrene Interviewerin für strukturierte Gespräche", "Einen Leitfaden für [POSITION] erstellen", "Interviewende im Betrieb",
         "Sachlich, wertschätzend", BSP, "8 verhaltensbasierte Fragen („Erzählen Sie von einer Situation, in der …“), je mit Hinweis und Bewertungsskala 1–5 mit Kriterien", "Keine Fragen zu geschützten Merkmalen wie Familienplanung, Religion, Herkunft, Gesundheit",
         "Anforderungen: [LISTE]",
         "Die KI trifft keine Auswahlentscheidung. Keine Bewerbungsunterlagen hochladen. Fragen vorab prüfen."),
        ("Feedbackgespräch vorbereiten", "Ein Gespräch strukturieren – ohne Personendaten.",
         "Führungskräftecoach", "Ein Feedbackgespräch vorbereiten", "Führungskraft; Gegenüber ist ein/e Mitarbeitende/r in der Rolle [ROLLE]",
         "Wertschätzend, sachlich", BSP, "Einstieg, Feedback nach Beobachtung–Wirkung–Wunsch, vier offene Fragen, Abschluss mit Vereinbarungen", "Nur mit der allgemeinen Situation arbeiten, keine Namen, Gesundheits- oder Leistungsdaten",
         "Situation (allgemein, ohne Namen): [BESCHREIBUNG]",
         "Keine Namen, Gesundheitsdaten oder Leistungsdaten eingeben. Die Bewertung der Person bleibt Sache der Führungskraft."),
        ("Lerneinheit oder Schulungsplan", "Interne Weiterbildung planen.",
         "Trainer/in für Erwachsenenbildung", "Eine Lerneinheit von [45] Minuten zum Thema „[THEMA]“ planen", "Beschäftigte ohne Vorkenntnisse",
         "Anschaulich", BSP, "Ziel, Einstieg, zwei Erklärblöcke, eine Übung, Wissenscheck mit 3 Fragen; Zeit je Block", GRZ0,
         "[STICHPUNKTE ZUM THEMA]",
         "Inhalte fachlich prüfen und an Ihren Betrieb anpassen."),
        ("Rundschreiben zur Regeländerung", "Eine interne Mitteilung verständlich formulieren.",
         "Interne Kommunikation", "Über die Änderung „[ÄNDERUNG]“ ab [DATUM] informieren: warum, was ist zu tun, wer hilft ([KONTAKT])", "Alle Beschäftigten",
         "Klar, respektvoll, kein Behördendeutsch", BSP, "Maximal [150] Wörter", "Nichts hinzufügen, was nicht angegeben ist",
         "[STICHPUNKTE ZUR ÄNDERUNG]",
         "Inhalt und Datum vor dem Versand prüfen; Beteiligungsrechte (z. B. Betriebsrat) bei Bedarf klären."),
    ]),
    ("Excel und Auswertung (mit Plausibilitätscheck)", [
        ("Auswertung nach Monat und Kategorie", "Eine Tabelle auswerten und das Ergebnis gegenrechnen lassen.",
         "Controlling-Assistenz", "Die Daten nach Monat und Kategorie auswerten; Ergebnis: Summentabelle und Kurzfazit in 3 Sätzen", "Geschäftsleitung ohne Tabellenkenntnisse",
         "Sachlich, klar", BSP, "Neue Blätter „Auswertung“ und „Plausibilität“", PLAUS,
         "Tabelle mit [ANONYMISIERTEN ODER AGGREGIERTEN DATEN: Spalten …]",
         "Nur Daten ohne Personenbezug (Datenampel!). Plausibilitätsblatt selbst stichprobenartig nachrechnen."),
        ("Daten bereinigen und Dubletten finden", "Eine Liste aufräumen, ohne dass etwas unbemerkt verloren geht.",
         "Datenpfleger/in", "Die Liste bereinigen (Schreibweisen vereinheitlichen, Dubletten markieren, Leerzeilen entfernen), aber nichts löschen, sondern markieren", "Kolleginnen und Kollegen, die die Liste weiterverwenden",
         "Sachlich", BSP, "Neue Spalte „Hinweis“ je Zeile; Blatt „Änderungsprotokoll“; Blatt „Plausibilität“",
         PLAUS + " Zähle Zeilen vorher und nachher und erkläre jede Differenz.",
         "Liste mit [ANONYMISIERTEN BEISPIELDATEN]",
         "Nur Test-/Beispieldaten ohne Personenbezug. Ergebnis immer mit dem Original abgleichen."),
        ("Plan-Ist-Vergleich", "Abweichungen berechnen und erklären lassen.",
         "Controller/in eines kleinen Betriebs", "Plan und Ist je Position vergleichen, Abweichungen in € und % berechnen, die drei größten markieren", "Geschäftsleitung",
         "Nüchtern", BSP, "Tabelle plus Blatt „Plausibilität“; Erklärungen als Vermutungen kennzeichnen (nicht als Tatsachen)",
         PLAUS + " Erfinde keine Ursachen für Abweichungen.",
         "Plan- und Ist-Werte [ANONYMISIERT/AGGREGIERT]",
         "Interne Zahlen sind meist gelb (Datenampel): nur in Tools der Stufe 2 oder 3. Berechnungen stichprobenartig selbst prüfen."),
        ("Kennzahlen-Übersicht mit Prüfblatt", "Eine einfache Übersicht für Besprechungen aufbauen.",
         "Business-Analyst/in", "Aus den Daten fünf Kennzahlen berechnen: [KENNZAHLEN] und übersichtlich darstellen", "Teamleitungen",
         "Verständlich, ohne Fachjargon", BSP, "Blatt „Übersicht“ mit Definitionen der Kennzahlen, Blatt „Plausibilität“",
         PLAUS + " Beschreibe bei jeder Kennzahl die Berechnung in einem Satz.",
         "Daten: [ANONYMISIERT/AGGREGIERT]",
         "Prüfen, ob die beschriebene Berechnung zu Ihrer Definition passt."),
    ]),
]

LABELS = ["ROLLE", "ZIEL", "ZIELGRUPPE", "TON", "BEISPIEL", "FORMAT", "GRENZEN", "MATERIAL"]


def assemble(p):
    _, _, rolle, ziel, zg, ton, bsp, fmt, grenzen, material, _ = p
    vals = [f"Du bist {rolle}.", ziel, zg, ton, bsp, fmt, grenzen, material]
    return "\n".join(f"{l}: {v}" for l, v in zip(LABELS, vals))


def build(outdir):
    D = Doc("Prompt-Bibliothek", "34 Vorlagen für den Arbeitsalltag in kleinen Unternehmen – mit dem Kontext-Baukasten", "Prompt-Bibliothek")
    D.disclaimer_box()
    D.h1("So nutzen Sie diese Bibliothek")
    D.numbered(
        [
            "**Tool wählen:** Nur ein von Ihrem Betrieb freigegebenes KI-Tool verwenden.",
            "**Datenampel prüfen:** Gehört das, was Sie eingeben wollen, zu grün, gelb oder rot? Rote Daten nur anonymisiert oder im dafür freigegebenen Tool.",
            "**Platzhalter ersetzen:** Alles in [ECKIGEN KLAMMERN] durch Ihre Angaben ersetzen, ohne echte Namen, Nummern oder vertrauliche Details.",
            "**Prompt einfügen** und das Ergebnis als Entwurf behandeln.",
            "**Prüfen:** Fakten, Zahlen/Quellen, Namen/Anrede, Ton/Zusagen, Vertraulichkeit/Rechte. Erst dann verwenden.",
        ]
    )
    D.h2("Der Kontext-Baukasten – in jedem Prompt sichtbar")
    D.p("Jeder Prompt ist nach demselben Schema aufgebaut. **Je mehr dieser Bausteine Sie füllen, desto besser trifft die KI.** Probieren Sie es selbst: Siehe Aha-Übung 1 im Arbeitsblatt.")
    D.table(
        ["Baustein", "Bedeutung", "Beispiel"],
        [
            ["ROLLE", "Wer soll die KI sein?", "Kundenservice-Mitarbeiter/in"],
            ["ZIEL", "Was soll am Ende erreicht sein?", "Eine Antwort, die den Ärger aufgreift"],
            ["ZIELGRUPPE", "Für wen ist der Text?", "Verärgerte Stammkundin"],
            ["TON", "Wie soll es klingen?", "Ruhig, freundlich"],
            ["BEISPIEL", "Wie klingt es bei uns? (stärkster Hebel für Ihren Stil)", "Zwei Sätze aus einer gelungenen Antwort"],
            ["FORMAT", "Länge und Gliederung", "Maximal 120 Wörter, zwei Absätze"],
            ["GRENZEN", "Was soll nicht passieren?", "Nichts erfinden, keine Zusagen"],
            ["MATERIAL", "Das, womit gearbeitet wird (anonymisiert!)", "Die Beschwerde ohne Namen"],
        ],
        widths=[3.0, 7.0, 6.4],
        size=9.5,
    )
    D.callout(
        "Wichtig",
        [
            "Bitten Sie die KI nie darum, Quellen, Paragraphen oder Urteile zu nennen und zu übernehmen. Sie kann sie erfinden. Wenn Sie Quellen brauchen, suchen Sie sie selbst und prüfen Sie sie.",
            "Alle Beispiele sind Vorlagen und keine Garantie für ein gutes Ergebnis. Je nach Tool fallen Antworten unterschiedlich aus. Probieren Sie Prompts mit unkritischen Beispielen aus.",
        ],
        fill=SOFT_FILL,
    )
    n = 0
    for cat, prompts in CATS:
        D.page_break()
        D.h1(cat)
        if cat.startswith("Excel"):
            D.callout(
                "Warum immer ein Plausibilitätscheck?",
                [
                    "**KI kann sich verrechnen, der Plausibilitätscheck macht Fehler sichtbar.** Deshalb fordern alle Prompts dieses Bereichs ein Blatt „Plausibilität“, in dem die Ergebnisse gegengerechnet werden. Prüfen Sie dieses Blatt trotzdem selbst: ein paar Stichproben mit dem Taschenrechner oder per eigener Formel.",
                    "Je nach Tool und Tarif kann die KI Tabellen direkt erzeugen oder bearbeiten. Wenn nicht, lassen Sie sich Formeln und eine Schritt-für-Schritt-Anleitung ausgeben und legen Sie die Blätter selbst an. Nur anonymisierte oder aggregierte Daten ohne Personenbezug verwenden.",
                ],
                fill=NOTE_FILL,
            )
        for p in prompts:
            n += 1
            t = D.table(
                [f"{n}. {p[0]}", ""],
                [["Zweck", p[1]], ["Prompt\n(kopieren)", assemble(p)], ["Hinweis", p[10]]],
                widths=[2.8, 13.6],
                size=10,
            )
            m = t.rows[0].cells[0].merge(t.rows[0].cells[1])
            for extra in m.paragraphs[1:]:
                extra._element.getparent().remove(extra._element)
    assert n == 34, n
    D.save(f"{outdir}/{FILE}")
    return FILE
