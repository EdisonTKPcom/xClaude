---
description: Generate case study stubs for multiple products at once — useful for seeding a /customers page across the entire OS portfolio.
argument-hint: [products-comma-separated OR --all]
allowed-tools: Read, Write, Bash, Glob
---

# Batch Case Studies

Scaffold placeholder case studies for multiple products in one pass.

## Arguments

$ARGUMENTS

## Process

1. Load the skill + product variants reference.
2. For each product, generate a template-only scaffold with correct accent color + hero-metric type.
3. Run the scaffold script per product.
4. Write a master index `./case-studies/README.md` with status dashboard.
5. Report: count scaffolded, products needing customer assignment, suggested priority order.

Every file will have many `[pending]` markers — intentional. User fills in via `/new-case-study` per product over time.
