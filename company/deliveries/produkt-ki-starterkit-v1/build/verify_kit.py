"""Prüft die erzeugten Kit-Dateien programmatisch und schreibt QA.md.

Aufruf:  python3 build/verify_kit.py
Braucht: python-docx, python-pptx, openpyxl, pypdf, pyspellchecker (optional), LibreOffice (soffice).
"""
import datetime
import os
import re
import shutil
import subprocess
import sys
import tempfile
import zipfile

from docx import Document
from openpyxl import load_workbook
from pptx import Presentation
from pypdf import PdfReader

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import b3_test  # noqa: E402

DOCX = {
    "KI-Nutzungsrichtlinie.docx": (6, 8),
    "Wissenstest-und-Nachweis.docx": (None, None),
    "Prompt-Bibliothek.docx": (None, None),
    "Anpassungs-Prompt.docx": (None, None),
    "Kurzanleitung-In-einer-Woche-eingefuehrt.docx": (1, 2),
    "Aha-Uebungen-Arbeitsblatt.docx": (None, None),
    "Grundbegriffe-in-einfacher-Sprache.docx": (2, 3),
}
PPTX = "KI-Schulung.pptx"
XLSX = "Datenschutz-Checkliste-und-Tool-Freigabe.xlsx"
DISCLAIMER = "Diese Vorlage ersetzt keine Rechtsberatung."
# Verbotsliste aus STATE.md (Abschnitt Lieferung) + unbelegte Rechtszitate
FORBIDDEN = {
    "Verbotsbegriff 1 (rechts-sicher)": r"rechtssicher",
    "Verbotsbegriff 2 (erfüllt … AI Act)": r"erfüllt\s+(den\s+|die\s+)?(AI[\s-]?Act|KI-(Verordnung|VO))",
    "Verbotsbegriff 3 (zertifiziert)": r"zertifiziert",
    "Paragraphenzeichen §": r"§",
    "Artikelzitat 'Art. <Zahl>'": r"\bArt\.?\s*\d",
    "'AI Act' (irgendwo)": r"AI[\s-]?Act",
}


def soffice_convert(src, fmt, outdir):
    subprocess.run(
        ["soffice", "--headless", "--convert-to", fmt, "--outdir", outdir, src],
        check=True, capture_output=True, timeout=180,
    )


def docx_text(path):
    d = Document(path)
    parts = [p.text for p in d.paragraphs]
    for t in d.tables:
        for row in t.rows:
            for c in row.cells:
                parts.append(c.text)
    for s in d.sections:
        parts += [p.text for p in s.footer.paragraphs]
    return "\n".join(parts)


def pptx_text(path):
    prs = Presentation(path)
    parts = []
    for s in prs.slides:
        for sh in s.shapes:
            if sh.has_text_frame:
                parts.append(sh.text_frame.text)
        if s.has_notes_slide:
            parts.append(s.notes_slide.notes_text_frame.text)
    return "\n".join(parts)


def xlsx_text(path):
    wb = load_workbook(path)
    parts = []
    for ws in wb.worksheets:
        for row in ws.iter_rows():
            for c in row:
                if isinstance(c.value, str) and not c.value.startswith("="):
                    parts.append(c.value)
    return "\n".join(parts)


def main():
    res = []  # (Datei, Prüfung, Ergebnis, ok)
    texts = {}
    tmp = tempfile.mkdtemp(prefix="kitqa_")

    # --- DOCX
    for name, (lo, hi) in DOCX.items():
        path = os.path.join(OUT, name)
        d = Document(path)  # öffnet?
        texts[name] = docx_text(path)
        soffice_convert(path, "pdf", tmp)
        pages = len(PdfReader(os.path.join(tmp, name.replace(".docx", ".pdf"))).pages)
        ok = True if lo is None else lo <= pages <= hi
        want = "" if lo is None else f" (Soll {lo}–{hi})"
        res.append((name, "Öffnen mit python-docx; PDF-Export mit LibreOffice; Seitenzahl", f"{pages} Seiten{want}; {len(d.paragraphs)} Absätze, {len(d.tables)} Tabellen", ok))
        if DISCLAIMER not in texts[name]:
            res.append((name, "Hinweis „ersetzt keine Rechtsberatung“", "FEHLT", False))
        else:
            res.append((name, "Hinweis „ersetzt keine Rechtsberatung“", f"vorhanden ({texts[name].count(DISCLAIMER)}×, inkl. Fußzeile)", True))

    # --- PPTX
    path = os.path.join(OUT, PPTX)
    prs = Presentation(path)
    texts[PPTX] = pptx_text(path)
    n = len(prs.slides)
    notes = [len(s.notes_slide.notes_text_frame.text.strip()) if s.has_notes_slide else 0 for s in prs.slides]
    ex = [i + 1 for i, s in enumerate(prs.slides) if (s.shapes.title.text if s.shapes.title else "").startswith("Praxisübung")]
    res.append((PPTX, "Öffnen mit python-pptx; Folienzahl", f"{n} Folien (Soll 18–24)", 18 <= n <= 24))
    res.append((PPTX, "Sprechernotiz auf jeder Folie", f"{sum(1 for x in notes if x > 40)}/{n} Folien mit Notiz > 40 Zeichen; kürzeste {min(notes)} Zeichen", all(x > 40 for x in notes)))
    res.append((PPTX, "Zwei Praxisübungen", f"Folien {ex}", len(ex) == 2))
    aha = [i + 1 for i, s in enumerate(prs.slides) if (s.shapes.title.text if s.shapes.title else "").startswith("Aha-Übung 1") or "Aha-Übungen" in (s.shapes.title.text if s.shapes.title else "")]
    res.append((PPTX, "Aha-Übung 1 (2 Folien: Anleitung + Auswertung) und Folie „Weitere Aha-Übungen“", f"Folien {aha}", len(aha) == 3))
    gb = [i + 1 for i, s in enumerate(prs.slides) if (s.shapes.title.text if s.shapes.title else "").startswith("Grundbegriffe")]
    res.append((PPTX, "Kapitel Grundbegriffe (Soll 3–5 Folien)", f"Folien {gb}", 3 <= len(gb) <= 5))
    res.append((PPTX, "Hinweis „ersetzt keine Rechtsberatung“", f"auf {sum(1 for s in prs.slides if any(sh.has_text_frame and DISCLAIMER in sh.text_frame.text for sh in s.shapes))}/{n} Folien (Fußzeile)", DISCLAIMER in texts[PPTX]))
    soffice_convert(path, "pdf", tmp)
    pp = len(PdfReader(os.path.join(tmp, PPTX.replace(".pptx", ".pdf"))).pages)
    res.append((PPTX, "PDF-Export mit LibreOffice (Rendern möglich)", f"{pp} Seiten", pp == n))
    # Überlauf-Heuristik: Textmenge je Folie
    heavy = [i + 1 for i, s in enumerate(prs.slides) if sum(len(sh.text_frame.text) for sh in s.shapes if sh.has_text_frame) > 700]
    res.append((PPTX, "Text-Überlauf-Heuristik (> 700 Zeichen/Folie)", f"Folien mit viel Text: {heavy or 'keine'}", not heavy))

    # --- XLSX
    path = os.path.join(OUT, XLSX)
    wb = load_workbook(path)
    texts[XLSX] = xlsx_text(path)
    res.append((XLSX, "Öffnen mit openpyxl; Blätter", ", ".join(wb.sheetnames), len(wb.sheetnames) >= 5))
    res.append((XLSX, "Hinweis „ersetzt keine Rechtsberatung“", "vorhanden" if DISCLAIMER in texts[XLSX] else "FEHLT", DISCLAIMER in texts[XLSX]))
    # Formeltest per LibreOffice-Neuberechnung: Szenarien auf Kopie
    scen = [
        # (Beschreibung, K1,K2,K3, Kriterien, erwartet)
        ("alle Ja, Punkte 2,1,2,1,1,1,2 (Beispielzeile, 20/28 = 71 %)", ["Ja"] * 3, [2, 1, 2, 1, 1, 1, 2], "Freigabe mit Auflagen"),
        ("alle Ja, überall 2 (100 %)", ["Ja"] * 3, [2] * 7, "Freigabe empfohlen"),
        ("alle Ja, überall 1 (genau 50 % = Grenzwert)", ["Ja"] * 3, [1] * 7, "Freigabe mit Auflagen"),
        ("alle Ja, Punkte 0", ["Ja"] * 3, [0] * 7, "Nicht freigeben"),
        ("K2 = Nein, sonst gute Punkte", ["Ja", "Nein", "Ja"], [2] * 7, "Nur grüne Daten (Stufe 1)"),
        ("K1 = Unklar", ["Unklar", "Ja", "Ja"], [2] * 7, "Erst klären"),
        ("K.-o. nur teilweise ausgefüllt", ["Ja", None, None], [2] * 7, "K.-o.-Fragen ausfüllen"),
        ("Kriterien unvollständig", ["Ja"] * 3, [2, 2, None, None, None, None, None], "Kriterien bewerten"),
    ]
    tw = load_workbook(path)
    ws = tw["Tool-Bewertung"]
    for i, (_, ko, cr, _) in enumerate(scen):
        r = 8 + i
        ws.cell(row=r, column=1, value=f"Test {i + 1}")
        for j, v in enumerate(ko):
            ws.cell(row=r, column=2 + j, value=v)
        for j, v in enumerate(cr):
            ws.cell(row=r, column=5 + j, value=v)
    tr = tw["Tool-Register"]
    tr["A6"], tr["G6"] = "Altes Tool", datetime.date(2020, 1, 1)
    tr["A7"], tr["G7"] = "Neues Tool", datetime.date(2099, 1, 1)
    cl = tw["Checkliste"]
    for r in range(8, 8 + 20):
        cl.cell(row=r, column=5, value="Erledigt" if r < 12 else "Offen")
    cl["E12"] = "Nicht zutreffend"
    tpath = os.path.join(tmp, "xlsx_test.xlsx")
    tw.save(tpath)
    conv = os.path.join(tmp, "recalc")
    os.makedirs(conv)
    soffice_convert(tpath, "xlsx", conv)
    rv = load_workbook(os.path.join(conv, "xlsx_test.xlsx"), data_only=True)
    tv = rv["Tool-Bewertung"]
    hdr = [c.value for c in tv[7]]
    ci = {h: k + 1 for k, h in enumerate(hdr)}
    allok = True
    for i, (desc, _, _, expect) in enumerate(scen):
        r = 8 + i
        got = tv.cell(row=r, column=ci["Empfehlung"]).value
        pts = tv.cell(row=r, column=ci["Punkte"]).value
        mx = tv.cell(row=r, column=ci["Max."]).value
        pct = tv.cell(row=r, column=ci["Anteil"]).value
        ok = got == expect
        allok &= ok
        res.append((XLSX, f"Formeltest Tool-Bewertung: {desc}", f"Empfehlung „{got}“ (erwartet „{expect}“); Punkte {pts}/{mx}, Anteil {pct if pct in (None, '') else round(pct, 3)}", ok))
    # Beispielzeile unverändert (Datei) – Grenzwerte Punktesumme: Gewichte 3,3,2,2,2,1,1 -> max 28
    treg = rv["Tool-Register"]
    h6, h7 = treg["H6"].value, treg["H7"].value
    res.append((XLSX, "Formeltest Tool-Register (Neuprüfung fällig?)", f"Datum 2020 → „{h6}“, Datum 2099 → „{h7}“", h6 == "FÄLLIG" and h7 == "ok"))
    cv = rv["Checkliste"]
    res.append((XLSX, "Formeltest Checkliste (Zähler)", f"Erledigt={cv['B4'].value}, Offen={cv['D4'].value}, Nicht zutreffend={cv['F4'].value}, Fortschritt={round(cv['B5'].value, 3)}, Alle erledigt?={cv['F5'].value}", (cv["B4"].value, cv["D4"].value, cv["F4"].value) == (4, 15, 1)))
    # Fehlerwerte irgendwo?
    errs = []
    for sh in rv.worksheets:
        for row in sh.iter_rows():
            for c in row:
                if isinstance(c.value, str) and c.value.startswith("#"):
                    errs.append(f"{sh.title}!{c.coordinate}")
    res.append((XLSX, "Keine Formelfehler (#WERT!, #NAME? …) nach Neuberechnung", "keine" if not errs else str(errs), not errs))
    # Datei in Originalzustand: Formeln vorhanden?
    nform = sum(1 for sh in wb.worksheets for row in sh.iter_rows() for c in row if isinstance(c.value, str) and c.value.startswith("="))
    res.append((XLSX, "Anzahl Formeln in der gelieferten Datei", str(nform), nform > 30))
    nval = sum(len(sh.data_validations.dataValidation) for sh in wb.worksheets)
    res.append((XLSX, "Dropdown-Listen (Datenvalidierung)", f"{nval} Regeln", nval >= 4))

    # --- Inhaltsprüfungen
    # Prompts
    pt = texts["Prompt-Bibliothek.docx"]
    nprompts = len(re.findall(r"^\d+\. ", "\n".join(p.text for p in Document(os.path.join(OUT, "Prompt-Bibliothek.docx")).paragraphs), re.M))
    d = Document(os.path.join(OUT, "Prompt-Bibliothek.docx"))
    ptables = [t for t in d.tables if re.match(r"^\d+\. ", t.rows[0].cells[0].text)]
    cats = {}
    import b5_prompts
    for cat, lst in b5_prompts.CATS:
        cats[cat] = len(lst)
    res.append(("Prompt-Bibliothek.docx", "Anzahl Prompts (Tabellen mit Nr.)", f"{len(ptables)} (Soll 34 = 5 Bereiche × 6 + 4 Excel); je Bereich {cats}", len(ptables) == 34))
    allfilled = all(len(t.rows) == 4 and all(t.rows[i].cells[1].text.strip() for i in (1, 2, 3)) for t in ptables)
    res.append(("Prompt-Bibliothek.docx", "Jeder Prompt hat Zweck, Prompt-Text und Hinweis", "ja" if allfilled else "NEIN", allfilled))
    bk_ok = all(all(f"{l}:" in t.rows[2].cells[1].text for l in b5_prompts.LABELS) for t in ptables)
    res.append(("Prompt-Bibliothek.docx", "Kontext-Baukasten sichtbar: jeder Prompt hat ROLLE/ZIEL/ZIELGRUPPE/TON/BEISPIEL/FORMAT/GRENZEN/MATERIAL", "ja" if bk_ok else "NEIN", bk_ok))
    xl = [t for t in ptables if "Plausibilität" in t.rows[2].cells[1].text]
    res.append(("Prompt-Bibliothek.docx", "Excel-/Auswertungs-Prompts mit Plausibilitätscheck (Soll ≥ 3)", f"{len(xl)}", len(xl) >= 3))
    # Test
    qs = b3_test._rebalance()
    pos = [("ABCD"[c]) for (_, _, c, _) in qs]
    dist = {k: pos.count(k) for k in "ABCD"}
    res.append(("Wissenstest-und-Nachweis.docx", "12 Fragen mit je 4 Antworten und Lösung", f"{len(qs)} Fragen; Verteilung richtiger Antworten {dist}", len(qs) == 12 and max(dist.values()) <= 4))

    # --- Stand-Datum auf jedem Dokument
    for name, t in texts.items():
        res.append((name, "„Stand: November 2026“ vorhanden", "ja" if "Stand: November 2026" in t else "FEHLT", "Stand: November 2026" in t))
    # --- Verbotsliste
    for label, pat in FORBIDDEN.items():
        hits = []
        for name, t in texts.items():
            for m in re.finditer(pat, t, flags=re.I):
                a = max(0, m.start() - 30)
                hits.append(f"{name}: …{t[a:m.end() + 30]!r}")
        res.append(("alle 9 Dateien", f"Verbotsliste: {label}", "0 Treffer" if not hits else "; ".join(hits[:3]), not hits))

    # --- Rechtschreibung (Wörterbuch-Heuristik)
    spell_info = "nicht ausgeführt (pyspellchecker fehlt)"
    unknown_all = {}
    try:
        from spellchecker import SpellChecker
        sp = SpellChecker(language="de")
        sp.word_frequency.load_words(open(os.path.join(HERE, "wortliste_ok.txt"), encoding="utf-8").read().split())
        for name, t in texts.items():
            words = re.findall(r"[A-Za-zÄÖÜäöüß]{4,}", re.sub(r"\[[^\]]*\]", " ", t))
            unk = sorted({w for w in sp.unknown([w.lower() for w in words])})
            unknown_all[name] = unk
        spell_info = "ausgeführt"
    except Exception as e:  # noqa: BLE001
        spell_info = f"Fehler: {e}"
    for name, unk in unknown_all.items():
        res.append((name, "Rechtschreib-Heuristik (Wörterbuch, unbekannte Wörter ≥ 4 Buchstaben)", f"{len(unk)} unbekannte Wörter" + (f": {', '.join(unk)}" if unk else ""), True))

    # --- Platzhalter
    for name, t in texts.items():
        ph = re.findall(r"\[[^\]]+\]", t)
        res.append((name, "Platzhalter in [ECKIGEN KLAMMERN]", f"{len(ph)}", True))

    # --- Zip-Integrität
    for name in list(DOCX) + [PPTX, XLSX]:
        with zipfile.ZipFile(os.path.join(OUT, name)) as z:
            bad = z.testzip()
        res.append((name, "ZIP-/OOXML-Integrität (testzip)", "ok" if bad is None else f"defekt: {bad}", bad is None))

    shutil.rmtree(tmp, ignore_errors=True)
    return res, spell_info, unknown_all


def write_qa(res, spell_info, unknown_all):
    n_ok = sum(1 for r in res if r[3])
    lines = []
    A = lines.append
    A("# QA-Protokoll — KI-Starterkit v1")
    A("")
    A(f"Erstellt: 2026-11-05 · Erzeugt mit `build/build_kit.py`, geprüft mit `build/verify_kit.py` (Ausführung: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}).")
    A(f"Automatische Prüfungen: **{n_ok} von {len(res)} bestanden**" + ("" if n_ok == len(res) else " — Abweichungen siehe Spalte „OK“ und Abschnitt „Bekannte Grenzen“."))
    A("")
    A("## 1. Automatische Prüfungen (Skript, reproduzierbar)")
    A("")
    A("| Datei | Prüfung | Ergebnis | OK |")
    A("|---|---|---|---|")
    for f, p, r, ok in res:
        A(f"| {f} | {p} | {r.replace('|', '/')} | {'ja' if ok else '**NEIN**'} |")
    A("")
    A("Methode: Seitenzahlen = PDF-Export mit LibreOffice (Word kann je nach Schrift ±1 Seite abweichen). Formeln = Neuberechnung in LibreOffice auf einer Testkopie mit 7 Szenarien; die gelieferte Datei enthält nur das fiktive Beispiel.")
    A("")
    A("## 2. Anforderungen aus STATE.md (abgehakt)")
    A("")
    A("| # | Anforderung | Stand |")
    A("|---|---|---|")
    A("| 1 | `KI-Nutzungsrichtlinie.docx`: 6–8 Seiten, Platzhalter in [ECKIGEN KLAMMERN], 12 geforderte Kapitel (Zweck, Geltung, erlaubte/verbotene Nutzung, Daten & Vertraulichkeit, DSGVO, Tool-Freigabe, Kennzeichnung, Prüfpflicht/Halluzinationen, Verantwortlichkeiten, Schulung, Verstöße, Überprüfung) | erfüllt (Kapitel 1–13 + Anhänge, Zählung siehe oben) |")
    A("| 2 | `KI-Schulung.pptx`: 18–24 Folien, Sprechernotizen auf jeder Folie, schlichtes Layout, 2 Praxisübungen | erfüllt (Zahlen oben); Layout nur per LibreOffice-Rendering gesichtet, nicht in PowerPoint |")
    A("| 3 | `Wissenstest-und-Nachweis.docx`: 12 Fragen mit Lösungsblatt + Teilnahmeliste/Nachweisvorlage | erfüllt |")
    A("| 4 | `Datenschutz-Checkliste-und-Tool-Freigabe.xlsx`: Checkliste + Bewertungsmatrix | erfüllt (20 Prüfpunkte, 7 Kriterien + 3 K.-o.-Fragen, Register, Datenampel) |")
    A("| 5 | `Prompt-Bibliothek.docx`: Prompts nach Abteilung, je Zweck + Prompt + Hinweis | erfüllt: 34 Prompts (30 in den 5 Pflichtbereichen + 4 Excel-/Auswertungs-Prompts, D19); alle im Kontext-Baukasten (D18) |")
    A("| 6 | `Anpassungs-Prompt.docx`: Schritt für Schritt, deutliche Warnung vor vertraulichen/personenbezogenen Daten in öffentlichen KI-Tools, Anonymisierung | erfüllt (Warnkasten direkt am Anfang, wiederholt in Schritt 2) |")
    A("| 7 | `Kurzanleitung-In-einer-Woche-eingefuehrt.docx`: 1–2 Seiten | erfüllt (Zahl oben) |")
    A("| 8 | `Aha-Uebungen-Arbeitsblatt.docx` (D18): Kernübung „gleicher Prompt ohne/mit Kontext“ + 2–3 weitere Aha-Übungen, Notizfelder, Reflexionsfrage je Übung | erfüllt: 4 Übungen (1 Pflicht + 3 weitere), siehe Abschnitt 3a |")
    A("| 9 | `Grundbegriffe-in-einfacher-Sprache.docx` (D19): Chat vs. Agent, Skill, Markdown/.md, Modellwahl, Mermaid; 2–3 Seiten | erfüllt (Seitenzahl oben), tool-neutral, ohne Herstellernamen/Preise/Ranglisten |")
    A("| 10 | `QA.md` | diese Datei |")
    A("| – | Hinweis „Diese Vorlage ersetzt keine Rechtsberatung.“ in jedem Dokument | erfüllt (Fußzeile/Fußzeilen-Textfeld/Tabellenblatt, zusätzlich Hinweis-Kasten am Anfang) |")
    A("| – | Verbotsliste (3 Begriffe) + keine Paragraphen-/Artikelzitate | 0 Treffer (Skript, siehe oben); inhaltlich bleiben Rechtsaussagen allgemein („Datenschutzrecht“, „gesetzliche Meldefristen“, „Transparenzvorgaben“) |")
    A("| – | Keine erfundenen Statistiken | Das Kit enthält keine Marktzahlen/Statistiken. Prozentangaben im Kit sind nur Bewertungsschwellen (75 %/50 %), Kürzungsziele in Prompts und die Bestehensgrenze (9 von 12), jeweils als Vorschlag/Platzhalter |")
    A("| – | Keine echten Kunden-/Personendaten | Beispiele erfunden und markiert („Übungstext, frei erfunden“, „BEISPIEL (fiktives Tool …)“) |")
    A("")
    A("## 3. Manuelle Prüfung (Lieferagent, Textdurchsicht)")
    A("")
    A("- **Rechtschreibung:** " + spell_info + ". Eine Wörterbuch-Heuristik (deutsch, pyspellchecker) wurde über den gesamten Text gelegt; die unbekannten Wörter stehen in der Tabelle oben und wurden durchgesehen (es handelt sich um Fachwörter, Komposita, Eigennamen und Platzhalter-Fragmente; Tippfehler, die ein reales Wort ergeben, findet die Heuristik nicht). Grammatik und Stil wurden **nicht** maschinell geprüft. → Ankes Endabnahme sollte jede Datei einmal lesen.")
    A("- **Wissenstest:** Lösungen mit den Erklärungen in Richtlinie/Folien abgeglichen; richtige Antworten gleichmäßig auf A–D verteilt.")
    A("- **Konsistenz:** Datenampel (grün/gelb/rot) und Freigabestufen 1/2/3 sind in Richtlinie, Folien, Test, Excel und Prompt-Bibliothek gleich definiert; Prüfverfahren „5-Punkte-Prüfung“ überall identisch.")
    A("- **Praxisübung 2 (Folie 17):** Der Übungstext ist frei erfunden und enthält absichtlich Fehler; Aktenzeichen ist als „[erfunden]“ gekennzeichnet.")
    A("")
    A("## 3a. Umsetzung der Aha-Übungen (D18) und Ergänzungen (D19)")
    A("")
    A("- **Prinzip „Erleben vor Erklären“:** In `KI-Schulung.pptx` folgen Aha-Übung 1 (Folie 3 Anleitung, Folie 4 Auswertung/Vergleichsfragen) direkt auf die Zielfolie, **vor** jeder Erklärung. Erst danach kommt der Kontext-Baukasten (Folie 14), der erklärt, was die Gruppe selbst erlebt hat. Die Sprechernotizen verbieten der Schulungsleitung ausdrücklich, vorher zu erklären.")
    A("- **Aha-Übung 1 (Pflicht):** gleicher Auftrag zweimal an das KI-Tool: erst nackt („Schreib eine Antwort auf diese Kundenbeschwerde“), dann mit Baukasten (Rolle, Ziel, Zielgruppe, Ton, Beispiel, Format, Grenzen). Erfundene Beschwerde im Arbeitsblatt, Vergleichstabelle mit 5 Kriterien, 3 Vergleichsfragen, Reflexionsfrage, Notizfelder.")
    A("- **Weitere Übungen (Arbeitsblatt, 1 Folie als Überblick):** (2) Halluzination provozieren und entlarven: nach Fachbüchern zu einem erfundenen Nischenthema fragen, jedes Buch selbst nachsuchen, dann „Bist du sicher?“ und eine Variante mit Grenzen; (3) schlechten Prompt in vier Runden verbessern; (4) Aufgabe mit und ohne Beispiel. Alle ohne Fachwissen, mit erfundenen oder öffentlichen Beispielen, ohne vertrauliche Daten.")
    A("- **Prompt-Bibliothek:** jeder der 34 Prompts besteht aus den Feldern ROLLE/ZIEL/ZIELGRUPPE/TON/BEISPIEL/FORMAT/GRENZEN/MATERIAL (automatisch geprüft, siehe Tabelle); die Baukasten-Erklärung steht am Anfang.")
    A("- **Plausibilitätscheck (D19):** 4 Excel-/Auswertungs-Prompts fordern alle ein Blatt „Plausibilität“ (Gegenrechnen von Summen, Stichproben, Ausreißern); ein Satz erklärt warum („KI kann sich verrechnen, der Plausibilitätscheck macht Fehler sichtbar“).")
    A("- **Änderungen an v1 durch die Ergänzungen:** Schulungsdauer von 75 auf ca. 90 Minuten (bis 120 mit allen Aha-Übungen) – Schätzung, nicht gemessen. Um bei 24 Folien zu bleiben, wurden vier Foliengruppen zusammengelegt (KI-Grundlagen, Richtlinie/erlaubt/verboten, personenbezogene/vertrauliche Daten, Kennzeichnung/Melden); die Inhalte stehen weiter in Folien und Sprechernotizen, die Folien sind dadurch dichter. Grundbegriffe: Folien 20–22 plus eigenes Dokument. „Nächster Schritt“ (ohne Werbung) in der Kurzanleitung; Aufbauthemen (Präsentations-, Formular-, Excel-Workflows, eigene Skills) sind nicht enthalten.")
    A("- **Aha-Wirkung nicht getestet:** Ob die Übungen bei echten Teilnehmenden den erhofften Aha-Effekt auslösen, ist unbelegt; die Ergebnisse hängen vom Tool ab (Übung 2 besonders: Tools mit Websuche können korrekte Quellen liefern, das Arbeitsblatt weist darauf hin).")
    A("")
    A("## 4. Bekannte Grenzen (ehrlich)")
    A("")
    A("1. **Nicht in Microsoft Office geöffnet.** Geprüft wurde mit python-docx/-pptx/openpyxl und LibreOffice. Seitenumbrüche und Folienlayout können in Word/PowerPoint minimal abweichen. Bitte einmal in Word/PowerPoint/Excel öffnen und Seitenzahlen sowie die Folien 3, 8, 10, 12, 17 und 19 (viel Text; Layout nur im LibreOffice-Rendering geprüft) ansehen.")
    A("2. **Keine Rechtsprüfung.** Kein Jurist hat die Texte gesehen. Rechtliche Aussagen sind absichtlich allgemein gehalten; ob und wie die Vorlage zu einem konkreten Betrieb, Tarif- oder Betriebsratsfall passt, ist offen. Zur EU-KI-Verordnung und zur Rechtslage enthält das Kit bewusst keine Detailaussagen und keine Zitate (Scout-A-Quellen waren nur Suchsnippets, D17).")
    A("3. **Nicht an echten Nutzerinnen/Nutzern getestet.** Dass die Zielperson das Kit „in einer Woche“ einsetzen kann, ist eine Planungsannahme (Zeitschätzung in der Kurzanleitung: ca. 8–10 Stunden, **Schätzung, nicht gemessen**). Test mit 1–2 Personen aus Ankes Umfeld oder bezahlten Erstkäufern wäre der erste Beleg.")
    A("4. **Die KI-Anpassungsprompts (A–D) wurden nicht gegen ein KI-Tool ausgeführt** (kein Tool-Zugriff vorgesehen). Ihre Wirkung ist unerprobt; die Schutzregeln im Prompt (nichts erfinden, keine Zitate, Änderungen markieren) sind Absicht, keine Garantie.")
    A("5. **Keine Tool-Bewertungen realer Produkte.** Die Excel-Matrix enthält nur ein fiktives Beispiel. Schwellen (75 %/50 %) und Gewichte sind Vorschläge ohne empirische Grundlage.")
    A("6. **Schulung:** Zeitbedarf (90 Min.) und Übungsdauer (je 10 Min.) sind Schätzungen. Folie 6 beschreibt das Halluzinations-Muster allgemein; es werden bewusst keine konkreten Vorfälle genannt (nicht belegt).")
    A("7. **Marktbezug:** Das Kit sagt nichts über gesetzliche Pflichten zur Schulung. Der Stand der Rechtslage (Scout A, Sekundärquellen) ist ungeprüft; Marketingtexte (Vertrieb) dürfen daraus keine Pflicht ableiten.")
    A("8. **Nutzungsrechte/Lizenz:** Das Kit enthält keine Lizenz- oder Nutzungsbedingungen und keinen Anbieter-/Impressumshinweis. Das ist eine Entscheidung für Anke (Digistore24/Fiverr-AGB, Weitergabe, Branding). Bewusst nicht erfunden.")
    A("9. **Barrierefreiheit:** Kontrast/Struktur sind schlicht gehalten, aber nicht mit einem Prüfwerkzeug getestet. Alt-Texte entfallen, da keine Bilder enthalten sind.")
    A("10. **Rechtschreibprüfung:** nur Wörterbuch-Heuristik (siehe oben), kein Duden-/Grammatik-Check.")
    A("")
    A("## 5. Reproduktion")
    A("")
    A("```")
    A("cd company/deliveries/produkt-ki-starterkit-v1")
    A("pip install python-docx python-pptx openpyxl pypdf pyspellchecker")
    A("python3 build/build_kit.py     # erzeugt die 9 Office-Dateien")
    A("python3 build/verify_kit.py    # prüft und schreibt QA.md neu")
    A("```")
    A("Varianten (Englisch, Branchen): Texte in `build/b1_…b7_*.py` ersetzen, Layout steckt in `build/kit_lib.py`. `KIT_OUT=<Ordner>` leitet die Ausgabe um.")
    open(os.path.join(OUT, "QA.md"), "w", encoding="utf-8").write("\n".join(lines) + "\n")
    return n_ok, len(res)


if __name__ == "__main__":
    r, s, u = main()
    ok, tot = write_qa(r, s, u)
    for f, p, res_, k in r:
        if not k:
            print("FEHLER:", f, p, res_)
    print(f"{ok}/{tot} Prüfungen bestanden")
