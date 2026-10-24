---
description: Generate a 15-minute customer interview script tailored to a specific product and customer.
argument-hint: [product-name] [customer-context]
allowed-tools: Read, Write
---

# Interview Script

Generate a pre-filled customer interview script using the `success-stories` skill.

## Arguments

$ARGUMENTS

## Process

1. Read `success-stories/references/interview-script.md`.
2. Read `success-stories/references/product-variants.md` for metric targeting.
3. Customize placeholders with product + likely pain points for that industry.
4. Add 1-2 product-specific probe questions based on supporting metrics.
5. Save to `./interviews/interview-{customer-slug}.md`.
6. Report path + remind user to run call within 7 days while usage data is fresh.

## Tone

Conversational, not corporate. The user is calling a customer who already likes them.
