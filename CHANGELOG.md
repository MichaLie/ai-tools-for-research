# Changelog

## v2026-02 — February 2026 edition

Initial import from `AI_Tools_Scientific_Research.xlsx` (sheet "AI Tools for
Research - version", updated to February 2026): 64 tools, 16 categories.

## v2026-05 — May 2026 edition

20 tools added (incl. new categories: Office Suite AI Integrations, Publisher &
Database AI Assistants, AI Manuscript Review & Disclosure additions, Code
Assistants growth, Ideation & Grant Funding). "Enago" renamed to "Enago AI
Disclosure". Category renames: Writing Assistants + Translation merged into
Writing & Translation; Grounded Knowledge → Grounded Knowledge & Specialized
Databases; AI Manuscript Review → AI Manuscript Review & Disclosure.

## Unreleased — verification sweep 2026-08-18

First full verification pass: all 84 tools checked against the live web
(10 parallel agents + reachability probes). 22 URL corrections, 17 provider
corrections, access model recorded for every tool. Status changes:
ChatGPT Atlas deprecated (discontinued 2026-08); 6 tools now `candidate`
(waitlist-gated: AlphaEvolve+ERA, Gemini Co-Scientist, Literature Insights,
Nature Research Assistant, Potato); 4 `needs-review` for Michaela's decision
(Falcon→Edison Literature rename, You.com enterprise pivot, Le Chat→Vibe
rename, 4o Image Generation superseded).

## Unreleased — task-palette restructure 2026-08-18

Reframed the catalog around task diversity: new `tier` field (46 core / 38
extended), max 6 active core tools per category (validator-enforced), category
blurbs phrased as tasks, and deep-dive links to the companion michalie.github.io
indexes (Autonomous Science Agents, Coding & Data Agents) so this catalog stays
the breadth layer. README and site now lead with the core palette; extended
tools collapse under "More tools for this task."

## Unreleased — discovery sweep 2026-08-18 (task-map expansion)

12 discovery agents mapped uncovered task areas. +66 tools, +12 categories:
Transcription & Qualitative Analysis, Systematic Review & Evidence Synthesis,
OCR & Document Digitization, Staying Current, Conference Prep, LaTeX &
Academic Language, Survey & Experiment Design, Research Communication &
Accessibility, Integrity Screening & Forensics, Lab Bench & Protocols,
Patents & Tech Transfer, Journal Selection & Publishing. SciScore and
RegCheck joined AI Manuscript Review & Disclosure (now 6/6 core). Notable
rejections: RobotReviewer (dead), Researcher app (closed 2024), LabTwin
(dead), Roundtable (dead), Turnitin/GPTZero AI detection (reliability),
Scholarcy (gate-3 fail). Catalog: 150 tools / 29 task categories.

## Unreleased — Grok gap-hunt integration 2026-08-18

External gap report (docs/task-coverage-gaps-2026-08-18.md) independently
re-verified by 6 agents; 26 tools integrated, +6 categories: Instrument Data
Interpretation, Data Management & FAIR, Bioimage Analysis, Behavioral Video
Analysis, De-identification & Data Sharing, Impact & Policy Tracking.
Search-strategy construction added as use cases under Systematic Review
(Polyglot, citationchaser core — 6/6); forced alignment under Transcription.
PowerGPT and RefereeBio enter as candidates (no privacy policy / early
access). BioSketch Builder rejected on the recommendable-gate. Catalog:
176 tools / 35 task categories.

## Unreleased — verification sweep 2026-09-11

Second full sweep (10 parallel agents): all 176 tools re-checked — 150 fetched
directly, 25 bot-blocked sites confirmed alive via search, 1 unreachable
(citationchaser Shiny app). 58 descriptions corrected, mostly by dropping
figures the product page no longer supports; 6 URL, 11 provider and 10 access
corrections. Product renames recorded in `name` (file slugs unchanged):
NotebookLM → Gemini Notebook (2 entries), Le Chat → Vibe, Falcon → Edison
Literature, ScienceDirect AI → LeapSpace, Claude for Chrome → Claude in Chrome,
4o Image Generation → ChatGPT Images, Scopus AI → Scopus with AI, Research Kick →
ChatAcademia, Code Interpreter → Data Analysis, Heureka → Heureka Bench, q.e.d.
→ QED Science. Status changes: Potato, Laser AI and InventGenie promoted
(candidate → active/extended, all five gates pass); Faraday active → candidate
(invite-only alpha); FormatMyPaper deprecated (satire site with no backend — it
held the core slot for journal reformatting, so that task is now unrepresented);
You.com deprecated (consumer answer engine gone, developer API only);
Transcription Pearl rejected (unmaintained since 2024-11, superseded by Archive
Studio); citationchaser and Prophy → needs-review. All four 2026-08-18
needs-review items resolved. 11 candidates re-vetted and kept, reason in notes.

## Unreleased — journal-reformatting follow-up 2026-09-11

Paper Pivot captured as a candidate (waitlist, in development) as the only
genuine journal-reformatting product found; CheckMyManuscript rejected as a
checker, not a reformatter. Writing & Translation blurb now states the honest
market position and points to coding agents (Claude Code, Codex) for
guideline-driven reformatting, so the task stays on the palette without a
placeholder entry.

## Unreleased — verification sweep 2026-10-15

Checked all 177 existing entries (174 distinct catalog URLs), with official
documentation and rendered-browser follow-up for blocked or JavaScript-only
pages. This is a public-source maintenance check, not a functional test or a
benchmark/security audit. The evidence ledger is `audits/2026-10-15.json`.

91 entries have substantive edits: 84 descriptions, 9 URLs, 5 names, 2 providers,
8 access classifications, 7 status changes, 1 tier promotion and 4 moves to extended. Another 7 entries receive
maintenance-note corrections or candidate decisions. Updated verification dates
for 172 entries; preserved older dates for 5 incomplete checks. No tools or
categories were added or deleted. Paper2Video becomes core; the four moves below
are approved for this local proposal. All other tiers are unchanged.

- Apply the approved core review: move Claude for Microsoft 365, Claude Research,
  Gemini Deep Research, and Jenni to extended. Core counts become one Office
  integration, two deep-research tools, and three writing/translation tools.
  Revise all ten reviewed descriptions and evidence notes around distinct tasks.
  Keep STORM for interactive perspective exploration, DeepL for document
  translation, Grammarly for ongoing language correction, and Paperpal for
  source-supported manuscript drafting and submission checks. Choose Microsoft
  Copilot and ChatGPT Deep Research as the Office and delegated-report exemplars.
  Record Gemini's strong institutional provision, Claude's Office pilot, and
  Grammarly's mixed adoption evidence; no measured adoption or quality ranking
  is claimed. Detailed rationale: `audits/core-tool-review-2026-10-15.md`.

- Restore citationchaser to active: its Shiny interface loads again. Searches
  were not submitted; the analysis/network panels still report ongoing updates.
- Flag Edison Literature and Kosmos for re-verification: the platform and the
  exact Try Kosmos route show a temporary service-outage notice. This is not a
  shutdown finding. Also flag Deepwriter (expired HTTPS certificate), FAIR-Checker
  (hosted service timed out; source code remains available), and Web of Science
  Research Assistant (live page could not be fetched despite indexed official
  evidence). Prophy remains needs-review for its existing inclusion decision.
- Correct access: Claude file creation/code execution and GrantBoost are
  freemium; Google Antigravity has free and paid tiers; AIVA has free/trial/paid
  tiers, with sample uploads restricted to trial/paid access; Presidio is free
  open-source software; SciScore's author route now advertises paid report
  credits. Paperclip by GXL has free and paid plans, overlooked in the initial
  proposal despite being present on its product page. Its terms permit training
  on submitted content, so the entry recommends public research material.
  PaperTok's payment status is unknown: its “credits” step means author attribution.
- Update current product scope and naming for Paperclip by GXL, BenchSci / EMET,
  Claude for Microsoft 365, Microsoft Copilot editing in Office, and AI Reference
  Checker (RefCheckAI). Grok's official pages identify SpaceXSI as its provider.
- Re-vet all 13 candidates. Admit Paper2Video for prerecorded conference talks:
  its installable open-source route meets the same specialist-software standard
  as Paper2Poster. Document the setup and recommended 48GB GPU rather than
  treating lack of a hosted service as disqualifying. This sole task representative
  becomes core, raising Conference Prep from two to three core tools without
  displacing another entry. No end-to-end video generation was run.
- Keep 12 candidates on the watchlist. Paper Pivot has an accessible
  privacy policy but is explicitly waitlist-only. Genemod's pages now fetch, but
  prices remain quote-based and its linked signup route returns 404. RefereeBio
  specifies governing law now, but its operator identity remains unresolved.
- Restore task-specific distinctions diluted in the initial prose cleanup:
  Consensus Meter, Rayyan's blinded screening, source-linked Notebook audio,
  BenchSci's reagent/resource evidence, and SciScore's concrete reporting checks.
- Remove stale model labels, unconfirmed prices/counts, and benchmark claims
  presented without their evaluation context. Correct Transcription Pearl's last
  commit to 29 April 2025; retain its existing retired status.
- Bring the three remaining descriptions over 40 words within the catalog limit.
- Correct generated header wording: the newest successful verification date no
  longer claims every entry was successfully verified on that date.
- Correct the task-coverage generator: only active entries count as available
  examples. List candidates and needs-review entries separately, exclude retired
  tools from coverage, and use current descriptions instead of historical
  discovery notes. Label the old gap list as historical rather than newly verified.

Catalog remains 177 records / 35 categories: 155 active, 6 needs-review,
12 candidates and 4 retired. The main catalog displays 161 records
(active plus needs-review).
