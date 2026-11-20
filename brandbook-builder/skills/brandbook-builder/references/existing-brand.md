# Existing brands: Paths B and C

Read this when part or all of the brand already exists. The common thread: audit before you design, and never redesign quietly under another label.

## Path B: complete what exists

- **Keep items are constraints.** Derive the missing parts from them: typography that matches the existing mark's geometry, neutrals that support the existing brand colour, a grid that fits the existing formats.
- **Evolve items** get a short, explicit change list with before and after. Show the change next to the original.
- **When a Keep item blocks a good system**, for example the logo fails below 32 px or the brand colour fails contrast with every text colour, raise it as a decision point. Options: keep it with a documented workaround / make a small fix / replace it. Don't silently work around it.
- Discover includes the audit below, limited to what exists.

## Path C: document as-is

- **Audit first.** Collect every live surface. Sample the values actually in use (colours, fonts, sizes); they often differ from the "official" ones. List every contradiction as a numbered decision point.
- **Define is extracted, not invented.** Write the positioning, attributes and voice from the existing material, then have the user confirm or correct them.
- **Codify what works, flag what doesn't.** Recommend a fix for each problem, but don't redesign under the label of documentation. If the problems are big enough to need a redesign, say so and offer the refresh route.
- **Output:** the brandbook and tokens reflecting the confirmed decisions.

## Path C: refresh

- **Agree the level of change** before any sketching:
  - *light touch*: cleanup and consistency, nothing a customer would notice;
  - *evolution*: a refined mark, an updated palette and type, clearly the same brand;
  - *bold*: a new expression that keeps the recognised equity.
- **Equity:** what people actually recognise (a colour, a shape, a name style, a sound). Keep at least one strong equity unless the explicit goal is a break.
- **Directions** are the 2–3 levels, shown on the same test set, next to the current version.
- **Migration plan:** what changes where, in what order, and how long old assets may stay in circulation.

## Path C: apply to a product or design system

**Keep the brand separate from the design system.** Brand values live in their own variable collection or token group, bound only to brand and documentation components. The design system's components and semantic tokens stay brand-neutral. That way the same system can carry another brand, and a brand change never breaks a component.

**Re-skinning an existing design system with a brand:**

1. Work in a copy, never in the source or template file.
2. Generate a full primitive scale from the brand colour (for example 50 to 950, plus dark-mode tints) on an even OKLCH lightness ladder. Anchor the input colour at a mid-dark step (around 600), so text-on-colour combinations work.
3. Overwrite the primitives in place, keeping the same names or IDs, so existing bindings survive.
4. Rebind the semantic tokens that depend on the brand: text on brand colour, brand-coloured text, focus ring, hover, and their dark-mode variants.
5. Fonts: map weights explicitly when the brand font lacks one (for example no Semibold, so map to Medium or Bold), then rebind the font-weight tokens.
6. If the brand colour is close to the error colour: neutral focus and filled states.
7. Check contrast with the standard agreed at intake. WCAG 2 contrast misjudges some hues (saturated reds and oranges especially); use APCA as a second opinion where it matters.
8. Replace logos and images; audit for leftover foreign content (old brand names, images, colours).
9. Scan for unbound or hard-coded values that escaped the token system.
