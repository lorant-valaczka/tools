# Identity: Develop and Build out

The second diamond. Develop opens 2–3 visual directions; Build out turns the chosen one into a system, chapter by chapter.

Every area below follows the same pattern: **what to decide**, **principles** that hold for almost any brand, **options**, and a **possible default**. The defaults suit a restrained, systematic brand. Say so when you use one, and change it when the Define sheet points somewhere else.

## Contents
- Develop: directions
- Build out: order of work
- Mark
- Typography
- Colour
- Layout, grid and spacing
- Imagery
- Patterns and graphic elements
- Motion

## Develop: directions

- 2–3 directions (2 at essential scope). Each is argued from the Define sheet: which attribute or which side of the core tension it pushes.
- Each direction is a quick sketch, a style tile rather than a system: a mark sketch or wordmark idea, a type pairing, a palette with roles, one layout principle, and an imagery sample if imagery matters.
- Show every direction on the **same fixed test set** with the same content (see `applications.md`), so the comparison is like for like and nobody chooses a direction because it got the nicest example.
- Cheapest medium: HTML pages or rough boards. No production files yet.
- **Gate:** one direction chosen, plus an explicit list of what carries over from the others.

## Build out: order of work

Mark → typography → colour → grid → imagery → patterns → motion. Each derives from what came before; doing them out of order produces rules that contradict each other. Chapters can run as parallel workstreams once their foundations are closed; which can start when, and how they stay out of each other's way: `decision-log.md`.

For each chapter: rule (one sentence) → specimen → values (written into the tokens) → do / don't → the reason. Usually 2–4 rounds per chapter. Close each one with the chapter checklist in `checklists.md`.

## Mark

**Decide:** the type of mark.

| Type | Good when |
|---|---|
| Wordmark | The name is short and distinctive, and it appears mostly where there is room |
| Lettermark or monogram | The name is long, or a compact form is needed |
| Symbol | Recognition without text is the goal (app icon, product, signage) |
| Combination (symbol + wordmark lockup) | Both needs exist; the most flexible |
| Emblem | Heritage, institutions, badges; weak at small sizes |

Check where it must appear: an app icon, favicon or avatar needs a compact form.

**From scratch:**
1. **Concepts from Define:** 3–5 ideas, each one sentence (what it means, why it fits the core tension).
2. **Rough sketches:** many and fast, black on white, at large and at small size.
3. **2–3 routes** refined enough to judge, shown on the test set, not alone on a white page.
4. **One route refined:** optical corrections, consistent strokes and angles, the small-size cut.

**Principles:**
- Judge it in context and at small size. A mark that only works at 400 px fails. To check, render it in an HTML page (or the design tool) at 16, 32 and 48 px and at the intended print minimum, on light and dark backgrounds, and look at the result before writing any size rule. Geometry alone (stroke width ÷ size) is a first estimate, not the check.
- **Small-size cut:** a separate simplified version with a size threshold, used below the size where detail breaks down.
- **Usage rules:** clear space as a share of the mark (for example its cap height), minimum size in px and mm, colour versions (full colour, one colour, reversed), a misuse list (stretching, rotation, recolouring outside the palette, insufficient contrast, drop shadows, outlines, gradients, crowding the clear space), shown with the real artwork, and allowed motion.
- **A wordmark is drawn, not typed.** Start from a typeface, convert to outlines, then adjust spacing, joins and details so it no longer depends on a font file. Make two masters if needed (display and small). Never retype it. If a typed placeholder is kept in a design file for alignment, hide it.
- **No wordmark?** Then the name is set as a typographic lockup with rules: typeface, weight, tracking, alignment to the symbol.
- **Originality:** run a reverse image search and a trademark database check on the final mark. Generic shapes (swooshes, globes, initials in circles, leaves) collide often.

**Option: a mark-derived system.** The mark never changes; the system is derived from its geometry: angle, proportion and rhythm become the pattern, the grid and the motion. With a slanted mark, the slant angle is the same in every application. Strong for systematic brands; less useful for expressive or illustrative ones.

## Typography

**Decide:** how many families, their roles, licences, and a type scale per medium.

**Principles:**
- **Roles before fonts:** a workhorse (UI, body text, almost everything) and, optionally, a voice or display face with a narrow role.
- **Language coverage first:** proof the candidates with real text in every target language, including diacritics and special characters (for example ő ű, ł ż, ç ã, stacked Vietnamese accents), at body size, *before* choosing. A font swap after the applications are built is expensive.
- **Licences per surface:** desktop, web, app embedding, email, social and video, broadcast. Record them in the book.
- **Fallbacks:** email and office tools (Word, PowerPoint, Google Docs) need system or freely available fallback fonts. Define them, with size adjustments if the metrics differ.
- **A scale per medium** (web, slides, print, social) with the same role names everywhere (display, h1, h2, body, caption, label), so a role means the same thing on every surface.
- **The voice face gets limits:** a minimum size and a "never for" list (for example numbers, company names, body text, labels, buttons, small print). Put it at the top of the typography chapter; exceptions creep in fast.
- **Optical pairing:** when two faces sit on the same line or side by side, match their x-heights by measurement, not by nominal size. Render both, measure the x-height, derive a size multiplier. Font metadata can be off by several percent. At large sizes, a display weight one step lighter often looks right.

**Options:**
- one family: the simplest and most consistent;
- system + voice pair: sans + serif, or sans + mono;
- expressive display face + neutral text face.

**Default system:** sizes, line-heights, tracking, strong styles, the heading scale for desktop and mobile, and the text colour tiers come from `typography-system.md` (Typography golden rules — by Lóránt). Use it unless the brand has a stated reason not to, and log any deviation.

**Possible default pairing:** one grotesque or neo-grotesque sans for everything, plus one serif in a strict voice role (for example, one serif sentence per surface).

## Colour

**Decide:** roles first, then values. Typical roles: background, surface, text (primary, secondary), line, brand or accent, interaction (link, focus), semantic (success, warning, error, info), data or supplementary colours.

**Principles:**
- **Contrast:** use the threshold set at intake. Build a contrast matrix: every foreground colour against every background colour, computed from the actual values and marked against AA normal (4.5:1), AA large (3:1) and AAA (7:1). Recompute it whenever a base value changes.
- **Derived colours are tools, not brand colours.** Tints, shades and harmonies generated from the palette become official only when the user adopts one as a logged decision.
- **Brand colour carrying text** must be legible: pair it with a text colour that passes.
- **Semantic colours stay separate from the brand colour.** An error message is never in the brand colour. If the brand colour is close to the error red, make focus and filled states neutral.
- **Text colour tiers** (primary, secondary, tertiary, disabled) follow `typography-system.md`: fixed contrast targets, and adjacent tiers at least 1.5× apart.
- **One link colour** everywhere.
- **No two similar hues side by side doing different jobs.**
- **Dark mode:** not pure black but a tinted dark; contrast recomputed for both modes; accents usually need lighter values on dark.
- **Work in a perceptual colour space** (OKLCH) when generating scales and lighter or darker variants, so the steps look even.
- **Contextual colour** (multi-client or multi-product brands): one source hue, two values. On light backgrounds, the value that passes the text threshold; on dark, the same hue lifted in OKLCH. Recompute when the base changes.
- **Exceptions are named:** image-like figures (diagrams, UI illustrations) are treated as images.

**Options, by accent strategy:**

| Strategy | Feel | Suits |
|---|---|---|
| One accent, everything else neutral | calm, precise, premium | professional services, tech, personal brands |
| A small palette (2–4 brand colours, each with a role) | friendly, flexible | consumer brands, retail, organisations with several programmes |
| Expressive multi-colour | energetic, playful | children, culture, festivals, food |

**Possible default (restrained):**
- One coloured element per surface at rest; everything else neutral.
- Colour only in designated places (a large number, a meter, a band, a link), never on body text, headlines, labels or page backgrounds.
- Interaction as a second axis: on hover, in an open state or in a detail view, more colour may appear (a full-colour image, a coloured card), as long as the at-rest rule holds.
- Layers separated by hairlines rather than lighter fills; tints reserved for states and small fills, not for containers.

## Layout, grid and spacing

- **One spacing unit** across all media (4 or 8 px), turned into spacing tokens.
- **A module grid per medium** (web, slides, print, social), derived from the format where possible. For example, 1920×1080 divides into 16×9 square modules of 120 px.
- **Layout types:** centred (covers, closing pages) and edge-anchored (content pages). Name which surfaces use which.
- **Social:** safe areas and the crops each platform applies on mobile.
- **Print:** bleed, margins, CMYK or Pantone conversions verified with a proof.

## Imagery

- **Photography:** subject, light, colour treatment, cropping, people or no people, own photos or stock; with do / don't examples.
- **Illustration:** style, line weight, colour use, level of detail.
- **Icons:** grid (for example 24 px), stroke weight, corners and caps, filled or outline; consistent with the mark's geometry.
- **Data visualisation:** colour order, neutral defaults, the rule for highlighting.
- In digital brands, imagery rules are often interaction rules (what happens on hover or when opened). They can live in the Motion chapter instead.
- **Rights:** a licence or proof of ownership for every image used in the book and the templates.

## Patterns and graphic elements (optional)

Derived from the mark or the core tension. A small set, each with its use and its limits. They support content and never compete with it.

## Motion (optional; load-bearing for digital-first brands)

- An easing set and a duration scale.
- 1–3 brand gestures: signature movements that recur.
- A base rule, for example "motion explains a change; it never decorates".
- Reduced-motion behaviour for users who switch animation off.
