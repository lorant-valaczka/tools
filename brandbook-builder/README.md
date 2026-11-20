# Brandbook Builder

A skill for Claude that guides a complete brand design process, from the first question to a finished brandbook.

It starts by asking what you already have. Then it builds the brand from scratch, completes a partial identity, or documents, refreshes or applies an existing brand to a product. Whatever the starting point, it ends in a brandbook someone else can apply without asking the designer, backed by a decision log and a single source of design values (tokens).

## Before you start

**This is a long process.** A real brand doesn't come out of one conversation. As a rough guide:

- **Essential scope** (a sole trader, a small business, a personal brand): about 5–8 working sessions.
- **Complete scope** (a company, a product, several surfaces): about 10–20 sessions, more with many surfaces, several rounds or a design tool in the loop.

**It uses a lot of usage.** The skill itself is light, but the work isn't: sketches, rounds, screenshots and files add up. Over a whole project, expect several hundred thousand tokens for essential scope and well over a million for complete scope. If that's more than you want to invest, start with the essential scope or a smaller first version.

**What it doesn't replace:**
- Claude can draw geometric, typographic and simple symbolic marks. For illustrative or hand-drawn marks it develops the concept and a drawing brief, and the final drawing is better done by you or an illustrator.
- Name and trademark screening is preliminary, not legal advice. Check with a trademark attorney before you invest in a name.
- Colours for print are confirmed with your printer, with a proof.

## What it does

**Three starting points**, chosen after the first question:

| Path | When |
|---|---|
| **A · From scratch** | nothing usable exists, or you want a clean start |
| **B · Complete what exists** | some pieces exist, such as a logo and a colour but no system |
| **C · Document, refresh or apply** | a working brand exists, but there's no brandbook, it's outdated, or it needs applying to a product or design system |

**Eight phases with gates.** Nothing moves on until you approve the step before it: intake → discover → define → directions → build out → applications → audit → brandbook and handoff.

**What you get at the end:**
- the brandbook (HTML by default, with a PDF export; Figma or other tools if you prefer);
- design tokens (JSON and CSS), the single source of every colour, size and font value;
- logo files in every version, with honest colour modes (RGB for screens, CMYK only from a real colour-managed export);
- templates for the surfaces you agreed on;
- the decision log, with every decision and the alternatives that were rejected.

## Highlights

- **Adapts to you.** It sets one of three levels: newcomer, familiar, or professional. A bakery owner gets plain language, decisions framed as outcomes, and ready-to-forward messages for the printer. A designer gets trade terms and specs.
- **Works across sessions and in parallel.** A hub log plus one file per workstream (typography, iconography, imagery…), one writer per file, cross-stream changes approved before they apply. Every session ends with a starter message for the next one, so nothing depends on chat history.
- **Typography golden rules, by Lóránt.** A tested text system: four body levels with regular and strong styles, line-height and tracking ratios for display sizes, a mobile rule, and text colour tiers with contrast targets.
- **Honest deliverables.** No invented facts, no placeholder buttons, no RGB files labelled CMYK, no generated tints passed off as brand colours.
- **Works with or without Figma.**

## Install

| Where | How |
|---|---|
| **Claude app** (web, desktop, mobile) | Download [`brandbook-builder.skill`](../../../releases/download/brandbook-builder-v1.5.0/brandbook-builder.skill) and upload it under Settings, in the Skills section. Code execution and file creation must be turned on. |
| **Claude Code** | Run `claude plugin marketplace add lorant-valaczka/tools`, then `claude plugin install brandbook-builder@tools-by-valaczka`. Or copy `skills/brandbook-builder` into `~/.claude/skills/` for all your projects, or into a project's `.claude/skills/` for one. |
| **Claude API / Agent SDK** | Use the `skills/brandbook-builder` folder as a skill. |
| **Other tools** | The skill uses the open [Agent Skills](https://agentskills.io) format, so other tools that support it may load it. It's written for Claude and tested only with Claude. |

**Recommended setup:**
- **Not a designer?** Use the Claude app, inside one Project per brand. Keep the log and token files in the project files, and replace them with the updated versions after each session.
- **A designer or a developer?** Use Claude Code, or the Code tab of the desktop app, with one folder per brand. The log, the tokens and the exports live on disk, and parallel sessions read the same files.
- **Model:** the most capable model you have for directions and build-out; a lighter one is fine for documentation and checks.

## Getting started

Just describe what you need; the skill starts on its own. For example:

- "I'm opening a bakery in the spring and I need a brand."
- "We have a logo and a brand colour but nothing else. We need guidelines before our website relaunch."
- "Our association has an old style guide nobody follows. We need a proper brandbook for new volunteers, not a redesign."

The first reply is a heads-up about the length of the process and two questions: what you already have, and where the brand needs to work first.

**To continue in a new session,** paste the starter message you got at the end of the previous session. It names the files to read, for example:

> Let's continue the Morzsa brand with the brandbook-builder skill. Workstream: typography. First read morzsa-brand-log.md, log/typography.md and tokens/tokens.json.

## What's inside

```
skills/brandbook-builder/
├─ SKILL.md                         the process: paths, phases, gates, working rules
├─ LICENSE.txt                      licence notice (full terms in LICENSE at the root)
└─ references/
   ├─ intake.md                     materials, paths, brief questions, defaults
   ├─ communication-levels.md       the three levels, plain-language examples, glossary
   ├─ decision-log.md               hub and workstream templates, parallel work, session handoff
   ├─ strategy.md                   discover, define, voice, naming
   ├─ identity.md                   mark, typography, colour, grid, imagery, patterns, motion
   ├─ typography-system.md          typography golden rules, by Lóránt
   ├─ existing-brand.md             completing, documenting, refreshing, applying to a design system
   ├─ applications.md               test set, order of application, surfaces by brand type
   ├─ brandbook.md                  layout, chapters, downloads and colour modes, optional modules
   └─ checklists.md                 audit, chapter close, handoff, pitfalls that became rules
```

Claude reads each reference file only when its phase starts, so the skill stays light in context.

## Credits

Method, rules and typography system by Lóránt, [valaczka.com](https://valaczka.com). Written with Claude.

The typography golden rules come from many typographic systems he has built.

## License

[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/), with one additional permission. In short:

- **You may** use the skill, share it and adapt it, as long as you credit "Brandbook Builder by Lóránt", link to the original and say if you changed it.
- **You may** use it as a tool in your own work, including paid client projects.
- **You may not** sell the skill or a modified version of it, or include it in a paid product or service.
- **What you make with it,** such as a brandbook, is yours.

The full terms are in [LICENSE](LICENSE).

## Changelog

See [CHANGELOG.md](CHANGELOG.md).
