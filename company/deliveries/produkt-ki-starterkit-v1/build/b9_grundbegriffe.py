from kit_lib import *

FILE = "Grundbegriffe-in-einfacher-Sprache.docx"


def build(outdir):
    D = Doc("Grundbegriffe in einfacher Sprache", "Fünf Begriffe, die Ihnen im KI-Alltag begegnen – mit Bildern statt Fachchinesisch", "Grundbegriffe")
    D.p("Funktionen und Bezeichnungen unterscheiden sich je nach Tool und Tarif und ändern sich schnell. Diese Seiten beschreiben das Prinzip, nicht ein bestimmtes Produkt. " + DISCLAIMER, italic=True, size=10)

    D.h1("1. Chat oder Agent?")
    D.p("**Ein Chat ist ein Gespräch.** Sie fragen, die KI antwortet, Sie entscheiden jeden Schritt. **Ein Agent ist eher ein Mitarbeiter:** Sie geben ein Ziel vor, er plant mehrere Schritte selbst und führt sie aus, zum Beispiel Dateien lesen, eine Tabelle anlegen oder Informationen in mehreren Programmen zusammensuchen.")
    D.callout("Merkbild", ["**Der Agent ist der Mitarbeiter, der Skill ist sein Handbuch.**"], fill=SOFT_FILL)
    D.table(
        ["", "Chat", "Agent"],
        [
            ["Typischer Einsatz", "Text entwerfen, umformulieren, erklären, Ideen sammeln, einzelne Fragen", "Mehrstufige, wiederkehrende Aufgaben mit Dateien oder anderen Programmen"],
            ["Wer steuert?", "Sie, bei jedem Schritt", "Die KI führt Schritte selbst aus, Sie geben Ziel und Rahmen vor"],
            ["Risiko", "Falsche Antwort", "Falsche Antwort **und** Handlungen: Dateien ändern, Dinge versenden"],
            ["Regel", "Ausgabe prüfen", "Zugriffe klein halten, Ergebnisse prüfen, vorher Freigabe nach Richtlinie"],
        ],
        widths=[3.2, 6.5, 6.7],
        size=9.5,
    )
    D.p("**Faustregel:** Reicht eine einzelne Antwort, nehmen Sie den Chat. Müssen mehrere Schritte nacheinander erledigt werden und kommen Dateien oder andere Programme ins Spiel, kann ein Agent helfen – sofern Ihr Tool das anbietet („je nach Tool und Tarif verfügbar“). Ein Agent bekommt Zugriff auf Ihre Daten und Programme, deshalb gilt die Datenampel dort erst recht.")

    D.h1("2. Skill: das Handbuch")
    D.p("Ein Skill ist ein **Handbuch mit Anweisungen**, das die KI bei Bedarf nachschlägt. Statt in jeder Anfrage zu erklären, wie bei Ihnen Angebote aussehen, steht das einmal im Handbuch: wann es gilt, welche Schritte, welche Regeln, ein Beispiel. Die KI schlägt nach, wenn die Aufgabe passt.")
    D.bullets(
        [
            "**Gut für:** Aufgaben, die Sie immer wieder gleich erledigen und bei denen Ihre Regeln gelten.",
            "**Wie es heißt:** je nach Tool unterschiedlich (zum Beispiel Anweisungen, Vorlagen, Projekte oder Assistenten) und nicht überall verfügbar.",
            "**Wichtig:** Ein Handbuch ist nur so gut wie seine Anweisungen. Schreiben Sie klar, geben Sie Beispiele und nehmen Sie keine vertraulichen Daten hinein.",
        ]
    )
    D.p("Eigene Skills zu bauen ist nicht Teil dieses Kits.", italic=True)

    D.h1("3. Markdown und .md-Dateien")
    D.p("Eine Markdown-Datei (Endung **.md**) ist eine **ganz normale Textdatei**, in der einfache Zeichen die Struktur zeigen. Sie lässt sich in jedem Texteditor öffnen. KI-Tools verstehen diese Struktur sehr gut.")
    D.mono("# Angebote schreiben (Überschrift 1)\n## Wann gilt das? (Überschrift 2)\n- Bei Anfragen von Neukunden\n- Bei Anfragen über [Produktgruppe]\n\n## Schritte\n1. Bedarf klären\n2. Angebot mit Preisstaffel erstellen\n3. Nachfassen nach [5] Werktagen\n\n**Wichtig:** Keine Rabatte ohne Freigabe.")
    D.p("**Wofür nutzt man es?**")
    D.bullets(
        [
            "**Anleitungen:** Abläufe Schritt für Schritt, die Menschen und KI gleichermaßen lesen können.",
            "**Wissensbasis:** Ihre Regeln, Produktinfos, Tonvorgaben, häufige Fragen – eine Datei pro Thema.",
            "**Prompts ablegen:** Ihre besten Prompts mit Überschrift, Zweck und Platzhaltern an einem Ort.",
        ]
    )
    D.p("**So bauen Sie eine einfache Struktur auf:** Eine Datei pro Thema · Überschriften für Gliederung (#, ##) · Listen für Schritte (- oder 1.) · kurze Sätze · ein Beispiel pro Regel · Datum und Verantwortliche/n nennen. **Datenschutz:** Was in einer Datei steht, die Sie in ein KI-Tool laden, folgt der Datenampel.")

    D.h1("4. Modellwahl: schnell oder stark?")
    D.p("Viele Tools bieten mehrere Modelle an. Ohne Namen und Ranglisten gilt als grobe Regel:")
    D.table(
        ["Aufgabe", "Eher passend"],
        [
            ["Einfaches: umformulieren, kürzen, übersetzen, Ideen, Standardantworten", "**Schnelles, günstiges Modell**"],
            ["Komplexes: lange Texte auswerten, mehrere Schritte, schwierige Abwägungen, Tabellen und Logik", "**Starkes Modell** (braucht meist mehr Zeit und Kontingent)"],
        ],
        widths=[10.4, 6.0],
        size=9.5,
    )
    D.bullets(
        [
            "Zuerst den **Prompt verbessern**, dann ein stärkeres Modell probieren. Ein besserer Auftrag bringt oft mehr als ein größeres Modell.",
            "Das Angebot, die Bezeichnungen und die Möglichkeiten ändern sich häufig. Schauen Sie in Ihr Tool und Ihre Tarifbeschreibung.",
            "Modellwahl ersetzt nicht die Tool-Freigabe und nicht die Prüfung der Ergebnisse.",
        ]
    )

    D.h1("5. Mermaid: Diagramme als Text")
    D.p("Mermaid ist eine einfache **Textsprache für Diagramme**. Sie lassen die KI den Text schreiben, und ein Programm zeichnet daraus Ablaufdiagramme, Organigramme oder Zeitpläne. Praktisch, um Abläufe zu klären, Einarbeitung zu erleichtern oder einen Prozess für die Richtlinie darzustellen.")
    D.mono("flowchart TD\n  A[Kundenanfrage geht ein] --> B{Dringend?}\n  B -- Ja --> C[Sofort beantworten]\n  B -- Nein --> D[Antwort innerhalb von 2 Werktagen]\n  C --> E[Im Verlauf dokumentieren]\n  D --> E")
    D.p("**Prompt-Idee:** „Beschreibe den folgenden Ablauf als Mermaid-Flussdiagramm und gib nur den Diagrammtext aus: [Ablauf in Stichpunkten, ohne Personendaten].“")
    D.bullets(
        [
            "Ob und wo sich das Diagramm anzeigen lässt, hängt vom Tool ab (je nach Tool und Tarif verfügbar). Ohne Darstellung bleibt der Text trotzdem lesbar und kann später eingefügt werden.",
            "Prüfen Sie das Ergebnis: Stimmt der Ablauf? Fehlen Schritte? Das Diagramm ist ein Entwurf wie jede KI-Ausgabe.",
        ]
    )
    D.save(f"{outdir}/{FILE}")
    return FILE
