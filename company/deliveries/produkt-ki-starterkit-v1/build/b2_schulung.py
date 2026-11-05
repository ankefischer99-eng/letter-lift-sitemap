from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.util import Inches, Pt
from kit_lib import DISCLAIMER, KIT_NAME, VERSION

FILE = "KI-Schulung.pptx"
DARK = RGBColor(0x1F, 0x3A, 0x5F)
GREY = RGBColor(0x55, 0x55, 0x55)

# (Titel, [Stichpunkte], Sprechernotiz)
SLIDES = [
    ("KI sicher nutzen im Arbeitsalltag",
     ["Schulung für alle Beschäftigten von [FIRMENNAME]", "Referent/in: [NAME] · Datum: [TT.MM.JJJJ]", "Dauer: ca. 75 Minuten inkl. 2 Übungen"],
     "Begrüßen Sie die Gruppe. Sagen Sie klar: Ziel ist nicht, Angst zu machen, sondern Sicherheit zu geben. Wer nach der Schulung weiß, was er eingeben darf und wie er Ergebnisse prüft, kann KI gut nutzen. "
     "Hinweis vorab: Diese Schulung und die Vorlage ersetzen keine Rechtsberatung. Planen Sie 75 Minuten ein; wenn es knapp wird, kürzen Sie die Folien 3 bis 6 und halten Sie Übungen und Datenampel ein."),
    ("Was Sie heute mitnehmen",
     ["Sie verstehen, was KI im Alltag kann – und was nicht", "Sie wissen, welche Daten NIE in ein KI-Tool gehören", "Sie prüfen KI-Ergebnisse mit einem festen Verfahren", "Sie kennen unsere Regeln und wissen, an wen Sie sich wenden"],
     "Gehen Sie die vier Ziele kurz durch. Fragen Sie vorab in die Runde: Wer nutzt schon KI, privat oder im Job? Handzeichen genügt. Das zeigt Ihnen das Niveau. Es ist normal, dass einige schon viel nutzen und andere noch nie. "
     "Betonen Sie: Es gibt keine dummen Fragen. Notieren Sie offene Fragen auf einem Flipchart oder in der Chatleiste ('Themenspeicher')."),
    ("Was ist „KI“ bei der Arbeit?",
     ["Meist gemeint: Generative KI – Programme, die Texte, Bilder oder Code erzeugen", "Beispiele: Chat-Assistenten, Übersetzer, Bildgeneratoren, Protokoll-Tools", "Oft versteckt in Software, die wir schon nutzen (Office, E-Mail, Meetings)", "Sie arbeitet mit Wahrscheinlichkeiten – sie „weiß“ nichts im menschlichen Sinn"],
     "Erklären Sie ohne Fachchinesisch. Beispiel: Ein Chat-Assistent ist wie ein sehr schneller Praktikant, der enorm viel gelesen hat, aber nicht weiß, was bei uns gilt, und der nie zugibt, wenn er etwas nicht weiß. "
     "Weisen Sie darauf hin, dass KI-Funktionen oft in bestehende Programme eingebaut sind. Deshalb gilt die Richtlinie auch dafür. Fragen Sie: Wo ist Ihnen KI schon begegnet?"),
    ("Wie ein Sprachmodell „denkt“ – stark vereinfacht",
     ["Es hat aus sehr vielen Texten gelernt, welche Wörter wahrscheinlich aufeinander folgen", "Es berechnet die plausibelste Fortsetzung – nicht die geprüfte Wahrheit", "Es kennt weder unsere Firma noch heutige Ereignisse automatisch", "Deshalb klingen auch falsche Antworten überzeugend"],
     "Das ist die wichtigste Grundlage für alles Weitere. Bildhaft: Die Autovervollständigung beim Handy – nur viel größer. Das Modell 'rät' sehr gut, aber es rät. "
     "Wichtig: Je mehr Kontext Sie liefern (Rolle, Ziel, Format), desto besser das Ergebnis. Aber Kontext heißt nicht: vertrauliche Daten. Das kommt gleich. Falls jemand nach technischen Details fragt: kurz antworten und auf den Themenspeicher verweisen."),
    ("Wo KI gut ist – und wo nicht",
     ["Gut: Entwürfe, Umformulieren, Zusammenfassen, Ideen, Struktur, Übersetzen, Formeln erklären", "Schwach: Fakten, Zahlen, Quellen, aktuelle Ereignisse, Rechtsfragen, Rechnen", "Nie allein: Entscheidungen über Menschen, verbindliche Zusagen", "Faustregel: KI liefert den ersten Entwurf – Sie liefern das Urteil"],
     "Machen Sie die Gegenüberstellung konkret mit Beispielen aus dem Alltag Ihres Betriebs: [BEISPIELE AUS IHREM BETRIEB EINSETZEN]. Sagen Sie klar: Rechnen und Faktenprüfen sind Schwächen, auch wenn die Antworten selbstsicher klingen. "
     "Wer das verinnerlicht, ist schon die halbe Strecke zu sicherer Nutzung."),
    ("Halluzinationen: überzeugend und trotzdem falsch",
     ["KI erfindet manchmal Fakten, Zahlen, Zitate und Quellen", "Typisches Muster: Sie fragen nach einer Quelle – die KI nennt einen plausibel klingenden Titel, den es nicht gibt", "Erkennbar? Oft nicht – deshalb prüfen Sie immer selbst", "Ein Tool, das sicher klingt, ist nicht deshalb richtig"],
     "Beschreiben Sie das Muster, das bekannt ist: Auf die Bitte um Quellen erzeugen Sprachmodelle manchmal Titel und Verweise, die echt aussehen, aber frei erfunden sind. Das ist ein bekanntes Phänomen, kein Einzelfall eines bestimmten Tools. "
     "Nennen Sie hier keine konkreten Fälle, die Sie nicht selbst belegen können. Zeigen Sie stattdessen live ein eigenes Beispiel: Fragen Sie ein freigegebenes Tool nach etwas sehr Speziellem aus Ihrer Branche und prüfen Sie die Antwort gemeinsam. Das wirkt stärker als jede Folie."),
    ("Unsere Richtlinie auf einen Blick",
     ["Nur freigegebene Tools (Liste in Anhang A)", "Datenampel beachten: grün – gelb – rot", "Jede Ausgabe prüfen, bevor sie verwendet wird", "KI-Hilfe bei wichtigen Dokumenten kennzeichnen", "Fehler und Vorfälle sofort melden"],
     "Die Richtlinie liegt allen vor (Link/Aushang: [ORT]). Gehen Sie die fünf Punkte durch und zeigen Sie Anhang A mit den freigegebenen Tools. Erwähnen Sie die Ansprechperson: [NAME/KONTAKT]. "
     "Passen Sie diese Folie an, falls Ihre Richtlinie abweicht. Weisen Sie darauf hin, dass die Richtlinie Orientierung geben soll, nicht Misstrauen ausdrücken."),
    ("Erlaubt und verboten",
     ["Erlaubt: Entwürfe, Ideen, Zusammenfassen nicht vertraulicher Texte, Formeln, Übersetzungen", "Verboten: rote Daten in ungeprüfte Tools, private Konten für Dienstliches, Passwörter, ungeprüftes Versenden", "Verboten: Entscheidungen über Menschen allein durch KI, Täuschung, fremde geschützte Inhalte ohne Berechtigung", "Unsicher? Erst fragen, dann eingeben"],
     "Lesen Sie die Verbote nicht vor, sondern erklären Sie die Logik: Alles, was Menschen schadet oder Vertrauen zerstört, ist verboten. Alles, was Arbeit erleichtert und geprüft wird, ist erwünscht. "
     "Fragen Sie nach Fällen aus der Praxis: 'Darf ich eine Kundenmail zum Umformulieren in das Tool kopieren?' Das führt zur nächsten Folie."),
    ("Die Datenampel",
     ["GRÜN: öffentlich/unkritisch → jedes freigegebene Tool", "GELB: intern, ohne Personenbezug → nur Tools ab Stufe 2", "ROT: personenbezogen oder vertraulich → nur Stufe 3 oder anonymisiert", "Im Zweifel: eine Stufe höher einordnen und nachfragen"],
     "Das ist das Herzstück der Schulung. Nehmen Sie sich Zeit. Beispiele: Grün: öffentlicher Webseitentext. Gelb: interner Ablaufentwurf ohne Namen. Rot: Kundenbeschwerde mit Name, Vertrag, Bewerbung, Gehaltsliste. "
     "Betonen Sie: Rot heißt nicht 'nie wieder KI', sondern 'nur anonymisiert oder im dafür freigegebenen Tool'. Zeigen Sie, wie Anonymisieren aussieht: [Kunde A] statt Namen."),
    ("Personenbezogene Daten: das ist mehr, als man denkt",
     ["Name + Kontext, E-Mail, Telefon, Kundennummer, Foto, Stimme", "Beschwerden, Bewerbungen, Krankmeldungen, Gehälter", "Auch Kombinationen: Beruf + Ort + besonderer Umstand", "Was einmal in ein fremdes Tool eingegeben wurde, lässt sich oft nicht zurückholen"],
     "Erklären Sie die Grundidee des Datenschutzes: Wer personenbezogene Daten verarbeitet, braucht eine Grundlage und muss sorgsam damit umgehen. Ob ein KI-Einsatz zulässig ist, klärt [Datenschutzbeauftragte/r] – nicht jede Person im Alleingang. "
     "Geben Sie keine rechtlichen Einzelauskünfte; verweisen Sie auf die Ansprechperson. Wer Fragen zu Rechtsgrundlagen hat, bekommt sie im Anschluss beantwortet."),
    ("Vertrauliche Firmendaten",
     ["Verträge, Preiskalkulationen, Strategien, Quellcode, Zugangsdaten", "Informationen von Kundinnen und Kunden, die uns anvertraut wurden", "Regel: Was Sie nicht auf eine öffentliche Pinnwand hängen würden, geben Sie nicht in ein ungeprüftes Tool ein", "Kein Foto, kein Screenshot, keine ganze Datei ohne vorherige Prüfung"],
     "Der Pinnwand-Vergleich funktioniert gut. Weisen Sie auf versteckte Informationen in Dateien hin (Metadaten, Kommentare, Änderungsverfolgung). Bei Screenshots: Auf dem Bild stehen oft Namen im Hintergrund. "
     "Falls Ihr Betrieb Verschwiegenheitspflichten gegenüber Kunden hat, nennen Sie sie hier: [BEISPIELE]."),
    ("So wird ein Tool freigegeben",
     ["1. Antrag an [NAME/Funktion]: Tool, Zweck, Daten", "2. Prüfung mit Checkliste und Bewertungsmatrix", "3. Entscheidung: freigegeben (Stufe 1/2/3), abgelehnt, erst klären", "4. Eintrag in die Freigabeliste (Anhang A)", "5. Regelmäßige Neuprüfung"],
     "Zeigen Sie kurz die Excel-Datei zur Tool-Freigabe. Wichtig: Es gibt einen Weg zu 'Ja'. Die Freigabe soll schnell gehen und nicht blockieren: Ziel [5] Arbeitstage. Fragen Sie, welche Tools sich die Gruppe wünscht, und notieren Sie die Namen für die Freigabeliste."),
    ("Praxisübung 1: Datenampel (10 Min.)",
     ["Gruppen zu 2–3 Personen. Ordnen Sie jeden Fall ein: GRÜN, GELB oder ROT?", "A: Bitte „Newsletter-Text kürzer und lockerer formulieren“ (eigener, schon veröffentlichter Text)", "B: Kundenbeschwerde mit Name und Bestellnummer zum Umformulieren einfügen", "C: Interner Ablauf „Urlaubsantrag“ ohne Namen als Checkliste aufbereiten lassen", "D: Bewerbungs-PDF hochladen und zusammenfassen lassen", "E: Preiskalkulation für das Angebot an [Kunde] prüfen lassen"],
     "Geben Sie 5 bis 7 Minuten, dann Auflösung auf der nächsten Folie. Lassen Sie jede Gruppe eine Einordnung begründen. Wichtig ist die Begründung, nicht die Treffsicherheit. "
     "Sinnvoll: Passen Sie die Fälle an Ihren Betrieb an. Wenn es Streit gibt, ist das gut – dann gibt es Klärungsbedarf, den Sie in der Richtlinie nachschärfen können."),
    ("Auflösung Übung 1",
     ["A: GRÜN – bereits veröffentlicht, kein Personenbezug", "B: ROT – Name und Bestellnummer; nur anonymisiert („Kunde A“, ohne Nummer)", "C: GELB – intern, ohne Personenbezug; nur in Tool ab Stufe 2", "D: ROT – Bewerbungsdaten; nicht in ein öffentliches Tool, Auswahl nie allein durch KI", "E: ROT – vertrauliche Kalkulation; nur Stufe 3 oder gar nicht"],
     "Besprechen Sie die Antworten. Bei B: Zeigen Sie, wie die anonymisierte Version aussieht. Bei D: Zusätzlich zum Datenschutz geht es um Entscheidungen über Menschen: Die KI darf höchstens Hilfsmittel sein, die Entscheidung trifft ein Mensch, und der Einsatz wird vorab geprüft. "
     "Bei E: Auch hier hilft ein anonymisiertes Beispiel mit erfundenen Zahlen. Erwähnen Sie, dass die Einordnung in Grenzfällen immer die vorsichtigere Stufe sein sollte."),
    ("Gut fragen: Prompts, die funktionieren",
     ["Rolle: „Du bist …“", "Aufgabe: Was genau soll entstehen?", "Kontext: Zielgruppe, Zweck, Ton (ohne vertrauliche Daten)", "Format: Länge, Gliederung, Sprache", "Grenzen: „Erfinde nichts. Kennzeichne Unsicheres.“"],
     "Zeigen Sie vorher/nachher: 'Schreib eine Mail' versus 'Du bist Kundenberaterin. Formuliere eine freundliche, kurze Antwort auf eine Lieferverzögerung. 120 Wörter. Erfinde keine Zusagen.' "
     "Verweisen Sie auf die Prompt-Bibliothek mit 30 Vorlagen. Erinnern Sie: Auch beim besten Prompt bleibt die Prüfpflicht."),
    ("Die 5-Punkte-Prüfung",
     ["1. Fakten: stimmt es?", "2. Zahlen und Quellen: nachrechnen, Quelle existiert?", "3. Namen und Anrede: richtig?", "4. Ton und Zusagen: passt es, verspricht es zu viel?", "5. Vertraulichkeit und Rechte: darf das raus?"],
     "Das ist das Prüfverfahren, das sich jede Person merken soll. Tipp: Prüfen Sie nicht nur, ob es plausibel klingt, sondern ob Sie es belegen könnten. "
     "Für hohe Risiken (Verträge, Preise, Rechtsaussagen) gilt: fachliche Prüfung durch [Funktion]. Verantwortlich ist immer die Person, die das Ergebnis verwendet."),
    ("Praxisübung 2: Fehler finden (10 Min.)",
     ["Aufgabe: Der folgende Text wurde von einer KI entworfen. Finden Sie mindestens 5 Probleme.", "„Sehr geehrter Herr Meyer, vielen Dank für Ihre Anfrage zur Bestellung 4711 von Frau Annika Berger. Unser Paket kostet laut Preisliste 2019 genau 480 €. Wir garantieren die Lieferung in 2 Werktagen. Nach dem Urteil Az. [erfunden] sind Sie zur Zahlung verpflichtet. Beste Grüße, Ihr KI-Team“", "(Übungstext, frei erfunden)"],
     "Lesen Sie den Text vor oder blenden Sie ihn groß ein. Geben Sie 5 bis 7 Minuten. Lassen Sie die Gruppen nach der 5-Punkte-Prüfung vorgehen. Der Text enthält absichtlich mehrere Fehlertypen. Die Auflösung folgt auf der nächsten Folie. "
     "Hinweis: Alles in diesem Text ist erfunden. Es gibt kein echtes Urteil und keine echte Kundschaft."),
    ("Auflösung Übung 2",
     ["Personenbezug: Name der Bestellerin und Bestellnummer gehören nicht in den Entwurf bzw. nicht in ein fremdes Tool", "Anrede passt nicht zur Person (Herr Meyer vs. Frau Berger)", "Veraltete Preisangabe (Preisliste 2019) – prüfen", "Absolute Zusage („garantieren“) – nur, wenn wir das wollen und können", "Erfundenes oder ungeprüftes Urteil/Aktenzeichen – Rechtsaussagen nie ungeprüft", "Ton: Drohung statt Hilfe; Absender „KI-Team“ unpassend"],
     "Gehen Sie die Fehler durch und ordnen Sie sie den 5 Prüfpunkten zu. Erinnern Sie daran: Die KI hat das alles überzeugend formuliert, und gerade das macht die Prüfung nötig. "
     "Fragen Sie: Welche dieser Fehler wären Ihnen im Alltag ohne die Liste aufgefallen? Das zeigt den Wert fester Prüfroutinen."),
    ("Kennzeichnung und Urheberrecht",
     ["Wichtige KI-gestützte Dokumente intern kennzeichnen: „mit KI-Unterstützung erstellt, geprüft von …“", "Wer mit KI spricht (z. B. Chatbot), muss das erkennen können", "Realistische Bilder/Stimmen echter Personen nur mit Einwilligung", "Fremde Texte, Bilder, Marken nicht unbedacht nachahmen oder hochladen"],
     "Erläutern Sie unsere internen Regeln: [Option aus Kapitel 8 der Richtlinie]. Zum Recht: Es gibt Transparenzvorgaben und Urheberrecht; wie sie im Einzelfall greifen, ist eine Rechtsfrage. Verweisen Sie bei Zweifeln auf [NAME/Funktion]. "
     "Kein Anspruch auf Vollständigkeit; sagen Sie das auch so."),
    ("Wenn etwas schiefgeht",
     ["Falsche oder vertrauliche Daten eingegeben? Sofort melden", "Verdacht auf Datenabfluss? Sofort melden", "Auffällige oder diskriminierende KI-Ausgabe? Melden", "Melden heißt nicht bestraft werden – verschweigen macht es schlimmer"],
     "Das ist die Folie für die Meldekultur. Nennen Sie Kontakt und Weg konkret: [NAME / E-Mail / Telefon]. Erzählen Sie, dass Fehler normal sind, und dass schnelle Meldung den Schaden begrenzt. "
     "Beim Thema Datenschutzpannen: Es gibt kurze gesetzliche Fristen, deshalb zählt jede Stunde. Die Details klärt [Datenschutzbeauftragte/r]."),
    ("Die 7 Regeln zum Mitnehmen",
     ["1. Nur freigegebene Tools", "2. Datenampel beachten, rote Daten nie ungeprüft eingeben", "3. Keine Passwörter, keine Zugangsdaten", "4. Jede Ausgabe ist ein Entwurf – 5-Punkte-Prüfung", "5. Entscheidungen über Menschen treffen Menschen", "6. Wichtiges kennzeichnen, Rechte Dritter beachten", "7. Im Zweifel fragen, Fehler sofort melden"],
     "Fassen Sie zusammen und fragen Sie, welche Regel am meisten überrascht hat. Ein Foto dieser Folie oder ein Aushang der 7 Regeln am Arbeitsplatz hilft im Alltag. "
     "Beantworten Sie jetzt die Fragen aus dem Themenspeicher."),
    ("Wissenstest, Nachweis, nächste Schritte",
     ["Wissenstest (12 Fragen, ca. 10 Min.) – Bestehensgrenze: [9] richtige", "Teilnahme wird dokumentiert (Teilnahmeliste)", "Auffrischung: [jährlich]", "Fragen und Tool-Wünsche an [NAME/KONTAKT]", "Diese Vorlage ersetzt keine Rechtsberatung."],
     "Verteilen Sie den Wissenstest oder senden Sie den Link. Sammeln Sie Unterschriften für die Teilnahmeliste. Erklären Sie: Der Nachweis dokumentiert, dass geschult wurde. Er ist keine amtliche Bescheinigung. "
     "Danken Sie für die Mitarbeit und nennen Sie den nächsten Termin: [AUFFRISCHUNG]. Schlusshinweis: Diese Vorlage ersetzt keine Rechtsberatung."),
]


def build(outdir):
    prs = Presentation()
    prs.slide_width, prs.slide_height = Inches(13.333), Inches(7.5)
    layout = prs.slide_layouts[1]  # Titel und Inhalt
    for idx, (title, bullets, notes) in enumerate(SLIDES, 1):
        s = prs.slides.add_slide(layout)
        t, body = s.shapes.title, s.placeholders[1]
        t.left, t.top, t.width, t.height = Inches(0.7), Inches(0.4), Inches(11.9), Inches(1.2)
        body.left, body.top, body.width, body.height = Inches(0.9), Inches(1.8), Inches(11.5), Inches(4.8)
        t.text_frame.text = title
        for p in t.text_frame.paragraphs:
            p.alignment = PP_ALIGN.LEFT
            for r in p.runs:
                r.font.size = Pt(34 if idx > 1 else 40)
                r.font.bold = True
                r.font.color.rgb = DARK
        tf = body.text_frame
        tf.word_wrap = True
        n = len(bullets)
        size = 28 if n <= 3 else 26 if n == 4 else 24 if n == 5 else 22
        total = len(" ".join(bullets))
        if total > 600:
            size = min(size, 20)
        elif total > 450:
            size = min(size, 22)
        if idx == 1:
            size = 26
        for i, b in enumerate(bullets):
            p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
            p.text = b
            p.space_after = Pt(8)
            for r in p.runs:
                r.font.size = Pt(size)
        # Fußzeile
        fb = s.shapes.add_textbox(Inches(0.7), Inches(6.95), Inches(11.9), Inches(0.4))
        fb.text_frame.text = f"{DISCLAIMER} · {KIT_NAME} · {VERSION} · Folie {idx}/{len(SLIDES)}"
        for r in fb.text_frame.paragraphs[0].runs:
            r.font.size = Pt(10)
            r.font.color.rgb = GREY
        s.notes_slide.notes_text_frame.text = notes
    prs.save(f"{outdir}/{FILE}")
    return FILE
