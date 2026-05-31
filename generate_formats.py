#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
generate_formats.py
-------------------
A FontForge scripting helper that converts a FontForge source file (.sfd)
into the four core distribution formats:

    • TrueType (.ttf)
    • OpenType (.otf)
    • SVG font (.svg)
    • UFO folder (.ufo)

Usage (from a terminal):
    fontforge -script generate_formats.py <input.sfd> <output_dir>

The script assumes FontForge is available in your PATH.
"""
import sys
import os

def main(argv):
    if len(argv) < 3:
        print("Usage: fontforge -script generate_formats.py <input.sfd> <output_dir>")
        sys.exit(1)

    input_sfd = argv[1]
    out_dir   = argv[2]

    # Make sure the output directory exists
    os.makedirs(out_dir, exist_ok=True)

    # -----------------------------------------------------------------
    # Load the source file
    # -----------------------------------------------------------------
    try:
        font = fontforge.open(input_sfd)
    except Exception as e:
        print(f"ERROR: Could not open '{input_sfd}': {e}")
        sys.exit(1)

    # -----------------------------------------------------------------
    # Optional: set a consistent font name (helps when the SFD
    #          does not already contain a proper PS/Full name)
    # -----------------------------------------------------------------
    # Uncomment and adjust if you want to enforce a name:
    # font.fontname = "OmniversifyMaghribFont"
    # font.fullname = "Omniversify Maghrib Font"
    # font.familyname = "Omniversify Maghrib"
    # font.weight = "Regular"

    # -----------------------------------------------------------------
    # Generate the four formats
    # -----------------------------------------------------------------
    base_name = "OmniversifyMaghribFont"   # you can change this if you like

    # TrueType
    ttf_path = os.path.join(out_dir, f"{base_name}.ttf")
    try:
        font.generate(ttf_path)
        print(f"Generated TTF: {ttf_path}")
    except Exception as e:
        print(f"WARNING: TTF generation failed: {e}")

    # OpenType (CFF outlines)
    otf_path = os.path.join(out_dir, f"{base_name}.otf")
    try:
        font.generate(otf_path)
        print(f"Generated OTF: {otf_path}")
    except Exception as e:
        print(f"WARNING: OTF generation failed: {e}")

    # SVG font (outline font in SVG format)
    svg_path = os.path.join(out_dir, f"{base_name}.svg")
    try:
        font.generate(svg_path)
        print(f"Generated SVG: {svg_path}")
    except Exception as e:
        print(f"WARNING: SVG generation failed: {e}")

    # UFO (unified font object – saved as a folder)
    ufo_path = os.path.join(out_dir, f"{base_name}.ufo")
    try:
        font.generate(ufo_path)
        print(f"Generated UFO folder: {ufo_path}")
    except Exception as e:
        print(f"WARNING: UFO generation failed: {e}")

    # -----------------------------------------------------------------
    # Clean up
    # -----------------------------------------------------------------
    font.close()
    print("\nAll done! 🎉")

if __name__ == "__main__":
    main(sys.argv)
