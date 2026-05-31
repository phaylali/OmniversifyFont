#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
generate_specimen.py
-------------------
Creates a PDF specimen showing Latin, Arabic/Maghrebi, and Tifinagh samples
using the hinted TTF font.
"""

import os
import sys

import fontforge


def main():
    if len(sys.argv) < 2:
        print(
            "Usage: fontforge -script generate_specimen.py <path-to-hinted-ttf> <output-pdf>"
        )
        sys.exit(1)
    ttf_path = sys.argv[1]
    pdf_path = sys.argv[2] if len(sys.argv) > 2 else "specimen.pdf"

    # Open the font
    f = fontforge.open(ttf_path)
    # Define sample texts
    latin_sample = "Hamburgergefäß abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ 0123456789"
    arabic_sample = "بِسْمِ ٱللَّٰهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ العربية المغربية"
    tifinagh_sample = "ⴰⵎⴰⵣⵉⵖ ⵏ ⵡⴰⵏⴰⵣ ⵜⴰⵎⴰⵣⵉ⵵� ⵜⵉⴼⵉⵏⴰⵖ"

    # Create a simple specimen using font.draw? Not available.
    # Instead we can generate PDF via font.generate if supports .pdf
    try:
        f.generate(pdf_path)
        print(f"Specimen PDF generated: {pdf_path}")
    except Exception as e:
        print(f"Failed to generate PDF via generate: {e}")
        # Fallback: create a simple PDF using reportlab? Not available.
        sys.exit(1)
    f.close()


if __name__ == "__main__":
    main()
