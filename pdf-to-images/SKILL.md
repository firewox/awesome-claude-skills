---
name: pdf-to-images
description: Convert PDF pages to PNG or JPG images with DPI/scale and page-range controls. Use when asked to render a PDF into image files.
---

# PDF To Images

## Overview

Convert a PDF into per-page PNG/JPG files. Support DPI or scale-based rendering and flexible page ranges. Default output is a `<pdf_stem>_pages/` folder next to the source PDF.

## Workflow

1. Confirm input PDF path and desired format (`png` or `jpg`).
2. Decide resolution using either `--dpi` (default 150) or `--scale` (overrides DPI).
3. Decide page selection using `--pages` or `--page-start/--page-end`.
4. Run the bundled script to generate images into the default output folder, unless a custom output directory is needed.

## Quick Start

```bash
python pdf-to-images/scripts/pdf_to_images.py "path/to/file.pdf"
```

## Common Options

```bash
# Choose output format
python pdf-to-images/scripts/pdf_to_images.py "file.pdf" --format jpg

# Higher resolution
python pdf-to-images/scripts/pdf_to_images.py "file.pdf" --dpi 300

# Explicit scale (overrides DPI)
python pdf-to-images/scripts/pdf_to_images.py "file.pdf" --scale 2.0

# Page range selection
python pdf-to-images/scripts/pdf_to_images.py "file.pdf" --pages "1-3,5,7-"
python pdf-to-images/scripts/pdf_to_images.py "file.pdf" --page-start 2 --page-end 4

# Custom output directory
python pdf-to-images/scripts/pdf_to_images.py "file.pdf" --output-dir "output_images"
```

## Notes

- Default output directory: `<pdf_stem>_pages/` next to the input PDF.
- Page selection is 1-based. Examples: `1-3,5,7-` (open-ended ranges are allowed).
- JPG output automatically strips alpha channels if present.
- Requires Python and PyMuPDF (`fitz`). If missing, install with `pip install pymupdf`.

## Resources

### scripts/

- `scripts/pdf_to_images.py`: Convert a PDF into PNG/JPG images with DPI/scale and page-range controls.

---

If references/ or assets/ are unused, delete their example files.
