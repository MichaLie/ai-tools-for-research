#!/usr/bin/env python3
"""Validate tools/*.yml against the schema in CLAUDE.md. Exit 1 on any failure."""
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent

REQUIRED = ["name", "category", "url", "description", "access", "domain", "status",
            "tier", "added"]
OPTIONAL = ["provider", "last_verified", "notes"]
ACCESS = {"free", "freemium", "paid", "institutional", "waitlist", "unknown"}
DOMAIN = {"general", "life-sciences"}
STATUS = {"active", "candidate", "needs-review", "deprecated", "acquired"}
TIER = {"core", "extended"}
MAX_CORE_PER_CATEGORY = 6


def main() -> int:
    errors = []
    warnings = []
    categories = yaml.safe_load((ROOT / "categories.yml").read_text())
    cat_slugs = set(categories)

    seen_names, seen_urls = {}, {}
    files = sorted((ROOT / "tools").glob("*.yml"))
    if not files:
        errors.append("tools/ contains no .yml files")

    for f in files:
        t = yaml.safe_load(f.read_text())
        where = f"tools/{f.name}"
        for field in REQUIRED:
            if not t.get(field):
                errors.append(f"{where}: missing required field '{field}'")
        for field in t:
            if field not in REQUIRED + OPTIONAL:
                errors.append(f"{where}: unknown field '{field}'")
        if t.get("category") and t["category"] not in cat_slugs:
            errors.append(f"{where}: category '{t['category']}' not in categories.yml")
        if t.get("access") not in ACCESS:
            errors.append(f"{where}: access '{t.get('access')}' not one of {sorted(ACCESS)}")
        if t.get("domain") not in DOMAIN:
            errors.append(f"{where}: domain '{t.get('domain')}' not one of {sorted(DOMAIN)}")
        if t.get("status") not in STATUS:
            errors.append(f"{where}: status '{t.get('status')}' not one of {sorted(STATUS)}")
        if t.get("tier") not in TIER:
            errors.append(f"{where}: tier '{t.get('tier')}' not one of {sorted(TIER)}")
        if t.get("added") and not re.fullmatch(r"\d{4}-\d{2}", str(t["added"])):
            errors.append(f"{where}: added '{t['added']}' is not YYYY-MM")
        lv = t.get("last_verified")
        if lv is not None and not re.fullmatch(r"\d{4}-\d{2}-\d{2}", str(lv)):
            errors.append(f"{where}: last_verified '{lv}' is not YYYY-MM-DD or null")
        if t.get("url") and not str(t["url"]).startswith("https://"):
            errors.append(f"{where}: url must start with https://")

        name = (t.get("name") or "").casefold()
        if name in seen_names:
            errors.append(f"{where}: duplicate name with {seen_names[name]}")
        seen_names[name] = f.name
        url = (t.get("url") or "").rstrip("/")
        if url and url in seen_urls:
            # legitimate when several entries are features of one product;
            # flag it so the next sweep tries to find more specific URLs
            warnings.append(f"{where}: shares url with {seen_urls[url]} ({url})")
        seen_urls[url] = f.name

    core_counts = {}
    for f in files:
        t = yaml.safe_load(f.read_text())
        if t.get("tier") == "core" and t.get("status") == "active":
            core_counts[t.get("category")] = core_counts.get(t.get("category"), 0) + 1
    for cat, n in sorted(core_counts.items()):
        if n > MAX_CORE_PER_CATEGORY:
            errors.append(f"category '{cat}' has {n} active core tools"
                          f" (max {MAX_CORE_PER_CATEGORY}) — one must be displaced")

    for w in warnings:
        print("warn:", w)
    if errors:
        print(f"FAIL — {len(errors)} problem(s):")
        for e in errors:
            print(" ", e)
        return 1
    print(f"OK — {len(files)} tools, {len(cat_slugs)} categories, no schema violations")
    return 0


if __name__ == "__main__":
    sys.exit(main())
