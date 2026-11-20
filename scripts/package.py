"""Validate and package the tools in this repository.

Usage:
    python scripts/package.py brandbook-builder     package one tool
    python scripts/package.py --all                 package every tool

For each tool it checks the plugin manifest, tool.json and every skill, then
writes two release files into dist/:
    <tool>.skill   the skill folder, for upload in the Claude app
    <tool>.zip     the whole tool folder (plugin, README, CHANGELOG, LICENSE)

Standard library only. Run it from the repository root.
"""

import json
import re
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DIST = ROOT / "dist"
SKIP_NAMES = {".DS_Store", "__pycache__"}
SKILL_ROOT_SKIP = {"evals"}
ALLOWED_KEYS = {"name", "description", "license", "allowed-tools", "metadata", "compatibility"}


def fail(msg):
    print(f"  ERROR: {msg}")
    return False


def check_skill(skill_dir):
    ok = True
    text = (skill_dir / "SKILL.md").read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return fail(f"{skill_dir.name}: SKILL.md has no frontmatter")
    fm = m.group(1)
    keys = set(re.findall(r"^([a-z_-]+):", fm, re.M))
    if keys - ALLOWED_KEYS:
        ok = fail(f"{skill_dir.name}: unexpected frontmatter keys {sorted(keys - ALLOWED_KEYS)}")
    name = re.search(r"^name:\s*(.+)$", fm, re.M)
    if not name or not re.fullmatch(r"[a-z0-9-]{1,64}", name.group(1).strip()):
        ok = fail(f"{skill_dir.name}: name missing or not lowercase-hyphen")
    elif name.group(1).strip() != skill_dir.name:
        ok = fail(f"{skill_dir.name}: name '{name.group(1).strip()}' differs from folder name")
    desc = re.search(r'^description:\s*"?(.*?)"?$', fm, re.M)
    if not desc:
        ok = fail(f"{skill_dir.name}: description missing")
    elif len(desc.group(1)) > 1024 or "<" in desc.group(1) or ">" in desc.group(1):
        ok = fail(f"{skill_dir.name}: description over 1024 chars or contains < >")
    # every referenced file in references/ must exist
    refs = set(re.findall(r"references/([A-Za-z0-9_.-]+\.md)", text))
    for f in skill_dir.glob("references/*.md"):
        refs |= set(re.findall(r"`([a-z0-9-]+\.md)`", f.read_text(encoding="utf-8")))
    missing = [r for r in sorted(refs) if not (skill_dir / "references" / r).exists() and r != "SKILL.md"]
    if missing:
        ok = fail(f"{skill_dir.name}: referenced but missing: {missing}")
    return ok


def files_under(base, skip_root=frozenset()):
    for p in sorted(base.rglob("*")):
        rel = p.relative_to(base)
        if not p.is_file() or any(part in SKIP_NAMES for part in rel.parts):
            continue
        if rel.parts and rel.parts[0] in skip_root:
            continue
        yield p


def package(tool):
    tool_dir = ROOT / tool
    print(f"{tool}")
    manifest = tool_dir / ".claude-plugin" / "plugin.json"
    if not manifest.exists():
        return fail("no .claude-plugin/plugin.json")
    plugin = json.loads(manifest.read_text(encoding="utf-8"))
    ok = True
    if plugin.get("name") != tool:
        ok = fail(f"plugin name '{plugin.get('name')}' differs from folder name")
    card_file = tool_dir / "tool.json"
    if card_file.exists():
        card = json.loads(card_file.read_text(encoding="utf-8"))
        if card.get("version") != plugin.get("version"):
            ok = fail(f"tool.json version {card.get('version')} != plugin.json {plugin.get('version')}")
        if card.get("release_tag") != f"{tool}-v{plugin.get('version')}":
            ok = fail(f"tool.json release_tag should be {tool}-v{plugin.get('version')}")
    else:
        ok = fail("no tool.json (the card data)")
    skills = sorted(p.parent for p in tool_dir.glob("skills/*/SKILL.md"))
    if not skills:
        ok = fail("no skills/<name>/SKILL.md")
    for s in skills:
        ok = check_skill(s) and ok
    if not ok:
        return False

    DIST.mkdir(exist_ok=True)
    zip_path = DIST / f"{tool}.zip"
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
        for f in files_under(tool_dir):
            z.write(f, f.relative_to(tool_dir).as_posix())
    print(f"  wrote dist/{zip_path.name}")
    for s in skills:
        skill_path = DIST / (f"{tool}.skill" if len(skills) == 1 else f"{s.name}.skill")
        with zipfile.ZipFile(skill_path, "w", zipfile.ZIP_DEFLATED) as z:
            for f in files_under(s, SKILL_ROOT_SKIP):
                z.write(f, f.relative_to(s.parent).as_posix())
        print(f"  wrote dist/{skill_path.name}")
    print(f"  version {plugin.get('version')}, release tag {tool}-v{plugin.get('version')}")
    return True


def main(args):
    if not args:
        print(__doc__)
        return 1
    if args == ["--all"]:
        tools = sorted(p.parent.parent.name for p in ROOT.glob("*/.claude-plugin/plugin.json"))
    else:
        tools = args
    results = [package(t) for t in tools]
    return 0 if all(results) else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
