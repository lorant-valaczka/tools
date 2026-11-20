# Communication levels

Brand work is full of terms that designers use without thinking (vector, bleed, kerning, tokens, CMYK) and that mean nothing to most people. A bakery owner who is told "I'll export the logo as SVG" doesn't know what they received or what to do with it. So set a level for the person you're talking to, and a level for each group of brandbook readers, and adapt to both.

The level is about vocabulary and familiarity with design work, not intelligence. A level-1 person can make sharp decisions about their brand; they just shouldn't have to learn a trade vocabulary to do it.

## Contents
- The three levels
- Inferring the level
- What changes per level
- The same thing at three levels
- Rules for every level
- Ready-to-forward messages
- Glossary

## The three levels

| Level | Who, typically | Signals |
|---|---|---|
| **1 · Newcomer**: no design background | owner of a non-design business, founder, private person, volunteer | describes needs in everyday words ("I need a logo and stuff"), sends photos or screenshots rather than files, asks what a term means |
| **2 · Familiar**: knows some terms | marketer, communications lead, office manager, social media manager, developer outside UI | uses some terms correctly (logo versions, brand colours, Canva brand kit, style guide), sends PDFs or old guidelines, works in Canva or Office |
| **3 · Professional** | designer, art director, brand strategist, design-system developer | uses trade terms on their own (vector, kerning, tokens, CMYK, x-height), sends source files (Figma, layered SVG, AI) |

## Inferring the level

- **Don't ask "how much do you know about design?"** It's awkward, and people misjudge themselves. Infer the level from the first message, the person's role and the materials they send.
- **State it in half a sentence** in the brief message (the one after the inventory), so it can be corrected:
  - level 1: "I'll keep this free of design jargon. If you're at home in this field, tell me and I'll switch."
  - level 2: "I'll use the common terms and explain the specialist ones. Tell me if you'd like it plainer or more technical."
  - level 3: "I'll use the trade terms. Tell me if you'd like plainer language, for example for other readers."
- **If you're unsure between two levels, pick the lower one.** It's easier to speed up than to win back a confused reader.
- **Adjust per topic.** Knowledge is uneven: a marketer knows positioning but not file formats; a developer knows tokens but not typography. If someone uses a term correctly on their own, don't explain it to them again, whatever their level.
- **Switch when asked, or at clear signals:** questions about basic terms (go down), or the person correcting your simplifications (go up). Record any change in the brief.

## What changes per level

| | 1 · Newcomer | 2 · Familiar | 3 · Professional |
|---|---|---|---|
| **Wording** | everyday words; a term only when the person will meet it again (at a printer, in Canva), explained once in one sentence | common terms used freely; specialist ones explained once | trade terms, no explanations |
| **Decisions** | framed as outcomes ("should the sign be readable from across the street?"), shown visually side by side | outcome plus the main criteria | framed as parameters ("AA or AAA threshold?") |
| **Technical decisions** | Claude decides, logs them as defaults, and tells only the consequences | Claude decides; one line on what and why | discussed as now |
| **Process** | the next step and what the person has to do; phases named in plain words | phases with short descriptions | phases and gates as in the skill |
| **Handoff** | a who-gets-which-file table and ready-to-forward messages to suppliers | a file list with what each file is for | specifications |

**What a technical decision is:** how something is achieved, as opposed to what the brand is or what it costs. Colour space, token format, file formats, grid unit, the exact contrast threshold, font file formats, export settings. At level 1 these are not put to the person.

**What is never hidden, at any level: the consequences.** If a technical choice costs money (a paid font licence), takes time (a print proof), limits something later (a font that isn't available in Canva or Google Slides), creates a task for the person (asking the printer for a colour value), or carries a legal or rights question (who owns the logo files), say so in plain words, and let them decide where the decision is theirs.

**Decisions that always belong to the person, at every level:** meaning, taste, money, time, legal and rights questions, and anything customers will see.

## The same thing at three levels

| Situation | 1 · Newcomer | 2 · Familiar | 3 · Professional |
|---|---|---|---|
| Logo files | "You'll get the logo in two kinds of file. One can be enlarged to any size without getting blurry: send that one to the printer and the sign maker. The other is an ordinary image: use that one on Instagram." | "The logo comes as SVG (vector, for print and signs) and PNG (for screens)." | "Logo: SVG, PNG @1x/@2x, print-ready PDF." |
| Contrast | "Should the lettering on the sign be readable from across the street? Then the text and its background need to be clearly different in brightness; this yellow with white text isn't." | "White text on this yellow fails the usual accessibility contrast standard; dark text works." | "White on #FFD43B is 1.4:1, below AA; #1A1A1A on it is 12.2:1." |
| Font licence | "This typeface costs about €300 to use on the website. A free one that looks similar would also work in Canva. Which do you prefer?" | "The web licence for this font is about €300; the free alternative is also available in Canva." | "Web licence ~€300, desktop included; free OFL alternative available in Canva and Google Fonts." |
| Colour for print | "Ask the printer for a test print of the green before the full run. Screens and paper show colours differently, and this avoids a surprise." | "Ask the printer for the CMYK value of the green and a proof." | "CMYK from the printer's profile, plus a proof; Pantone match if it's a spot-colour job." |

## Rules for every level

- **Explain once.** At the first use, one plain sentence, in the conversation and in the glossary. After that the term is used freely; don't re-explain it in every message.
- **No condescension.** No "don't worry, it's simple", no exclamation marks to sound friendly, no simplified decisions dressed up as complete ones.
- **Consistency.** Use the glossary's wording, so the same term is explained the same way every time and matches the brandbook.
- **The skill's own terms are internal.** "Path B", "gate", "Develop", "Define sheet", "core tension", "test set" are words for you. At levels 1 and 2, describe what happens instead ("next, I'll show you two different looks side by side on your sign, a post and a bag").

## Ready-to-forward messages

At levels 1 and 2, the hardest part is often talking to suppliers: the printer, the sign maker, the web developer, the person who runs social media. When a surface needs something from a supplier, draft a short message the person can send as it is, in their language:

- what the file is and which one to use;
- the values the supplier needs (size, colours, typeface names);
- what to ask for in return (a proof, their file requirements, a deadline).

The person sends it themselves. Mark any value you're unsure of as a question to the supplier rather than a fact.

## Glossary

Plain-language explanations for level 1 and 2 conversations, and the source for the brandbook's glossary. Translate them into the user's language, keeping the wording close.

| Term | Plain explanation |
|---|---|
| Vector file (SVG, PDF, EPS, AI) | A logo or graphic drawn from shapes rather than dots, so it stays sharp at any size. Printers and sign makers need this kind. |
| Raster image (PNG, JPG) | An ordinary image made of dots (pixels). Fine on screens at the size it was made for; blurry if enlarged. |
| SVG | The most common vector format for the web. Opens in browsers and design tools. |
| PNG | An image format that can have a transparent background, so the logo can sit on any colour. |
| Print-ready PDF | A PDF prepared to the printer's requirements (size, bleed, colours), which they can print directly. |
| Resolution (DPI) | How many dots per inch an image has. Print needs far more (around 300) than screens. |
| RGB | How screens mix colours. Colours for anything digital are given in RGB, usually as a hex code. |
| Hex code | A six-character colour code such as #2E7D32. Used in Canva, websites and design tools. |
| CMYK | How printers mix colours from four inks. The same colour has different values on screen and in print. |
| Pantone (spot colour) | A specific ink picked from a standard swatch book, so a colour prints exactly the same every time. Costs more than CMYK. |
| Proof | A test print before the full run, to check colours and details. |
| Bleed | A few millimetres of extra image beyond the trim edge, so no white strip appears if the cut is slightly off. |
| Safe area | The part of a layout that won't be cropped, for example on a phone screen or a social media preview. |
| Contrast | How clearly text stands out from its background. Low contrast makes text hard to read, especially at a distance or on a phone. |
| Typeface and font family | A designed set of letters (for example Montserrat). The family includes its weights and styles. |
| Weight | How thick the letters are: light, regular, bold, and so on. |
| Font licence | Permission to use a typeface. It can differ for desktop, website, app and other uses; some fonts are free for everything. |
| Kerning and letter spacing | The spacing between letters. Adjusted by hand in a logo, set once for text. |
| x-height | The height of lowercase letters such as x. Two typefaces at the same size can look different sizes because of it. |
| Grid | Invisible guides that keep layouts consistent, so pages and posts feel like they belong together. |
| Clear space | The empty area that must stay around the logo, so it doesn't get crowded. |
| Minimum size | The smallest size at which the logo is still clear; below it, a simplified version is used. |
| Wordmark | A logo that is the name itself, drawn as lettering. |
| Lockup | A fixed arrangement of the symbol and the name that is always used together. |
| Favicon | The tiny icon in the browser tab, next to the page title. |
| Template | A ready-made layout (for example in Canva) where only the text and images are replaced. |
| Brand kit | Canva's place for a brand's logos, colours and fonts, so everyone uses the same ones. |
| Design tokens | A file holding every colour, size and font value in one place, which websites and design tools read from. |
| Mockup | A realistic preview of the design on the real object (a bag, a sign, a phone). |
