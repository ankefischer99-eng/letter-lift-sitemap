from kit_lib import *

FILE = "Wissenstest-und-Nachweis.docx"

# (Frage, [A,B,C,D], Index richtig 0-3, Begründung)
QUESTIONS = [
    ("Was beschreibt eine „Halluzination“ bei KI-Tools am besten?",
     ["Das Tool stürzt ab und liefert keine Antwort.", "Das Tool gibt überzeugend klingende, aber falsche oder erfundene Inhalte aus.", "Das Tool speichert Ihre Eingaben dauerhaft.", "Das Tool verweigert eine Antwort aus Datenschutzgründen."],
     1, "Halluzinationen sind erfundene oder falsche Inhalte (Fakten, Zahlen, Quellen), die sprachlich überzeugend wirken. Deshalb ist jede Ausgabe zu prüfen."),
    ("Sie möchten eine Kundenbeschwerde mit Name und Bestellnummer von einem öffentlichen KI-Tool umformulieren lassen. Was ist richtig?",
     ["Erlaubt, wenn das Ergebnis danach geprüft wird.", "Erlaubt, wenn Sie nur den Nachnamen löschen.", "Nicht erlaubt in dieser Form: Personenbezogene Daten gehören nicht in ein dafür nicht freigegebenes Tool. Anonymisieren Sie vorher.", "Erlaubt, solange Sie das Tool privat bezahlen."],
     2, "Name und Bestellnummer sind personenbezogene Daten (rote Stufe). Prüfen des Ergebnisses ändert nichts an der Weitergabe der Daten. Private Bezahlung ebenfalls nicht."),
    ("Welche Aussage zur Datenampel stimmt?",
     ["Grün: öffentlich/unkritisch, Gelb: intern ohne Personenbezug, Rot: personenbezogen oder vertraulich.", "Grün heißt, die Daten dürfen in jedes beliebige Tool.", "Rot heißt, KI darf nie genutzt werden – auch nicht mit anonymisierten Daten.", "Die Einstufung ist Geschmackssache jeder Person."],
     0, "Grün gilt nur für freigegebene Tools; rot bedeutet: nur anonymisiert oder im dafür freigegebenen Tool (Stufe 3). Im Zweifel nachfragen."),
    ("Wer ist dafür verantwortlich, dass ein KI-Text vor dem Versand an einen Kunden stimmt?",
     ["Das KI-Tool bzw. der Anbieter.", "Die IT-Abteilung.", "Die Person, die den Text verwendet.", "Niemand, solange die KI als Quelle genannt wird."],
     2, "Die Verantwortung bleibt beim Menschen, der das Ergebnis verwendet – nicht beim Tool."),
    ("Welche Eingabe ist in ein KI-Tool grundsätzlich verboten?",
     ["Eine Bitte um ein Brainstorming zu Themen für den Newsletter.", "Eine Bitte, einen öffentlichen Webseitentext zu kürzen.", "Ihr Passwort oder Zugangsdaten, damit das Tool etwas für Sie erledigen kann.", "Eine allgemeine Frage zu einer Excel-Formel ohne echte Daten."],
     2, "Passwörter und Zugangsdaten gehören nie in ein KI-Tool."),
    ("Ein Kollege nutzt privat ein KI-Tool, das nicht in der Freigabeliste steht, für Kundentexte. Was tun Sie?",
     ["Nichts – es ist seine Sache.", "Sie melden es an [NAME/Funktion], damit geprüft werden kann, ob und wie das Tool freigegeben werden kann.", "Sie machen mit, weil es praktisch ist.", "Sie rufen den Anbieter an."],
     1, "Nicht freigegebene Tools für dienstliche Inhalte sind nicht erlaubt. Melden hilft, Risiken zu begrenzen und gute Tools freizugeben."),
    ("Was gehört zur 5-Punkte-Prüfung?",
     ["Fakten, Zahlen/Quellen, Namen/Anrede, Ton/Zusagen, Vertraulichkeit/Rechte.", "Rechtschreibung, Schriftart, Länge, Farbe, Bilder.", "Preis, Anbieter, Tool, Version, Sprache.", "Tempo, Kosten, Menge, Qualität, Stil."],
     0, "Diese fünf Punkte sind das feste Prüfverfahren vor jeder Verwendung einer KI-Ausgabe."),
    ("Eine KI nennt Ihnen für eine Aussage ein Gerichtsurteil mit Aktenzeichen. Was tun Sie?",
     ["Sie übernehmen es, weil ein Aktenzeichen genannt wird.", "Sie prüfen, ob das Urteil existiert und passt – bei Rechtsfragen holen Sie fachlichen Rat ein.", "Sie fragen die KI, ob sie sich sicher ist, und glauben die Antwort.", "Sie ändern das Aktenzeichen etwas ab."],
     1, "Quellen und Rechtsaussagen können erfunden sein. Eine Rückfrage an dieselbe KI ersetzt keine Prüfung."),
    ("Wofür dürfen Sie KI NICHT allein einsetzen?",
     ["Für einen ersten Gliederungsentwurf.", "Für die Entscheidung über eine Einstellung oder Kündigung.", "Für eine Zusammenfassung eines öffentlichen Artikels.", "Für Übersetzungsvorschläge, die Sie prüfen."],
     1, "Entscheidungen über Menschen treffen Menschen. Der Einsatz von KI dafür ist vorab zu prüfen und nicht allein zulässig."),
    ("Wann sollten Sie ein KI-Ergebnis besonders streng (fachlich) prüfen lassen?",
     ["Bei einer internen Ideensammlung.", "Bei Verträgen, Preisen, verbindlichen Zusagen oder Rechts-, Steuer- und Gesundheitsaussagen.", "Bei einem Gruß-Text zum Feiertag.", "Nie, wenn das Tool teuer war."],
     1, "Hohes Risiko = fachliche Prüfung durch eine dafür qualifizierte Person."),
    ("Was sollten Sie tun, wenn Sie aus Versehen Kundendaten in ein nicht freigegebenes Tool eingegeben haben?",
     ["Den Verlauf löschen und schweigen.", "Warten, ob etwas passiert.", "Sofort an [NAME/KONTAKT] melden, damit der Vorfall bewertet werden kann.", "Das Tool wechseln und dort neu eingeben."],
     2, "Schnelle Meldung begrenzt den Schaden; gesetzliche Meldefristen können kurz sein. Verschweigen verschlimmert die Lage."),
    ("Wer muss erkennen können, dass er mit einer KI interagiert?",
     ["Niemand, das ist unsere interne Entscheidung.", "Personen, die mit einem KI-System (z. B. Chatbot) sprechen oder schreiben – wir sind hier transparent.", "Nur Behörden.", "Nur Personen unter 18."],
     1, "Transparenz ist ein Grundsatz unserer Richtlinie; es gibt zudem gesetzliche Vorgaben, die je nach Anwendungsfall greifen können. Im Zweifel nachfragen."),
]


TARGETS = [3, 0, 2, 1, 3, 0, 1, 2, 3, 0, 1, 2]  # Position der richtigen Antwort, gleichmäßig verteilt


def _rebalance():
    out = []
    for (q, opts, c, why), t in zip(QUESTIONS, TARGETS):
        right = opts[c]
        rest = [o for i, o in enumerate(opts) if i != c]
        rest.insert(t, right)
        out.append((q, rest, t, why))
    return out


def build(outdir):
    questions = _rebalance()
    D = Doc("Wissenstest und Schulungsnachweis", "zur KI-Schulung bei [FIRMENNAME]", "Wissenstest und Nachweis")
    D.disclaimer_box()
    D.h1("Teil 1: Wissenstest")
    D.table(
        ["Name", "Abteilung", "Datum"],
        [["", "", ""]],
        widths=[6.4, 5.0, 5.0],
    )
    D.p("12 Fragen, je **eine** richtige Antwort. Bearbeitungszeit etwa 10 Minuten. Bestanden bei mindestens **[9]** richtigen Antworten. Kreuzen Sie pro Frage einen Buchstaben an.")
    for i, (q, opts, correct, why) in enumerate(questions, 1):
        D.p(f"**Frage {i}.** {q}", after=3)
        for letter, o in zip("ABCD", opts):
            para = D.p(f"☐  **{letter}**  {o}", after=1)
            para.paragraph_format.left_indent = Cm(0.8)
        D.p("", after=2)
    D.p("Auswertung (von der Schulungsleitung auszufüllen): Richtige Antworten: ____ von 12 · Bestanden: ☐ ja ☐ nein · Datum/Kürzel: ______")

    D.page_break()
    D.h1("Teil 2: Lösungsblatt (nicht an Teilnehmende verteilen)")
    rows = [[str(i), "ABCD"[c], why] for i, (q, o, c, why) in enumerate(questions, 1)]
    D.table(["Frage", "Richtig", "Begründung"], rows, widths=[1.6, 1.8, 13.0])
    D.p("Hinweis: Passen Sie Fragen, die auf [NAME/KONTAKT] oder auf Regeln Ihrer Richtlinie verweisen, an Ihre Fassung an.", italic=True)

    D.page_break()
    D.h1("Teil 3: Teilnahmeliste")
    D.table(
        ["Schulung", ""],
        [
            ["Thema", "KI sicher nutzen im Arbeitsalltag (Einführung)"],
            ["Datum / Dauer", "[TT.MM.JJJJ] / [90 Minuten]"],
            ["Ort / Format", "[Ort bzw. Online-Plattform]"],
            ["Schulungsleitung", "[NAME, Funktion]"],
            ["Inhalte", "Grundlagen und Grenzen von KI; Datenampel; Datenschutz; Tool-Freigabe; Prompts; 5-Punkte-Prüfung; Kennzeichnung; Meldung von Vorfällen; zwei Praxisübungen; Wissenstest"],
        ],
        widths=[4.0, 12.4],
    )
    D.table(
        ["Nr.", "Name", "Abteilung", "Test bestanden (ja/nein)", "Unterschrift"],
        [[str(i), "", "", "", ""] for i in range(1, 13)],
        widths=[1.1, 4.8, 3.4, 3.0, 4.1],
    )

    D.h1("Teil 4: Nachweis über die Schulung (Einzelblatt)")
    D.p("Dokumentiert, dass die genannte Person an der Schulung teilgenommen hat. Dieses Blatt ist eine betriebsinterne Bestätigung und **keine amtliche Bescheinigung oder Prüfung durch Dritte**.", italic=True)
    D.table(
        ["Angabe", "Eintrag"],
        [
            ["Name der Teilnehmerin / des Teilnehmers", ""],
            ["Funktion / Abteilung", ""],
            ["Schulung (Thema, Datum, Dauer)", "KI sicher nutzen im Arbeitsalltag · [TT.MM.JJJJ] · [90 Minuten]"],
            ["Wissenstest", "Ergebnis: ____ von 12 · Bestehensgrenze [9] · ☐ bestanden ☐ nicht bestanden (Wiederholung am: ______)"],
            ["Auffrischung fällig bis", "[TT.MM.JJJJ]"],
            ["Schulungsleitung (Name, Unterschrift, Datum)", ""],
            ["Teilnehmende/r (Unterschrift, Datum)", ""],
        ],
        widths=[6.4, 10.0],
    )
    D.callout(
        "Aufbewahrung und Datenschutz",
        [
            "Teilnahmelisten und Nachweise enthalten personenbezogene Daten. Bewahren Sie sie getrennt von allgemeinen Unterlagen auf, legen Sie eine Aufbewahrungsfrist fest ([FRIST]) und beschränken Sie den Zugriff auf [NAME/Funktion].",
            "Welche Fristen für Ihr Unternehmen sinnvoll oder erforderlich sind, klären Sie bei Bedarf mit Ihrer Datenschutz- oder Rechtsberatung.",
        ],
    )
    D.save(f"{outdir}/{FILE}")
    return FILE
