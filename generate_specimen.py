#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
generate_specimen.py
-------------------
Creates a PDF specimen showing Latin, Arabic/Maghrebi, and Tifinagh samples.

Uses Chromium headless to render an HTML specimen page (with @font-face)
to PDF, producing a proper document with actual text content.

Usage:
    python3 generate_specimen.py [<font-ttf>] [<output-pdf>]

Requires:
    - chromium (headless) in PATH
    - The HTML template at documentation/specimen.html
"""

import os
import sys
import subprocess
import tempfile


def resolve_path(p):
    return os.path.abspath(os.path.join(os.path.dirname(__file__), p))


def main():
    ttf_path = sys.argv[1] if len(sys.argv) > 1 else resolve_path(
        "exports/OmniversifyMaghribFont-hinted.ttf"
    )
    pdf_path = sys.argv[2] if len(sys.argv) > 2 else resolve_path(
        "documentation/specimen.pdf"
    )
    html_src = resolve_path("documentation/specimen.html")

    if not os.path.exists(html_src):
        print(f"ERROR: specimen.html not found at {html_src}")
        sys.exit(1)
    if not os.path.exists(ttf_path):
        print(f"ERROR: Font not found at {ttf_path}")
        sys.exit(1)

    # Find chromium binary
    chromium = None
    for candidate in ["chromium", "chromium-browser", "google-chrome", "chrome"]:
        try:
            subprocess.run(
                [candidate, "--version"],
                capture_output=True,
                check=True,
            )
            chromium = candidate
            break
        except (subprocess.CalledProcessError, FileNotFoundError):
            continue
    if not chromium:
        print("ERROR: Chromium/Chrome not found. Install chromium or google-chrome.")
        sys.exit(1)

    # Convert HTML to PDF
    file_url = f"file://{html_src}"
    cmd = [
        chromium,
        "--headless",
        "--no-sandbox",
        "--disable-gpu",
        f"--print-to-pdf={pdf_path}",
        "--no-pdf-header-footer",
        file_url,
    ]
    print(f"Generating PDF: {pdf_path}")
    print(f"  Font: {ttf_path}")
    print(f"  HTML: {html_src}")
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"ERROR: Chromium failed: {result.stderr}")
        sys.exit(1)

    size = os.path.getsize(pdf_path)
    print(f"PDF generated: {pdf_path} ({size} bytes)")


if __name__ == "__main__":
    main()
