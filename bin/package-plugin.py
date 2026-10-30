#!/usr/bin/env python3
"""Build allowlisted local-plugin and submission-skill archives."""

import json
import re
import struct
from urllib.parse import urlsplit
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile



def validate_submission(plugin: Path, manifest: dict, compat: dict) -> None:
    """Check local submission facts; public access and portal checks remain separate."""
    extension = manifest["extensions"]["com.openai"]
    interface = extension["interface"]
    for key, limit in (("displayName", 30), ("shortDescription", 30),
                       ("longDescription", 4000), ("developerName", 80)):
        value = interface.get(key)
        if not isinstance(value, str) or not value.strip() or len(value) > limit:
            raise ValueError(f"Invalid {key}: required, at most {limit} characters")
    categories = {"Business & Operations", "Communication", "Creativity",
                  "Data & Analytics", "Developer Tools", "Education & Research",
                  "Entertainment", "Finance", "Healthcare", "Other", "Productivity",
                  "Scientific Research", "Security", "Travel"}
    if interface.get("category") not in categories:
        raise ValueError("Unsupported listing category")

    def https(value: str, field: str) -> None:
        if not isinstance(value, str) or len(value) > 1024 or any(c.isspace() for c in value):
            raise ValueError(f"Invalid HTTPS URL: {field}")
        parsed = urlsplit(value)
        if parsed.scheme != "https" or not parsed.hostname or parsed.username or parsed.password:
            raise ValueError(f"Invalid public HTTPS URL: {field}")

    for key in ("websiteURL", "supportURL", "privacyPolicyURL", "termsOfServiceURL"):
        https(interface.get(key), key)
    prompts = interface.get("defaultPrompt", [])
    prompts = [prompts] if isinstance(prompts, str) else prompts
    if not isinstance(prompts, list) or len(prompts) > 3:
        raise ValueError("At most three starter prompts are supported")
    normalized = []
    for prompt in prompts:
        if (not isinstance(prompt, str) or not prompt.strip() or len(prompt) > 128
                or "\n" in prompt or "\r" in prompt or "@" in prompt):
            raise ValueError("Invalid starter prompt")
        normalized.append(" ".join(prompt.split()))
    if len(set(normalized)) != len(normalized):
        raise ValueError("Starter prompts must be unique")

    for key in ("logo", "composerIcon"):
        path = plugin / interface[key]
        if not path.resolve().is_relative_to(plugin.resolve()) or path.is_symlink():
            raise ValueError(f"Unsafe asset path: {key}")
        data = path.read_bytes()
        # This package uses PNGs; detect the actual format rather than the suffix.
        if len(data) < 24 or data[:8] != b"\x89PNG\r\n\x1a\n":
            raise ValueError(f"Expected a PNG asset: {key}")
        width, height = struct.unpack(">II", data[16:24])
        if width != height or not 48 <= width <= 4096 or len(data) > 5 * 1024 * 1024:
            raise ValueError(f"Invalid icon dimensions or size: {key}")

    if (plugin / ".app.json").exists():
        raise ValueError("Public upload must not include .app.json")
    for obj in (manifest, compat):
        if (obj.get("apps") is not None or
                obj.get("extensions", {}).get("com.openai", {}).get("apps") is not None):
            raise ValueError("Public upload must not declare app bindings")
    for key in ("review", "publication"):
        if extension.get(key) != compat.get("extensions", {}).get("com.openai", {}).get(key):
            raise ValueError(f"Manifest mismatch: {key}")
    review = extension.get("review", {})
    for kind, count in (("positive", 5), ("negative", 3)):
        cases = review.get("test_cases", {}).get(kind, [])
        if len(cases) != count:
            raise ValueError(f"Expected {count} {kind} cases")
        required = ("description", "prompt", "tools_triggered", "expected_behavior") if kind == "positive" else ("description", "prompt")
        for case in cases:
            if any(not isinstance(case.get(k), str) or not case[k].strip() for k in required):
                raise ValueError(f"Missing required string field in {kind} case")
    https(review.get("demo_recording_url"), "demo_recording_url")
    if not isinstance(review.get("commerce"), bool) or not review.get("commerce_description", "").strip():
        raise ValueError("Commerce declaration and description are required by this release")
    publication = extension.get("publication", {})
    if publication.get("countries") != ["US"]:
        raise ValueError("This release is explicitly limited to the United States")
    if not isinstance(publication.get("release_notes"), str) or not publication["release_notes"].strip():
        raise ValueError("Release notes must describe this version")


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
    validate_submission(plugin, manifest, compat)
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
