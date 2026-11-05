from kit_lib import *

FILE = "Kurzanleitung-In-einer-Woche-eingefuehrt.docx"


def build(outdir):
    D = Doc("In einer Woche eingeführt", "Kurzanleitung zum KI-Starterkit", "Kurzanleitung")
    D.p("Sie sind für KI-Regeln und Schulung zuständig und haben wenig Zeit? So kommen Sie mit etwa **8–10 Stunden** verteilt auf eine Woche zum Ziel. " + DISCLAIMER, after=4)
    D.table(
        ["Tag", "Aufgabe", "Datei", "Dauer"],
        [
            ["Mo", "Kit durchsehen. Entscheiden: Wer ist KI-Beauftragte/r? Wer gibt frei? Fragebogen ausfüllen (anonymisiert).", "Anpassungs-Prompt (Schritt 1–3)", "1,5 Std."],
            ["Di", "Richtlinie mit KI anpassen lassen und selbst prüfen; Platzhalter [IN KLAMMERN] ersetzen.", "KI-Nutzungsrichtlinie, Anpassungs-Prompt (Schritt 4, 6)", "2 Std."],
            ["Mi", "Tools sammeln, die schon genutzt werden. Die wichtigsten 1–3 mit Checkliste/Matrix prüfen und im Register eintragen.", "Datenschutz-Checkliste-und-Tool-Freigabe.xlsx", "1,5 Std."],
            ["Do", "Richtlinie von Geschäftsleitung (ggf. Datenschutz, Betriebsrat) freigeben lassen. Folien anpassen: Beispiele, Kontakt, Tool-Liste.", "KI-Schulung.pptx", "2 Std."],
            ["Fr", "Schulung halten (ca. 75 Min.), Wissenstest, Teilnahmeliste unterschreiben lassen.", "KI-Schulung, Wissenstest-und-Nachweis", "2 Std."],
            ["Danach", "Prompt-Bibliothek verteilen, Meldeweg bekannt machen, Termin für Auffrischung und Überprüfung eintragen.", "Prompt-Bibliothek", "0,5 Std."],
        ],
        widths=[1.6, 8.0, 4.8, 2.0],
        size=9.5,
    )
    D.h2("Das brauchen Sie")
    D.bullets(
        [
            "Ein freigegebenes oder zumindest unkritisch nutzbares KI-Tool für die Anpassung (nur anonymisierte, allgemeine Angaben eingeben).",
            "Word, PowerPoint, Excel (oder kompatible Programme), einen Raum oder eine Videokonferenz und etwa 75 Minuten Zeit aller Betroffenen.",
            "Jemanden, der entscheiden darf (Geschäftsleitung).",
        ]
    )
    D.h2("Häufige Stolpersteine")
    D.bullets(
        [
            "**Alles auf einmal perfekt machen wollen.** Besser: Version 1.0 einführen, nach drei Monaten überarbeiten.",
            "**Vertrauliche Daten beim Anpassen eingeben.** Nicht nötig – allgemein beschreiben, anonymisieren.",
            "**KI-Ergebnis ungeprüft übernehmen.** Gerade Rechtliches, Fristen und Paragraphen prüfen lassen oder streichen.",
            "**Keine Entscheidung zu Tools.** Ohne Freigabeliste hilft die beste Richtlinie wenig.",
            "**Nachweis vergessen.** Teilnahmeliste am Schulungstag unterschreiben lassen.",
        ]
    )
    D.h2("Bevor Sie starten")
    D.p(
        "Dieses Kit unterstützt Sie dabei, Regeln aufzustellen und Beschäftigte zu schulen. Es ersetzt keine Rechtsberatung, und es sagt nichts darüber, welche gesetzlichen Vorgaben in Ihrem Fall im Einzelnen gelten. "
        "Offene rechtliche Fragen klären Sie bitte mit einer fachkundigen Person."
    )
    D.save(f"{outdir}/{FILE}")
    return FILE
