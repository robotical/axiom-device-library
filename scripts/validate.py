#!/usr/bin/env python3
"""Check repository structure and JSON, without claiming hardware compatibility."""

import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]


def require(condition, message):
    if not condition:
        raise ValueError(message)


def unique_keys(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, f"Duplicate JSON key: {key}")
        result[key] = value
    return result


def reject_constant(value):
    raise ValueError(f"Invalid JSON constant: {value}")


def load_json(path):
    return json.loads(
        path.read_text(encoding="utf-8"),
        object_pairs_hook=unique_keys,
        parse_constant=reject_constant,
    )


def validate_profile(folder):
    require(re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._-]{0,79}", folder.name), "Invalid profile folder name")
    for name in ("profile.json", "metadata.json", "README.md", "test-results/TEMPLATE.md"):
        path = folder / name
        require(path.is_file(), f"Missing {name}")
        require(path.read_text(encoding="utf-8").strip(), f"Empty {name}")

    profile = load_json(folder / "profile.json")
    metadata = load_json(folder / "metadata.json")
    require(isinstance(profile, dict), "profile.json must contain an object")
    require(isinstance(metadata, dict), "metadata.json must contain an object")
    require(
        type(metadata.get("schemaVersion")) is int and metadata["schemaVersion"] == 1,
        "metadata.schemaVersion must be 1",
    )
    require(metadata.get("name") == folder.name, "metadata.name must match the folder name")
    require(profile.get("deviceType") == folder.name, "profile.deviceType must match the folder name")
    require(isinstance(profile.get("devInfoJson"), dict), "profile.devInfoJson must be an object")

    for key in ("title", "manufacturer", "reviewStatus"):
        value = metadata.get(key)
        require(isinstance(value, str) and value.strip(), f"metadata.{key} must be nonempty")

    require(metadata.get("profile") == "profile.json", "metadata.profile must be profile.json")
    require(metadata.get("documentation") == "README.md", "metadata.documentation must be README.md")

    reports = metadata.get("testReports")
    require(isinstance(reports, list), "metadata.testReports must be a list")
    report_root = (folder / "test-results").resolve()
    for report in reports:
        require(isinstance(report, str) and report.strip(), "Test report paths must be nonempty strings")
        require(not Path(report).is_absolute(), "Test report paths must be relative")
        path = (folder / report).resolve()
        require(path.is_relative_to(report_root), "Test reports must stay inside test-results/")
        require(path.suffix == ".md" and path.is_file(), f"Missing Markdown report: {report}")
        require(path.name != "TEMPLATE.md", "The template is not a completed test report")
        require(path.read_text(encoding="utf-8").strip(), f"Empty test report: {report}")


def main():
    errors = []
    profiles = ROOT / "profiles"
    folders = sorted(path for path in profiles.glob("*") if path.is_dir())
    if not folders:
        errors.append("No integration folders found under profiles/")

    for path in sorted(profiles.rglob("*.json")):
        try:
            load_json(path)
        except (OSError, ValueError) as error:
            errors.append(f"{path.relative_to(ROOT)}: {error}")

    for folder in folders:
        try:
            validate_profile(folder)
        except (OSError, ValueError) as error:
            errors.append(f"{folder.relative_to(ROOT)}: {error}")

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print(f"Validated {len(folders)} integration(s). Hardware compatibility is not checked.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
