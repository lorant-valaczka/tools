# Maintaining this repository

Notes for adding tools and publishing releases.

## Layout

```
<repo>/
├─ README.md                         the tool cards
├─ MAINTAINING.md                    this file
├─ .claude-plugin/marketplace.json   Claude Code marketplace: one entry per tool
├─ scripts/package.py                validates a tool and builds its release files
├─ <tool>/
│  ├─ tool.json                      card data: the website and the README read from it
│  ├─ cover.png                      card image
│  ├─ README.md, CHANGELOG.md, LICENSE
│  ├─ .claude-plugin/plugin.json     name = folder name; the version lives here
│  └─ skills/<skill>/SKILL.md (+ references/, LICENSE.txt)
└─ dist/                             built release files (not committed)
```

## Names and addresses

- Repository: `lorant-valaczka/tools`.
- Marketplace name: `tools-by-valaczka` (in `.claude-plugin/marketplace.json`). Users type it in the install command. ASCII letters, digits, `.`, `_` and `-` only, and never `<owner>-<repo>`.

## Still open

- [ ] Add `cover.png` for each tool, in the same ratio as the cards on the website, then add it to the tool's card in `README.md`.
- [ ] Add `<tool>/.claude-plugin/icon.png` for each tool: a square PNG, 512–2048 px, under 2 MB (SVG and WebP aren't accepted). `claude plugin validate` warns without it, and the plugin directory uses it as the listing icon.

Before every push: no test runs, workspaces or private material in the folder.

## Adding a tool

1. Create a folder named after the tool (lowercase, hyphens).
2. Add `.claude-plugin/plugin.json` with the same `name` as the folder, a `version`, `description`, `author`, `license` and `keywords`.
3. Put each skill in `skills/<skill-name>/SKILL.md`. The skill's `name` matches its folder.
4. Add `tool.json` (copy the shape from `brandbook-builder/tool.json`), `README.md`, `CHANGELOG.md`, `LICENSE`, `cover.png` and `.claude-plugin/icon.png`.
5. Add an entry to `.claude-plugin/marketplace.json` with `"source": "./<tool>"`. Keep the version only in `plugin.json`.
6. Add the tool's card to `README.md`.
7. Release it (below).

## Releasing a version

1. Update the version in `<tool>/.claude-plugin/plugin.json`.
2. Update `<tool>/tool.json`: `version`, `release_tag` (`<tool>-v<version>`) and `updated`.
3. Add the changes to `<tool>/CHANGELOG.md`, and update the version and links in the card in `README.md`.
4. Build and check:
   ```bash
   python scripts/package.py <tool>
   ```
   ```bash
   claude plugin validate .
   ```
5. Commit, then create a GitHub release with the tag `<tool>-v<version>` and attach `dist/<tool>.skill` and `dist/<tool>.zip`.

Download links on the website follow one pattern, built from `tool.json`:

```
https://github.com/lorant-valaczka/tools/releases/download/<release_tag>/<downloads.skill or downloads.zip>
```
