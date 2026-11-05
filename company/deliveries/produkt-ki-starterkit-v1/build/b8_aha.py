from kit_lib import *

FILE = "Aha-Uebungen-Arbeitsblatt.docx"

BESCHWERDE = ("„Mein Paket ist jetzt schon zum zweiten Mal zu spät gekommen. Beim ersten Mal hieß es, das sei ein Ausnahmefall. "
              "Ich bin ehrlich enttäuscht und überlege, ob ich noch einmal bei Ihnen bestelle.“  (frei erfundenes Beispiel)")

CONTEXT_PROMPT = """ROLLE: Du bist Kundenservice-Mitarbeiter/in in einem kleinen Online-Shop für [PRODUKTART].
ZIEL: Schreibe eine Antwort, die den Ärger ernst nimmt, den Vorfall ohne Ausreden anerkennt und einen konkreten nächsten Schritt anbietet: [z. B. Versandstatus prüfen und innerhalb von 24 Stunden melden].
ZIELGRUPPE: Eine Stammkundin, die enttäuscht, aber noch nicht verloren ist.
TON: Freundlich, ruhig, persönlich; kein Behördendeutsch, keine Floskeln.
BEISPIEL (so klingt unser Haus): „Guten Tag Frau [Name], das ist ärgerlich, und ich verstehe Ihren Unmut. Ich kümmere mich heute noch darum …“
FORMAT: Maximal 120 Wörter, Anrede und Gruß, zwei kurze Absätze.
GRENZEN: Mache keine Zusagen zu Erstattung oder Gutschrift. Erfinde keine Fakten.

BESCHWERDE: [Text einfügen]"""

BAUKASTEN = [
    ["Rolle", "Wer soll die KI sein? (Beruf, Perspektive)"],
    ["Ziel", "Was soll am Ende erreicht sein? (nicht nur: „Schreib etwas“)"],
    ["Zielgruppe", "Für wen ist der Text? Was wissen/fühlen sie?"],
    ["Ton", "Wie soll es klingen? (freundlich, sachlich, knapp …)"],
    ["Beispiel", "Ein kurzes Muster, wie es bei uns klingen soll"],
    ["Format", "Länge, Gliederung, Sprache, Ausgabeform"],
    ["Grenzen", "Was soll sie nicht tun? (nichts erfinden, keine Zusagen)"],
]


def ergebnis_felder(D, a="Ergebnis A", b="Ergebnis B", h=4.2):
    D.notes_box(a + " (hier einfügen oder Stichpunkte)", h)
    D.notes_box(b + " (hier einfügen oder Stichpunkte)", h)


def build(outdir):
    D = Doc("Aha-Übungen", "Arbeitsblatt: KI selbst erleben statt erklärt bekommen", "Aha-Übungen-Arbeitsblatt")
    D.disclaimer_box()
    D.callout(
        "Vorab: Spielregeln für alle Übungen",
        [
            "Sie brauchen **ein beliebiges KI-Tool, das Ihr Betrieb freigegeben hat** (oder – falls es noch keines gibt – nur die frei erfundenen Beispieltexte in diesem Blatt verwenden).",
            "**Keine vertraulichen oder personenbezogenen Daten.** Alle Übungen kommen mit erfundenen oder öffentlichen Beispielen aus. Nutzen Sie bitte keine echten Kunden- oder Mitarbeiterdaten.",
            "**Neue Unterhaltung pro Durchgang:** Starten Sie für jeden Prompt einen neuen Chat, damit frühere Eingaben das Ergebnis nicht beeinflussen.",
            "Ergebnisse unterscheiden sich von Tool zu Tool und von Mal zu Mal. Das ist kein Fehler, sondern Teil der Erfahrung.",
            "Das Ergebnis ist immer ein Entwurf (5-Punkte-Prüfung).",
        ],
    )
    D.h3("Für die Schulungsleitung")
    D.bullets(
        [
            "Übung 1 ist **Pflicht** (ca. 20 Min.). Die Übungen 2 bis 4 sind optional (je ca. 15 Min.); wählen Sie nach Zeit und Gruppe.",
            "Prinzip: **erst erleben, dann erklären.** Lassen Sie die Gruppe zuerst ausprobieren und den Unterschied selbst benennen; erst danach erläutern Sie das Baukasten-Schema.",
            "Gruppen zu 2–3 Personen funktionieren gut: Ein Bildschirm, gemeinsames Vergleichen.",
        ]
    )

    # ---------------- Übung 1
    D.page_break()
    D.h1("Übung 1 (Pflicht): Gleicher Auftrag – einmal ohne, einmal mit Kontext")
    D.p("**Dauer:** ca. 20 Minuten · **Ziel:** Sie erleben selbst, wie stark Kontext die Antwort verändert.", after=4)
    D.p("**Ausgangslage – die Beschwerde** (erfunden):")
    D.callout("Kundenbeschwerde", [BESCHWERDE], fill=SOFT_FILL)
    D.h3("Schritt 1: Der „nackte“ Prompt")
    D.numbered(
        [
            "Öffnen Sie eine **neue Unterhaltung** in Ihrem KI-Tool.",
            "Geben Sie ein: **„Schreib eine Antwort auf diese Kundenbeschwerde: [Beschwerde von oben einfügen]“** – sonst nichts.",
            "Kopieren Sie das Ergebnis in das Feld unten.",
        ]
    )
    D.notes_box("Ergebnis A – ohne Kontext", 4.5)
    D.h3("Schritt 2: Derselbe Auftrag mit Kontext")
    D.p("Öffnen Sie wieder eine **neue Unterhaltung** und geben Sie diesen Prompt ein (Platzhalter in [Klammern] ersetzen oder erfinden):")
    D.callout("Prompt mit Kontext-Baukasten", CONTEXT_PROMPT.split("\n"), fill=NOTE_FILL)
    D.notes_box("Ergebnis B – mit Kontext", 4.5)
    D.h3("Schritt 3: Nebeneinander vergleichen")
    D.table(
        ["Kriterium", "Ergebnis A (ohne)", "Ergebnis B (mit)", "Wer ist besser?"],
        [[k, "", "", ""] for k in (
            "Ton: Klingt es nach uns?",
            "Konkretheit: nächster Schritt klar?",
            "Länge: passend oder aufgebläht?",
            "Zusagen: Hat die KI etwas versprochen, das wir nicht wollen?",
            "Aufwand: Wie viel müsste ich noch ändern?",
        )],
        widths=[6.0, 3.6, 3.6, 3.2],
        size=9.5,
    )
    D.h3("Vergleichsfragen")
    D.numbered(
        [
            "Was ist der **größte Unterschied** zwischen A und B? Benennen Sie drei Punkte.",
            "Welches Element aus dem Baukasten hat Ihrer Meinung nach am meisten bewirkt: Rolle, Ziel, Zielgruppe, Ton, Beispiel, Format oder Grenzen?",
            "Hat Ergebnis B etwas Erfundenes oder Falsches enthalten, das Sie prüfen müssten?",
        ]
    )
    D.notes_box("Meine Antworten", 3.2)
    D.callout(
        "Der Kontext-Baukasten (zum Merken)",
        ["Je mehr davon Sie liefern, desto besser trifft die KI. Aber: **Kontext ist nicht dasselbe wie vertrauliche Daten.** Beschreiben Sie die Situation, nicht die Person."],
        fill=SOFT_FILL,
    )
    D.table(["Baustein", "Frage dazu"], BAUKASTEN, widths=[3.2, 13.2])
    D.callout("Reflexionsfrage", ["Wo in meinem Arbeitsalltag schreibe ich heute „nackte“ Aufträge – und wie könnte ich daraus einen Auftrag mit Kontext machen?"], fill=GREEN_FILL)
    D.notes_box("Meine Reflexion", 3.0)

    # ---------------- Übung 2
    D.page_break()
    D.h1("Übung 2: Eine Halluzination selbst provozieren – und entlarven")
    D.p("**Dauer:** ca. 15 Minuten · **Ziel:** Sie erleben, wie überzeugend falsche Antworten klingen können, und lernen, sie zu prüfen.", after=4)
    D.numbered(
        [
            "Neue Unterhaltung. Denken Sie sich ein **sehr spezielles Thema** aus, zu dem es vermutlich kaum Literatur gibt, z. B. „Büroorganisation in Imkereibetrieben mit unter 10 Beschäftigten“.",
            "Prompt: **„Nenne mir drei Fachbücher zum Thema [Ihr Thema] mit Autor, Erscheinungsjahr und Verlag.“**",
            "Prüfen Sie jedes genannte Buch selbst: Suchen Sie Titel und Autor in einem Buchkatalog oder einer Suchmaschine. Notieren Sie unten, ob es das Buch **wirklich gibt**.",
            "Fragen Sie nach: **„Bist du sicher, dass diese Bücher existieren?“** Wie reagiert die KI?",
            "Neue Unterhaltung, derselbe Auftrag mit Grenzen: **„… Nenne nur Bücher, die du sicher kennst. Wenn du keine kennst, sage das ausdrücklich und erfinde nichts.“**",
        ]
    )
    D.table(
        ["Genannte Quelle", "Gefunden? (ja/nein/teils)", "Wie geprüft?"],
        [["1.", "", ""], ["2.", "", ""], ["3.", "", ""]],
        widths=[7.4, 4.5, 4.5],
    )
    D.notes_box("Was hat die KI auf „Bist du sicher?“ geantwortet? Was hat sich mit der Grenze geändert?", 3.8)
    D.p("Hinweis: Hat Ihr Tool eine Websuche, kann das Ergebnis anders ausfallen. Prüfen Sie dann trotzdem, ob die Fundstelle wirklich zur Aussage passt. Funktionen unterscheiden sich je nach Tool und Tarif.", italic=True)
    D.callout("Reflexionsfrage", ["Woran hätte ich ohne eigene Prüfung erkannt, dass etwas erfunden war – und welche Regel ziehe ich daraus für meinen Alltag?"], fill=GREEN_FILL)
    D.notes_box("Meine Reflexion", 3.0)

    # ---------------- Übung 3
    D.page_break()
    D.h1("Übung 3: Einen schlechten Prompt Schritt für Schritt verbessern")
    D.p("**Dauer:** ca. 15 Minuten · **Ziel:** Sie sehen, welcher Baustein welche Wirkung hat.", after=4)
    D.p("Startauftrag (absichtlich schlecht): **„Mach was zu Weihnachten für Kunden.“** Führen Sie vier Runden durch, jeweils in einer **neuen Unterhaltung**, und bewerten Sie jedes Ergebnis von 1 (unbrauchbar) bis 5 (fast fertig).")
    D.table(
        ["Runde", "Prompt", "Note (1–5)", "Was hat sich verändert?"],
        [
            ["1", "„Mach was zu Weihnachten für Kunden.“", "", ""],
            ["2", "Runde 1 + **Rolle und Ziel:** „Du bist Marketingassistenz eines Fahrradladens. Ziel: Kundinnen und Kunden zu einem Wintercheck einladen.“", "", ""],
            ["3", "Runde 2 + **Zielgruppe und Ton:** „Zielgruppe: Pendler, 30–55 Jahre. Ton: warm, kurz, nicht aufdringlich.“", "", ""],
            ["4", "Runde 3 + **Format, Beispiel und Grenzen:** „Format: Newsletter-Text, max. 100 Wörter, Betreff dazu. Beispielton: [ein Satz, so klingt unser Haus]. Erfinde keine Rabatte.“", "", ""],
        ],
        widths=[1.4, 8.8, 2.0, 4.2],
        size=9.5,
    )
    D.p("(Ersetzen Sie „Fahrradladen“ durch eine erfundene Branche Ihrer Wahl, wenn Sie möchten.)", italic=True)
    D.notes_box("Welche Runde brachte den größten Sprung? Warum?", 3.5)
    D.callout("Reflexionsfrage", ["Welchen Baustein vergesse ich selbst am häufigsten – und was ändert sich, wenn ich ihn künftig immer ergänze?"], fill=GREEN_FILL)
    D.notes_box("Meine Reflexion", 3.0)

    # ---------------- Übung 4
    D.h1("Übung 4: Dieselbe Aufgabe mit Beispiel und ohne Beispiel")
    D.p("**Dauer:** ca. 15 Minuten · **Ziel:** Sie erleben, wie ein kurzes Muster den Stil der Antwort steuert.", after=4)
    D.numbered(
        [
            "Neue Unterhaltung. Prompt A: **„Schreibe fünf Betreffzeilen für einen Newsletter über [Thema, z. B. Herbstangebote im Gartencenter].“**",
            "Neue Unterhaltung. Prompt B: derselbe Auftrag plus **zwei Beispiel-Betreffzeilen im gewünschten Stil** (z. B. kurz, mit Frage) und den Zusatz: „Orientiere dich am Stil der Beispiele, kopiere sie nicht.“",
            "Vergleichen Sie: Welche Liste klingt eher nach **Ihrem** Haus?",
        ]
    )
    ergebnis_felder(D, "Prompt A – ohne Beispiel", "Prompt B – mit Beispiel", 3.4)
    D.callout("Reflexionsfrage", ["Welche gelungenen Texte aus meinem Betrieb könnte ich als Beispiele sammeln, damit die KI künftig unseren Stil trifft? (Nur Texte ohne vertrauliche Inhalte.)"], fill=GREEN_FILL)
    D.notes_box("Meine Reflexion", 3.0)

    D.h2("Mein Fazit nach den Übungen")
    D.notes_box("Das nehme ich mit (3 Punkte) · Das probiere ich diese Woche aus", 3.6)
    D.save(f"{outdir}/{FILE}")
    return FILE
