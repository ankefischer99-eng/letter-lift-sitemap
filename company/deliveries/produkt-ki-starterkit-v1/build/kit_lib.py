"""Gemeinsame Hilfsfunktionen für das KI-Starterkit (DOCX/PPTX/XLSX).

Alle Texte stehen in build_kit.py; hier nur Layout-Logik, damit Varianten
(Englisch, Branchen) nur die Inhalte austauschen müssen.
"""
from docx import Document
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_BREAK
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor

DISCLAIMER = "Diese Vorlage ersetzt keine Rechtsberatung."
KIT_NAME = "KI-Starterkit für kleine Unternehmen"
VERSION = "Version 1.0 · Stand 05.11.2026"

DARK = RGBColor(0x1F, 0x3A, 0x5F)
GREY = RGBColor(0x55, 0x55, 0x55)
HEAD_FILL = "1F3A5F"
SOFT_FILL = "EAF0F7"
WARN_FILL = "FDECEA"
NOTE_FILL = "FFF6DD"
GREEN_FILL = "DFF2E1"
YELLOW_FILL = "FFF1C2"
RED_FILL = "F8D4D0"


def _shade(cell, hex_fill):
    tc_pr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), hex_fill)
    tc_pr.append(shd)


def _set_lang(style, lang="de-DE"):
    rpr = style.element.get_or_add_rPr()
    for el in rpr.findall(qn("w:lang")):
        rpr.remove(el)
    lang_el = OxmlElement("w:lang")
    lang_el.set(qn("w:val"), lang)
    lang_el.set(qn("w:eastAsia"), lang)
    rpr.append(lang_el)


def _add_field(paragraph, instr):
    run = paragraph.add_run()
    for kind, text in (("begin", None), (None, instr), ("end", None)):
        if kind:
            el = OxmlElement("w:fldChar")
            el.set(qn("w:fldCharType"), kind)
        else:
            el = OxmlElement("w:instrText")
            el.set(qn("xml:space"), "preserve")
            el.text = text
        run._r.append(el)
    run.font.size = Pt(8)
    run.font.color.rgb = GREY


class Doc:
    """Dünne Hülle um python-docx mit festem Layout."""

    def __init__(self, title, subtitle, footer_name):
        self.d = Document()
        sec = self.d.sections[0]
        sec.page_width, sec.page_height = Cm(21.0), Cm(29.7)
        sec.left_margin = sec.right_margin = Cm(2.3)
        sec.top_margin, sec.bottom_margin = Cm(2.0), Cm(2.0)
        st = self.d.styles
        st["Normal"].font.name = "Calibri"
        st["Normal"].font.size = Pt(11)
        st["Normal"].paragraph_format.space_after = Pt(6)
        st["Normal"].paragraph_format.line_spacing = 1.1
        _set_lang(st["Normal"])
        for name, size in (("Heading 1", 16), ("Heading 2", 13), ("Heading 3", 11.5)):
            s = st[name]
            s.font.name = "Calibri"
            s.font.size = Pt(size)
            s.font.bold = True
            s.font.color.rgb = DARK
            s.paragraph_format.space_before = Pt(14 if name == "Heading 1" else 10)
            s.paragraph_format.space_after = Pt(4)
            s.paragraph_format.keep_with_next = True
        for name in ("List Bullet", "List Number"):
            st[name].font.name = "Calibri"
            st[name].font.size = Pt(11)
            st[name].paragraph_format.space_after = Pt(3)
        # Fußzeile
        fp = sec.footer.paragraphs[0]
        r = fp.add_run(f"{DISCLAIMER} · {KIT_NAME} · {footer_name} · Seite ")
        r.font.size = Pt(8)
        r.font.color.rgb = GREY
        _add_field(fp, "PAGE")
        # Titelblock
        t = self.d.add_paragraph()
        tr = t.add_run(title)
        tr.bold = True
        tr.font.size = Pt(24)
        tr.font.color.rgb = DARK
        t.paragraph_format.space_after = Pt(2)
        s = self.d.add_paragraph()
        sr = s.add_run(subtitle)
        sr.font.size = Pt(12)
        sr.font.color.rgb = GREY
        v = self.d.add_paragraph()
        vr = v.add_run(VERSION)
        vr.font.size = Pt(9)
        vr.font.color.rgb = GREY

    # --- Bausteine -------------------------------------------------------
    def h1(self, text):
        return self.d.add_heading(text, level=1)

    def h2(self, text):
        return self.d.add_heading(text, level=2)

    def h3(self, text):
        return self.d.add_heading(text, level=3)

    def p(self, text="", bold=False, italic=False, size=None, color=None, after=None):
        para = self.d.add_paragraph()
        self._runs(para, text, bold, italic, size, color)
        if after is not None:
            para.paragraph_format.space_after = Pt(after)
        return para

    @staticmethod
    def _runs(para, text, bold=False, italic=False, size=None, color=None):
        """Unterstützt **fett** innerhalb von Text."""
        parts = text.split("**")
        for i, part in enumerate(parts):
            if not part:
                continue
            run = para.add_run(part)
            run.bold = bold or (i % 2 == 1)
            run.italic = italic
            if size:
                run.font.size = Pt(size)
            if color:
                run.font.color.rgb = color

    def bullets(self, items):
        for it in items:
            para = self.d.add_paragraph(style="List Bullet")
            self._runs(para, it)

    def numbered(self, items):
        # eigene Nummerierung (robust, keine Listen-Fortsetzungsprobleme)
        for i, it in enumerate(items, 1):
            para = self.d.add_paragraph()
            para.paragraph_format.left_indent = Cm(0.9)
            para.paragraph_format.first_line_indent = Cm(-0.6)
            para.paragraph_format.space_after = Pt(3)
            self._runs(para, f"{i}.  {it}")

    def table(self, header, rows, widths=None, fills=None, size=10, header_fill=HEAD_FILL):
        tbl = self.d.add_table(rows=1, cols=len(header))
        tbl.style = "Table Grid"
        tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
        for i, h in enumerate(header):
            c = tbl.rows[0].cells[i]
            c.text = ""
            run = c.paragraphs[0].add_run(h)
            run.bold = True
            run.font.size = Pt(size)
            run.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
            _shade(c, header_fill)
        # Kopfzeile bei Seitenumbruch wiederholen
        trpr = tbl.rows[0]._tr.get_or_add_trPr()
        th = OxmlElement("w:tblHeader")
        th.set(qn("w:val"), "true")
        trpr.append(th)
        for ri, row in enumerate(rows):
            cells = tbl.add_row().cells
            for ci, val in enumerate(row):
                cells[ci].text = ""
                para = cells[ci].paragraphs[0]
                para.paragraph_format.space_after = Pt(2)
                lines = str(val).split("\n")
                for li, line in enumerate(lines):
                    if li:
                        para = cells[ci].add_paragraph()
                        para.paragraph_format.space_after = Pt(2)
                    self._runs(para, line, size=size)
                if fills and fills.get((ri, ci)):
                    _shade(cells[ci], fills[(ri, ci)])
            # Zeilen nicht zerreißen
            trpr = tbl.rows[-1]._tr.get_or_add_trPr()
            cs = OxmlElement("w:cantSplit")
            cs.set(qn("w:val"), "true")
            trpr.append(cs)
        if widths:
            tbl.autofit = False
            for i, w in enumerate(widths):
                tbl.columns[i].width = Cm(w)
            for row in tbl.rows:
                for i, w in enumerate(widths):
                    row.cells[i].width = Cm(w)
        self.d.add_paragraph().paragraph_format.space_after = Pt(2)
        return tbl

    def callout(self, title, lines, fill=NOTE_FILL):
        tbl = self.d.add_table(rows=1, cols=1)
        tbl.style = "Table Grid"
        tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
        c = tbl.rows[0].cells[0]
        _shade(c, fill)
        c.text = ""
        para = c.paragraphs[0]
        run = para.add_run(title)
        run.bold = True
        run.font.size = Pt(11)
        for line in lines:
            q = c.add_paragraph()
            q.paragraph_format.space_after = Pt(2)
            self._runs(q, line, size=10.5)
        self.d.add_paragraph().paragraph_format.space_after = Pt(2)

    def disclaimer_box(self):
        self.callout(
            "Hinweis",
            [
                f"**{DISCLAIMER}** Die Inhalte sind allgemeine Orientierung für kleine Unternehmen. "
                "Sie berücksichtigen Ihre konkrete Situation, Branche und Verträge nicht. "
                "Bei rechtlichen Fragen wenden Sie sich an eine Rechtsanwältin, einen Rechtsanwalt "
                "oder Ihre Datenschutzbeauftragte bzw. Ihren Datenschutzbeauftragten."
            ],
        )

    def page_break(self):
        self.d.add_paragraph().add_run().add_break(WD_BREAK.PAGE)

    def save(self, path):
        self.d.save(path)
