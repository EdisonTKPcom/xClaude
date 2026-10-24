# success-stories plugin

Generate customer success stories and case studies for SaaS product portfolios.

Produces four artifacts per case study:
- `case-study-{slug}.md` — canonical markdown source
- `case-study-{slug}.html` — drop-in page component matching the dark editorial design system
- `case-study-{slug}-gated.md` — extended PDF-ready version
- `snippets-{slug}.md` — LinkedIn + X distribution pack

Plus a per-case-study publish checklist.

## Install

```bash
# Claude Code
/plugin install EdisonTKPcom/success-stories-plugin
```

## Commands

| Command | Purpose |
|---|---|
| `/new-case-study [product] [customer]` | Build a complete case study from scratch |
| `/interview-script [product] [customer]` | Generate 15-min customer call script |
| `/batch-case-studies [products OR --all]` | Scaffold stubs across the OS portfolio |
| `/publish-checklist [slug]` | Generate publish-and-distribute checklist |

## Portfolio support

Pre-configured accent colors and metric templates for:
VehicleOS, SenangBoss, EmasOS, ChatOS, FleetOS, FacilityOS, HomeOS, PetOS, CorpOS, DebtOS,
WealthOS, RetireEmas, InsurOS, Web3Insur, FunnelOS, MarketingOS, EventOS, McpOS, DB-OS,
LogOS, SignalOS, AgentOS, HealthOS, LongevityOS, LearnOS, LearnChain, ChainOS, MYRX.

## Design system

Dark editorial. Bebas Neue + Space Mono + Syne + JetBrains Mono. Per-product accent colors.
Matches techvisory.io, edisontkp.com, emas.estate.

## Credits

Built by [EdisonTKP](https://edisontkp.com) · Powers the `/customers` pages across the OS portfolio.
