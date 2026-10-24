#!/usr/bin/env python3
"""
scaffold.py — Scaffold a new case study from a JSON input.

Usage:
    python scaffold.py --input input.json --output-dir ./case-studies
"""

import argparse
import json
import sys
from pathlib import Path
from datetime import datetime

PLACEHOLDER = lambda f: f"[pending: {f}]"

DEFAULTS = {
    "customer_name": PLACEHOLDER("customer_name"),
    "slug": "customer-slug",
    "product_name": PLACEHOLDER("product_name"),
    "product_url": "#",
    "demo_url": "#",
    "industry": PLACEHOLDER("industry"),
    "size": PLACEHOLDER("size"),
    "country": PLACEHOLDER("country"),
    "plan": "Pro",
    "customer_since": PLACEHOLDER("customer_since"),
    "anonymized": False,
    "one_line_outcome": PLACEHOLDER("one_line_outcome"),
    "hero_value": PLACEHOLDER("hero_value"),
    "hero_label": PLACEHOLDER("hero_label"),
    "challenge": PLACEHOLDER("challenge"),
    "solution": PLACEHOLDER("solution"),
    "implementation": PLACEHOLDER("implementation"),
    "pull_quote": PLACEHOLDER("pull_quote"),
    "quote_attribution": PLACEHOLDER("quote_attribution"),
    "quote_role": PLACEHOLDER("quote_role"),
    "whats_next": PLACEHOLDER("whats_next"),
    "accent_color": "#d4ff00",
    "date": datetime.now().strftime("%Y-%m-%d"),
}


def build_context(input_data: dict) -> dict:
    ctx = {**DEFAULTS, **input_data}
    metrics = ctx.get("metrics", [])
    while len(metrics) < 4:
        metrics.append({"value": "—", "label": "[pending metric]"})
    ctx["metric_2_value"] = metrics[0]["value"]
    ctx["metric_2_label"] = metrics[0]["label"]
    ctx["metric_3_value"] = metrics[1]["value"]
    ctx["metric_3_label"] = metrics[1]["label"]
    ctx["metric_4_value"] = metrics[2]["value"]
    ctx["metric_4_label"] = metrics[2]["label"]
    ctx["metric_5_value"] = metrics[3]["value"]
    ctx["metric_5_label"] = metrics[3]["label"]
    return ctx


def substitute(template: str, ctx: dict) -> str:
    result = template
    for key, value in ctx.items():
        token = "{{" + key.upper() + "}}"
        result = result.replace(token, str(value))
    return result


def main():
    parser = argparse.ArgumentParser(description="Scaffold a success story.")
    parser.add_argument("--input", required=True, help="Path to JSON input.")
    parser.add_argument("--output-dir", default="./case-studies", help="Output directory.")
    parser.add_argument("--templates-dir", default=None, help="Templates dir (defaults to ../assets/templates relative to script).")
    args = parser.parse_args()

    script_dir = Path(__file__).parent
    templates_dir = Path(args.templates_dir) if args.templates_dir else script_dir.parent / "assets" / "templates"

    with open(args.input) as f:
        input_data = json.load(f)

    ctx = build_context(input_data)
    slug = ctx["slug"]

    output_dir = Path(args.output_dir) / slug
    output_dir.mkdir(parents=True, exist_ok=True)

    outputs = {
        "case-study.md": f"case-study-{slug}.md",
        "case-study.html": f"case-study-{slug}.html",
        "case-study-gated.md": f"case-study-{slug}-gated.md",
        "snippets.md": f"snippets-{slug}.md",
    }

    for template_file, output_file in outputs.items():
        template_path = templates_dir / template_file
        if not template_path.exists():
            print(f"Warning: template not found: {template_path}", file=sys.stderr)
            continue
        content = template_path.read_text()
        rendered = substitute(content, ctx)
        (output_dir / output_file).write_text(rendered)
        print(f"✓ Wrote {output_dir / output_file}")

    checklist_path = output_dir / f"checklist-{slug}.md"
    checklist = f"""# Publish Checklist — {ctx['customer_name']}

## Pre-publish
- [ ] Fill any `[pending: ...]` placeholders with verified data
- [ ] Customer has approved the final draft
- [ ] Pull-quote matches customer's actual words (or paraphrased with consent)
- [ ] Metrics double-checked against product dashboard
- [ ] Anonymization is consistent ({'yes' if ctx.get('anonymized') else 'no'})

## Publish
- [ ] Product site: `/customers/{slug}` on {ctx['product_url']}
- [ ] Cross-post: edisontkp.com brand blog
- [ ] Cross-post: LinkedIn article (use snippets file)
- [ ] Gated PDF: `/resources/{slug}` with email capture
- [ ] Sales enablement: share in internal channel

## Post-publish
- [ ] Tag customer on LinkedIn (with permission)
- [ ] Add to `/case-studies` index page
- [ ] Add to HRDF training deck if relevant
- [ ] Schedule a 30-day review to update metrics
"""
    checklist_path.write_text(checklist)
    print(f"✓ Wrote {checklist_path}")
    print(f"\nAll files written to: {output_dir.resolve()}")


if __name__ == "__main__":
    main()
