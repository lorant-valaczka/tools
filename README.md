# Design skills

Skills for Claude by Lóránt: design processes and rules from practice, packaged so anyone can use them. Each tool lives in its own folder, with its own README, changelog and licence.

## Tools

### Brandbook Builder · v1.5.0

A complete brand design process, from the first question to a finished brandbook.

Starts by asking what you already have, then builds the brand from scratch, completes a partial identity, or documents, refreshes or applies an existing brand. Ends in a brandbook, design tokens and a decision log.

Works in the Claude app and Claude Code · Licence: CC BY-NC 4.0

[Download .skill](../../releases/download/brandbook-builder-v1.5.0/brandbook-builder.skill) · [Download plugin .zip](../../releases/download/brandbook-builder-v1.5.0/brandbook-builder.zip) · [Read more](brandbook-builder/README.md)

## Install

**Claude app** (web, desktop, mobile): download the tool's `.skill` file from its release and upload it in Settings, under Skills. Code execution and file creation must be turned on.

**Claude Code:** add this repository as a plugin marketplace once, then install any tool from it:

```bash
claude plugin marketplace add lorant-valaczka/tools
```

```bash
claude plugin install brandbook-builder@tools-by-valaczka
```

Inside a session, the same works as `/plugin marketplace add lorant-valaczka/tools` and `/plugin install brandbook-builder@tools-by-valaczka`. You can also copy a tool's `skills/<name>` folder into `~/.claude/skills/`.

## Licences

Each tool has its own licence, in its folder. Read it before you reuse or share a tool.

## About

Made by Lóránt, [valaczka.com](https://valaczka.com). Written with Claude.
