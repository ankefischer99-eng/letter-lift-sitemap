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
     ["Schulung für alle Beschäftigten von [FIRMENNAME]", "Referent/in: [NAME] · Datum: [TT.MM.JJJJ]", "Dauer: ca. 90 Minuten inkl. Aha-Übung und 2 Praxisübungen (mit allen Aha-Übungen bis 120 Minuten) · Stand: November 2026"],
     "Begrüßen Sie die Gruppe. Sagen Sie klar: Ziel ist nicht, Angst zu machen, sondern Sicherheit zu geben. Wer nach der Schulung weiß, was er eingeben darf und wie er Ergebnisse prüft, kann KI gut nutzen. "
     "Hinweis vorab: Diese Schulung und die Vorlage ersetzen keine Rechtsberatung. Planen Sie 90 Minuten ein; wenn es knapp wird, kürzen Sie die Folien 3 bis 6 und halten Sie Übungen und Datenampel ein."),
    ("Was Sie heute mitnehmen",
     ["Sie erleben selbst, wie stark guter Kontext die Antwort verändert", "Sie wissen, welche Daten NIE in ein KI-Tool gehören", "Sie prüfen KI-Ergebnisse mit einem festen Verfahren", "Sie kennen unsere Regeln und wissen, an wen Sie sich wenden"],
     "Gehen Sie die vier Ziele kurz durch; das erste erleben Sie gleich selbst. Fragen Sie vorab in die Runde: Wer nutzt schon KI, privat oder im Job? Handzeichen genügt. Das zeigt Ihnen das Niveau. Es ist normal, dass einige schon viel nutzen und andere noch nie. "
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
    ("Auflösung Praxisübung 1",
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
    ("Auflösung Praxisübung 2",
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


def _by(title_start):
    for sl in SLIDES:
        if sl[0].startswith(title_start):
            return sl
    raise KeyError(title_start)


def _merge(new_title, bullets, *titles):
    notes = " ".join(_by(t)[2] for t in titles)
    return (new_title, bullets, notes)


AHA1_A = ("Aha-Übung 1: Gleicher Auftrag – ohne und mit Kontext (15 Min.)",
          ["Beschwerde (erfunden): „Mein Paket kam zum zweiten Mal zu spät. Ich überlege, ob ich noch einmal bestelle.“",
           "Durchgang A, neue Unterhaltung: „Schreib eine Antwort auf diese Kundenbeschwerde: …“ – sonst nichts",
           "Durchgang B, neue Unterhaltung: derselbe Auftrag mit Rolle, Ziel, Zielgruppe, Ton, Beispiel, Format",
           "Beide Ergebnisse nebeneinander legen (Arbeitsblatt, Übung 1)"],
          "Das ist die zentrale Übung. Prinzip: erst erleben, dann erklären. Erklären Sie vorab NICHT, was ein guter Prompt ist. Teilen Sie das Arbeitsblatt 'Aha-Übungen' aus (Übung 1) oder blenden Sie den Beispielprompt B ein. "
          "Wichtig: Jeder Durchgang in einer NEUEN Unterhaltung, sonst läuft der Kontext aus Durchgang A mit. Gruppen zu 2 bis 3 Personen, ein Bildschirm. Nur das erfundene Beispiel verwenden, keine echten Kundendaten. "
          "Planen Sie etwa 10 Minuten für das Ausprobieren und 5 Minuten für die Auswertung. Hinweis: Ergebnisse unterscheiden sich von Tool zu Tool; das ist Teil der Erfahrung. Wer nach einigen Minuten fertig ist, vergleicht schon die Kriterien aus dem Arbeitsblatt.")
AHA1_B = ("Aha-Übung 1: Was ist aufgefallen?",
          ["Was ist der größte Unterschied zwischen A und B? Nennen Sie drei Punkte", "Welcher Baustein hat am meisten bewirkt? Rolle · Ziel · Zielgruppe · Ton · Beispiel · Format · Grenzen", "Hat B etwas Erfundenes oder zu viel versprochen?", "Reflexion: Wo schreibe ich im Alltag „nackte“ Aufträge?"],
          "Lassen Sie 3 bis 4 Gruppen berichten, bevor Sie etwas erklären. Typische Beobachtungen: B klingt persönlicher und konkreter; A ist allgemein und lang; manchmal enthält B Zusagen, die wir nicht wollten (daher die Grenzen im Prompt und die Prüfung). "
          "Erst jetzt erklären Sie den Kontext-Baukasten (nächste Folie). Fragen Sie: Welcher Baustein war der stärkste Hebel? Häufig ist es das Beispiel oder das Ziel. Nehmen Sie die Antworten ernst, auch wenn sie abweichen. "
          "Notieren Sie, was an der Beschwerde im Alltag der Gruppe sonst noch typisch ist.")
AHA_MORE = ("Weitere Aha-Übungen (optional, je 15 Min.)",
            ["Übung 2: Halluzination selbst provozieren – nach Fachbüchern zu einem sehr speziellen Thema fragen, jedes Buch selbst nachsuchen", "Übung 3: Schlechten Prompt in vier Runden verbessern („Mach was zu Weihnachten für Kunden.“)", "Übung 4: Dieselbe Aufgabe mit und ohne Beispiel (Betreffzeilen)", "Alle mit erfundenen oder öffentlichen Beispielen – keine vertraulichen Daten"],
            "Wählen Sie je nach Zeit eine oder zwei Übungen; alle stehen im Arbeitsblatt mit Schritten, Notizfeldern und einer Reflexionsfrage. Übung 2 ist besonders eindrucksvoll, weil sie Halluzinationen selbst sichtbar macht (Ergebnisse können je nach Tool und Websuche unterschiedlich ausfallen; prüfen Sie immer die Fundstelle). "
            "Übung 3 zeigt, welcher Baustein welchen Sprung bringt. Übung 4 zeigt, wie ein kurzes Muster den Stil steuert. Alle Übungen sind ohne Fachwissen mit jedem gängigen Tool möglich. Passen Sie die Zeit an: Die Schulung dauert mit allen Übungen bis zu 120 Minuten.")
GB1 = ("Grundbegriffe 1: Chat, Agent, Skill",
       ["Chat: Sie fragen, die KI antwortet – Sie steuern jeden Schritt", "Agent: Sie geben ein Ziel vor, die KI erledigt mehrere Schritte selbst (je nach Tool und Tarif verfügbar)", "Der Agent ist der Mitarbeiter, der Skill ist sein Handbuch", "Mehr Selbstständigkeit = mehr Zugriff = mehr Risiko: Datenampel gilt erst recht"],
       "Verwenden Sie das Bild: Der Agent ist wie ein Mitarbeiter, dem Sie ein Ziel geben. Der Skill ist das Handbuch, das er bei Bedarf nachschlägt (zum Beispiel: So schreiben wir bei uns Angebote). Je nach Tool heißen Handbücher anders und sind nicht überall verfügbar. "
       "Faustregel: Reicht eine einzelne Antwort, genügt der Chat. Mehrere Schritte mit Dateien oder Programmen: ein Agent kann helfen. Warnen Sie: Ein Agent handelt, nicht nur antwortet, daher Zugriffe klein halten, Ergebnisse prüfen, Freigabe nach Richtlinie. Eigene Skills zu bauen ist nicht Gegenstand dieser Schulung.")
GB2 = ("Grundbegriffe 2: Markdown und Mermaid",
       ["Markdown (.md): normale Textdatei, Struktur durch einfache Zeichen: # Überschrift, - Liste, 1. Schritt", "Wofür: Anleitungen, Wissensbasis, Prompts ablegen – KI versteht die Struktur gut", "Mermaid: Diagramm als Text beschreiben lassen (Ablauf, Organigramm)", "Anzeige je nach Tool und Tarif; Ergebnis immer prüfen"],
       "Zeigen Sie auf dem Bildschirm eine kleine .md-Datei in einem Texteditor und das Mermaid-Beispiel aus dem Dokument 'Grundbegriffe in einfacher Sprache'. Botschaft: keine Magie, nur Text mit einfachen Regeln. Markdown eignet sich, um Wissen und Anleitungen so abzulegen, dass Menschen und KI sie gleichermaßen lesen können. "
       "Mermaid: Sie beschreiben einen Ablauf in Stichpunkten, die KI schreibt den Diagrammtext, ein Programm zeichnet das Bild. Dateien, die in ein KI-Tool geladen werden, folgen der Datenampel.")
GB3 = ("Grundbegriffe 3: Modellwahl",
       ["Einfaches (umformulieren, kürzen, übersetzen): schnelles, günstiges Modell", "Komplexes (lange Texte auswerten, mehrere Schritte, Logik): starkes Modell", "Erst den Prompt verbessern, dann ein stärkeres Modell probieren", "Angebot und Bezeichnungen ändern sich oft – Tool und Tarif prüfen"],
       "Bewusst keine Namen, Ranglisten oder Preise: Sie veralten schnell und unterscheiden sich je nach Tool und Tarif. Die Regel ist einfach: Für einfache Aufgaben reicht das schnelle Modell, für komplexe lohnt das starke. Oft bringt ein besserer Auftrag (Kontext-Baukasten) mehr als ein stärkeres Modell. "
       "Erinnern Sie: Modellwahl ersetzt weder die Tool-Freigabe noch die Prüfung der Ergebnisse.")


def _assemble():
    s = SLIDES
    out = []
    out.append(s[0])                                   # Titel
    out.append(_by("Was Sie heute mitnehmen"))
    out += [AHA1_A, AHA1_B]                            # Erleben vor Erklären
    out.append(_merge("Was ist KI – und wie „denkt“ sie?",
                      ["Meist gemeint: generative KI – erzeugt Texte, Bilder, Code (oft versteckt in Office, E-Mail, Meetings)", "Gelernt aus sehr vielen Texten: welches Wort wahrscheinlich folgt", "Sie berechnet das Plausibelste – nicht das Geprüfte", "Deshalb klingen auch falsche Antworten überzeugend"],
                      "Was ist „KI“", "Wie ein Sprachmodell"))
    out.append(_by("Wo KI gut ist"))
    out.append(_by("Halluzinationen"))
    out.append(_merge("Unsere Richtlinie: Überblick, erlaubt, verboten",
                      ["Nur freigegebene Tools (Anhang A) · Datenampel · jede Ausgabe prüfen", "Erlaubt: Entwürfe, Ideen, Zusammenfassen nicht vertraulicher Texte, Formeln, Übersetzungen", "Verboten: rote Daten in ungeprüfte Tools, private Konten, Passwörter, ungeprüftes Versenden", "Verboten: Entscheidungen über Menschen allein durch KI, Täuschung, fremde geschützte Inhalte", "Unsicher? Erst fragen, dann eingeben"],
                      "Unsere Richtlinie auf einen Blick", "Erlaubt und verboten"))
    out.append(_by("Die Datenampel"))
    out.append(_merge("Personenbezogene und vertrauliche Daten",
                      ["Personenbezogen: Name + Kontext, E-Mail, Kundennummer, Beschwerden, Bewerbungen, Gehälter – auch Kombinationen", "Vertraulich: Verträge, Kalkulationen, Strategien, Quellcode, Zugangsdaten", "Faustregel: Was nicht an eine öffentliche Pinnwand gehört, gehört nicht in ein ungeprüftes Tool", "Eingegebenes lässt sich oft nicht zurückholen – auch Screenshots und ganze Dateien beachten"],
                      "Personenbezogene Daten", "Vertrauliche Firmendaten"))
    out.append(_by("So wird ein Tool freigegeben"))
    out += [_by("Praxisübung 1"), _by("Auflösung Praxisübung 1")]
    prompts = ("Kontext-Baukasten: so fragen Sie gut",
               ["Rolle: Wer soll die KI sein?", "Ziel und Zielgruppe: Was soll erreicht werden, für wen?", "Ton und Beispiel: Wie klingt es bei uns?", "Format und Grenzen: Länge, Struktur – und was nicht passieren soll (nichts erfinden)", "Die Prompt-Bibliothek nutzt diesen Baukasten in allen 34 Vorlagen"],
               "Jetzt erklären Sie, was die Gruppe in Aha-Übung 1 selbst erlebt hat: Der Unterschied zwischen A und B kommt aus diesen Bausteinen. Verweisen Sie auf die Prompt-Bibliothek: Jede Vorlage hat die Felder ROLLE, ZIEL, ZIELGRUPPE, TON, BEISPIEL, FORMAT, GRENZEN, MATERIAL. "
               "Betonen Sie: Kontext heißt nicht vertrauliche Daten. Beschreiben Sie die Situation, nicht die Person. Auch beim besten Prompt bleibt die Prüfpflicht.")
    out.append(prompts)
    out.append(_by("Die 5-Punkte-Prüfung"))
    out.append(AHA_MORE)
    out += [_by("Praxisübung 2"), _by("Auflösung Praxisübung 2")]
    out.append(_merge("Kennzeichnen, Urheberrecht, Melden",
                      ["Wichtige KI-gestützte Dokumente intern kennzeichnen: „mit KI-Unterstützung erstellt, geprüft von …“", "Wer mit KI spricht (z. B. Chatbot), muss das erkennen können; realistische Bilder/Stimmen echter Personen nur mit Einwilligung", "Fremde Texte, Bilder, Marken nicht unbedacht nachahmen oder hochladen", "Falsche oder vertrauliche Daten eingegeben? Verdacht auf Abfluss? Sofort melden – melden heißt nicht bestraft werden"],
                      "Kennzeichnung und Urheberrecht", "Wenn etwas schiefgeht"))
    out += [GB1, GB2, GB3]
    out.append(_by("Die 7 Regeln"))
    out.append(_by("Wissenstest"))
    return out


SLIDES = _assemble()


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
