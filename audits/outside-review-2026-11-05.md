# Outside review — 5 November 2026

**What this is.** Michaela asked a visiting Claude Code session to read the repo and
contribute "any insight, contribution or opinion". This memo and the three code
commits on branch `claude/fervent-cray-64d8ti` are the result, for Quill to merge,
cherry-pick or reject. Nothing in `tools/` or `categories.yml` was changed. The only
live fetch was github.com, to see how GitHub renders the README; the sandbox could
not reach other hosts, so no tool was re-verified and no new URL appears below.

Every number here is computed from the catalog at commit `9c27095`; every claim about
a tool comes from its YAML file, not from the live web.

## 1. Fixed on this branch (verified)

**README task map: 22 of 35 category links were broken on GitHub.** The map at the
top of README.md links each category to its section heading. `build.py` derived the
anchor by deleting the "&" and collapsing the double hyphen, but GitHub's slug rule
keeps both spaces around a dropped character, so "Literature Discovery & Analysis"
renders as `#literature-discovery--analysis` (double hyphen), and the em dash in
"Conference Prep — Posters & Talk Practice" is dropped outright. Checked against the
rendered page: GitHub emits `id="user-content-literature-discovery--analysis"`,
`…conference-prep--posters--talk-practice`, `…ocr--document-digitization`,
`…latex--academic-language`. Every title containing "&" or "—" was affected; the 13
titles without them were fine. `build.py` now applies GitHub's own rule
(`gh_anchor`); the rebuilt README differs only in the six map lines.

**Validator: five AGENTS.md rules were stated but not checked.** `validate.py` now
fails on: a description over 40 words; a category blurb that does not start with
"The task:"; `access: waitlist` on an `active` tool (gate 2); a deprecated or
acquired tool without an epitaph in `notes`; a `candidate` holding a core slot. All
five pass on the current data, so CI stays green. Three editorial rules are reported
as warnings only: marketing adjectives in a description (the style guide's own three
examples plus five obvious siblings), a core slot with no `notes` (AGENTS.md asks for
adoption evidence or the sole-use-case rationale there), and more than three active
core tools in a category that has a `deep_dive` index. `--strict` turns warnings into
failures for a clean-room check before a course tag. The summary line now reports
status counts and the oldest verification date, which is the number a sweep wants
first.

**Site: shareable filter links and a field filter.** The four filters (search,
category, access, field) are mirrored in the URL hash, e.g.
`…/ai-tools-for-research/#cat=bioimage-analysis&dom=life-sciences`, so a slide or a
syllabus can link straight to one task's view; opening such a link scrolls to the
tools. Back/forward and pasted hashes are honoured; typing does not pollute the
history. The new field select isolates the life-sciences entries (28 of the 161 shown).
Tested in headless Chromium: counts match the data for every combination tried, an
unknown category in the hash is ignored, no console errors.

## 2. Found, not changed — data decisions for Quill

- `nano-banana-pro-gemini`: the 2026-09-11 note says "access paid -> freemium", but
  the field is still `paid`, and the 2026-10-15 ledger recorded no change. One of the
  two is wrong. Its description also opens with "State-of-the-art", the one marketing
  adjective the new validator flags.
- `jstor-ai-research-tool` is the only active core entry with no `notes` at all. The
  core-slot rule asks for the evidence to live there.
- `EMPTY_EDGES` (the list of deliberately empty tasks) is a Python list inside
  `build.py`. A sweep that fills an edge has to edit code. It would sit more naturally
  in a small `gaps.yml` next to `categories.yml`, rendered the same way.
- The three "shares url" warnings (Google Labs trio, the two Notebook entries) are
  known and legitimate; they stay as warnings.
- `validate.py`'s docstring pointed at a schema "in CLAUDE.md"; it is in AGENTS.md.
  Fixed in passing.

## 3. The shape of the catalog (opinion, numbers from the data)

| | |
|---|---|
| Records | 177: 155 active, 12 candidate, 6 needs-review, 4 retired |
| Tiers | 98 core, 79 extended |
| Field | 145 general, 32 life-sciences (in 14 of the 35 categories) |
| Access | 55 free, 76 freemium, 28 paid, 9 institutional, 6 waitlist, 3 unknown |
| Entered | 64 in 2026-02, 20 in 2026-05, 92 in 2026-08, 1 in 2026-09 |
| Verified | 172 on 2026-10-15; 5 on 2026-09-11, all of them `needs-review` |

**Four tasks hang on one tool.** AI-Powered Search Engines (Perplexity, since You.com
retired), Grounded Knowledge & Specialized Databases (Gemini Notebook), Journal
Selection & Publishing (B!SON) and Impact & Policy Tracking (Sage Policy Profiles)
each have exactly one active entry; Office Suite, Browser Automation and Instrument
Data Interpretation have two. FormatMyPaper showed what happens when a sole
representative dies: the task falls off the palette. Suggestion: for each
single-tool category, either add one extended alternative at the next sweep, or say
in the blurb that the field was searched and nothing else qualifies, so thinness reads
as a finding rather than an omission.

**The stale set is the flagged set, and two flagged tools still hold core.** The five
entries last verified in September are exactly five of the six `needs-review` tools;
Kosmos and Web of Science Research Assistant are among them and still sit on the
default palette with an asterisk. Resolving those two first at the next sweep would
clear the only visible inconsistency on the front page. A rule such as "needs-review
for more than 90 days vacates the core slot" would make this automatic, but it is a
protocol change and needs Michaela's approval.

**August doubled the catalog.** 92 of 177 records entered in 2026-08. `added` records
when a tool entered *this catalog*, not when it launched, so the semester-diff slide
AGENTS.md describes (`git diff v2026-05..<next tag> --stat -- tools/`) will show the
hunt, not the market. Worth
one sentence on the slide.

**The ratchet is mostly slack.** The 6-per-category cap is reached in one category
(Systematic Review); three sit at 5 (Literature Discovery, AI Manuscript Review,
Research Communication); the other 31 hold 1–4 core. What actually keeps core small
is the editorial sole-representative and community-standard rules, which is fine, but
it means the validator cannot help much with tier discipline beyond the cap and the
new deep-dive warning.

**Three quarters have a free path.** 131 of 177 are free or freemium. Good for a
student audience; the 9 institutional entries are the ones to flag in a course as
"check your library first".

## 4. Task-gap leads (unverified — leads, not facts)

Per the "integrate an external gap report" procedure: nothing below was fetched
today. Vet before any file is written.

1. **Dataset discovery and reuse** — "does a dataset that answers this already
   exist?" Data Management & FAIR covers plans and deposit, Literature Discovery
   covers papers; neither covers finding data. Lead: the dataset search service run
   by Google, plus repository-level search (Zenodo, Dryad, Hugging Face datasets).
   Some of these are infrastructure rather than AI, which the 2026-08-18 gap hunt
   already accepted as the bar.
2. **Statistical reporting checks before submission** — consistency of reported test
   statistics and p-values. Lead: statcheck (R package and web app from the Tilburg
   meta-research group). Nearest home: AI Manuscript Review & Disclosure, next to
   SciScore's rigor checks.
3. **Reviewer-side peer review** — probably an *intentionally* empty edge: NIH
   prohibited generative AI in its peer review in 2023, and several large publishers
   forbid reviewers from uploading manuscripts under review to generative tools. If
   that holds up, record it in the empty-edges list with the reason, as was done for
   press releases, so students do not read the gap as "nobody built it yet".
4. **Finding collaborators and expert finding** — a real early-career task; Prophy
   (needs-review) is the only neighbour in the catalog. No tool proposed.

Considered and set aside: AI-assisted formal mathematics (Lean-based proof
assistants) belongs in a depth index, not this palette; ethics/consent paperwork
drafting is a task, but no tool beyond a general assistant came to mind.

## 5. Tooling proposals, not implemented

- **`scripts/linkcheck.py` as sweep triage.** Fetch every URL once, classify
  (2xx on the same host / redirected to another host / 403–429 bot-blocked /
  404–5xx–timeout), write `audits/linkcheck-YYYY-MM-DD.json`, and let the sweep
  agents start from the short list instead of 177 fetches. Not shipped: this sandbox
  reached github.com only, so the script could not be tested honestly.
- **CI:** once the one adjective is settled, run `validate.py --strict` on pull
  requests (keep pushes lenient), and pin `pyyaml` in `ci.yml` or a `requirements.txt`.
- **`gaps.yml`** for the empty edges, as above.

## 6. How the branch is organised

Four commits, each standing alone: README anchors; validator; site filters; this
memo plus the CHANGELOG entry. Take any subset.
