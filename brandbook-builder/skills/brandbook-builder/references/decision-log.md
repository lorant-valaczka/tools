# Decision log, workstreams and sessions

A brand process outlives any single conversation. It runs over many sessions, sometimes in parallel threads (typography in one, iconography in another), and a conversation's context eventually fills up and gets compressed. The only things that survive reliably are files. So every decision lives in a file the moment it's made, every thread has its own file, and every session ends in a state the next one can pick up without the previous conversation.

## Contents
- Folder structure
- The hub: the brand log
- Workstream files
- Running workstreams in parallel
- Session handoff
- Where the files live

## Folder structure

```
<brand>/
├─ <brand>-brand-log.md    the hub: brief, foundations, workstreams, cross-stream decisions, session log
├─ log/                    one file per workstream, plus archive/
├─ tokens/                 tokens.json and tokens.css, the single source of values
├─ sources/                the user's original files, never modified
├─ sketches/               directions and rounds, dated
├─ exports/                logo files and other exports, by asset, format and colour mode
└─ brandbook/              the book (HTML, PDF)
```

**Keep it as small as the project.** An essential-scope project with one thread of work needs only the hub and the tokens. Workstream files appear when the work splits. At level 1, the user doesn't need to understand this structure: Claude keeps it and hands them a starter message for the next session.

## The hub: the brand log

`<brand>-brand-log.md` is the source of truth. The brandbook, the tokens and the design files implement it; if they disagree, the log wins and the others get fixed.

```markdown
# <Brand> brand log
Last updated: <date> · by: <workstream or "hub">

## Brief
Path: A / B / C · Scope: essential / complete · Brandbook: format, language, readers
Conversation level: 1 / 2 / 3 (inferred from: …) · Reader levels: e.g. owner 1, printer 3
Who or what: … · Offer: … · Audience: …
Surfaces, in priority order: …
Tools: …
Constraints: fixed elements, deadline, licence budget, languages …
Defaults used without asking: … (listed so they can be challenged)

## Inventory (Path B and C)
| Item | Source | Keep / Evolve / Replace | Notes (quality, licence, consistency) |

## Foundations
The shared, closed decisions every workstream builds on, each with the date it was closed:
Define sheet (positioning, attributes and what the brand is not, core tension, voice) ·
mark · colour base · type base · spacing unit and grid.
Changing a foundation is a cross-stream decision.

## Workstreams
| Stream | File | Status | Owns (chapters, token groups) | Depends on | Last session |

## Cross-stream decisions
| Date | From stream | Decision | Affects | Status: proposed / approved / applied in … |

## Decisions (hub level: brief, path, scope, foundations)
| Date | Area | Decision | Rejected alternatives | Why |

## Parked
| Item | Essence (one sentence) | Why parked | What would unblock it | Existing material |

## Open questions
- [ ] …

## Session log
| Date | Stream | What happened | Next step |
```

## Workstream files

One file per thread of work in `log/`, for example `log/typography.md`, `log/iconography.md`, `log/imagery.md`.

```markdown
# <Brand>: <stream>

## Status
3–5 lines, rewritten every session: where this stream stands.

## Scope
Owns: chapters, token groups, files this stream may change.
Reads only: what it depends on (foundations, other streams' tokens).

## Decisions
| Date | Decision | Rejected alternatives | Why |

## Open
- [ ] …

## Proposals for other streams
Decisions this stream needs from others, or that would change something others own.
Each one is also copied to the hub's cross-stream table.

## Resume here
Next step · files to read first · the last approved state (file names, versions) · what the user still owes.
```

**Superseded decisions:** a new dated row overrides the old one, and the old row stays as history. Status lines and "Resume here" are rewritten, not appended; stale lines are deleted.

**Size:** when a workstream file grows past about 15 KB, move closed rounds and superseded detail to `log/archive/<stream>-<date>.md`. The decisions table stays in the live file.

## Running workstreams in parallel

Parallel threads are fine once their foundations are closed. Starting one earlier means building on something that may still move.

| Workstream | Can start once these are closed |
|---|---|
| Voice and messaging | Define |
| Typography | Define; the mark, if the wordmark shares letterforms with the typeface |
| Colour | Define; the mark |
| Layout and grid | type base; spacing unit |
| Iconography | mark geometry; type weights (icon strokes are matched to them); grid unit |
| Illustration | colour; mark geometry or the core tension |
| Photography and imagery | colour; Define |
| Patterns | mark |
| Motion | mark; colour; layout for digital brands |
| Applications | the chapters each surface uses |

**Rules:**
1. **One writer per file.** A session writes only its own workstream file. It writes to the hub only at the start and end of the session (session log, its own workstream row, cross-stream proposals), and always reads the hub again right before writing, adds rows, and never rewrites another stream's rows.
2. **Token ownership.** Each stream owns its token groups (typography owns `type.*` and the text tiers, iconography owns `icon.*`) and never edits another group. Shared tokens (colour base, spacing, base type) change only through an approved cross-stream decision.
3. **Cross-stream effects go through the hub.** If a decision in one stream changes something another stream owns, don't change it locally. Example: iconography wants a 1.75 px stroke that only works with a heavier type weight. It goes into the hub as a proposal, naming the affected streams. Once the user approves it, each affected stream applies it in its next session and marks it applied.
4. **Foundations are frozen while streams run.** Reopening a foundation (say, the colour base) is a cross-stream decision; dependent streams re-read it before continuing.
5. **No decision lives only in the chat.** Write it, dated, in the stream file in the same session, right after it's made, not at the end. A session can end abruptly.
6. **Conflicts are decided, never resolved silently.** If two streams' decisions contradict each other, neither wins by default: raise a numbered decision point to the user in the hub.
7. **Closing a stream:** its workstream row becomes "closed", its chapter in the brandbook is updated, and its decisions feed the book's Record chapter. The stream file stays as the history.

## Session handoff

### When to start a new session
- At the end of a phase or a chapter.
- Before starting a parallel workstream: one session per stream.
- When the conversation gets long: earlier details start slipping, the tool warns about context, or replies slow down. Hand off while everything is still in view; don't wait for the context to run out.

### Closing a session
1. **Workstream file:** rewrite the status; add this session's decisions, dated; update the open items; write "Resume here".
2. **Hub:** one row in the session log; update this stream's row; add any cross-stream proposals.
3. **Tokens** regenerated if any value changed.
4. **Files saved** with clear names and dates: sketches, specimens, exports. Nothing exists only in the chat.
5. **The next step for the user:** a ready-to-paste starter message for the next session. In a Claude app Project, also give them the updated log and token files to replace in the project files, because project files don't update themselves.

**Starter message template** (in the user's language):

> Let's continue the <brand> brand with the brandbook-builder skill. Workstream: <stream>. First read <brand>-brand-log.md, log/<stream>.md and tokens/tokens.json.

### Opening a session
1. Read the hub, this stream's file and the tokens. Not the previous conversation, not old sketches or rounds.
2. Check the hub for cross-stream decisions and foundation changes since this stream's last session. Apply the approved ones first.
3. Say in one or two sentences where you're resuming and what comes next, then continue.
4. If the files contradict what the user says now, ask; don't guess which is right.

### Keeping sessions light
- Take screenshots at reduced size, and only when something must be seen.
- Read only the parts of design files you need (specific frames or nodes, not whole files).
- Don't paste whole files into the chat; refer to them by name and path.
- Old sketches and rounds stay in `sketches/`; reopen one only when a decision needs it.

## Where the files live

- **Claude Code, or the Code tab of the desktop app:** a real project folder with the structure above. The best fit for parallel workstreams, since each session reads the same files on disk.
- **Claude app (web, desktop, mobile):** one Project per brand. The hub, the workstream files and the tokens go into the project files. After each session, replace them with the updated versions Claude provides.
- **Other tools:** any folder or drive the user controls. The rules are the same; only the place changes.
