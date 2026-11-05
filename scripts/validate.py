#!/usr/bin/env python3
"""Validate tools/*.yml and categories.yml against the protocol in AGENTS.md.

Exit 1 on any error. Rules that need editorial judgment are reported as
warnings and do not fail the run; `--strict` turns warnings into errors (useful
as a clean-room check before a course-edition tag).
"""
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
RETIRED = {"deprecated", "acquired"}
TIER = {"core", "extended"}
STAGES = {"everyday", "discover", "plan", "collect", "write", "publish", "impact"}
MAX_CORE_PER_CATEGORY = 6
MAX_DESCRIPTION_WORDS = 40      # style guide: "One or two sentences, ≤ 40 words"
MAX_CORE_WITH_DEEP_DIVE = 3     # "keep core minimal (2–3 exemplars)" where a deep_dive exists
BLURB_PREFIX = "The task:"      # categories.yml: blurb "starts 'The task:'"
# the style guide bans marketing adjectives; the first three are its own examples
MARKETING = re.compile(
    r"\b(revolutionary|cutting-edge|seamless(?:ly)?|state-of-the-art|best-in-class"
    r"|game-changing|next-generation|world-class)\b", re.I)


def main() -> int:
    strict = "--strict" in sys.argv[1:]
    errors = []
    warnings = []
    categories = yaml.safe_load((ROOT / "categories.yml").read_text())
    cat_slugs = set(categories)
    for cslug, cmeta in categories.items():
        where = f"categories.yml: {cslug}"
        if cmeta.get("stage") not in STAGES:
            errors.append(f"{where} stage '{cmeta.get('stage')}' not one of {sorted(STAGES)}")
        if not str(cmeta.get("blurb", "")).startswith(BLURB_PREFIX):
            errors.append(f"{where} blurb must start with '{BLURB_PREFIX}'")
        dd = cmeta.get("deep_dive")
        if dd is not None and not (isinstance(dd, dict) and dd.get("title")
                                   and str(dd.get("url", "")).startswith("https://")):
            errors.append(f"{where} deep_dive needs 'title' and an https 'url'")

    files = sorted((ROOT / "tools").glob("*.yml"))
    if not files:
        errors.append("tools/ contains no .yml files")
    tools = [(f, yaml.safe_load(f.read_text())) for f in files]

    seen_names, seen_urls = {}, {}
    for f, t in tools:
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

        # --- protocol rules from AGENTS.md ---
        desc = str(t.get("description") or "")
        n_words = len(desc.split())
        if n_words > MAX_DESCRIPTION_WORDS:
            errors.append(f"{where}: description is {n_words} words"
                          f" (style guide: ≤ {MAX_DESCRIPTION_WORDS})")
        m = MARKETING.search(desc)
        if m:
            warnings.append(f"{where}: description uses '{m.group(0)}' — the style guide"
                            " bans marketing adjectives")
        status, tier, access = t.get("status"), t.get("tier"), t.get("access")
        if access == "waitlist" and status == "active":
            errors.append(f"{where}: waitlist-gated tools are status: candidate,"
                          " not active (admission gate 2)")
        if status == "candidate" and tier == "core":
            errors.append(f"{where}: a candidate has not passed the gate and cannot"
                          " hold a core slot")
        if status in RETIRED and not t.get("notes"):
            errors.append(f"{where}: {status} tools need a one-line epitaph in notes")
        if status in ("candidate", "needs-review") and not t.get("notes"):
            warnings.append(f"{where}: no notes — record why it is {status}")
        if status == "active" and tier == "core" and not t.get("notes"):
            warnings.append(f"{where}: core slot without notes — AGENTS.md asks for the"
                            " adoption evidence or sole-use-case rationale")

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
    for _, t in tools:
        if t.get("tier") == "core" and t.get("status") == "active":
            core_counts[t.get("category")] = core_counts.get(t.get("category"), 0) + 1
    for cat, n in sorted(core_counts.items()):
        if n > MAX_CORE_PER_CATEGORY:
            errors.append(f"category '{cat}' has {n} active core tools"
                          f" (max {MAX_CORE_PER_CATEGORY}) — one must be displaced")
        elif n > MAX_CORE_WITH_DEEP_DIVE and categories.get(cat, {}).get("deep_dive"):
            warnings.append(f"category '{cat}' has {n} active core tools but a deep_dive"
                            f" index — AGENTS.md says keep core to 2–3 exemplars there")

    for w in warnings:
        print("warn:", w)
    if strict and warnings:
        errors += [f"(strict) {w}" for w in warnings]
    if errors:
        print(f"FAIL — {len(errors)} problem(s):")
        for e in errors:
            print(" ", e)
        return 1

    by_status = {}
    for _, t in tools:
        by_status[t.get("status")] = by_status.get(t.get("status"), 0) + 1
    status_txt = ", ".join(f"{by_status.get(s, 0)} {s}" for s in
                           ("active", "candidate", "needs-review") if by_status.get(s))
    n_retired = sum(by_status.get(s, 0) for s in RETIRED)
    if n_retired:
        status_txt += f", {n_retired} retired"
    dates = [str(t["last_verified"]) for _, t in tools if t.get("last_verified")]
    oldest = min(dates) if dates else "never"
    n_oldest = dates.count(oldest)
    print(f"OK — {len(files)} tools ({status_txt}), {len(cat_slugs)} categories,"
          f" no schema violations; oldest verification {oldest} ({n_oldest} tools);"
          f" {len(warnings)} warning(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
