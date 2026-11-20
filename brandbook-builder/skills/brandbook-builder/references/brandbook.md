# The brandbook

## Contents
- Who it is for
- Format
- Default layout of an HTML book
- Chapter structure
- The chapter pattern
- What the book leaves out
- Downloads and colour modes
- Building an HTML brandbook
- Optional modules

## Who it is for

Write for the person who applies the brand without you: a new designer, an agency, a marketing colleague, the owner a year from now. They need the rule first, then a specimen that shows it, then the values, then the reason. If a rule can't be shown, it is probably not a rule yet.

**Write at the readers' level** (set at intake, see `communication-levels.md`). Books usually have mixed readers: the owner at level 1, a printer or developer at level 3. Layer each rule instead of writing two books: the rule in plain words and the specimen first, then the technical values in a clearly marked "for specialists" block (sizes, colour codes per medium, file and export settings). A level-1 reader can stop before that block and still apply the brand correctly.

## Format (agreed at intake)

| Format | Good for | Notes |
|---|---|---|
| **HTML** (default) | everyone; linkable; values read live from the tokens; interactive specimens | one long scrolling page for small brands, multi-page with a sidebar for complete ones; a print stylesheet or PDF export for sharing |
| PDF | agencies, print-heavy brands, archiving | export it from the HTML or the design tool; keep the source |
| Figma | teams already working in Figma | can host the whole book, or only the asset library next to an HTML book |
| Docs or Notion | teams that edit together | weaker for specimens; link to the assets |

Web references and inspiration used during the design belong in the log, not in the book.

## Default layout of an HTML book

Use this unless the brand has a reason for another layout (a handbook with a numbered chapter strip, or one long scrolling page for a small brand, follow the same rules).

- **Desktop: a persistent navigation panel on the left.** At its top: the wordmark, a small "Brand guidelines" label (a monospace or caps label style works well), and the date of the last update with the version number.
- **Chapter numbers only in the navigation.** Page headers show the title alone; numbers repeated in both places are noise.
- **Each chapter opens with a large header** holding its title. A brand-colour header is an option, and under a one-accent colour rule it can be the surface's single coloured element.
- **At the bottom of the navigation:** the light/dark switch (if the brand has both modes) and the download of the whole guide.
- **Mobile:** the navigation becomes an accessible menu: a labelled button, focus kept inside while it's open, Esc closes it.

## Chapter structure

| # | Chapter | Contents |
|---|---|---|
| 0 | Idea and voice | positioning, attributes and what the brand is not, the core tension, 3 core rules, voice with examples and do / don't, identity texts. At complete scope, voice and messaging can become their own chapter |
| 0.1 | Quick start | one page: a short checklist and the key rules, each linked to its chapter. A bento overview (see Optional modules) can take this role in a visually led book, as long as the checklist stays somewhere |
| 1 | Mark | anatomy, versions, small-size cut, clear space, minimum size, colour versions, favicon and avatar, motion, misuse shown with the real artwork. For a wordmark: drawn logotype, small master, never retype it |
| 2 | Typography | families and roles, body levels with their strong styles, heading scale for desktop and mobile, text colour tiers, lockups, minimum sizes, the "never for" list, fallbacks, licences |
| 3 | Colour | palette cards with the colour name inside the swatch and HEX and RGB values with copy buttons (CMYK only where verified with the printer); neutral scale per mode; roles; accent rules; contextual colour if any; tints and shades, marked as derived; the contrast matrix; semantic colours; named exceptions |
| 4 | Layout and grid | spacing tokens, grids per medium, layout types, safe areas |
| 5 | Imagery | photography, illustration, icons, data visualisation (optional) |
| 6 | Patterns and graphic elements | the set, use, limits (optional) |
| 7 | Motion | easings, durations, brand gestures, the base rule, reduced motion (optional; required for digital-first brands, where image and interaction colour rules can live here too) |
| 8 | Applications | every surface with an image and the rules specific to it |
| T | Tokens and downloads | grouped downloads (see Downloads and colour modes). When any reader is at level 1 or 2, it opens with a who-gets-which-file table (which file goes to the printer, which to Instagram, which to the web developer) and the ready-to-forward supplier messages |
| G | Glossary | the terms used in the book, in plain words (from the glossary in `communication-levels.md`); included when any reader is at level 1 or 2 |
| R | Record | decision history by chapter, parked items, process timeline, version history |

**Why this order:** rules first, reasons last. The chapters move outward from the mark (mark → type → colour → grid → imagery → patterns → motion) because each one derives from the one before. The applications then prove the system, and the Record explains how it got there.

**Minimum (essential scope):** 0, 0.1, 1, 2, 3, 4, 8 (at least three real applications) and T, plus G when any reader is at level 1 or 2. The Record can be a single page.

**The contrast matrix:** every foreground colour of the palette against every background colour, with the ratio computed from the actual values and marked against AA normal text (4.5:1), AA large text (3:1) and AAA normal text (7:1). Showing the foreground as a circle on the background swatch reads well. Recompute it whenever a value changes.

**Derived colours are not brand colours.** Tints, shades and colour harmonies generated from the palette are tools. They become official only when the user adopts one as a logged decision.

## The chapter pattern

Each chapter, and each rule inside it:
1. **Rule**, in one sentence.
2. **Specimen:** a visual that shows it.
3. **Values**, read from the tokens, never retyped by hand. With mixed readers, in the "for specialists" block.
4. **Do / don't**, with images where possible.
5. **Why**, in one or two sentences.

If the chapter has an exception, it is named here, and only here.

## What the book leaves out

- A brand label repeated above every title. The wordmark appears once, in the navigation.
- Decorative navigation icons.
- Approval badges and status banners ("Published", "Approved", "Draft") in the version readers see.
- Generic filler ("use the brand consistently to build recognition") and instructions that apply to any brand.
- Technical implementation details, unless they help the reader decide or act.
- Invented content. A chapter without material is left out, or marked as coming in the next version, never filled with made-up guidance.
- Placeholder content in specimens ("Aa" in every swatch, lorem ipsum): use the colour's name and real brand text.

## Downloads and colour modes

**Groups**, shown only when they have content: logos · images and applications · gradients · videos · fonts and source files · colours.

**Rules:**
- **Originals stay distinct from previews.** A recoloured, resized or cropped preview in the book is never offered as the official artwork. Downloads come from the master files, labelled as originals.
- **RGB for screen formats:** SVG, PNG and web JPEG.
- **CMYK only when it's genuine:** a CMYK JPEG or PDF is offered only if it was made through a real colour-managed export (ideally with the printer's profile). Never label an RGB file as CMYK; PNG and SVG don't carry CMYK at all.
- **Transparency** is preserved wherever the format supports it (SVG, PNG, PDF). A JPEG gets an intentional solid background, named in the file name (for example `-on-white`).
- **Palette exports** come from the tokens, never retyped: JSON and CSS, plus a swatch sheet (SVG, PNG or PDF) for people who don't work with code.
- **File names** follow one pattern: brand, asset, variant, colour, colour mode, for example `brand-logo-horizontal-black-rgb.svg`.
- **Only valid downloads are shown.** Every link is tested and produces a working file; there are no "coming soon" buttons.

## Building an HTML brandbook

- Values come from the tokens file (CSS variables), so the book can't drift from the tokens.
- Specimens are real: live text in the brand fonts, real colour swatches with their computed contrast values.
- The "for specialists" blocks are collapsible (a `<details>` element works), open by default in the print version.
- Terms in the text link to the glossary at their first use in each chapter.
- **It stands alone.** The delivered book works without the tool or session that made it: fonts, media and tokens are bundled or linked to stable copies, and navigation and the theme switch still work.
- **Every visible control works.** No placeholder buttons, no dead links, no download that fails.
- **Light and dark mode**, if the brand has both; specimens show each mode.
- **Accessible:** keyboard navigation, visible focus states, alt text for meaningful images, decorative media kept out of the tab order, reduced-motion preferences respected (animated specimens become static).
- **Videos**, where used: muted, looping, inline, without native controls, paused when off-screen or when the tab is hidden.
- It works on a phone: check at about 390 px wide, with no horizontal overflow.
- Closed pages carry no "draft", "round" or "proposal" wording.
- Version number and date in the navigation; the changelog in the Record.
- If the user wants a PDF, add a print stylesheet (page breaks per chapter, no interactive-only content) and export from it.

## Optional modules

Add these when they help the readers; none is required.

- **Bento overview.** The book's home page as tiles: each summarises a chapter (the logo, a palette strip, a type specimen, an application image) and links to it. Simple widths (1/4, 1/3, 1/2, 2/3, full) and two or three heights; the grid stays responsive and keeps its hierarchy on mobile. A video tile must still work as a link.
- **Live type specimen.** Editable sample text, size, weight, letter spacing, line-height, an uppercase toggle, and foreground and background picked from the palette. It starts from the token values (`typography-system.md`) and can be reset to them. Readers at level 1 learn the system fastest by trying it.
- **Logo colour explorer.** Foreground and background chosen independently from the palette; combinations that fail contrast are flagged. It is labelled as a preview, with the official files in the downloads.
- **Clear-space diagram.** Two dashed outlines: the artwork's real bounds and the outer clear-space boundary, with the value from the rule (for example the cap height). It's a guide, not a measuring tool.
- **Misuse gallery with the real artwork.** Each case generated from the brand's own mark and marked as a don't: stretching, rotation, insufficient contrast, drop shadow, outline, a gradient on the wordmark, colours from outside the palette, crowding the clear space.
- **Published snapshot.** When the book is shared by link, the shared version is a frozen release. Changes collect in the next version and go out as a new release with a version bump. At handoff, agree whether the link always shows the latest release, or each release keeps its own link.
