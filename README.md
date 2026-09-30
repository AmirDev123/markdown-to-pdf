# markdown-to-pdf

Convert Markdown files to beautifully styled PDFs from the command line.

## Setup

```bash
pip install markdown2 weasyprint
```

## Usage

```bash
python main.py document.md
python main.py document.md -o output.pdf
```

Falls back to `pdfkit` (requires wkhtmltopdf) if WeasyPrint is unavailable, or saves as HTML if neither is installed.

## Requirements

- `markdown2` (pip)
- `weasyprint` (pip) — recommended PDF backend
- or `pdfkit` + `wkhtmltopdf` as alternative
