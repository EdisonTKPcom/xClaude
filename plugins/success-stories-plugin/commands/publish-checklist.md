---
description: Generate a publish checklist for an existing case study, covering product site deployment, cross-posts, gated PDF, and sales enablement.
argument-hint: [case-study-slug]
allowed-tools: Read, Write, Bash, Glob
---

# Publish Checklist

Generate the full publish-and-distribute checklist for a finished case study.

## Arguments

$ARGUMENTS

## Process

1. Locate `./case-studies/{slug}/case-study-{slug}.md`. If missing, ask.
2. Read frontmatter to extract product name, customer name, product URL.
3. Generate `./case-studies/{slug}/publish-{slug}.md` with sections:
   - Pre-flight (resolve pending, approvals, metric re-verify)
   - Deploy to product site (routes, OG tags, mobile breakpoint)
   - Cross-post (LinkedIn, edisontkp.com, X thread, Slack/Discord)
   - Gated asset (PDF via `pdf` skill, email capture, CRM wire-up)
   - Sales enablement (deck slide, outreach templates, CRM tags)
   - Post-publish 7-day actions
4. If `pdf` skill available, generate `case-study-{slug}.pdf` from the gated markdown.
5. Return checklist path + next action.
