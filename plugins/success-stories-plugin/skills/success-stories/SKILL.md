---
name: success-stories
description: Generate customer success stories, case studies, and testimonials for SaaS products — including interview scripts, structured narratives, metric-driven results sections, and publishable output in Markdown, HTML page components, and gated PDF formats. Use this skill whenever the user mentions "case study", "success story", "customer story", "testimonial", "case studies page", or wants to turn a customer win into marketing content. Especially relevant for OS-branded portfolio products (VehicleOS, SenangBoss, EmasOS, ChatOS, FleetOS, etc.) where case studies drive SaaS conversions. Trigger even when the user only says things like "write up how [customer] used [product]" or "we need customer proof for the landing page" — always consult this skill before drafting case-study content freehand.
---

# Success Stories

A structured workflow for turning raw customer wins into publishable case studies across a SaaS product portfolio. Optimized for the OS-branded stack (Cloudflare Pages + D1/KV + dark editorial design system).

## When to use

- User asks for a case study, success story, customer story, or testimonial
- User wants to populate `/customers` or `/case-studies` pages on a product site
- User mentions needing "customer proof" or "social proof" for a landing page
- User wants to extract metrics from product usage data and turn them into a narrative
- User wants HRDF/training case material derived from a real client engagement

## Core workflow

Follow these phases in order. Each phase has a clear deliverable.

### Phase 1 — Intake

Gather the minimum inputs needed. If any are missing, ask for them in a single batched question, not one-by-one:

1. **Product** (VehicleOS, SenangBoss, etc.) — dictates which template variant to use
2. **Customer identifier** — company name, industry, size, country. Anonymized is OK (`"Malaysian logistics SME, 50 employees"`)
3. **Pain point before** — what were they doing manually or badly?
4. **What they use now** — which product features, which plan
5. **Outcome metrics** — even rough numbers (hours saved, % improvement, revenue)
6. **Quote** — one line from the customer, even paraphrased
7. **Publish permission** — named story, anonymized, or internal-only?

If the user has access to product usage data (Cloudflare D1/KV dashboards), remind them metrics can be pulled directly — don't invent numbers.

### Phase 2 — Select template variant

Choose the variant that matches the product category. See `references/product-variants.md` for the full mapping. Quick guide:

- **Operational SaaS** (VehicleOS, FleetOS, FacilityOS) → time/cost-saved angle
- **Compliance/Legal** (SenangBoss, CorpOS) → hours-of-lawyer-fees-avoided angle
- **Financial** (EmasOS, WealthOS, RetireEmas) → AUM/yield/return angle
- **Communication** (ChatOS, FunnelOS) → response-time/close-rate angle
- **Developer/Infra** (McpOS, DB-OS, LogOS) → uptime/deploy-velocity angle

### Phase 3 — Draft the story

Use the 5-part structure every case study needs. Write it into `assets/templates/case-study.md` filled in, saving the output to the user's working directory.

1. **Customer snapshot** (1 line) — name, industry, size, country
2. **Challenge** (2-3 sentences) — specific, quantified pain
3. **Solution** (3-4 sentences) — which features, how they were configured
4. **Implementation** (2-3 sentences) — timeline, integration steps, who was involved
5. **Results** (bullet list of 3-5 metrics) — hard numbers + one pull-quote

Never invent metrics. If a number is not verified, write `[pending: confirm with customer]`.

### Phase 4 — Generate multi-format output

Produce three artifacts in the user's working directory, using the templates in `assets/templates/`:

1. **`case-study-{slug}.md`** — canonical source (edit this; all others regenerate from it)
2. **`case-study-{slug}.html`** — drop-in page component matching the dark editorial design system (Bebas Neue / Space Mono / Syne / JetBrains Mono)
3. **`case-study-{slug}-gated.md`** — extended PDF version with additional technical detail, suitable for email-gated download

See `references/design-system.md` for the exact tokens to use in the HTML component.

### Phase 5 — Distribution checklist

Produce a short checklist in the response showing where to publish:

- Product site: `/customers/{slug}` or `/case-studies/{slug}`
- Cross-post: edisontkp.com (if user owns the brand), LinkedIn article, HRDF training deck
- Email capture: gated PDF behind `/resources/{slug}`
- Snippet pack: 3 LinkedIn post variants + 1 Twitter/X thread, saved as `snippets-{slug}.md`

## Interview mode

If the user has a customer lined up but no content yet, offer to run **interview mode**: generate a 15-minute call script with 8-10 questions targeting the 5-part structure. Save as `interview-{slug}.md`. Script is in `references/interview-script.md`.

## Anonymization

If the customer hasn't granted named permission, anonymize consistently:
- Company → `"[Industry] [size] in [country]"` (e.g., "Logistics SME in Malaysia")
- People → role only ("the Operations Manager")
- Numbers → keep exact (these are the proof)
- Never use fake company names — readers notice

## References

- `references/product-variants.md` — template-variant-per-product mapping
- `references/design-system.md` — brand tokens for HTML output
- `references/interview-script.md` — customer call questions
- `references/metrics-library.md` — which metrics matter per product category

## Templates

- `assets/templates/case-study.md` — canonical markdown structure
- `assets/templates/case-study.html` — dark editorial HTML component
- `assets/templates/case-study-gated.md` — extended PDF-ready version
- `assets/templates/snippets.md` — LinkedIn + X distribution pack

## Quality bar

Before returning output, self-check:

- [ ] Every number has a source (customer-provided, dashboard-pulled, or marked `[pending]`)
- [ ] The pull quote sounds like a human, not marketing copy
- [ ] The challenge section is specific (not "they struggled with efficiency")
- [ ] The results section leads with the most impressive verified metric
- [ ] Anonymization is consistent if used
- [ ] HTML uses the design system tokens, not generic Tailwind defaults
