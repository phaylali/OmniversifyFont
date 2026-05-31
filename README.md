# OmniversifyFont 🖋️

### 💪🏻 **_THE Font For Every Moroccan_**

**OmniversifyFont** is a modern multilingual typeface designed to bridge cultures and scripts. It uniquely combines **Latin (English)**, **Arabic (Moroccan/Maghrebi script)**, and **Tamazight (Tifinagh script)** into a cohesive, high-performance font family.

Inspired by the rich architectural and calligraphic heritage of Morocco, OmniversifyFont brings a "Moroccan Luxury" aesthetic to digital typography, ensuring legibility and elegance across diverse linguistic landscapes.

---

## 🌍 Supported Scripts

OmniversifyFont is built on the philosophy of universal connectivity:

### 🇦🔤 Latin (English)

Modern, clean, and highly legible. Designed to complement the organic flow of Arabic and the geometric precision of Tifinagh.

### 🇲🇦 Arabic (Moroccan Maghrebi)

Dedicated to the traditional Moroccan Maghrebi script, characterized by its distinctive roundness and unique diacritic placements, optimized for modern digital displays without losing its calligraphic soul.

### ⵣ Tamazight (Tifinagh)

Honoring the ancestral script of North Africa. The Tifinagh characters are designed with a balance of geometric tradition and modern clarity, making it suitable for both headlines and body text.

---

## ✨ Key Features

- **Harmonious Multi-script Design**: Consistent weight and optical balance across all three scripts.
- **Moroccan Aesthetic**: Subtle nods to Moroccan artistry and geometry.
- **Modern Performance**: Optimized for web, mobile, and print applications.
- **OpenType Support**: Advanced features for ligature handling and script switching.

---

## 🛠 Project Structure (Planned)

```text
OmniversifyFont/
├── sources/               # Font source files (Glyphs, UFO, etc.)
├── exports/               # Generated OTF, TTF, WOFF2 files
├── documentation/         # Design docs and specimens
├── images/         # Design docs and specimens
└── README.md
```

### Supporting Tools

To assist with glyph manipulation and analysis, we use the [FontGlyphExtractor](https://github.com/phaylali/FontGlyphExtractor), a dedicated tool for high-precision SVG extraction.

---

## 🚀 Roadmap

### Phase 1: Foundation & Design (Current Phase)

- [x] **ASCII Character Set** (C0 Controls and Basic Latin)
- [x] **Latin-1 Character Set** (Latin-1 Supplement)
- [x] **Tifinagh Character Set** (Tifinagh)
- [x] **Arabic Character Set** (Arabic)
- [x] **Arabic Character Set Forms-A** (Arabic Presentation Forms-A)
- [x] **Arabic Character Set Forms-B** (Arabic Presentation Forms-B)
- [x] **Currency Character Set** (Currency Symbols)
- [x] **Superscripts and Subscripts** (Superscripts and Subscripts)
- [x] **General Punctuation** (General Punctuation)
- [x] **Mathematical Operators** (Mathematical Operators)
- [x] **Letterlike Symbols** (Letterlike Symbols)

### Phase 2: Refinement & Production (WIP)

- [x] **OpenType Feature Programming**
- [x] **Tifinagh Kerning**
- [x] **Arabic Kerning**
- [x] **Latin Kerning**
- [x] **Multilingual Specimen Page**
- [ ] **Final Production Release**

---

## Work In Progress (Added Unicodes)

### ASCII (C0 Controls and Basic Latin)

![ASCII Character Set](images/ascii_charset.png)

[ASCII+Latin Character Set](https://www.unicode.org/charts/PDF/U0000.pdf)

### Latin-1 Supplement

![Latin-1 Supplement Character Set](images/latin-1_charset.webp)

[Latin-1 Supplement Character Set](https://www.unicode.org/charts/PDF/U0080.pdf)

### Tifinagh

![Tifinagh Character Set](images/tifinagh_charset.png)

[Tifinagh Character Set](https://www.unicode.org/charts/PDF/U2D30.pdf)

### Arabic

![Arabic Character Set Page 1](images/arabic-0-p1_charset.png)
![Arabic Character Set Page 2](images/arabic-0-p2_charset.png)

[Arabic Character Set](https://www.unicode.org/charts/PDF/U0600.pdf)

### Arabic Presentation Forms-A

![Arabic Presentation Forms-A Character Set](images/arabic-pfa_charset.png)

[Arabic Presentation Forms-A Character Set](https://www.unicode.org/charts/PDF/UFB50.pdf)

### Arabic Presentation Forms-B

![Arabic Presentation Forms-B Character Set](images/arabic-pfb_charset.png)

[Arabic Presentation Forms-B Character Set](https://www.unicode.org/charts/PDF/UFB00.pdf)

### Currency Symbols

![Currency Symbols Character Set](images/currency_charset.png)

[Currency Symbols Character Set](https://www.unicode.org/charts/PDF/U20A0.pdf)

### Superscripts and Subscripts

![Superscripts and Subscripts Character Set](images/supsub_charset.png)

[Superscripts and Subscripts Character Set](https://www.unicode.org/charts/PDF/U2070.pdf)

### General Punctuation

![General Punctuation Character Set](images/general-pun_charset.png)

[General Punctuation Character Set](https://www.unicode.org/charts/PDF/U2000.pdf)

### Mathematical Operators

![Mathematical Operators Character Set](images/math-operators_charset.png)

[Mathematical Operators Character Set](https://www.unicode.org/charts/PDF/U2200.pdf)

### Letterlike Symbols

![Letterlike Symbols Character Set](images/letterlike-symbols_charset.png)

[Letterlike Symbols Character Set](https://www.unicode.org/charts/PDF/U2100.pdf)

---

This project is licensed under the [SIL Open Font License 1.1](http://scripts.sil.org/OFL).

---

## 🙏 Thanks & Credits

This font draws inspiration from numerous open-source and community-driven projects. Special thanks to:

- **IRCAM (Institut Royal de la Culture Amazighe)** for their pioneering work in standardizing and digitizing the Tifinagh script, having released over 25 Unicode-encoded Tifinagh fonts available for free download from [their website](https://www.ircam.ma/) and documented at [ScriptSource](https://scriptsource.org/entry/at6n5wwva8)

- **Google Fonts** for providing high-quality open-source fonts like [Noto Sans Arabic](https://fonts.google.com/noto/specimen/Noto+Sans+Arabic), [Noto Sans Tifinagh](https://fonts.google.com/noto/specimen/Noto+Sans+Tifinagh), [Cairo](https://fonts.google.com/specimen/Cairo), [Roboto](https://fonts.google.com/specimen/Roboto), [Tajawal](https://fonts.google.com/specimen/Tajawal), and many others that served as technical references

- **Achamel Soft** for the [Maghribi Assile font](https://www.wfonts.com/font/maghribi-assile), an important reference for Maghrebi Arabic calligraphy

- **Bouazzi** for their Maghribi font contributions

- **Samir Khouaja** for Maghribi font designs

- **The ArabSwells** community for arabicswell_1.ttf

- **Various open-source Maghribi and Tifinagh fonts** in the inspirations folder that helped shape our understanding of North African scripts

- **Academic researchers** whose work like "Tifinagh & the IRCAM, Explorations in Cursiveness and Bicamelarism in the Tifinagh script" (available via Academia.edu) provided crucial context
- **fontamin** for the [AutoMark script](https://github.com/fontamin/AutoMark), which automatically added OpenType GPOS lookups for Arabic diacritic positioning (mark and mkmk features).

---

## Support Us

<p align="center">
  <a href="https://ko-fi.com/omniversify">
    <img src="https://raw.githubusercontent.com/phaylali/Omniversify/main/public/images/kofi_logo.svg" width="200" alt="Ko-Fi" />
  </a>
</p>

<p align="center">
  <strong>Keep us going</strong>
</p>

---

&copy; 2026 [Omniversify](https://omniversify.com). All rights reserved.

_Made by Moroccans, for the Omniverse_

[![ReadMeSupportPalestine](https://raw.githubusercontent.com/Safouene1/support-palestine-banner/master/banner-project.svg)](https://donate.unrwa.org/-landing-page/en_EN)
