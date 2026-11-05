from openpyxl import Workbook
from openpyxl.formatting.rule import CellIsRule, FormulaRule
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation
from kit_lib import DISCLAIMER, KIT_NAME, VERSION

FILE = "Datenschutz-Checkliste-und-Tool-Freigabe.xlsx"
HEAD = PatternFill("solid", fgColor="1F3A5F")
SOFT = PatternFill("solid", fgColor="EAF0F7")
INPUT = PatternFill("solid", fgColor="FFF6DD")
GREEN = PatternFill("solid", bgColor="DFF2E1", fgColor="DFF2E1")
YELLOW = PatternFill("solid", bgColor="FFF1C2", fgColor="FFF1C2")
RED = PatternFill("solid", bgColor="F8D4D0", fgColor="F8D4D0")
thin = Side(style="thin", color="BBBBBB")
BORDER = Border(left=thin, right=thin, top=thin, bottom=thin)
WRAP = Alignment(wrap_text=True, vertical="top")

CHECKLIST = [
    ("A. Zweck und Einsatz", "A1", "Der Einsatzzweck ist in einem Satz beschrieben.", "Wofür genau soll das Tool genutzt werden? Ohne klaren Zweck keine Freigabe."),
    ("A. Zweck und Einsatz", "A2", "Es ist festgelegt, welche Datenstufen (grün/gelb/rot) eingegeben werden dürfen.", "Siehe Datenampel in der Richtlinie. Voreinstellung: nur grün."),
    ("A. Zweck und Einsatz", "A3", "Der Nutzerkreis ist festgelegt (Abteilungen/Rollen).", "Nicht jede Funktion braucht jedes Tool."),
    ("A. Zweck und Einsatz", "A4", "Der Einsatz betrifft KEINE Entscheidungen über Menschen (Bewerbung, Bewertung, Kündigung, Bonität).", "Falls doch: vor Start Prüfung durch [NAME/Funktion] und fachlichen Rat einholen."),
    ("B. Anbieter und Vertrag", "B1", "Anbieter, Firmensitz und Kontakt sind bekannt und dokumentiert.", "Impressum/Anbieterangaben prüfen."),
    ("B. Anbieter und Vertrag", "B2", "Nutzungsbedingungen und Datenschutzerklärung wurden gelesen und das Datum der Fassung notiert.", "Änderungen später erneut prüfen."),
    ("B. Anbieter und Vertrag", "B3", "Bei personenbezogenen Daten: Vertrag zur Auftragsverarbeitung ist verfügbar und abgeschlossen.", "Ohne diesen Vertrag keine personenbezogenen Daten eingeben. Im Zweifel Datenschutzberatung fragen."),
    ("B. Anbieter und Vertrag", "B4", "Es ist geklärt, wo die Daten verarbeitet werden (Land/Region) und ob Übermittlungen außerhalb der EU stattfinden.", "Angaben des Anbieters dokumentieren; bei Unklarheit Datenschutzberatung."),
    ("B. Anbieter und Vertrag", "B5", "Es ist geklärt, ob Eingaben zum Training der Modelle genutzt werden – und ob sich das ausschalten oder vertraglich ausschließen lässt.", "Einstellungen prüfen und per Screenshot/Notiz dokumentieren."),
    ("C. Sicherheit und Zugang", "C1", "Zugang nur mit persönlichem Firmenkonto (kein geteiltes/privates Konto).", "Konten über [IT] einrichten."),
    ("C. Sicherheit und Zugang", "C2", "Zusätzliche Anmeldesicherheit (z. B. Zwei-Faktor) ist aktiv, falls angeboten.", ""),
    ("C. Sicherheit und Zugang", "C3", "Es gibt eine Möglichkeit, Verläufe/Eingaben zu löschen oder zu begrenzen.", "Aufbewahrungsdauer notieren."),
    ("C. Sicherheit und Zugang", "C4", "Admin-Einstellungen (Nutzerverwaltung, Freigaben) sind bekannt; Zuständigkeit ist geklärt.", ""),
    ("D. Datenschutz im Betrieb", "D1", "Das Verzeichnis der Verarbeitungstätigkeiten ist ergänzt (falls zutreffend).", "Zuständig: [Datenschutz]."),
    ("D. Datenschutz im Betrieb", "D2", "Datenschutzhinweise für Kunden/Beschäftigte sind angepasst (falls zutreffend).", ""),
    ("D. Datenschutz im Betrieb", "D3", "Die Folgen für Betroffenenrechte (Auskunft, Löschung) sind bedacht.", "Eingegebene Personendaten lassen sich oft schwer zurückholen."),
    ("D. Datenschutz im Betrieb", "D4", "Bei Beschäftigtendaten: Betriebsrat/Mitbestimmung geklärt (falls vorhanden).", "Mit Rechtsberatung abstimmen."),
    ("E. Einführung", "E1", "Beschäftigte sind geschult (Teilnahme dokumentiert).", "Siehe Wissenstest und Nachweis."),
    ("E. Einführung", "E2", "Das Tool ist in der Freigabeliste (Anhang A der Richtlinie) mit Stufe und Auflagen eingetragen.", ""),
    ("E. Einführung", "E3", "Termin für die Neuprüfung ist eingetragen.", "Mindestens jährlich."),
]

CRITERIA = [  # (Name, Gewicht, Erklärung)
    ("Transparenz (Datenschutzerklärung, Doku)", 3, "0 = unklar/lückenhaft · 1 = teils klar · 2 = klar und verständlich"),
    ("Datenverarbeitung/Standort geklärt", 3, "0 = unbekannt · 1 = teils bekannt · 2 = dokumentiert und akzeptabel"),
    ("Zugriffsschutz (Konten, 2-Faktor)", 2, "0 = nur geteilte Konten · 1 = persönliche Konten · 2 = persönliche Konten + zusätzliche Sicherung"),
    ("Löschen von Verläufen/Eingaben", 2, "0 = nicht möglich · 1 = teilweise · 2 = jederzeit möglich/steuerbar"),
    ("Admin- und Rechteverwaltung", 2, "0 = keine · 1 = einfach · 2 = Rollen/Freigaben steuerbar"),
    ("Reife des Anbieters (Support, Doku, Updates)", 1, "0 = kaum · 1 = ausreichend · 2 = gut"),
    ("Nutzen im Verhältnis zu den Kosten", 1, "0 = gering · 1 = ok · 2 = hoch"),
]

KO = [
    "K1: Vertrag zur Auftragsverarbeitung verfügbar? (nur nötig, wenn personenbezogene Daten verarbeitet werden sollen)",
    "K2: Training mit unseren Eingaben ausschließbar?",
    "K3: Verarbeitung/Standort vom Anbieter nachvollziehbar angegeben?",
]


def _hdr(ws, row, values, widths=None):
    for i, v in enumerate(values, 1):
        c = ws.cell(row=row, column=i, value=v)
        c.font = Font(bold=True, color="FFFFFF")
        c.fill = HEAD
        c.alignment = Alignment(wrap_text=True, vertical="center")
        c.border = BORDER


def _title(ws, title, sub=None):
    ws["A1"] = title
    ws["A1"].font = Font(bold=True, size=16, color="1F3A5F")
    ws["A2"] = f"{DISCLAIMER}  ·  {KIT_NAME}  ·  {VERSION}"
    ws["A2"].font = Font(italic=True, size=9, color="555555")
    if sub:
        ws["A3"] = sub
        ws["A3"].alignment = Alignment(wrap_text=True, vertical="top")


def build(outdir):
    wb = Workbook()

    # ---------------- Anleitung ----------------
    ws = wb.active
    ws.title = "Anleitung"
    _title(ws, "Datenschutz-Checkliste und Tool-Freigabe")
    lines = [
        ("Wofür ist diese Datei?", "Sie hilft Ihnen, ein KI-Tool vor der Nutzung strukturiert zu prüfen und die Entscheidung zu dokumentieren. Sie ist ein Arbeitsmittel, kein Rechtsgutachten. " + DISCLAIMER),
        ("Blatt „Checkliste“", "Pro Tool einmal ausfüllen (Kopie des Blatts anlegen). Status je Zeile wählen: Offen / Erledigt / Nicht zutreffend. Die Kennzahlen oben zeigen den Stand."),
        ("Blatt „Tool-Bewertung“", "Eine Zeile pro Tool. Zuerst die drei K.-o.-Fragen mit Ja/Nein/Unklar beantworten, dann die sieben Kriterien mit 0, 1 oder 2 bewerten. Die Spalten ganz rechts rechnen Punkte, Prozent und eine Empfehlung aus."),
        ("Wie wird die Empfehlung berechnet?", "1) Steht in einer K.-o.-Frage „Nein“ → „Nur grüne Daten“ (Stufe 1). 2) Steht dort „Unklar“ → „Erst klären“. 3) Sonst nach Prozent der möglichen Punkte: ab 75 % „Freigabe empfohlen“, 50–74 % „Freigabe mit Auflagen“, darunter „Nicht freigeben“. Die Schwellen (75 %/50 %) sind Vorschläge und stehen in den Zellen auf dem Blatt „Tool-Bewertung“; Sie können sie ändern."),
        ("Wichtig", "Die Empfehlung ersetzt nicht die Entscheidung. Entscheiden müssen Menschen ([Freigabestelle]). Rote Daten (personenbezogen/vertraulich) nur in Tools der Stufe 3, nach Prüfung durch [Datenschutz]. Die Bewertungen müssen Sie selbst anhand der Anbieterangaben vornehmen – die Datei enthält keine Bewertungen echter Produkte."),
        ("Blatt „Tool-Register“", "Hier tragen Sie freigegebene Tools mit Stufe, Zweck, Auflagen und Neuprüfungsdatum ein. Es entspricht Anhang A der Richtlinie. Die Spalte „Neuprüfung fällig?“ markiert überfällige Termine."),
        ("Blatt „Datenampel“", "Ihre Einstufung von Datenarten in grün/gelb/rot – Beispiele sind vorausgefüllt, bitte anpassen."),
        ("Gelbe Felder", "Gelb hinterlegte Felder sind zum Ausfüllen gedacht. Beispieleinträge sind als „BEISPIEL“ gekennzeichnet; bitte löschen."),
    ]
    r = 4
    for k, v in lines:
        ws.cell(row=r, column=1, value=k).font = Font(bold=True)
        c = ws.cell(row=r, column=2, value=v)
        c.alignment = WRAP
        ws.cell(row=r, column=1).alignment = WRAP
        ws.row_dimensions[r].height = max(30, 15 * (len(v) // 95 + 1))
        r += 1
    ws.column_dimensions["A"].width = 30
    ws.column_dimensions["B"].width = 110

    # ---------------- Checkliste ----------------
    cl = wb.create_sheet("Checkliste")
    _title(cl, "Datenschutz-Checkliste für ein KI-Tool")
    cl["A3"] = "Tool:"
    cl["B3"] = "[TOOLNAME]"
    cl["B3"].fill = INPUT
    cl["D3"] = "Geprüft von / am:"
    cl["E3"] = "[NAME, DATUM]"
    cl["E3"].fill = INPUT
    cl["A4"] = "Erledigt:"
    first, last = 8, 8 + len(CHECKLIST) - 1
    cl["B4"] = f'=COUNTIF(E{first}:E{last},"Erledigt")'
    cl["C4"] = "Offen:"
    cl["D4"] = f'=COUNTIF(E{first}:E{last},"Offen")'
    cl["E4"] = "Nicht zutreffend:"
    cl["F4"] = f'=COUNTIF(E{first}:E{last},"Nicht zutreffend")'
    cl["A5"] = "Fortschritt:"
    cl["B5"] = f'=IF(ROWS(E{first}:E{last})-F4=0,0,B4/(ROWS(E{first}:E{last})-F4))'
    cl["B5"].number_format = "0%"
    cl["C5"] = "Alle offenen Punkte erledigt?"
    cl["F5"] = f'=IF(D4=0,"Ja","Nein")'
    for a in ("A3", "A4", "A5", "D3", "C4", "E4", "C5"):
        cl[a].font = Font(bold=True)
    _hdr(cl, 7, ["Bereich", "Nr.", "Prüfpunkt", "Hinweis", "Status", "Verantwortlich", "Datum", "Bemerkung"])
    for i, (area, nr, text, hint) in enumerate(CHECKLIST):
        row = first + i
        vals = [area, nr, text, hint, "Offen", "", "", ""]
        for j, v in enumerate(vals, 1):
            c = cl.cell(row=row, column=j, value=v)
            c.alignment = WRAP
            c.border = BORDER
            if j >= 5:
                c.fill = INPUT
        cl.row_dimensions[row].height = 48
    dv = DataValidation(type="list", formula1='"Offen,Erledigt,Nicht zutreffend"', allow_blank=False)
    cl.add_data_validation(dv)
    dv.add(f"E{first}:E{last}")
    cl.conditional_formatting.add(f"E{first}:E{last}", CellIsRule(operator="equal", formula=['"Erledigt"'], fill=GREEN))
    cl.conditional_formatting.add(f"E{first}:E{last}", CellIsRule(operator="equal", formula=['"Offen"'], fill=YELLOW))
    for col, w in zip("ABCDEFGH", (22, 6, 60, 46, 17, 16, 12, 30)):
        cl.column_dimensions[col].width = w
    cl.freeze_panes = "A8"

    # ---------------- Tool-Bewertung ----------------
    tb = wb.create_sheet("Tool-Bewertung")
    _title(tb, "Bewertungsmatrix für KI-Tools")
    tb["A3"] = "Schwelle „Freigabe empfohlen“ (Anteil):"
    tb["D3"] = 0.75
    tb["A4"] = "Schwelle „Freigabe mit Auflagen“ (Anteil):"
    tb["D4"] = 0.5
    for a in ("D3", "D4"):
        tb[a].number_format = "0%"
        tb[a].fill = INPUT
    for a in ("A3", "A4"):
        tb[a].font = Font(bold=True)
    # Kopf: Tool | K1 K2 K3 | 7 Kriterien | Punkte | max | Prozent | Empfehlung | Bemerkung
    ncols_ko = len(KO)
    c_ko1 = 2
    c_cr1 = c_ko1 + ncols_ko
    c_pts = c_cr1 + len(CRITERIA)
    c_max, c_pct, c_rec, c_note = c_pts + 1, c_pts + 2, c_pts + 3, c_pts + 4
    hdr_row, w_row, first_t = 7, 6, 8
    names = ["Tool (Name/Version)"] + [k.split(":")[0] for k in KO] + [c[0] for c in CRITERIA] + ["Punkte", "Max.", "Anteil", "Empfehlung", "Bemerkung"]
    _hdr(tb, hdr_row, names)
    tb.row_dimensions[hdr_row].height = 62
    tb.cell(row=w_row, column=1, value="Gewicht (1–3) →").font = Font(bold=True)
    for i, (_, wt, _) in enumerate(CRITERIA):
        c = tb.cell(row=w_row, column=c_cr1 + i, value=wt)
        c.fill = INPUT
        c.alignment = Alignment(horizontal="center")
        c.border = BORDER
    n_rows = 12
    last_t = first_t + n_rows - 1
    cr1, crN = get_column_letter(c_cr1), get_column_letter(c_cr1 + len(CRITERIA) - 1)
    ko1, koN = get_column_letter(c_ko1), get_column_letter(c_ko1 + ncols_ko - 1)
    for r in range(first_t, last_t + 1):
        for cidx in range(1, c_note + 1):
            c = tb.cell(row=r, column=cidx)
            c.border = BORDER
            c.alignment = WRAP if cidx in (1, c_note, c_rec) else Alignment(horizontal="center", vertical="top")
            if cidx < c_pts or cidx == c_note:
                c.fill = INPUT
        pts = f"=IF($A{r}=\"\",\"\",SUMPRODUCT(${cr1}${w_row}:${crN}${w_row},{cr1}{r}:{crN}{r}))"
        tb.cell(row=r, column=c_pts, value=pts)
        mx = f"=IF($A{r}=\"\",\"\",2*SUM(${cr1}${w_row}:${crN}${w_row}))"
        tb.cell(row=r, column=c_max, value=mx)
        pc = get_column_letter(c_pts)
        mc = get_column_letter(c_max)
        pct = f"=IF($A{r}=\"\",\"\",IF({mc}{r}=0,0,{pc}{r}/{mc}{r}))"
        tb.cell(row=r, column=c_pct, value=pct).number_format = "0%"
        prc = get_column_letter(c_pct)
        # unvollständig bewertet? -> Hinweis
        rec = (
            f'=IF($A{r}="","",IF(COUNTA({ko1}{r}:{koN}{r})<{ncols_ko},"K.-o.-Fragen ausfüllen",'
            f'IF(COUNTIF({ko1}{r}:{koN}{r},"Nein")>0,"Nur grüne Daten (Stufe 1)",'
            f'IF(COUNTIF({ko1}{r}:{koN}{r},"Unklar")>0,"Erst klären",'
            f'IF(COUNT({cr1}{r}:{crN}{r})<{len(CRITERIA)},"Kriterien bewerten",'
            f'IF({prc}{r}>=$D$3,"Freigabe empfohlen",IF({prc}{r}>=$D$4,"Freigabe mit Auflagen","Nicht freigeben")))))))'
        )
        tb.cell(row=r, column=c_rec, value=rec)
    # Beispielzeile (fiktiv)
    ex = first_t
    tb.cell(row=ex, column=1, value="BEISPIEL (fiktives Tool, keine echte Bewertung) – bitte überschreiben")
    for i, v in enumerate(["Ja", "Ja", "Ja"]):
        tb.cell(row=ex, column=c_ko1 + i, value=v)
    for i, v in enumerate([2, 1, 2, 1, 1, 1, 2]):
        tb.cell(row=ex, column=c_cr1 + i, value=v)
    dvko = DataValidation(type="list", formula1='"Ja,Nein,Unklar"', allow_blank=True)
    dvsc = DataValidation(type="list", formula1='"0,1,2"', allow_blank=True)
    tb.add_data_validation(dvko)
    tb.add_data_validation(dvsc)
    dvko.add(f"{ko1}{first_t}:{koN}{last_t}")
    dvsc.add(f"{cr1}{first_t}:{crN}{last_t}")
    rc = get_column_letter(c_rec)
    rng = f"{rc}{first_t}:{rc}{last_t}"
    tb.conditional_formatting.add(rng, FormulaRule(formula=[f'{rc}{first_t}="Freigabe empfohlen"'], fill=GREEN))
    tb.conditional_formatting.add(rng, FormulaRule(formula=[f'{rc}{first_t}="Freigabe mit Auflagen"'], fill=YELLOW))
    tb.conditional_formatting.add(rng, FormulaRule(formula=[f'OR({rc}{first_t}="Nicht freigeben",{rc}{first_t}="Nur grüne Daten (Stufe 1)",{rc}{first_t}="Erst klären")'], fill=RED))
    # Legende
    lr = last_t + 2
    tb.cell(row=lr, column=1, value="K.-o.-Fragen").font = Font(bold=True)
    for i, k in enumerate(KO):
        tb.cell(row=lr + 1 + i, column=1, value=k)
    tb.cell(row=lr + 5, column=1, value="Bewertungsskala je Kriterium (0/1/2)").font = Font(bold=True)
    for i, (n, wt, ex_) in enumerate(CRITERIA):
        tb.cell(row=lr + 6 + i, column=1, value=f"{n}: {ex_}")
    tb.cell(row=lr + 14, column=1, value="Die Empfehlung ist eine Entscheidungshilfe. " + DISCLAIMER).font = Font(italic=True)
    tb.column_dimensions["A"].width = 44
    for ci in range(2, c_note + 1):
        tb.column_dimensions[get_column_letter(ci)].width = 16
    tb.column_dimensions[get_column_letter(c_rec)].width = 28
    tb.column_dimensions[get_column_letter(c_note)].width = 32
    tb.freeze_panes = f"B{first_t}"

    # ---------------- Tool-Register ----------------
    tr = wb.create_sheet("Tool-Register")
    _title(tr, "Register freigegebener KI-Tools (Anhang A der Richtlinie)")
    tr["A3"] = "Stand heute:"
    tr["B3"] = "=TODAY()"
    tr["B3"].number_format = "DD.MM.YYYY"
    _hdr(tr, 5, ["Tool / Version", "Stufe (1/2/3)", "Erlaubter Zweck", "Auflagen", "Freigegeben am", "Freigegeben von", "Neuprüfung bis", "Neuprüfung fällig?"])
    for r in range(6, 18):
        for ci in range(1, 9):
            c = tr.cell(row=r, column=ci)
            c.border = BORDER
            c.alignment = WRAP
            if ci < 8:
                c.fill = INPUT
        tr.cell(row=r, column=5).number_format = "DD.MM.YYYY"
        tr.cell(row=r, column=7).number_format = "DD.MM.YYYY"
        tr.cell(row=r, column=8, value=f'=IF(G{r}="","",IF(G{r}<$B$3,"FÄLLIG","ok"))')
    dvs = DataValidation(type="list", formula1='"1,2,3"', allow_blank=True)
    tr.add_data_validation(dvs)
    dvs.add("B6:B17")
    tr.conditional_formatting.add("H6:H17", CellIsRule(operator="equal", formula=['"FÄLLIG"'], fill=RED))
    tr["A19"] = "Stufe 1: nur grüne Daten · Stufe 2: grün + gelb · Stufe 3: zusätzlich rote Daten für einen festgelegten Zweck, nur nach Datenschutzprüfung."
    tr["A20"] = DISCLAIMER
    tr["A20"].font = Font(italic=True)
    for col, w in zip("ABCDEFGH", (28, 13, 36, 36, 16, 20, 16, 18)):
        tr.column_dimensions[col].width = w

    # ---------------- Datenampel ----------------
    da = wb.create_sheet("Datenampel")
    _title(da, "Datenampel: Einstufung typischer Daten")
    da["A3"] = "Beispiele zur Orientierung. Passen Sie die Einstufung an Ihren Betrieb an; im Zweifel die höhere Stufe wählen."
    _hdr(da, 5, ["Datenart", "Beispiel", "Stufe", "Darf in Tool-Stufe", "Hinweis"])
    rows = [
        ("Öffentliche Texte", "Veröffentlichter Newsletter, Webseitentext", "GRÜN", "1, 2, 3", "Nur freigegebene Tools"),
        ("Allgemeine Fragen", "„Erkläre mir, wie eine Pivot-Tabelle funktioniert“", "GRÜN", "1, 2, 3", ""),
        ("Interne Abläufe ohne Personenbezug", "Ablaufbeschreibung Urlaubsantrag ohne Namen", "GELB", "2, 3", ""),
        ("Entwürfe/Konzepte intern", "Konzeptentwurf ohne Kunden-/Personennamen", "GELB", "2, 3", "Vorher auf versteckte Namen/Metadaten prüfen"),
        ("Anonymisierte Beispiele", "Kundenanfrage mit „Kunde A“", "GELB", "2, 3", "Anonymisierung prüfen (Kombinationen!)"),
        ("Kundendaten", "Name, Adresse, E-Mail, Bestellnummer", "ROT", "3 (nur nach Prüfung)", "Sonst nur anonymisiert"),
        ("Beschwerden/Korrespondenz", "Kundenmail mit Name und Anliegen", "ROT", "3 (nur nach Prüfung)", "Sonst anonymisieren"),
        ("Bewerbungs- und Personaldaten", "Lebenslauf, Gehalt, Krankmeldung", "ROT", "3 (nur nach Prüfung)", "Auswahl-/Bewertungsentscheidungen nie allein durch KI"),
        ("Verträge und Kalkulationen", "Angebotskalkulation, Vertragsentwurf", "ROT", "3 (nur nach Prüfung)", ""),
        ("Zugangsdaten", "Passwörter, API-Schlüssel", "ROT", "nie", "Nie in KI-Tools"),
        ("[Ihre Datenart]", "", "[ ]", "", ""),
        ("[Ihre Datenart]", "", "[ ]", "", ""),
    ]
    for i, row in enumerate(rows):
        r = 6 + i
        for j, v in enumerate(row, 1):
            c = da.cell(row=r, column=j, value=v)
            c.alignment = WRAP
            c.border = BORDER
        da.cell(row=r, column=3).fill = {"GRÜN": GREEN, "GELB": YELLOW, "ROT": RED}.get(row[2], SOFT)
        da.cell(row=r, column=3).alignment = Alignment(horizontal="center", vertical="top")
    for col, w in zip("ABCDE", (32, 46, 10, 22, 44)):
        da.column_dimensions[col].width = w
    da[f"A{6 + len(rows) + 1}"] = DISCLAIMER
    da[f"A{6 + len(rows) + 1}"].font = Font(italic=True)

    for sheet in wb.worksheets:
        sheet.sheet_view.zoomScale = 100
        sheet.page_setup.orientation = "landscape"
        sheet.page_setup.fitToWidth = 1
        sheet.page_setup.fitToHeight = 0
        sheet.sheet_properties.pageSetUpPr.fitToPage = True
        sheet.oddFooter.center.text = DISCLAIMER
    wb.save(f"{outdir}/{FILE}")
    return FILE
