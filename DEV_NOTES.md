# DEVELOPER NOTES 🤖

## Project Mission: OmniversifyFont

Developing a premium, open-source multilingual font for Latin, Arabic (Moroccan Maghrebi), and Tamazight (Tifinagh).

## Philosophy & Constraints

- **Core Value**: Strong support for Open Source. OmniversifyFont is an open-source project from its inception.
- **Platform**: Linux-first development environment.
- **Package Manager**: **Bun** (Required). We do not use npm or yarn.
- **Design Tools**:
  - **Inkscape**: For vector graphics and initial glyph design.
  - **FontForge**: For font assembly, kerning, and advanced typography work.
- **License**: Any added tools or libraries must be Open Source and Linux-friendly.

## Automated Agents Responsibilities

- Maintain a clean and modular directory structure.
- Prioritize performance and modern web standards.
- Ensure cross-script harmony in all aesthetic decisions.
- Follow the "Moroccan Luxury" design language.

## Recent Accomplishments (Arabic Mark Positioning)

- Integrated the **AutoMark** script (fontamin) to automatically add OpenType GPOS lookups for Arabic diacritics:
  - Added `top` and `bottom` anchors to Arabic base glyphs.
  - Added matching anchors to Arabic mark glyphs (fatḥa, kasra, ḍamma, sukūn, shadda, etc.).
  - Generated `mark` (Mark-to-Base) and `mkmk` (Mark-to-Mark) lookups.
- Generated hinted TrueType font using `gftools fix-hinting` (ttfautohint).
- Validated the font with Google Fonts requirements via `gftools`:
  - Passed OTS (OpenType Sanitizer).
  - Passed name table checks (required IDs present).
  - Confirmed language support for en, ar, zgh (Tifinagh).
  - Verified GPOS lookups for `mark` and `mkmk` features.
- Backup strategy:
  - Original source file renamed to `OmniversifyFont.sfd.backup`.
  - AutoMark-enhanced version becomes the main `OmniversifyFont.sfd`.

## Tools Used

- **FontForge** (v20251009) – primary font editor, used via CLI and GUI.
- **AutoMark** (https://github.com/fontamin/AutoMark) – FontForge Python script for automatic Arabic anchor placement and GPOS feature generation.
- **gftools** (v0.9.996) – Google Fonts validation toolkit (ots, fix-hinting, check-name, lang-support, find-features, metadata, etc.).
- **uv** (0.11.16) – fast Python package installer, used to create a isolated environment for gftools.
- **ttfautohint** (via gftools autohint) – hinting engine for improved rasterization.
- **Git** – version control; backed up original SFD before changes.
- **generate_formats.py** – custom FontForge Python script to batch‑export TTF, OTF, SVG, and UFO from the .sfd source.
