# Intake: materials, path, brief

Intake turns "we need a brand" into a confirmed plan. It has five steps: the first message (in SKILL.md), the inventory, choosing the path, the brief, and confirming the plan. Everything decided here goes into the brand log.

## 1. Inventory what came in

Open and look at everything the user shares (files, links, screenshots) before asking more questions.

**Handling source files.** When the user points to a folder of source files:
- Show the inventory (what's there, which files can be used) before processing anything.
- Never modify originals; work on copies. Prefer master files (vector sources) for extraction, and reuse good existing exports.
- Keep the originals in `sources/` and put new exports in `exports/` (folder structure in `decision-log.md`), organised by asset, format and colour mode. Don't overwrite existing exports without the user's yes.
- Stay inside the folder the user named. Don't upload master files to outside services without explicit approval.
- If a file can't be opened or read (a format your tools can't parse, no access), say so and ask for an export (PDF or SVG). Never claim to have read a file you couldn't. Then list it in the log's inventory table, one row per item, and mark each:

- **Keep**: fixed; the new work builds around it.
- **Evolve**: stays recognisable, but may be refined.
- **Replace**: will be redesigned.

Ask the user about anything you can't judge from the material itself: emotional attachment, legal status, what customers recognise, what was paid for.

Be honest about quality, but don't fix anything yet. Flag it in the notes column. What to check by item type:

| Item | Check |
|---|---|
| Logo | Is there a vector file? Which versions exist? Is it legible at 16–32 px? Is it registered as a trademark? |
| Colours | The values actually used on live surfaces. Sample them; they often differ from the "official" ones |
| Fonts | Names, licences per surface (desktop, web, app, email, social), coverage of the target languages |
| Old guidelines | Date; how much of them is actually followed |
| Live surfaces | Website, social, print, packaging: what is consistent, what has drifted |
| Strategy documents | Positioning, audience, values: still true? |
| Photos and illustrations | Ownership or licence, quality, consistency of style |

**Estimate the conversation level at the same time** (`communication-levels.md`): from the first message, the person's role and what they sent. Photos of a shop sign and "I need a logo and stuff" point to level 1; an old style guide PDF and a Canva brand kit to level 2; layered source files and trade terms to level 3. Record it in the brief.

## 2. Choose the path

- If mark, colour and typography are all Keep or Evolve, and are used consistently: **Path C** (document, refresh or apply).
- If at least one core element (mark, colour, typography, strategy) is Keep: **Path B** (complete what exists).
- Otherwise: **Path A** (from scratch).

The user's explicit wish overrides the rule ("I have a logo but I want to start fresh" means Path A, with the old logo as background material). Mixed cases are normal: say which part follows which path.

## 3. The brief: ask once, then use defaults

After the inventory, send one message with the questions that are still open, usually 4–6. Ask only what you can't infer from the materials. Include the half sentence that states the language level you'll use (wording in `communication-levels.md`), and phrase the questions at that level: at level 1, "how should people feel when they walk in?" rather than "brand attributes". Once the brief is set, don't re-ask these questions during the build; it erodes trust and slows the work.

### Ask if unknown

1. **What the brand is:** company, product, organisation, local business or person; what it offers; to whom.
2. **Surfaces and priority:** where it must work first (website, social, packaging, signage, app or product UI, print, decks, CV, menu…). The top three shape most decisions.
3. **Constraints:** fixed elements, deadline, budget for fonts and photography, the languages it must work in.
4. **Tools:** what the user and the future brandbook readers work in. Figma is optional; HTML works for everyone.
5. **The brandbook:** who will use it (the user alone, a marketing team, designers, external agencies, suppliers such as a printer), in which format and language. This also sets the reader levels: a book read by the owner and the printer needs plain rules and technical values side by side.
6. **Feel** (optional but valuable): three words the brand should feel like; one to three brands they admire or dislike, and why.

### Decide early: ask if relevant, otherwise default and mark it

These are the decisions that, when made late, forced rework in past projects. If a topic doesn't apply, skip it. If it applies and the user hasn't answered, use the default and list it under "Defaults used without asking" in the brief, so it can be challenged.

| Topic | Why early | Default |
|---|---|---|
| Brand architecture: parent brand, sub-brands, shared DNA | Changes the colour and mark system | A single brand |
| Own brand colour, or contextual colour (e.g., each client's colour in a multi-client brand) | Changes the whole colour model | Own brand colour |
| Typeface licences per surface, and language coverage | Late discoveries force font swaps after applications are built | Fonts with an open licence unless there is a budget; proofed in all target languages before choosing |
| Contrast standard and threshold | Must be stated up front, not negotiated mid-build | WCAG 2.2 AA: 4.5:1 for body text, 3:1 for large text and UI components. Stricter option for key brand text pairs: 7:1 (AAA), or APCA Lc 75 for body text |
| Base mode (light or dark) and the role of the second mode | Digital brands only | Light, with dark derived from it |
| Identity texts in one place: name per language, descriptor or title, tagline, links, names and nicknames that must not be used | Otherwise they drift between surfaces | Collected in the log, reused everywhere |
| Who owns content (copy, photos) | Blocks applications if unclear | The user |
| Brandbook format and structure | Decided at the end, it causes a large reshuffle | HTML, chapter structure from `brandbook.md` |
| Where values live | One source from day one | `tokens/tokens.json` plus `tokens/tokens.css` (folder structure in `decision-log.md`) |
| Imagery, photography and icons in the first version, and where they sit in the book | Scope | Included if a top-three surface needs them |
| Scope level | Sets the depth of every phase | Essential for a person or sole trader; complete otherwise |

**Scope levels.** *Essential*: minimum brandbook, one round of 2 directions, three applications, short Record. *Complete*: full chapter set, 3 directions, every agreed surface, brand architecture and token pipeline where relevant.

## 4. Confirm the plan

One message, short, at the user's level (at levels 1 and 2, describe the steps in plain words rather than naming paths and phases):
- the path (and which parts follow which path, if mixed),
- the phases with their gates, in a line each,
- what the user will be asked to decide at each gate,
- the deliverables (the brandbook in the agreed format, tokens, logo files, templates, the log),
- **how long it will take**: a rough number of working sessions, and a plain reminder that the process uses a lot of usage overall. As a rough guide, essential scope takes about 5–8 sessions and complete scope 10–20, more with many surfaces, several rounds or a design tool in the loop. If that's more than the user wants to invest, offer the essential scope or a smaller first version.
- how the work continues between sessions: the files keep it, and at the end of each session they'll get a short message to start the next one (`decision-log.md`).

Wait for a yes. Then create the log from the hub template in `decision-log.md`, write the brief into it, and start Discover (`strategy.md`).
