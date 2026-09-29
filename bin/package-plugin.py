#!/usr/bin/env python3
"""Build allowlisted local-plugin and submission-skill archives."""

import json
import re
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile


def main() -> None:
    root = Path(__file__).resolve().parent.parent
    plugin = root / "in-case-of-crisis"
    manifest = json.loads((plugin / "plugin.json").read_text())
    compat = json.loads((plugin / ".codex-plugin/plugin.json").read_text())
    version = manifest["version"]
    if not re.fullmatch(r"\d+\.\d+\.\d+", version):
        raise ValueError("Expected a three-part release version")
    for field in ("name", "version", "description", "author", "license"):
        if manifest[field] != compat[field]:
            raise ValueError(f"Manifest mismatch: {field}")
    if manifest["name"] != plugin.name:
        raise ValueError("Plugin name must match directory")
    if manifest["extensions"]["com.openai"]["interface"] != compat["interface"]:
        raise ValueError("OpenAI presentation metadata differs")
    if json.loads((plugin / "mcp.json").read_text()) != json.loads(
        (plugin / ".mcp.json").read_text()
    ):
        raise ValueError("MCP configurations differ")
    skill = "skills/in-case-of-crisis/SKILL.md"
    if f'version: "{version}"' not in (plugin / skill).read_text():
        raise ValueError("Skill version differs")
    shared = ["plugin.json", ".codex-plugin/plugin.json", skill, "icon.png", "LICENSE", "README.md"]
    files = shared + ["mcp.json", ".mcp.json"]
    for name in files:
        path = plugin / name
        if not path.is_file() or path.is_symlink() or not path.resolve().is_relative_to(plugin.resolve()):
            raise ValueError(f"Missing or unsafe package file: {name}")
    dist = root / "dist"
    dist.mkdir(exist_ok=True)
    for suffix, names in (("", files), ("-skills", shared)):
        archive = dist / f"{plugin.name}{suffix}-{version}.zip"
        with ZipFile(archive, "w", ZIP_DEFLATED) as output:
            for name in names:
                content = (plugin / name).read_bytes()
                if suffix and name == ".codex-plugin/plugin.json":
                    skill_manifest = {k: v for k, v in compat.items() if k != "mcpServers"}
                    content = (json.dumps(skill_manifest, indent=2) + "\n").encode()
                output.writestr(f"{plugin.name}/{name}", content)
        with ZipFile(archive) as check:
            if check.testzip() is not None:
                raise ValueError(f"Archive integrity check failed: {archive}")
        print(archive)


if __name__ == "__main__":
    main()
