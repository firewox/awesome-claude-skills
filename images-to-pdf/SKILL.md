---
name: images-to-pdf
description: Convert a single image (PNG/JPG/etc.) into a one-page PDF in the same folder. Use when asked to turn one image into a PDF.
---

# Images To PDF

## Overview

Convert a single image into a single-page PDF. The output defaults to `<image_stem>.pdf` in the same directory as the source image.

## Workflow

1. Confirm the input image path.
2. Run the bundled script to create a one-page PDF.
3. Use `--output` only if a custom output path is required.

## Quick Start

```bash
python images-to-pdf/scripts/image_to_pdf.py "path/to/image.png"
```

## Common Options

```bash
# Custom output path
python images-to-pdf/scripts/image_to_pdf.py "image.jpg" --output "out.pdf"
```

## Notes

- Output defaults to `<image_stem>.pdf` in the same folder as the source image.
- Supports PNG/JPG and other formats supported by PyMuPDF.
- Requires Python and PyMuPDF (`fitz`). If missing, install with `pip install pymupdf`.

## Resources

### scripts/

- `scripts/image_to_pdf.py`: Convert a single image into a one-page PDF.

---

If references/ or assets/ are unused, delete their example files.
