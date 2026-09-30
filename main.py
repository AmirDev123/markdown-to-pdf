#!/usr/bin/env python3
"""
Markdown to PDF converter.
Uses markdown2 + weasyprint (or falls back to pdfkit/wkhtmltopdf).
Install: pip install markdown2 weasyprint
"""
import argparse
import os
import sys

CSS = """
body { font-family: Georgia, serif; max-width: 800px; margin: 40px auto; line-height: 1.6; color: #222; }
h1, h2, h3 { color: #111; border-bottom: 1px solid #ddd; padding-bottom: 4px; }
code { background: #f4f4f4; padding: 2px 5px; border-radius: 3px; font-family: monospace; }
pre code { display: block; padding: 12px; overflow-x: auto; }
blockquote { border-left: 4px solid #aaa; margin: 0; padding-left: 16px; color: #555; }
table { border-collapse: collapse; width: 100%; }
th, td { border: 1px solid #ccc; padding: 8px; text-align: left; }
th { background: #f0f0f0; }
"""


def convert(md_path: str, output: str | None = None):
    try:
        import markdown2
    except ImportError:
        sys.exit("Install markdown2: pip install markdown2")

    with open(md_path, encoding="utf-8") as f:
        md_text = f.read()

    html_body = markdown2.markdown(md_text, extras=["fenced-code-blocks", "tables", "strike"])
    html = f"<!DOCTYPE html><html><head><meta charset='utf-8'><style>{CSS}</style></head><body>{html_body}</body></html>"

    out_path = output or os.path.splitext(md_path)[0] + ".pdf"

    try:
        from weasyprint import HTML
        HTML(string=html).write_pdf(out_path)
        print(f"Converted with WeasyPrint → {out_path}")
        return
    except ImportError:
        pass

    try:
        import pdfkit
        pdfkit.from_string(html, out_path)
        print(f"Converted with pdfkit → {out_path}")
        return
    except ImportError:
        pass

    # Fallback: save as HTML
    html_out = out_path.replace(".pdf", ".html")
    with open(html_out, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"No PDF backend found. Saved as HTML → {html_out}")
    print("Install a backend: pip install weasyprint  OR  pip install pdfkit")


def main():
    parser = argparse.ArgumentParser(description="Convert Markdown to PDF")
    parser.add_argument("input", help="Path to .md file")
    parser.add_argument("-o", "--output", help="Output PDF path")
    args = parser.parse_args()
    convert(args.input, args.output)


if __name__ == "__main__":
    main()
