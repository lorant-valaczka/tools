# Typography golden rules — by Lóránt

A tested default system for text typography, distilled from many typographic systems that consistently produced refined results. It gives someone without typographic training a reliably good result; a professional will fine-tune it to the typeface and the project.

Use it as the starting point for every brand unless the brand has a stated reason to deviate, and record any deviation in the log. The ratios come from working systems; the values below carry a small safety margin, especially in line-height.

## Contents
- The golden rule
- Body text: choosing the typeface
- Body text: four levels
- Body text: regular and strong
- Optical fine-tuning
- Display and headings
- Mobile
- Text colour tiers
- Tokens
- Checks

## The golden rule: a small difference is no difference

In typography, a small difference doesn't read as hierarchy; it reads as a mistake. Two weights, sizes or colours that are almost the same look unintended. So whenever two styles must differ, make the difference clearly visible, or don't make it at all. This applies to weights, sizes and colour tiers alike, and it is behind most of the rules below.

## Body text: choosing the typeface

Give search principles, not a list to pick from. Lists date fast and get copied without thought. The body face must be either designed for screens, or a classical text face whose long-text legibility is proven (the Renaissance antiqua tradition, such as the Garamond family). Serif or sans both work.

Look for:
- **Open, clear letterforms:** open apertures (c, e, a, s), a generous x-height for a sans.
- **Distinguishable characters:** I, l and 1; O and 0; rn and m.
- **Real weights for the strong rule:** at least two cuts the right distance apart (see below), plus a real italic.
- **Full language coverage:** every character of the target languages, tested in real text (see `identity.md`).
- **Figures:** tabular figures if the brand shows prices, tables or data.
- **Rendering:** good at 12–16 px on ordinary screens, including Windows.
- **Licence** for every surface the brand needs (desktop, web, app, email, office tools).

Examples of the kind of face meant: Inter, Lexend, Nunito, the Garamond family. These are examples of the category, not a shortlist.

**Classical serifs on screen** work well, also for long texts, but set them larger than a screen sans: their x-height is smaller. As a guide, a classical serif needs about 1.2–1.3× the size of a screen sans for the same x-height. Match them by measured x-height, not by nominal size.

## Body text: four levels

| Level | Size / line-height | Ratio | Tracking | Typical use |
|---|---|---|---|---|
| **XS** | 12 / 18 px | 1.50 | 0 | captions, metadata, legal lines |
| **S** | 14 / 21 px | 1.50 | 0 | dense interfaces, secondary text |
| **M** | 16 / 24 px | 1.50 | 0 | the default body text |
| **L** | 18 / 26 px | 1.44 | 0 | long reading, introductions |

- The line-height ratio grows slightly as the size drops: small text needs relatively more air.
- Measure (line length): 60–80 characters for running text.
- Each level has a regular and a strong style. That gives eight body styles, which covers almost every need.

## Body text: regular and strong

The strong style must be clearly stronger than the regular, by the golden rule. There are two ways to get there. Both are good; **pick one per system and use it for every strong style**, because mixing them makes emphasis inconsistent.

- **Path A: two weight steps.** Skip the next weight up and use the one after it.
  - Regular base → **Bold** (SemiBold is skipped).
  - Book base → **Medium** (Regular is skipped).
- **Path B: one weight step plus one colour step.** The strong style moves up one weight *and* one colour tier at the same time. For example: Book in the body colour → Regular in the primary colour. Neither change would be enough alone; together they read clearly.

Check the result at XS: if the strong doesn't stand out at 12 px, it doesn't work.

## Optical fine-tuning

The values above are a system, not a formula; the system and its ratios are what matter. Every typeface needs a small optical adjustment:
- **x-height:** a large x-height makes lines look tighter, so it may need slightly more line-height; a small one, slightly less.
- **Ascenders and descenders:** long ones need more room between lines; short ones allow tighter setting.
- Adjust by looking at real text in the real face, at the real size, on the target screen. Change the line-height by a pixel or two, not the system.

## Display and headings

The display face can be more characterful and harder to read than the body face; how far to go is a project decision. If it is hard to read, keep it to large sizes and give it a size floor below which the body face takes over.

**Line-height tightens as the size grows.** The most common fault in headings is too much line-height, especially in the large sizes.

| Size | Line-height | Tracking |
|---|---|---|
| 15–20 px | 1.25 | 0 |
| 22–28 px | 1.15–1.2 | −0.01em |
| 36–44 px | 1.05–1.1 | −0.02em |
| 60–96 px | 1.0–1.05 | −0.03em |

**Tracking rule of thumb:** below 20 px, 0. At 20 px, −0.01em, then another −0.01em each time the size doubles (40 px: −0.02em, 80 px: −0.03em). Light weights at very large sizes can go a little tighter.

**Collision test.** Tight leading is right until ascenders and descenders start touching. Set a test with accented capitals (Á, Ő, Ű, Ç, Ł, or whatever the target languages use) directly below a line full of descenders (g, j, p, y). If they touch often, the work looks careless: loosen the line-height. Find the middle ground between airy and colliding.

**Two families are harder than one.** With a separate display face, the two must be matched optically by x-height (see `identity.md`, Typography). With one family, this step disappears.

**Example starting scale**, if the project has no reason for another: H1 48 · H2 36 · H3 28 · H4 22 · H5 18 · H6 16 px, line-heights and tracking from the table above. Adjust it to the display face.

## Mobile

- **Mobile H1 = desktop H3.** This usually works as a starting point. The lower levels shift down the same way where the scale allows; where it runs out, they merge with the floor (H6 never below body M strong). Then fine-tune on a real phone width (about 390 px).
- **Body sizes stay the same** on mobile. Don't shrink running text for small screens.
- **Form fields at least 16 px**, otherwise iOS zooms in when the user starts typing.

## Text colour tiers

| Tier | Contrast to its background | Example on white | Where |
|---|---|---|---|
| **Primary** | ≥ 15:1 | #1A1A1A (17.4:1) | everywhere |
| **Secondary** | about 7:1 | #555555 (7.5:1) | everywhere |
| **Tertiary** | 4.5–5:1, the lower edge of AA | #737373 (4.7:1) | M and larger only; never XS or S |
| **Disabled** text | about 2:1 to its own surface | #A6A6A6 on #F0F0F0 (2.1:1) | doesn't need to be readable |
| **Disabled** surface | 1.1–1.3:1 to the page | #F0F0F0 on white (1.1:1) | just enough to show the control's shape |

- **Primary and secondary cover about 95% of needs.** Tertiary is an extra; use it only when the information really has three levels.
- **Adjacent tiers at least 1.5× apart** in contrast ratio (in the example: 17.4 → 7.5 → 4.7, that is 2.3× and 1.6×). This is the golden rule applied to colour: tiers that are too close read as an error.
- **Disabled:** it doesn't have to be legible (contrast standards exempt inactive controls), but it must still be faintly readable on a close look, and clearly not active. Keep the disabled button's surface very subtle against the page; a disabled control that is too contrasty looks enabled.
- **Dark mode:** recompute every tier on the dark background. The ratios hold; the values change.

## Tokens

- Body: `body-xs`, `body-s`, `body-m`, `body-l`, each with `-strong`.
- Headings: `h1`…`h6`, with `-mobile` variants where they differ.
- Colour: `text-primary`, `text-secondary`, `text-tertiary`, `text-disabled`, `surface-disabled`.

Each typography token carries family, weight, size, line-height and tracking, so no value is set by hand anywhere else.

## Checks

- [ ] The collision test passes at every heading size.
- [ ] The strong style is clearly visible at XS.
- [ ] Every strong style follows the same path (A or B).
- [ ] Tertiary is not used at XS or S.
- [ ] Adjacent colour tiers are at least 1.5× apart; recomputed for dark mode.
- [ ] Running text stays within 60–80 characters per line.
- [ ] Mobile headings checked on a real phone width.
