# AI Tools for Scientific Research — maintenance protocol

Curated catalog of AI tools that are genuinely usable in academic research.
Maintained by Michaela Liegertová; Claude Code performs updates under the rules below.
These rules are binding for every session working in this repo.

## Data flow

```
tools/*.yml + categories.yml        ← SOURCE OF TRUTH (hand/agent-edited)
        │
        └─ python3 scripts/build.py ← regenerates everything below
                ├─ README.md
                ├─ docs/index.html   (browsable, filterable catalog)
                └─ exports/tools.csv, exports/tools.json
```

**Never hand-edit generated files** (README.md, docs/index.html, exports/*).
After any change to `tools/` or `categories.yml`: run `python3 scripts/validate.py`,
then `python3 scripts/build.py`, and commit source + regenerated outputs together.

## Schema (tools/<slug>.yml)

| field | required | rules |
|---|---|---|
| `name` | yes | official product name; filename is its slug |
| `category` | yes | must be a key in `categories.yml`; new categories need Michaela's explicit approval |
| `provider` | no | company / lab / org behind the tool |
| `url` | yes | canonical product page, verified by actually fetching it |
| `description` | yes | see style guide below |
| `access` | yes | `free` \| `freemium` \| `paid` \| `institutional` \| `waitlist` \| `unknown` |
| `domain` | yes | `general` \| `life-sciences` |
| `status` | yes | `active` \| `candidate` \| `needs-review` \| `deprecated` \| `acquired` |
| `added` | yes | `"YYYY-MM"` — when it entered the catalog |
| `last_verified` | yes | `"YYYY-MM-DD"` of the last successful verification, or `null` |
| `notes` | no | maintenance notes, epitaphs for deprecated tools, teaching remarks |

## Admission gate

A tool enters (or stays) `active` only if it passes **all five**:

1. **Maps to a research-workflow stage** — it would belong on a slide for a concrete
   stage of doing research. No home category → no entry.
2. **Usable this week** — free tier, trial, purchasable subscription, or available via
   typical university library subscriptions (then mark `access: institutional`).
   Waitlist/demo-only tools are `status: candidate`, not `active`.
3. **Beyond a general assistant** — does something ChatGPT/Claude/Gemini can't, or is
   itself one of the few category-defining general assistants. The 15th paraphrasing
   wrapper does not get in for existing.
4. **Recommendable to students** — real organization, privacy policy, transparent
   pricing. Listing here is an endorsement.
5. **Alive** — maintained and reachable.

When Michaela asks to add a tool that fails the gate, say which criterion fails and why,
then follow her decision — she can overrule.

## Procedures

### Add a tool
1. Fetch the URL. Confirm it is the actual product page for this tool (not a
   namesake, parked domain, or press release). Cross-check the provider name.
2. Check `tools/` and exports for duplicates (also under alternative names).
3. Run the admission gate.
4. Write `tools/<slug>.yml` with `added` = current month, `last_verified` = today.
5. Validate, build, commit.

### Capture a candidate (fast path)
When Michaela mentions a tool in passing ("candidate: X"), create the file with
`status: candidate`, whatever fields are known, and `last_verified: null` — no vetting,
under a minute. The next update sweep vets it fully and promotes or rejects with a
stated reason in `notes`.

### Update sweep (on request, or scheduled later)
1. Fan out link checks over every tool; fetch, don't just ping.
2. For failures and stale entries: search for renames, acquisitions, shutdowns.
3. Update `url`/`provider`/`status`/`access` as evidence dictates; set `last_verified`
   on every tool actually verified. A tool that can't be confirmed becomes
   `needs-review`, never silently dropped.
4. Vet pending `candidate` entries against the gate.
5. Propose everything as one commit with a summary Michaela can review;
   update CHANGELOG.md.

### Remove a tool
Never delete the file. Dead → `status: deprecated`; bought → `status: acquired`;
in both cases add a one-line epitaph in `notes` (what happened, when). Deprecated
tools are teaching history and disappear from active views automatically.

### Rename / restructure categories
Only with Michaela's explicit approval in the current conversation. Then: update
`categories.yml`, update every affected tool's `category`, rebuild.

## Anti-fabrication rules (hard)

- **Never write a URL, provider, number, or claim you did not verify by fetching.**
  Plausible fabrication is the one failure Michaela cannot recover from.
- Claimed figures inside descriptions ("220M+ papers") stay only if the product page
  still supports them; otherwise drop the number, keep the capability.
- If verification is impossible right now, mark `status: needs-review` and leave
  `last_verified` untouched. UNVERIFIED is an honest result.

## Description style guide

One or two sentences, ≤ 40 words. Capability first: what a researcher does with it.
Concrete, verified numbers welcome; marketing adjectives ("revolutionary",
"cutting-edge", "seamless") are banned. Write for a colleague deciding in five
seconds whether to click. English only.

## Versioning

- Each course edition gets an annotated git tag `vYYYY-MM` and a CHANGELOG.md entry
  (added / removed / renamed / recategorized).
- `git diff v2026-02..v2026-05 --stat -- tools/` is the "what changed this semester"
  slide.
- Commits: imperative subject, body listing affected tools when more than one.

## Commands

```bash
python3 scripts/validate.py   # schema + duplicates + category integrity; exit 1 on failure
python3 scripts/build.py      # regenerate README.md, docs/index.html, exports/
```
