import argparse
from pathlib import Path

import fitz  # PyMuPDF


def main():
    parser = argparse.ArgumentParser(description='Convert a single image to a single-page PDF.')
    parser.add_argument('image', help='Path to input image (PNG/JPG/etc.)')
    parser.add_argument('--output', help='Output PDF path (default: <image_stem>.pdf)')
    args = parser.parse_args()

    img_path = Path(args.image)
    if not img_path.exists():
        raise SystemExit(f'Input not found: {img_path}')

    out_path = Path(args.output) if args.output else img_path.with_name(f'{img_path.stem}.pdf')

    pix = fitz.Pixmap(str(img_path))
    doc = fitz.open()
    page = doc.new_page(width=pix.width, height=pix.height)
    page.insert_image(fitz.Rect(0, 0, pix.width, pix.height), filename=str(img_path))
    doc.save(str(out_path))
    doc.close()

    print(f'Wrote PDF: {out_path}')


if __name__ == '__main__':
    main()
