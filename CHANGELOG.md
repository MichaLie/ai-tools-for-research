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
