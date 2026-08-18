#!/usr/bin/env python3
"""Regenerate README.md, docs/index.html and exports/ from tools/*.yml + categories.yml.

Deterministic: output depends only on the source files.
"""
import csv
import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent

ACCESS_LABEL = {
    "free": "Free",
    "freemium": "Freemium",
    "paid": "Paid",
    "institutional": "Institutional",
    "waitlist": "Waitlist",
    "unknown": "—",
}

# research-lifecycle stages: slug -> (title, light hex, dark hex)
# palette: dataviz reference categorical slots 1-7, validated against this
# page's surfaces (light #ffffff panels, dark #1f1f25) on 2026-08-18
STAGES = {
    "everyday": ("Everyday AI", "#2a78d6", "#3987e5"),
    "discover": ("Discover & Learn", "#eb6834", "#d95926"),
    "plan": ("Plan & Design", "#1baf7a", "#199e70"),
    "collect": ("Collect & Analyze", "#eda100", "#c98500"),
    "write": ("Write & Illustrate", "#e87ba4", "#d55181"),
    "publish": ("Review & Publish", "#008300", "#008300"),
    "impact": ("Share & Impact", "#4a3aa7", "#9085e9"),
}


def fmt_date(iso):
    months = ["January", "February", "March", "April", "May", "June", "July",
              "August", "September", "October", "November", "December"]
    y, m, d = iso.split("-")
    return f"{int(d)} {months[int(m) - 1]} {y}"


def load():
    categories = yaml.safe_load((ROOT / "categories.yml").read_text())
    tools = []
    for f in sorted((ROOT / "tools").glob("*.yml")):
        t = yaml.safe_load(f.read_text())
        t["slug"] = f.stem
        tools.append(t)
    order = {slug: i for i, slug in enumerate(categories)}
    tools.sort(key=lambda t: (order.get(t["category"], 99), t["name"].casefold()))
    return categories, tools


def build_readme(categories, tools):
    active = [t for t in tools if t["status"] in ("active", "needs-review")]
    candidates = [t for t in tools if t["status"] == "candidate"]
    retired = [t for t in tools if t["status"] in ("deprecated", "acquired")]
    verified_dates = [t["last_verified"] for t in tools if t.get("last_verified")]
    last_verified = fmt_date(max(verified_dates)) if verified_dates else "never"

    lines = [
        "# AI Tools for Scientific Research",
        "",
        "A curated list of AI tools that are actually useful in research work. I keep it",
        "for my courses and workshops on AI in science, which makes it opinionated on",
        "purpose: for each research task you get a handful of tools people really use,",
        "not everything that exists.",
        "",
        f"Right now: {len(active)} tools across {len(categories)} task areas."
        f" Last checked against the live web on {last_verified}.",
        "",
        "This space moves fast. Tools rename, merge and die constantly, so if something",
        "you need is missing, check back in a week or open an issue. For real depth in",
        "three areas (biological foundation models, autonomous science agents,",
        "privacy-first coding and data tools) I keep separate indexes at",
        "[michalie.github.io](https://michalie.github.io/).",
        "",
        "A searchable version of this list, with the task map up top, lives at",
        "[docs/index.html](docs/index.html).",
        "",
        "## How the list works",
        "",
        "Every tool belongs to one task category and is either shown directly (the few",
        "worth putting on a course slide) or folded into \"more tools for this task\"",
        "in its section. Entries marked \\* are flagged for re-verification. Dead tools",
        "are not deleted; they move to the Retired section at the bottom, because the",
        "history is part of the story.",
        "",
        "## The map",
        "",
        "Tasks grouped by research stage:",
        "",
    ]
    for stage, (stitle, _, _) in STAGES.items():
        links = []
        for slug, meta in categories.items():
            if meta.get("stage") != stage:
                continue
            n = sum(1 for t in active if t["category"] == slug)
            if n:
                anchor = meta["title"].lower().replace(" ", "-").replace("&", "").replace("--", "-")
                links.append(f"[{meta['title']}](#{anchor}) ({n})")
        if links:
            lines.append(f"- **{stitle}** · " + " · ".join(links))
    lines.append("")

    for slug, meta in categories.items():
        cat_tools = [t for t in active if t["category"] == slug]
        if not cat_tools:
            continue
        lines += [f"## {meta['title']}", ""]
        if meta.get("blurb"):
            lines += [f"*{meta['blurb']}*", ""]
        if meta.get("deep_dive"):
            dd = meta["deep_dive"]
            lines += [f"**Going deeper:** [{dd['title']}]({dd['url']}) →", ""]

        def row(t):
            flag = " \\*" if t["status"] == "needs-review" else ""
            provider = t.get("provider") or "—"
            desc = t["description"].replace("|", "\\|").replace("\n", " ")
            return (f"| [{t['name']}]({t['url']}){flag} | {provider} |"
                    f" {ACCESS_LABEL[t['access']]} | {desc} |")

        header = ["| Tool | Provider | Access | Description |", "|---|---|---|---|"]
        core = [t for t in cat_tools if t.get("tier") == "core"]
        ext = [t for t in cat_tools if t.get("tier") != "core"]
        lines += header + [row(t) for t in core] + [""]
        if ext:
            lines += [f"<details><summary>More tools for this task ({len(ext)})</summary>",
                      ""] + header + [row(t) for t in ext] + ["", "</details>", ""]

    if candidates:
        lines += ["## Watchlist", "", "Noticed but not properly vetted yet — waitlisted,"
                  " too young, or missing a privacy policy.", ""]
        for t in candidates:
            lines.append(f"- [{t['name']}]({t['url']}) — {t.get('notes') or t['description']}")
        lines.append("")
    if retired:
        lines += ["## Retired", "", "Kept for the record.", ""]
        for t in retired:
            lines.append(f"- **{t['name']}** ({t['status']}) — {t.get('notes') or t['description']}")
        lines.append("")

    lines += [
        "---",
        "",
        "\\* = flagged for re-verification.",
        "",
        "Corrections and suggestions are welcome as issues or PRs. The maintenance rules",
        "live in [AGENTS.md](AGENTS.md); every entry needs a working URL and has to pass",
        "`scripts/validate.py`. This README is generated from [`tools/`](tools/) by",
        "`scripts/build.py` — edit the YAML, not this file.",
        "",
        "Data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Code: MIT.",
        "",
    ]
    (ROOT / "README.md").write_text("\n".join(lines))


def build_exports(categories, tools):
    out = ROOT / "exports"
    out.mkdir(exist_ok=True)
    payload = {
        "title": "AI Tools for Scientific Research",
        "categories": categories,
        "tools": tools,
    }
    (out / "tools.json").write_text(json.dumps(payload, indent=1, ensure_ascii=False) + "\n")
    with (out / "tools.csv").open("w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["category", "name", "provider", "url", "description", "access",
                    "domain", "status", "tier", "added", "last_verified"])
        for t in tools:
            w.writerow([categories[t["category"]]["title"], t["name"], t.get("provider") or "",
                        t["url"], t["description"], t["access"], t["domain"], t["status"],
                        t.get("tier", ""), t["added"], t.get("last_verified") or ""])


def build_site(categories, tools):
    (ROOT / "docs").mkdir(exist_ok=True)
    dates = [t["last_verified"] for t in tools if t.get("last_verified")]
    verified = fmt_date(max(dates)) if dates else "not yet verified"
    stages = {k: {"title": v[0]} for k, v in STAGES.items()}
    payload = json.dumps({"categories": categories, "tools": tools, "stages": stages},
                         ensure_ascii=False)
    light_vars = "\n".join(f"    --st-{k}: {v[1]};" for k, v in STAGES.items())
    dark_vars = "\n".join(f"      --st-{k}: {v[2]};" for k, v in STAGES.items())
    html = (TEMPLATE.replace("__DATA__", payload.replace("</", "<\\/"))
            .replace("__STAGELIGHT__", light_vars)
            .replace("__STAGEDARK__", dark_vars)
            .replace("__VERIFIED__", verified))
    (ROOT / "docs" / "index.html").write_text(html)


# Edges the gap hunts checked and found empty — update when one gets filled
EMPTY_EDGES = [
    "Press-release drafting for a paper — and EurekAlert's guidelines now ban",
    "  AI-generated text outright, so this edge stays empty on purpose",
    "AI conference matching (upload paper, get ranked live CFPs)",
    "Journal-ready figure alt-text from a paper PDF (FigurA11y is not production)",
    "Narrative CV builders (UKRI R4RI / Horizon / NWO templates only)",
    "NIH biosketch: one live indie product exists but fails the recommendable-",
    "  to-students gate (unnamed organization); SciENcv itself is not AI",
]


def build_coverage(categories, tools):
    import re as _re
    dates = [t["last_verified"] for t in tools if t.get("last_verified")]
    verified = max(dates) if dates else "never"
    lines = [
        "# Task-coverage map — AI Tools for Scientific Research",
        "",
        f"Generated from the catalog data: {len(tools)} tools,"
        f" {len(categories)} task categories; newest verification {verified}.",
        "Purpose: input for external gap-hunting — which academic/research tasks",
        "augmentable by AI are NOT yet represented below?",
        "",
        "Scope rules: research workflow only — teaching/grading and general office admin",
        "are deliberately excluded. Depth areas covered by companion indexes (not this",
        "catalog): biological foundation models, autonomous science agents at scale,",
        "privacy-first coding/data agents (https://michalie.github.io/).",
        "",
        "## Covered task types",
        "",
    ]
    for slug, meta in categories.items():
        n = sum(1 for t in tools if t["category"] == slug and t["status"] != "deprecated")
        unit = "tool" if n == 1 else "tools"
        lines.append(f"### {meta['title']} ({n} {unit})")
        lines.append("Task: " + _re.sub(r"^The task: ", "", meta.get("blurb", "")))
        ucs = []
        for t in tools:
            if t["category"] != slug:
                continue
            m = _re.search(r"Unique use case: (.+?)(?: Adoption:| \[|$)", t.get("notes") or "")
            if m:
                ucs.append(m.group(1).strip().rstrip(".").rstrip(";"))
        if ucs:
            lines.append("Specific use cases already covered:")
            lines += [f"- {u}" for u in ucs]
        lines.append("")
    lines += ["## Edges already checked and found EMPTY", ""]
    lines += [f"- {e}" if not e.startswith(" ") else e for e in EMPTY_EDGES]
    lines += [
        "",
        "## What a proposed addition must satisfy",
        "",
        "1. Maps to a research-workflow task; 2. usable this week (no waitlist/demo-only);",
        "3. does something a general assistant (ChatGPT/Claude/Gemini) cannot do well;",
        "4. real organization, privacy policy, transparent pricing; 5. alive and maintained.",
        "Proposals should name the TASK first, then candidate tools with URLs. Working URLs",
        "and honest uncertainty expected — unverifiable claims are useless.",
        "",
    ]
    (ROOT / "docs" / "task-coverage.md").write_text("\n".join(lines))


TEMPLATE = r"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>AI Tools for Scientific Research</title>
<style>
  :root {
    --bg: #f7f7f5; --panel: #ffffff; --ink: #1a1a20; --muted: #6b6b74;
    --line: #e4e4e0; --accent: #275e5a; --accent-ink: #ffffff; --chip: #ecece8;
    --flag: #9a6b00;
__STAGELIGHT__
  }
  @media (prefers-color-scheme: dark) {
    :root {
      --bg: #16161a; --panel: #1f1f25; --ink: #ececf0; --muted: #9a9aa4;
      --line: #2e2e36; --accent: #57a49e; --accent-ink: #10201e; --chip: #2a2a31;
      --flag: #d9a53a;
__STAGEDARK__
    }
  }
  * { box-sizing: border-box; }
  :root { --serif: "Charter", "Iowan Old Style", Georgia, "Times New Roman", serif; }
  body { margin: 0; background: var(--bg); color: var(--ink);
         font: 15px/1.5 -apple-system, "Segoe UI", system-ui, sans-serif; }
  header { padding: 2.4rem 1.2rem 1.4rem; max-width: 62rem; margin: 0 auto;
           border-bottom: 4px double var(--line); }
  h1 { margin: 0 0 .15rem; font: 700 2rem/1.15 var(--serif); letter-spacing: 0; }
  .sub { color: var(--muted); margin: 0 0 1.1rem; font-size: .88rem;
         letter-spacing: .04em; text-transform: uppercase; }
  .controls { display: flex; flex-wrap: wrap; gap: .5rem; align-items: center; }
  input[type=search], select {
    background: var(--panel); color: var(--ink); border: 1px solid var(--line);
    border-radius: 2px; padding: .5rem .7rem; font: inherit;
  }
  input[type=search] { flex: 1 1 14rem; }
  .count { color: var(--muted); font-size: .85rem; margin-left: auto; }
  main { max-width: 62rem; margin: 0 auto; padding: 0 1.2rem 4rem; }
  h2.cat { font: 700 1.12rem/1.3 var(--serif); margin: 1.8rem 0 .15rem;
           padding-bottom: .3rem; border-bottom: 1px solid var(--line); }
  h2.cat small { color: var(--muted); font-weight: 400;
                 font-family: -apple-system, "Segoe UI", system-ui, sans-serif;
                 font-size: .78rem; }
  .idx { font-family: -apple-system, "Segoe UI", system-ui, sans-serif;
         font-size: .72rem; font-weight: 400; color: var(--muted);
         letter-spacing: .06em; margin-right: .45rem; vertical-align: .12em; }
  .intro { max-width: 46rem; font-size: .9rem; line-height: 1.55; color: var(--muted);
           margin: 0 0 .4rem; }
  .intro strong, .intro .date { color: var(--ink); }
  .intro a { color: var(--accent); }
  #map { margin: 1.1rem 0 .5rem; }
  .stage-group { margin: 0 0 .7rem; }
  .stage-lab, .stage-rule {
    display: flex; align-items: center; gap: .5rem; font-size: .72rem;
    font-weight: 600; letter-spacing: .08em; text-transform: uppercase;
    color: var(--muted);
  }
  .stage-lab { margin: 0 0 .4rem; }
  .stage-lab::before, .stage-rule::before {
    content: ""; width: .55rem; height: .55rem; border-radius: 2px;
    background: var(--st); flex: none;
  }
  .bricks { display: grid; grid-template-columns: repeat(auto-fill, minmax(9.5rem, 1fr));
            gap: .45rem; }
  .brick { display: flex; flex-direction: column; gap: .12rem; text-align: left;
           background: var(--panel); border: 1px solid var(--line);
           border-left: 3px solid var(--st); border-radius: 2px;
           padding: .5rem .65rem; cursor: pointer; font: inherit; color: var(--ink); }
  .brick:hover { border-color: var(--st); }
  .brick[aria-pressed="true"] { outline: 2px solid var(--st); outline-offset: -1px; }
  .b-name { font-weight: 600; font-size: .82rem; line-height: 1.25; }
  .b-n { font-size: .72rem; color: var(--muted); }
  .stage-rule { margin: 2.3rem 0 -.9rem; }
  .blurb { color: var(--muted); font-style: italic; margin: 0 0 .3rem; font-size: .9rem; }
  a.deep { display: inline-block; font-size: .72rem; letter-spacing: .07em;
           text-transform: uppercase; color: var(--accent);
           text-decoration: none; margin: 0 0 .6rem; }
  a.deep:hover { text-decoration: underline; text-underline-offset: 3px; }
  details.more { margin: .1rem 0 .9rem; }
  details.more summary { cursor: pointer; color: var(--muted); font-size: .85rem;
                         padding: .25rem 0; user-select: none; }
  details.more .tool { opacity: .88; }
  .tool { background: var(--panel); border: 1px solid var(--line);
          border-radius: 2px; padding: .7rem .9rem; margin: 0 0 .5rem; }
  .row1 { display: flex; flex-wrap: wrap; gap: .55rem; align-items: baseline; }
  .tool a.name { color: var(--ink); font: 600 1.02rem var(--serif);
                 text-decoration: none; }
  .tool a.name:hover { text-decoration: underline; text-underline-offset: 3px; }
  .prov { color: var(--muted); font-size: .85rem; }
  .badge { font-size: .68rem; letter-spacing: .08em; text-transform: uppercase;
           color: var(--muted); white-space: nowrap; }
  .badge.free, .badge.freemium { color: var(--accent); }
  .badge.review { color: var(--flag); }
  .desc { margin: .25rem 0 0; color: var(--ink); }
  .empty { color: var(--muted); padding: 2rem 0; text-align: center; }
  footer { max-width: 62rem; margin: 0 auto; padding: 0 1.2rem 2.5rem;
           color: var(--muted); font-size: .85rem; }
</style>
</head>
<body>
<header>
  <h1>AI Tools for Scientific Research</h1>
  <p class="sub">Curated &amp; verified for academic use · Michaela Liegertová</p>
  <p class="intro"><strong>A map, not an encyclopedia.</strong> Each task shows a small,
  deliberately varied selection of the tools academics actually use — breadth over
  depth; for depth in specific areas, see the companion
  <a href="https://michalie.github.io/" target="_blank" rel="noopener">AI for Science
  indexes</a>. Every entry verified against the live web on <span class="date">__VERIFIED__</span>.
  This territory expands and shifts by the week — if you don't find a tool for your
  use case today, come back next week; the map will have moved.</p>
  <nav id="map" aria-label="Task map"></nav>
  <div class="controls">
    <input type="search" id="q" placeholder="Search tools, providers, descriptions…">
    <select id="cat"><option value="">All categories</option></select>
    <select id="acc">
      <option value="">Any access</option>
      <option value="free">Free</option><option value="freemium">Freemium</option>
      <option value="paid">Paid</option><option value="institutional">Institutional</option>
    </select>
    <span class="count" id="count"></span>
  </div>
</header>
<main id="list"></main>
<footer>Generated from the repository’s <code>tools/</code> directory — the page is a
build artifact; edits belong in the YAML source.</footer>
<script>
const DATA = __DATA__;
const ACCESS = {free:"Free", freemium:"Freemium", paid:"Paid",
                institutional:"Institutional", waitlist:"Waitlist", unknown:"Access?"};
const q = document.getElementById("q"), cat = document.getElementById("cat"),
      acc = document.getElementById("acc"), list = document.getElementById("list"),
      count = document.getElementById("count"), mapEl = document.getElementById("map");
for (const [slug, meta] of Object.entries(DATA.categories)) {
  const o = document.createElement("option"); o.value = slug; o.textContent = meta.title;
  cat.appendChild(o);
}
const esc = s => (s || "").replace(/[&<>"]/g, c => ({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]));
const CATNUM = Object.fromEntries(Object.keys(DATA.categories)
  .map((s, i) => [s, String(i + 1).padStart(2, "0")]));
const card = t => `<div class="tool"><div class="row1">
      <a class="name" href="${esc(t.url)}" target="_blank" rel="noopener">${esc(t.name)}</a>
      ${t.provider ? `<span class="prov">${esc(t.provider)}</span>` : ""}
      <span class="badge ${esc(t.access)}">${ACCESS[t.access]}</span>
      ${t.domain === "life-sciences" ? `<span class="badge">life sciences</span>` : ""}
      ${t.status === "needs-review" ? `<span class="badge review">needs review</span>` : ""}
      </div><p class="desc">${esc(t.description)}</p></div>`;
function render() {
  const term = q.value.trim().toLowerCase();
  const filtering = !!(term || cat.value || acc.value);
  const match = t =>
    (t.status === "active" || t.status === "needs-review") &&
    (!cat.value || t.category === cat.value) &&
    (!acc.value || t.access === acc.value) &&
    (!term || (t.name + " " + (t.provider||"") + " " + t.description).toLowerCase().includes(term));
  let html = "", nCore = 0, nExt = 0, lastStage = null;
  for (const [slug, meta] of Object.entries(DATA.categories)) {
    const inCat = DATA.tools.filter(t => t.category === slug && match(t));
    if (!inCat.length) continue;
    const core = inCat.filter(t => t.tier === "core");
    const ext = inCat.filter(t => t.tier !== "core");
    nCore += core.length; nExt += ext.length;
    if (meta.stage !== lastStage) {
      lastStage = meta.stage;
      html += `<div class="stage-rule" style="--st:var(--st-${esc(meta.stage)})">${esc(DATA.stages[meta.stage].title)}</div>`;
    }
    html += `<h2 class="cat"><span class="idx">${CATNUM[slug]}</span>${esc(meta.title)} <small>· ${inCat.length}</small></h2>`;
    if (meta.blurb) html += `<p class="blurb">${esc(meta.blurb)}</p>`;
    if (meta.deep_dive) html += `<a class="deep" href="${esc(meta.deep_dive.url)}"
      target="_blank" rel="noopener">Going deeper: ${esc(meta.deep_dive.title)} →</a>`;
    html += core.map(card).join("");
    if (ext.length) html += `<details class="more"${filtering ? " open" : ""}>
      <summary>More tools for this task (${ext.length})</summary>${ext.map(card).join("")}</details>`;
  }
  list.innerHTML = html || `<p class="empty">Nothing matches.</p>`;
  count.textContent = `${nCore} core · ${nExt} extended`;
  mapEl.querySelectorAll(".brick").forEach(b =>
    b.setAttribute("aria-pressed", String(b.dataset.cat === cat.value)));
}
function buildMap() {
  let html = "";
  for (const [sk, sv] of Object.entries(DATA.stages)) {
    const catsIn = Object.entries(DATA.categories).filter(([, m]) => m.stage === sk);
    if (!catsIn.length) continue;
    html += `<div class="stage-group"><div class="stage-lab" style="--st:var(--st-${sk})">${esc(sv.title)}</div><div class="bricks">`;
    for (const [slug, m] of catsIn) {
      const n = DATA.tools.filter(t => t.category === slug &&
        (t.status === "active" || t.status === "needs-review")).length;
      html += `<button class="brick" style="--st:var(--st-${sk})" data-cat="${esc(slug)}"
        aria-pressed="false"><span class="b-name">${esc(m.title)}</span>
        <span class="b-n">${n} tool${n === 1 ? "" : "s"}</span></button>`;
    }
    html += `</div></div>`;
  }
  mapEl.innerHTML = html;
  mapEl.querySelectorAll(".brick").forEach(b => b.addEventListener("click", () => {
    cat.value = (cat.value === b.dataset.cat) ? "" : b.dataset.cat;
    cat.dispatchEvent(new Event("change"));
    if (cat.value) list.scrollIntoView({ behavior: "smooth" });
  }));
}
q.addEventListener("input", render); cat.addEventListener("change", render);
acc.addEventListener("change", render); buildMap(); render();
</script>
</body>
</html>
"""


def main():
    categories, tools = load()
    build_readme(categories, tools)
    build_exports(categories, tools)
    build_site(categories, tools)
    build_coverage(categories, tools)
    print(f"built: README.md, docs/, exports/ — {len(tools)} tools,"
          f" {len(categories)} categories")


if __name__ == "__main__":
    main()
