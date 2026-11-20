# Checklists and pitfalls

## Audit (phase 7)

Read the whole system end to end, as a newcomer would. List every finding as a numbered decision point with options, the recommended one first. Look for:
- errors and stale values (old colour codes, sizes, angles, titles, statuses);
- contradictions between chapters, or between the book and the tokens;
- rules without a specimen, and specimens that break their own rule;
- exceptions that aren't named, or are named in more than one place;
- missing licences (fonts per surface, images, icons);
- identity texts that differ between surfaces;
- parked items whose blockers are gone.

The user answers point by point ("1B, 2A, 3 keep as is"). Apply the answers, log them, then re-run the chapter checklist on the affected chapters.

## Closing a chapter

- [ ] No "round", "proposal" or "draft" text on the closed page.
- [ ] No old values: after every changed decision, search all files for the previous value.
- [ ] The decision is in the log and in the Record.
- [ ] Parallel work: the workstream file is current, its row in the hub updated, and no cross-stream proposal touching this chapter is still open.
- [ ] HTML pages: the mobile view (about 390 px) is clean, with no horizontal overflow.
- [ ] The contrast matrix is current (recomputed after any base colour change).
- [ ] Nothing from "What the book leaves out" (`brandbook.md`) has crept in: repeated brand labels, decorative icons, status banners, filler, invented content.
- [ ] Tokens regenerated; design-tool variables (if any) match them.
- [ ] Brand values are kept separate from any design system's semantic tokens.
- [ ] Identity texts are identical on every surface.
- [ ] The user and Claude mean the same thing by every element in the chapter.
- [ ] Typography chapter: the checks at the end of `typography-system.md` pass.

## Handoff

- [ ] Brandbook complete for the agreed scope, with version number and date.
- [ ] Token files exported (JSON and CSS).
- [ ] Logo files: every version, SVG and PNG, small-size cut, favicon, app icon, avatar.
- [ ] Templates for the agreed surfaces.
- [ ] Every download tested: valid file, honest colour mode (no RGB labelled CMYK, CMYK only from a real colour-managed export), transparency kept where the format allows, originals distinct from previews, file names in the agreed pattern.
- [ ] The HTML book works standalone, every visible control works, and keyboard, focus, reduced motion and both colour modes are checked.
- [ ] Original source files unchanged; exports in their own folder.
- [ ] Licences listed: fonts per surface, images, icons.
- [ ] Decision log up to date; parked list reviewed; every workstream closed or explicitly handed over; no open cross-stream proposals.
- [ ] Open questions handed to the owner, each with a suggested next step.
- [ ] Readers at level 1 or 2: who-gets-which-file table, ready-to-forward supplier messages and glossary included; every term in the book is either plain or in the glossary.

## Pitfalls that became rules

| What happened | Rule |
|---|---|
| After a decision changed, the old value survived in code and text | One source of values; search for the old value after every change |
| Two link colours lived side by side | One link colour, decided once |
| A base colour changed and a contextual colour fell below the contrast threshold | Recompute the contrast matrix on every base change |
| A material was developed in depth, then parked, and later returned in a different place | Detours are allowed; parking is a logged decision, not a deletion |
| Two different understandings of the same element grew in parallel and had to be merged at the end | Proposals stay proposals; two one-sentence purposes at the start; form feedback is not approval of meaning; "do we mean the same thing?" at every part close |
| The log predicted where parked material would end up, and was wrong | Record the essence separately from the placement; don't predict |
| An application produced new rules and the book didn't follow (book 1.0, tokens 1.2) | Write back and bump the version at every surface close |
| Web design started before the web font licence was bought, and that was fine | Licences gate publishing, not design |
| The voice typeface produced old-style numerals, and a company name got set in it | The "never for" list sits at the top of the typography chapter |
| The one-colour rule collided with colourful diagrams | The image-like figure exception is stated up front |
| A person's title differed between surfaces | Identity texts live in one place |
| A typeface had to be swapped late because of missing diacritics | Proof in every target language before choosing |
| The brandbook structure was decided at the end, causing a large reshuffle | Decide format and structure at intake |
| Directions were built twice: in a design tool, then again in HTML | Sketch first; production tools only after the choice |
| Decision points were sent in a bundle | One question, 2–3 numbered options, recommended first |
| One message carried seven decisions, four strategy questions and several requests, over 1,000 words | About five decision points per message; the user's part first; drafts and analysis in the log, summarised in the message |
| A long conversation was compressed and decisions made in it were lost | Write each decision to the file in the same session; switch sessions at phase ends or when the conversation gets long; resume from the files |
| Two parallel threads changed the same values and overwrote each other | One writer per file; token groups owned by one stream; cross-stream changes through the hub |
| Terms like SVG, tokens, CMYK and OKLCH reached a non-designer without explanation | Set a conversation level at intake; explain a term once, in plain words; hide technical decisions at level 1, never their consequences |
