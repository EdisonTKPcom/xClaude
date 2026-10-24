# xClaude

A monorepo of Claude Code and Cowork plugins by [EdisonTKP](https://edisontkp.com).

## Plugins

### `success-stories` — Customer case study generator

Generate complete customer success stories across the OS portfolio (VehicleOS, SenangBoss, EmasOS, ChatOS, FleetOS, etc.):

- Canonical markdown source
- Drop-in HTML page component (dark editorial — Bebas Neue + Space Mono + Syne + JetBrains Mono)
- Gated PDF-ready extended version
- LinkedIn + X distribution snippet pack
- Publish checklist per case study

**Commands:** `/new-case-study`, `/interview-script`, `/batch-case-studies`, `/publish-checklist`

**Install path:** `plugins/success-stories-plugin/`

```bash
# From Claude Code
/plugin install EdisonTKPcom/xClaude/plugins/success-stories-plugin
```

Per-product accent colors pre-configured for the full OS portfolio. See `plugins/success-stories-plugin/skills/success-stories/references/product-variants.md`.

---

## About

Built to run on Claude Code and Cowork. All plugins target Edison's SaaS portfolio stack (Cloudflare Pages + D1/KV + dark editorial design system across techvisory.io, edisontkp.com, emas.estate).
