# Gacha Simulator — User Guide

A single-file browser mini-game: spend pulls to draw cards, where every card is a
dot (R), a flat shape (SR) or a solid (SSR). No install, no server, no network.

**File:** `SAM_CLASS_05_GACHA.html`

---

## 1. How to open it

Double-click `SAM_CLASS_05_GACHA.html`. It opens in your default browser and runs
immediately.

If your browser asks what to do with the file, choose **Open with → Chrome / Edge**.
Everything is inlined in that one file (HTML, CSS, JavaScript, SVG art), so it also
works offline, from a USB stick, or after being emailed.

Optional: serve it over HTTP instead of `file://`:

```bash
cd class-05
python -m http.server 8000
# then open http://localhost:8000/SAM_CLASS_05_GACHA.html
```

Both ways give identical behaviour. There is no build step and no dependency.

---

## 2. What you see

| Area | What it shows |
| --- | --- |
| Top row of tiles | pulls left, current SSR rate, pulls since last SSR, total pulls, SSR count |
| Buttons | single pull, ten-pull, simulate 10,000 draws, reset everything |
| Drop rates | every card in the pool with its group rate and per-card share |
| Latest result | the cards from your most recent pull |
| History | your last 200 pulls, newest first, with a timestamp |
| How to use | a collapsible copy of the short instructions |

---

## 3. Controls

| Button | Cost | Effect |
| --- | --- | --- |
| **Pull ×1** | 1 pull | Draws one card. |
| **Pull ×10** | 10 pulls | Draws ten cards; the batch is guaranteed to contain at least one SR or SSR. |
| **Simulate 10,000** | free | Runs 10,000 draws in memory and reports the measured distribution. Your balance, history and pity counter are untouched. |
| **Reset all** | — | Asks for confirmation, then clears pulls, history and the pity counter, and restores the 1000-pull balance. |

Buttons disable themselves when the balance is too low (fewer than 1 or 10 pulls).

---

## 4. Cards and drop rates

16 cards in three rarities, split evenly inside each rarity.

| Rarity | Cards | Group rate | Per-card share |
| --- | --- | --- | --- |
| **R** | Circle Dot, Square Dot, Triangle Dot, Diamond Dot, Cross Dot, Star Dot | 80% | 13.33% |
| **SR** | Triangle, Square, Circle, Pentagon, Hexagon, Star | 18% | 3.00% |
| **SSR** | Cube, Sphere, Triangular Pyramid, Cylinder | 2% | 0.50% |

Group rates sum to 100%. Inside a rarity every card is equally likely, so a
single SSR card is 0.5% and a single R card is 13.33%.

---

## 5. How the draw actually works

For each pull, in this order:

1. Compute the SSR probability from the pity counter (see below).
2. Roll it. If it hits, the card is an SSR and the counter resets to 0.
3. Otherwise split the remaining probability between SR and R in an 18 : 80 ratio,
   then pick a random card of that rarity.

At the base rate the numbers come out as 2% / 18% / 80%; during pity the SSR share
grows and the SR/R split takes the remainder.

**Ten-pull guarantee:** the 10th card is only forced when the first nine contain no
SR or SSR. That forced slot rolls SSR at the current pity rate and otherwise gives
SR, so a lucky ten-pull is never downgraded.

---

## 6. Pity rules

- Pulls 1–40 without an SSR: flat 2% each.
- From the 41st pull on: **+4 percentage points per pull**.
- The 65th consecutive pull without an SSR is guaranteed.

```
p(n) = 2%                       for n <= 40
p(n) = min(100%, 2% + 4% * (n - 40))   for n > 40
```

| Pull since last SSR | SSR chance |
| --- | --- |
| 1 – 40 | 2% |
| 41 | 6% |
| 45 | 22% |
| 50 | 42% |
| 55 | 62% |
| 60 | 82% |
| 65 | 100% (guaranteed) |

The counter resets the moment an SSR appears, whether it came from a single pull,
a ten-pull, or the guaranteed slot. The current value is always on screen, so the
displayed rate is the rate actually being used.

---

## 7. Saving

Progress lives in the browser's `localStorage` under the key `sam_gacha_v1`:

- remaining pulls and total pulls used
- the pity counter
- per-rarity totals
- the last 200 history entries

Refreshing or closing the tab keeps everything. The data is per browser and per
machine: another browser, another computer, or a private window starts fresh, and
nothing is uploaded anywhere. **Reset all** clears all four items.

---

## 8. Language

The **EN / 中文** switch in the top-right changes the whole interface, the card
names, the rate table and the help text. The choice is saved with your progress.

---

## 9. Verified behaviour

Checked with a simulation harness driving the real draw code:

- 12 runs of 1,000 pulls: **31.8 SSRs on average** (26–38 per run), consistent with
  a 2% base plus pity.
- 1,200 ten-pulls: **every batch contained at least one SR or SSR**.
- Longest gap between SSRs observed: **55 pulls**, below the 65-pull ceiling.

Use **Simulate 10,000** to reproduce a distribution check yourself.

---

## 10. Known limitations

- No backend, no accounts, no cross-device sync — by design.
- History is capped at 200 entries; older entries are dropped, the totals are kept.
- Only the standard browser APIs are used, so there is nothing to install, but the
  file must be opened in a modern browser (Chrome, Edge, Firefox, Safari).
- Cards are drawn as SVG, not images, which keeps the file small but means the
  art is geometric rather than illustrative.

---

## 11. Troubleshooting

| Symptom | Cause / fix |
| --- | --- |
| Pulls reset to 1000 after reopening | The browser blocks `localStorage` for `file://` (some hardened settings) or you are in a private window. Serve over `http://localhost` instead. |
| Buttons greyed out | Balance is under 1 or 10 pulls. Click **Reset all** to start over. |
| Nothing happens on double-click | The file association is missing; right-click → **Open with** → your browser. |
| Page renders without styling | The file was opened as plain text (e.g. in an editor). Open it with a browser, not a text editor. |
