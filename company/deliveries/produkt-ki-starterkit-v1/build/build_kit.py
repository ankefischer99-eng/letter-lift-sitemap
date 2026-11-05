"""Erzeugt alle Dokumente des KI-Starterkits v1 in den übergeordneten Ordner.

Aufruf:  python3 build/build_kit.py            (aus dem Ordner produkt-ki-starterkit-v1)
Ausgabe: 7 Office-Dateien neben dem Ordner build/ (QA.md erzeugt verify_kit.py)
Varianten: Inhalte stehen in b1..b7; für EN/Branchen die Texte dort kopieren/ersetzen.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import b1_richtlinie, b2_schulung, b3_test, b4_xlsx, b5_prompts, b6_anpassung, b7_kurz  # noqa: E402

OUT = os.environ.get("KIT_OUT", os.path.dirname(HERE))

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for m in (b1_richtlinie, b2_schulung, b3_test, b4_xlsx, b5_prompts, b6_anpassung, b7_kurz):
        print("erzeugt:", m.build(OUT))
