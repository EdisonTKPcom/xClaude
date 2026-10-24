---
description: Generate a complete case study (markdown + HTML + gated PDF + distribution snippets) for a product in the OS portfolio.
argument-hint: [product-name] [customer-name-or-slug]
allowed-tools: Read, Write, Edit, Bash, Glob
---

# New Case Study

Create a complete customer success story using the `success-stories` skill.

## Arguments

$ARGUMENTS

Parse: first arg = product (e.g. VehicleOS, SenangBoss), second arg = customer name/slug.
If missing, ask in ONE batched question.

## Process

1. Load `success-stories/SKILL.md` and follow its 5-phase workflow.
2. Read `success-stories/references/product-variants.md` for the correct angle.
3. Read `success-stories/references/design-system.md` for the accent color.
4. Batched intake: ask for all required fields in one message.
5. Write input JSON to `/tmp/case-study-input-{slug}.json`.
6. Run: `python3 <skill>/scripts/scaffold.py --input /tmp/case-study-input-{slug}.json --output-dir ./case-studies`
7. Refine prose in generated files. Keep `[pending: ...]` where metrics aren't verified.
8. Report file paths + pending items + distribution checklist.

## Non-negotiables

- Never invent metrics.
- Follow the 5-part structure: snapshot, challenge, solution, implementation, results.
- Use design system tokens — no generic Tailwind.
- Consistent anonymization if customer isn't named.
