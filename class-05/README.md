# Class 05 — Web Gacha Simulator

A small browser game: pull cards, each card a point, a flat shape or a solid.
Built as one self-contained HTML file with plain JavaScript — no framework, no
build step, no network calls.

![The gacha page](screenshot.png)

## Files

| File | What it is |
| --- | --- |
| [`SAM_CLASS_05_GACHA.html`](SAM_CLASS_05_GACHA.html) | The whole app: markup, CSS, JavaScript and SVG card art inlined. Double-click to play. |
| [`SAM_CLASS_05_USAGE.md`](SAM_CLASS_05_USAGE.md) | English user guide: controls, rates, pity formula, saving, troubleshooting. |
| [`screenshot.png`](screenshot.png) | What the page looks like after three ten-pulls. |

## Quick start

Double-click `SAM_CLASS_05_GACHA.html`, or serve the folder:

```bash
python -m http.server 8000
# http://localhost:8000/SAM_CLASS_05_GACHA.html
```

## Spec in one table

| Item | Decision |
| --- | --- |
| Card pool | 16 cards: 6 dots (R), 6 flat shapes (SR), 4 solids (SSR) |
| Rarity rates | R 80%, SR 18%, SSR 2% (equal split inside each rarity) |
| Pity | 2% flat for pulls 1–40; +4 points per pull after that; guaranteed at 65 |
| Ten-pull | guarantees at least one SR or SSR; the forced slot rolls SSR at the current pity rate |
| Balance | 1000 pulls, single costs 1, ten-pull costs 10 |
| Saving | `localStorage`: balance, pity counter, totals, last 200 history entries |
| Extras | live SSR rate display, 10,000-draw simulation button, EN / 中文 switch |

## Verification

Driving the real drawing code from a harness:

- 12 × 1,000 pulls → 31.8 SSRs on average (26–38), matching 2% base plus pity.
- 1,200 ten-pulls → every batch contained at least one SR or SSR.
- Longest observed gap between SSRs: 55 pulls, under the 65-pull ceiling.

## Notes

- Layout: controls on the left, card stage on the right; below ~620px the panel
  stacks on top and the card grid drops to two columns.
- Cards carry their rarity in the frame, not only in a label: plain for R, a blue
  glow for SR, an animated gold shimmer for SSR.
- Single file on purpose: the requirement was "double-click and it runs", and that
  also means it works offline and can be handed in as one artifact.
- Card art is SVG (isometric for the solids) so the file stays small and needs no
  image assets or licenses.
- Progress is stored per browser and per machine; there is no backend.
