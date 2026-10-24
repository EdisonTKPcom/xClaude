# Design System Tokens

These tokens match the dark editorial design system used across the OS-portfolio (techvisory.io, edisontkp.com, emas.estate, chains.my).

## Typography

| Use | Font | Weight | Source |
|---|---|---|---|
| Hero headlines | Bebas Neue | 400 | Google Fonts |
| Display / decorative | Syne | 600–800 | Google Fonts |
| Body copy | Space Mono | 400 | Google Fonts |
| Code / data | JetBrains Mono | 400–500 | Google Fonts |

Import block for any HTML template:
```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=JetBrains+Mono:wght@400;500&family=Space+Mono:wght@400;700&family=Syne:wght@600;800&display=swap" rel="stylesheet">
```

## Color palette

Base dark editorial. Override per-product accent color if that product has one.

```css
:root {
  --bg: #0a0a0a;
  --bg-elevated: #141414;
  --border: #262626;
  --text: #f5f5f5;
  --text-muted: #8a8a8a;
  --text-dim: #4a4a4a;
  --accent: #d4ff00;
  --accent-dim: #7a9600;
}
```

### Per-product accent overrides

| Product | Accent |
|---|---|
| VehicleOS | `#ff6b35` (signal orange) |
| SenangBoss | `#00d9a3` (trust teal) |
| EmasOS | `#d4af37` (gold) |
| ChatOS | `#4ade80` (active green) |
| FleetOS | `#60a5fa` (logistics blue) |
| RetireEmas | `#d4af37` (gold) |
| Default | `#d4ff00` (techvisory lime) |

## Spacing

Use an 8px base grid: `8, 16, 24, 32, 48, 64, 96, 128`.

## Component patterns

### Stat card (for results section)
```html
<div class="stat">
  <div class="stat-value">94%</div>
  <div class="stat-label">reduction in filing time</div>
</div>
```
Stat-value uses Bebas Neue at 4–6rem. Stat-label uses Space Mono uppercase at 0.75rem with letter-spacing 0.1em.

### Pull quote
```html
<blockquote class="pull-quote">
  <p>The quote goes here, no more than 25 words.</p>
  <cite>— Name, Role, Company</cite>
</blockquote>
```
Pull-quote body uses Syne 600 italic. Cite uses Space Mono uppercase 0.75rem.

### Section divider
Horizontal rule 1px solid `var(--border)` with 64px vertical margin. No decorative flourishes — keep it editorial.

## Do / don't

- **Do** use generous negative space, long line-heights (1.6+ for body).
- **Do** keep stat numbers huge (4–6rem) — they are the proof.
- **Don't** use rounded corners larger than 4px. Editorial, not playful.
- **Don't** use gradients except on the hero accent line.
- **Don't** introduce new fonts — if you need variety, use weight/size changes within the existing four families.
