from kit_lib import *

FILE = "KI-Nutzungsrichtlinie.docx"


def build(outdir):
    D = Doc("KI-Nutzungsrichtlinie", "für [FIRMENNAME] · Entwurf zur Anpassung", "KI-Nutzungsrichtlinie")
    D.disclaimer_box()
    D.callout(
        "So nutzen Sie diese Vorlage",
        [
            "Alles in **[ECKIGEN KLAMMERN]** ist ein Platzhalter: ersetzen Sie ihn durch Ihre Angabe oder wählen Sie eine Option und streichen Sie die andere.",
            "Lesen Sie die Richtlinie einmal komplett durch und streichen Sie, was bei Ihnen nicht passt. Lassen Sie sie vor der Einführung von [Geschäftsleitung] "
            "und, falls vorhanden, von Datenschutzbeauftragten und Betriebsrat prüfen.",
            "Löschen Sie diesen Kasten und den Hinweis oben, bevor Sie die Richtlinie verteilen (die Fußzeile mit dem Hinweis darf stehen bleiben).",
        ],
    )

    D.table(
        ["Dokumentinfo", ""],
        [
            ["Gilt für", "[FIRMENNAME], [Standort/Standorte]"],
            ["Version / gültig ab", "[1.0] / [TT.MM.JJJJ]"],
            ["Verantwortlich für diese Richtlinie", "[NAME, Funktion – z. B. KI-Beauftragte/r]"],
            ["Freigegeben durch", "[NAME, Geschäftsleitung] am [TT.MM.JJJJ]"],
            ["Nächste Überprüfung", "[TT.MM.JJJJ – spätestens in 12 Monaten]"],
        ],
        widths=[5.5, 10.9],
    )

    D.h1("1. Zweck")
    D.p(
        "[FIRMENNAME] nutzt Werkzeuge mit künstlicher Intelligenz (KI), um Routinearbeit zu erleichtern und die Qualität unserer Arbeit zu verbessern. "
        "Diese Richtlinie legt fest, wie wir das tun: sicher für unsere Kundinnen und Kunden, für unsere Beschäftigten und für unser Unternehmen."
    )
    D.p("Sie soll Orientierung geben, nicht bremsen. Wir wollen, dass Sie KI nutzen – aber mit klaren Leitplanken. Die Richtlinie soll:")
    D.bullets(
        [
            "erklären, **was erlaubt ist** und was nicht,",
            "schützen: personenbezogene Daten, Geschäftsgeheimnisse und die Rechte Dritter,",
            "sicherstellen, dass **Menschen die Verantwortung behalten** und KI-Ergebnisse geprüft werden,",
            "den Aufbau von **KI-Kompetenz** im Team unterstützen (siehe Kapitel 11).",
        ]
    )
    D.p("**Grundregel: Im Zweifel erst fragen, dann eingeben.** Ansprechperson ist [NAME / E-Mail / Telefon].")

    D.h1("2. Geltungsbereich")
    D.p(
        "Die Richtlinie gilt für alle, die für [FIRMENNAME] arbeiten: [Angestellte, Auszubildende, Praktikantinnen und Praktikanten, "
        "freie Mitarbeitende, Leiharbeitskräfte – nicht Zutreffendes streichen]. Sie gilt für dienstliche Geräte und, soweit dienstliche Inhalte betroffen sind, auch für private Geräte."
    )
    D.p("Als „KI-Tool“ gilt jede Anwendung, die Texte, Bilder, Töne, Code oder Entscheidungsvorschläge mithilfe von KI erzeugt oder auswertet. Dazu zählen zum Beispiel:")
    D.bullets(
        [
            "Chat-Assistenten und Sprachmodelle (im Browser, als App oder in andere Programme eingebaut),",
            "KI-Funktionen in Office-Programmen, E-Mail, Videokonferenzen und Übersetzungsdiensten,",
            "Bild-, Video- und Audiogeneratoren, Transkriptions- und Protokollwerkzeuge,",
            "Browser-Erweiterungen und Plug-ins mit KI-Funktion.",
        ]
    )
    D.table(
        ["Begriff", "Bedeutung in dieser Richtlinie"],
        [
            ["Eingabe / Prompt", "Alles, was Sie in ein KI-Tool eingeben oder hochladen: Fragen, Texte, Dateien, Bilder."],
            ["Ausgabe", "Das, was das KI-Tool Ihnen zurückgibt. Eine Ausgabe ist immer ein **Entwurf**."],
            ["Personenbezogene Daten", "Alle Angaben, die sich auf eine bestimmte oder bestimmbare Person beziehen, z. B. Name mit Kontext, E-Mail-Adresse, Telefonnummer, Kundennummer, Beschwerde, Bewerbungsunterlagen, Gehalt, Gesundheitsangaben."],
            ["Vertrauliche Informationen", "Interne Informationen, die nicht öffentlich sind und deren Bekanntwerden uns schaden könnte: Verträge, Preiskalkulationen, Strategien, Quellcode, Zugangsdaten."],
            ["Freigegebenes Tool", "Ein KI-Tool, das nach Kapitel 7 geprüft und in Anhang A eingetragen wurde."],
        ],
        widths=[4.2, 12.2],
    )

    D.h1("3. Erlaubte Nutzung")
    D.p("Sie dürfen **freigegebene KI-Tools** für Ihre dienstlichen Aufgaben nutzen, zum Beispiel um")
    D.bullets(
        [
            "Texte zu entwerfen, zu kürzen, zu übersetzen oder sprachlich zu verbessern,",
            "Ideen zu sammeln, Gliederungen und Checklisten zu erstellen,",
            "lange, **nicht vertrauliche** Texte zusammenzufassen,",
            "Tabellenformeln, einfache Skripte oder Vorlagen zu erstellen (ohne echte Daten),",
            "Besprechungen vorzubereiten und Notizen zu ordnen.",
        ]
    )
    D.p("Dabei gelten immer diese Bedingungen:")
    D.numbered(
        [
            "Nur Tools aus **Anhang A** (Freigabeliste).",
            "Nur Daten, die nach der **Datenampel** (Kapitel 5) für das jeweilige Tool zulässig sind.",
            "Jede Ausgabe wird **von einem Menschen geprüft**, bevor sie verwendet wird (Kapitel 9).",
            "Die Verantwortung für das Ergebnis liegt bei der Person, die es verwendet – nicht beim Tool.",
        ]
    )

    D.h1("4. Verbotene Nutzung")
    D.p("Nicht erlaubt ist:")
    D.bullets(
        [
            "**Rote Daten** (Kapitel 5) in Tools einzugeben, die dafür nicht ausdrücklich freigegeben sind,",
            "nicht freigegebene Tools oder **private Konten** für dienstliche Inhalte zu nutzen [OPTION: Ausnahmen nur nach schriftlicher Zustimmung von NAME],",
            "Passwörter, Zugangsdaten, Schlüssel oder Zahlungsdaten einzugeben,",
            "Entscheidungen **über Menschen** (z. B. Einstellung, Kündigung, Leistungsbewertung, Kreditwürdigkeit) allein von einer KI treffen oder vorbereiten zu lassen, ohne dass vorher [NAME/Funktion] den Einsatz geprüft hat,",
            "Ausgaben ungeprüft an Kundinnen, Kunden oder Behörden zu senden oder automatisiert versenden zu lassen,",
            "rechtliche, steuerliche oder medizinische Auskünfte der KI als verbindlich weiterzugeben,",
            "andere zu täuschen: gefälschte Bewertungen, vorgetäuschte Identitäten, realistisch wirkende Bilder, Stimmen oder Videos echter Personen ohne deren Einwilligung,",
            "urheberrechtlich geschützte oder fremde vertrauliche Inhalte ohne Berechtigung hochzuladen,",
            "Schutzmaßnahmen von Tools oder unserer IT zu umgehen,",
            "von KI erzeugten Programmcode ungeprüft in Produktivsysteme zu übernehmen.",
        ]
    )
    D.p(
        "Für neue Anwendungsfälle, die Auswirkungen auf Menschen haben (z. B. Bewerbungsauswahl, Mitarbeiterbewertung), gelten nach EU-Recht unter Umständen "
        "strengere Anforderungen. Sprechen Sie vorher mit [NAME/Funktion] und holen Sie bei Bedarf fachlichen Rat ein."
    )

    D.h1("5. Daten und Vertraulichkeit")
    D.p("Jede Eingabe in ein KI-Tool ist eine Weitergabe von Informationen an einen Dienst außerhalb unseres Betriebs. Deshalb gilt die **Datenampel**:")
    fills = {(0, 0): GREEN_FILL, (1, 0): YELLOW_FILL, (2, 0): RED_FILL}
    D.table(
        ["Stufe", "Beispiele", "Wo erlaubt?"],
        [
            ["GRÜN\nöffentlich / unkritisch", "Öffentliche Webseitentexte, allgemeine Fragen, Ideen ohne Firmenbezug, eigene Texte ohne Interna, Übungsbeispiele", "In jedem freigegebenen Tool (Stufe 1, 2 und 3)."],
            ["GELB\nintern, ohne Personenbezug", "Interne Abläufe, Entwürfe, Konzepte, anonymisierte Beispiele, Statistiken ohne Personenbezug [Ihre Definition ergänzen]", "Nur in Tools der Freigabestufe 2 oder 3 (Anhang A)."],
            ["ROT\npersonenbezogen / vertraulich", "Namen mit Kontext, Kontakt-, Kunden-, Bewerber-, Personal- und Gesundheitsdaten, Verträge, Preiskalkulationen, Geschäftsgeheimnisse, Zugangsdaten, [Quellcode]", "Nur in Tools der Freigabestufe 3 und nur für den dort festgelegten Zweck. Sonst **nur anonymisiert** – oder gar nicht."],
        ],
        widths=[3.6, 7.6, 5.2],
        fills=fills,
    )
    D.h3("Anonymisieren – aber richtig")
    D.bullets(
        [
            "Ersetzen Sie Namen, Firmen, Adressen, Nummern durch Platzhalter wie [Kunde A], [Ort], [Betrag].",
            "Achtung: Auch eine Kombination von Angaben (Beruf + Ort + besondere Umstände) kann eine Person erkennbar machen. Im Zweifel weglassen.",
            "Hochgeladene Dateien enthalten oft versteckte Angaben (Autor, Kommentare, Metadaten). Kopieren Sie lieber bereinigten Text als ganze Dateien.",
        ]
    )
    D.p("Freigabestufen: **Stufe 1** = nur grüne Daten · **Stufe 2** = grün und gelb · **Stufe 3** = zusätzlich rote Daten für einen festgelegten Zweck, nur nach Datenschutzprüfung.")

    D.h1("6. Datenschutz (DSGVO)")
    D.p(
        "Wenn personenbezogene Daten im Spiel sind, gilt zusätzlich das Datenschutzrecht (insbesondere die Datenschutz-Grundverordnung, DSGVO). "
        "Die wichtigsten Grundsätze in einfacher Sprache:"
    )
    D.bullets(
        [
            "**So wenig wie möglich:** Geben Sie nur ein, was für die Aufgabe nötig ist. Meist geht es auch ohne Namen.",
            "**Nur für den Zweck:** Daten, die wir für einen Zweck erhoben haben (z. B. Auftragsabwicklung), dürfen nicht einfach für etwas anderes genutzt werden.",
            "**Rechtsgrundlage nötig:** Personenbezogene Daten dürfen nur verarbeitet werden, wenn es dafür eine Grundlage gibt. Ob sie für einen KI-Einsatz vorliegt, klärt [Datenschutzbeauftragte/r bzw. externe Beratung] – nicht Sie allein.",
            "**Vertrag mit dem Anbieter:** Verarbeitet ein Anbieter Daten in unserem Auftrag, braucht es in der Regel einen Vertrag zur Auftragsverarbeitung. Das prüfen wir bei der Tool-Freigabe (Kapitel 7).",
            "**Datenübermittlung ins Ausland:** Wo der Anbieter Daten verarbeitet, ist ein Prüfpunkt der Freigabe.",
            "**Rechte Betroffener:** Menschen können Auskunft, Berichtigung und Löschung ihrer Daten verlangen. Was einmal in ein fremdes KI-Tool eingegeben wurde, lässt sich oft nicht zuverlässig zurückholen. Darum: keine Personendaten ohne Not.",
            "**Verzeichnisse und Hinweise:** Setzen wir KI mit personenbezogenen Daten ein, aktualisiert [NAME/Funktion] das Verzeichnis der Verarbeitungstätigkeiten und – falls nötig – die Datenschutzhinweise.",
        ]
    )
    D.p("Datenschutzbeauftragte/r: [NAME, intern/extern, Kontakt] · [OPTION: Wir haben keine/n Datenschutzbeauftragte/n benannt; Ansprechperson ist NAME.]")
    D.p("**Datenschutzpanne?** Sofort melden (Kapitel 12). Gesetzliche Meldefristen sind kurz, deshalb zählt jede Stunde.")

    D.h1("7. Freigabe von KI-Tools")
    D.p("Kein KI-Tool wird dienstlich genutzt, bevor es freigegeben ist. So läuft die Freigabe:")
    D.numbered(
        [
            "**Antrag:** Sie schildern [NAME/Funktion] kurz, welches Tool Sie wofür und mit welchen Daten nutzen möchten.",
            "**Prüfung:** [NAME/Funktion] bewertet das Tool mit der Datenschutz-Checkliste und der Bewertungsmatrix (Datei „Datenschutz-Checkliste-und-Tool-Freigabe.xlsx“). Bei roten Daten wird [Datenschutzbeauftragte/r] einbezogen.",
            "**Entscheidung:** [Geschäftsleitung/Freigabestelle] entscheidet innerhalb von [5] Arbeitstagen: freigegeben (mit Stufe 1, 2 oder 3 und Auflagen), abgelehnt oder „erst klären“.",
            "**Eintrag:** Freigegebene Tools stehen mit Stufe, Zweck und Auflagen in Anhang A.",
            "**Neuprüfung:** mindestens [jährlich] sowie bei Änderungen von Anbieter, Preis, Nutzungsbedingungen oder Funktionen.",
        ]
    )
    D.p("Ist ein Tool nur „irgendwie in Gebrauch“ (sogenannte Schatten-KI), melden Sie das bitte. [OPTION: Eine freiwillige Meldung eines früheren Einsatzes wird als Hinweis behandelt, nicht als Verstoß.]")

    D.h1("8. Kennzeichnung und Transparenz")
    D.bullets(
        [
            "**Intern:** Bei Dokumenten, die maßgeblich mit KI erstellt wurden und als Entscheidungsgrundlage dienen, vermerken Sie „mit KI-Unterstützung erstellt, geprüft von [Kürzel]“ [im Dokumentkopf / Versionsvermerk].",
            "**Gegenüber Kundinnen und Kunden:** Wer mit einem KI-System spricht (z. B. Chatbot), muss das erkennen können. Fragt jemand, ob ein Text mit KI entstanden ist, antworten wir ehrlich.",
            "**Bilder, Audio, Video:** Realistische KI-Inhalte, die echte Personen oder Ereignisse darstellen könnten, werden nur mit Einwilligung der Betroffenen und erkennbar als KI-erzeugt verwendet.",
            "Es gibt gesetzliche Transparenzvorgaben, die je nach Anwendungsfall greifen können. Im Zweifel fragen Sie [NAME/Funktion].",
            "**Urheberrecht:** Prüfen Sie, ob KI-Ausgaben fremde Inhalte (Texte, Bilder, Marken) zu stark nachahmen. Nutzen Sie fremdes Material nur mit Berechtigung.",
        ]
    )

    D.h1("9. Prüfpflicht und Halluzinationen")
    D.p(
        "KI-Tools erzeugen Sprache, die überzeugend klingt – auch dann, wenn sie falsch ist. Fachleute sprechen von „Halluzinationen“: erfundene Fakten, Zahlen, Quellen, Namen oder Zitate. "
        "Auch veraltete oder verzerrte Aussagen kommen vor. **Jede Ausgabe ist ein Entwurf, kein Ergebnis.**"
    )
    D.h3("Die 5-Punkte-Prüfung vor jeder Verwendung")
    D.numbered(
        [
            "**Fakten:** Stimmt das? Wichtige Aussagen gegen eine verlässliche Quelle prüfen.",
            "**Zahlen und Quellen:** Rechnen Sie nach. Existiert die genannte Quelle wirklich? Quellen und Zitate nie ungeprüft übernehmen.",
            "**Namen und Anrede:** Richtige Person, Firma, Produkt, Datum?",
            "**Ton und Zusagen:** Passt es zu uns? Enthält der Text Versprechen, Fristen oder Preise, die wir nicht geben wollen?",
            "**Vertraulichkeit und Rechte:** Steckt etwas Internes oder Fremdes drin, das nicht hinausgehen darf?",
        ]
    )
    D.table(
        ["Risiko", "Beispiele", "Prüfung"],
        [
            ["niedrig", "interne Notiz, Ideensammlung, Rohentwurf", "Durchsicht durch die Person selbst"],
            ["mittel", "Kunden-E-Mail, Social-Media-Beitrag, Angebotstext", "Selbstprüfung nach den 5 Punkten; [OPTION: Vier-Augen-Prinzip bei …]"],
            ["hoch", "Verträge, Preise, verbindliche Zusagen, Rechts-/Steuer-/Gesundheitsaussagen, Zahlen für Behörden oder Geschäftsberichte", "Fachliche Prüfung durch [Funktion/Fachperson] vor Verwendung"],
        ],
        widths=[2.4, 8.0, 6.0],
    )

    D.h1("10. Verantwortlichkeiten")
    D.table(
        ["Wer", "Aufgabe"],
        [
            ["Geschäftsleitung\n[NAME]", "Setzt die Richtlinie in Kraft, entscheidet über Tool-Freigaben und Ausnahmen, stellt Zeit und Mittel für Schulung bereit."],
            ["KI-Beauftragte/r\n[NAME]", "Pflegt Richtlinie und Freigabeliste, ist Ansprechperson, organisiert Schulung und Nachweise, sammelt Fragen und Vorfälle."],
            ["Datenschutz\n[NAME / extern]", "Berät bei personenbezogenen Daten, prüft rote Daten und Verträge, begleitet Datenschutzpannen."],
            ["IT\n[NAME / extern]", "Richtet Zugänge und Konten ein, sichert Geräte, sperrt nicht freigegebene Tools, soweit technisch möglich."],
            ["Führungskräfte", "Machen die Richtlinie bekannt, achten auf Einhaltung, melden Vorfälle und neue Anwendungsideen."],
            ["Alle Beschäftigten", "Halten die Richtlinie ein, prüfen KI-Ausgaben, melden Unsicherheiten und Vorfälle, nehmen an der Schulung teil."],
            ["[Betriebsrat, falls vorhanden]", "[Wird vor Einführung beteiligt, soweit Mitbestimmungsrechte berührt sind – bitte mit Rechtsberatung klären.]"],
        ],
        widths=[4.4, 12.0],
    )

    D.h1("11. Schulung und Nachweis")
    D.bullets(
        [
            "Alle Beschäftigten, die KI-Tools nutzen, werden **vor der ersten Nutzung** bzw. innerhalb von [4 Wochen] nach Eintritt geschult. [OPTION: Der Zugang zu freigegebenen Tools wird erst nach der Schulung eingerichtet.]",
            "Eine **Auffrischung** findet [jährlich] und bei wesentlichen Änderungen statt.",
            "Grundlage sind die Schulungsfolien und der Wissenstest. Wer in bestimmten Bereichen (z. B. Personal, Kundenservice) mit höherem Risiko arbeitet, erhält eine Vertiefung zu [THEMA].",
            "Teilnahme und Testergebnis werden **dokumentiert** (Teilnahmeliste/Nachweis). Aufbewahrung: [FRIST festlegen]. Die Listen enthalten personenbezogene Daten und werden entsprechend geschützt.",
        ]
    )
    D.p(
        "Die Schulung unterstützt den Aufbau von KI-Kompetenz im Betrieb. Welche gesetzlichen Anforderungen für [FIRMENNAME] im Einzelnen gelten und wie sie auszulegen sind, "
        "ist nicht Gegenstand dieser Vorlage; das klärt bei Bedarf eine Rechtsberatung."
    )

    D.h1("12. Verstöße und Meldung")
    D.bullets(
        [
            "**Fehler passieren.** Wer merkt, dass etwas Falsches, Vertrauliches oder Personenbezogenes in ein KI-Tool geraten ist oder eine KI-Ausgabe Schaden angerichtet hat, meldet das **sofort** an [NAME / E-Mail / Telefon]. Je früher, desto besser lässt sich der Schaden begrenzen.",
            "Meldepflichtig sind außerdem: Verdacht auf Datenabfluss, Zugangsdaten in fremden Händen, unerlaubte Tools, auffällige oder diskriminierende KI-Ausgaben.",
            "Wer meldet, wird nicht dafür bestraft, dass er gemeldet hat.",
            "Verstöße werden **verhältnismäßig** behandelt: Erst klären, Ursache beheben, nachschulen. Vorsätzliche oder grob fahrlässige Verstöße können arbeitsrechtliche Folgen haben [nach den Regeln Ihres Arbeitsvertrags/Ihrer Betriebsvereinbarung – bitte mit Rechtsberatung abstimmen].",
        ]
    )

    D.h1("13. Überprüfung und Inkrafttreten")
    D.p(
        "[KI-Beauftragte/r] überprüft diese Richtlinie mindestens [jährlich] und zusätzlich bei neuen Tools, Vorfällen oder wesentlichen Änderungen von Gesetzen, Verträgen oder Abläufen. "
        "Änderungen werden im Änderungsprotokoll festgehalten und allen mitgeteilt. Diese Richtlinie tritt am [TT.MM.JJJJ] in Kraft."
    )
    D.table(
        ["Version", "Datum", "Änderung", "Von"],
        [["[1.0]", "[TT.MM.JJJJ]", "Erstfassung", "[Kürzel]"], ["", "", "", ""], ["", "", "", ""]],
        widths=[2.2, 3.0, 8.2, 3.0],
    )
    D.p("Ort, Datum: [ORT, TT.MM.JJJJ]          Unterschrift Geschäftsleitung: ______________________________")

    D.h1("Anhang A: Freigegebene KI-Tools")
    D.p("Wird von [KI-Beauftragte/r] gepflegt. Ein Tool, das hier nicht steht, ist nicht freigegeben.", italic=True)
    D.table(
        ["Tool / Version", "Stufe (1/2/3)", "Erlaubter Zweck", "Auflagen", "Freigegeben am / bis"],
        [["[TOOL 1]", "[ ]", "[ ]", "[ ]", "[ ]"], ["[TOOL 2]", "[ ]", "[ ]", "[ ]", "[ ]"], ["", "", "", "", ""], ["", "", "", "", ""]],
        widths=[3.6, 2.2, 4.0, 3.6, 3.0],
    )

    D.h1("Anhang B: Kenntnisnahme")
    D.p("Ich habe die KI-Nutzungsrichtlinie von [FIRMENNAME] (Version [1.0]) erhalten, gelesen und verstanden. Offene Fragen habe ich mit [NAME] geklärt.")
    D.table(
        ["Name", "Datum", "Unterschrift"],
        [["", "", ""], ["", "", ""], ["", "", ""]],
        widths=[6.0, 3.5, 6.9],
    )
    D.save(f"{outdir}/{FILE}")
    return FILE
