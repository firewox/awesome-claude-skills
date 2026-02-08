import argparse
import os
from pathlib import Path

import fitz  # PyMuPDF


def _parse_pages(pages_str, total_pages):
    if not pages_str:
        return list(range(total_pages))
    pages = set()
    for part in pages_str.split(','):
        part = part.strip()
        if not part:
            continue
        if '-' in part:
            start_s, end_s = part.split('-', 1)
            start = int(start_s) if start_s else 1
            end = int(end_s) if end_s else total_pages
            if start > end:
                start, end = end, start
            for p in range(start, end + 1):
                pages.add(p)
        else:
            pages.add(int(part))
    pages = sorted(p for p in pages if 1 <= p <= total_pages)
    return [p - 1 for p in pages]


def main():
    parser = argparse.ArgumentParser(description='Convert a PDF into PNG/JPG images.')
    parser.add_argument('pdf', help='Path to input PDF')
    parser.add_argument('--format', choices=['png', 'jpg'], default='png', help='Output image format')
    parser.add_argument('--dpi', type=int, default=150, help='Output DPI (default: 150)')
    parser.add_argument('--scale', type=float, help='Scale factor (overrides DPI if provided)')
    parser.add_argument('--pages', help='Page ranges, e.g. "1-3,5,7-" (1-based)')
    parser.add_argument('--page-start', type=int, help='Start page (1-based)')
    parser.add_argument('--page-end', type=int, help='End page (1-based)')
    parser.add_argument('--output-dir', help='Output directory (default: <pdf>_pages)')
    args = parser.parse_args()

    pdf_path = Path(args.pdf)
    if not pdf_path.exists():
        raise SystemExit(f'Input not found: {pdf_path}')

    out_dir = Path(args.output_dir) if args.output_dir else pdf_path.with_name(f'{pdf_path.stem}_pages')
    out_dir.mkdir(parents=True, exist_ok=True)

    doc = fitz.open(str(pdf_path))
    total = len(doc)

    if args.page_start or args.page_end:
        start = args.page_start or 1
        end = args.page_end or total
        if start > end:
            start, end = end, start
        page_indices = [p - 1 for p in range(start, end + 1) if 1 <= p <= total]
    else:
        page_indices = _parse_pages(args.pages, total)

    if not page_indices:
        raise SystemExit('No pages selected to render.')

    zoom = args.scale if args.scale else (args.dpi / 72.0)
    matrix = fitz.Matrix(zoom, zoom)
    ext = args.format

    for i in page_indices:
        page = doc.load_page(i)
        pix = page.get_pixmap(matrix=matrix)
        if ext == 'jpg' and pix.alpha:
            pix = fitz.Pixmap(fitz.csRGB, pix)
        out_path = out_dir / f'page_{i + 1:03d}.{ext}'
        pix.save(str(out_path))

    print(f'Wrote {len(page_indices)} pages to {out_dir}')


if __name__ == '__main__':
    main()
