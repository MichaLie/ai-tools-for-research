# Task-coverage gaps — hunt of 2026-08-18

Input: `docs/task-coverage.md` (150 tools, 29 task types, verified live 2026-08-18).
Job: expand the **map**, not the tool list. Unit of interest is the TASK.

This file is the record of that hunt. It does **not** change `task-coverage.md`
or `categories.yml`. Adding a category still needs Michaela's explicit approval.

**If you add only three tasks to the map:** (1) laboratory instrument-data
interpretation, (2) systematic-review search-strategy construction,
(3) funder-compliant machine-actionable DMP / FAIR assessment.

Those are the ones a European PI actually hits and a US-shaped catalog never names.

---

## How this was done

- `/deep-research` workflow (`deep-research`) plus eight parallel search lanes:
  empty edges, university library taxonomies, EU/non-English, Reddit/methods,
  DMP/FAIR/de-id, search-strategy, image/video/plot, impact/collab/quality/safety.
- Every URL ranked below was fetched on 2026-08-18 unless marked otherwise.
- Assumption: “AI can already augment” includes ML and decision-support
  research infrastructure (same bar as ASReview, SciScore, NC3Rs EDA, Transkribus),
  not only chat products.
- Official `/deep-research` status: **Partial**. It agreed on the main map,
  missed PowerGPT / RefereeBio / BioSketch Builder, and declined search-strategy
  and DMP as “catalog comparison uncited” (verifier artefact). This file is the
  coordinated record; the workflow report is not a second source of truth.

Confidence labels: **verified live** = product page fetched this date;
**seen referenced** = named on a fetched official/libguide page, product itself
JS-thin or not logged into; **unverified** = not independently confirmed.

Access: `free` | `freemium` | `paid` | `institutional`.

---

## Ranked gaps (strongest first)

### 1. Laboratory instrument-data interpretation

**Empty edge, now filled.** After the run, the job is “what is this peak /
unknown,” not “paste the CSV into the ELN.”

Why it is a real academic task: metabolomics, natural products, and
small-molecule ID from LC-MS/MS are routine methods steps. The catalog had
marked this empty as “enterprise-only.” That is true for Thermo/Waters/Agilent
consoles. It is false for academic MS structure ID.

| Tool | Provider | URL | Access | What a general assistant cannot do |
|---|---|---|---|---|
| SIRIUS 6 (CSI:FingerID, CANOPUS, MSNovelist) | Böcker group, FSU Jena + Bright Giant GmbH | [github.com/sirius-ms/sirius](https://github.com/sirius-ms/sirius) · [academic licence](https://v6.docs.sirius-ms.io/account-and-license/) · [bright-giant.com](https://bright-giant.com/) | free academic (institutional email; auto-granted). v6.3.12 dated 2026-07-30, Win/Mac/Linux | Ingest LC-MS/MS and return formula + ranked structures + ClassyFire classes + de-novo graphs |
| MetFrag | IPB Halle (de.NBI) | [msbi.ipb-halle.de/MetFrag](https://msbi.ipb-halle.de/MetFrag/) | free web | In-silico fragmentation against PubChem / HMDB / LIPID MAPS from *your* peak list |

Confidence: **verified live**. EU (Jena, Halle). Benchling AI (already in the
catalog) files instrument output into an ELN; it does not identify the molecule.
Shipping product covers tandem-MS, not NMR. NMRium is browser NMR *processing*,
not automated elucidation.

---

### 2. AI power analysis / sample-size planning

**Empty edge, now filled — with a caveat.** IRBs, funders, and journals want an
a priori *n* and a named test.

| Tool | Provider | URL | Access | What a general assistant cannot do |
|---|---|---|---|---|
| PowerGPT | UPenn-led multi-institution group (Yong Chen et al.) | [power-gpt.net](https://power-gpt.net/) · Other Institutions: [power-gpt.net/others](https://power-gpt.net/others) | free; listed institutions or “Other Institutions”; chat starts, no waitlist | Conversational intake wired to statistical engines (t, ANOVA, proportions, χ², Cox, logrank); “Used …” tab shows the computation |

Confidence: **verified live**. Paper: [arXiv:2509.12471](https://arxiv.org/abs/2509.12471)
(RCT: 94.1% vs 55.4% sample-size accuracy vs unaided).

Caveats: homepage showed **0 daily users / 0 conversations** on 2026-08-18;
research deployment, not a company; no standalone privacy policy on the fetched
page; study-design text goes to a US academic server. r/AskStatistics still lives
in G\*Power-land and has not found this. Official `/deep-research` missed it and
left the edge empty.

Not already covered: NC3Rs EDA is animal-design-with-a-module. SciScore only
audits whether you *reported* a power analysis. G\*Power, PASS, nQuery, ClinCalc,
UCSF sample-size.net are not AI. N-Power AI remains a bioRxiv preprint
([10.1101/2025.02.06.636776](https://doi.org/10.1101/2025.02.06.636776));
`https://ai.swmed.edu/N-PowerAI/` was a JS shell.

---

### 3. Systematic-review search-strategy construction

The step *before* Covidence / Rayyan / ASReview. PRISMA/MECIR require the
executed multi-database Boolean. Librarians treat this as a different job from
screening.

Named separately by Toronto Gerstein, McGill, KCL, Edinburgh, Stanford Lane,
Utrecht, Sheffield Hallam, and [NTK Praha](https://www.techlib.cz/cs/84764-ai-nastroje-pro-vyzkum-umela-inteligence).

Methods paper that kills “just ask ChatGPT”: Clark et al., *Research Synthesis
Methods* 2025, 16:601–619, [DOI 10.1017/rsm.2025.16](https://doi.org/10.1017/rsm.2025.16).
GenAI search recall 4–32%, median miss 91%.

| Tool | Provider | URL | Access | What a general assistant cannot do |
|---|---|---|---|---|
| TERA (ex-SR-Accelerator), Polyglot | Bond University IEBH | [tera-tools.com](https://tera-tools.com) · legacy [polyglot.sr-accelerator.com](https://polyglot.sr-accelerator.com) | Polyglot: free web. TERA: free-account claim vs one 2026 libguide saying the suite went paid Oct 2025 — **pricing unverified** (no login) | Translate a PubMed or Ovid MEDLINE string into Embase / CINAHL / PsycINFO / Scopus / WoS field tags |
| Yale MeSH Analyzer | Yale Cushing/Whitney Medical Library | [mesh.med.yale.edu](https://mesh.med.yale.edu/) | free, no login | Paste ≤20 PMIDs → live MeSH comparison grid (headings, subheadings, major-topic flags) |
| PubReMiner | Jan Koster, Amsterdam UMC | [hgserver2.amc.nl/cgi-bin/miner/miner2.cgi](https://hgserver2.amc.nl/cgi-bin/miner/miner2.cgi) | free | Frequency tables of words / MeSH / journals from a live PubMed set |

Also live, not needed as a fourth core slot: [Medline Transpose](https://medlinetranspose.github.io/)
(PubMed ↔ Ovid / EBSCO); [citationchaser](https://estech.shinyapps.io/citationchaser/)
(Haddaway; Lens.org forward/backward → RIS) — a second missing *use-case*,
exhaustive citation chasing for the PRISMA identification box, distinct from
Litmaps/ResearchRabbit discovery maps.

Confidence: Yale + Polyglot + PubReMiner + citationchaser **verified live**.
TERA in-app inventory **seen referenced** (Bond page + libguides; app is a JS shell).

ChatGPT drafts a plausible PubMed block; it invents MeSH and silently breaks
Ovid/Embase proximity. Polyglot does **not** auto-map MeSH → Emtree (still human).
No shipping PRESS-AI product.

Catalog implication: new use-case inside `systematic-review-evidence-synthesis`
(the category already holds screening/extraction/living-review). One TERA-or-Yale
core slot is justified. Split the category only if you want the full librarian
palette on the default slide.

---

### 4. Funder-compliant machine-actionable DMP / FAIR assessment

Horizon Europe, NIH DMSP, GAČR, TAČR, and Research Council of Norway treat the
DMP as a living structured object, not a grant appendix.

**Name collision:** the catalog’s Argos is Scitility’s retraction screener, not
OpenAIRE ARGOS. That hid this gap.

| Tool | Provider | URL | Access | What a general assistant cannot do |
|---|---|---|---|---|
| Data Stewardship Wizard | ELIXIR CZ / CTU Prague | [ds-wizard.org](https://ds-wizard.org/) | free OSS; ELIXIR cloud + Czech instances | Knowledge-model questionnaires, FAIR metrics, Horizon / Science Europe export, maDMP JSON |
| ARGOS | OpenAIRE | [argos.openaire.eu/portal](https://argos.openaire.eu/portal/) · [subscriptions](https://argos.openaire.eu/portal/subscriptions.html) | **free for researchers** (0 €); paid org tiers | Funder blueprints, publish DMP to Zenodo with a PID, OpenAIRE Graph link |
| F-UJI | PANGAEA / FAIRsFAIR (H2020 831558) | [f-uji.net](https://www.f-uji.net/) | free web + API | Score a live dataset DOI against FsF metrics from its actual metadata |
| FAIR-Checker | IFB / ELIXIR-FR | [fair-checker.france-bioinformatique.fr](https://fair-checker.france-bioinformatique.fr/) | free | SPARQL/SHACL checks against DataCite, OpenAIRE, Wikidata, LOV, OLS, BioPortal, Bioschemas |

Confidence: **verified live**. EU, and Czech-native (DSW is an ELIXIR Recommended
Interoperability Resource; named in the Horizon Programme Guide).

Honest AI label: the shipping products are decision-support, not chat. The DSW
[AI document plugin](https://github.com/ds-wizard/ai-document-plugin) is self-host
only. [DMP Chef](https://fairdataihub.org/dmp-chef) is a real RAG pipeline aiming
at DMPTool — **not in the DMPTool UI this week**. DMPTool itself (155k users) is
a funder-template wizard with no model on the homepage; genAI was “targeting
summer 2026” and was not confirmed shipped.

Do not file this as “AI DMP writer.” File it as *funder-compliant /
machine-actionable DMP*. F-UJI / FAIR-Checker are the *deposit-time* use-case
(score a DOI), distinct from writing the plan.

---

### 5. Bioimage analysis of your own microscopy / histology

Quantify cells, nuclei, whole-slides. Distinct from BioRender (draw a figure)
and Proofig (forensic matching). Not the biological-foundation-models companion
index — these are GUI/CLI products you point at *your* data.

| Tool | Provider | URL | Access | What a general assistant cannot do |
|---|---|---|---|---|
| Cellpose / Cellpose-SAM | Stringer & Pachitariu (HHMI) | [cellpose.org](https://www.cellpose.org/) · [HF Space](https://huggingface.co/spaces/mouseland/cellpose) | free | Instance segmentation + human-in-the-loop training on *your* channels |
| ilastik | EMBL Heidelberg — **EU** | [ilastik.org](https://www.ilastik.org/) | free; v1.4.2 released 2026-05-28 | Interactive ML segment / classify / track / count, no DL expertise |
| QuPath | Pete Bankhead / Edinburgh | [qupath.github.io](https://qupath.github.io/) | free; v0.7.0 live | Whole-slide histology + StarDist / Cellpose inside the viewer |

Confidence: **verified live**. A VLM can describe a screenshot; it cannot
segment a 3D stack or a WSI. BioImage Model Zoo is an index (companion-wiki
territory). DeepImageJ is the “run zoo models in Fiji” layer.

r/labrats treats Cellpose as the community default for cell counting.

---

### 6. Behavioral video analysis / markerless pose

Ethology, neuroscience, ecology. Distinct from interview CAQDAS.

| Tool | Provider | URL | Access | What a general assistant cannot do |
|---|---|---|---|---|
| DeepLabCut + SuperAnimal | Mathis Lab, EPFL | [docs](https://deeplabcut.github.io/DeepLabCut/README.html) · landing [mlabofai.org/deeplabcut](https://mlabofai.org/deeplabcut) | free (SuperAnimal: research / non-commercial) | Train/run markerless keypoints on *your* videos |
| SLEAP | Talmo Pereira lab | [sleap.ai](https://sleap.ai/) | free | Multi-animal pose + identity, GUI, PyTorch 1.5+ |
| idtracker.ai | de Polavieja lab, Champalimaud — **EU** | [idtracker.ai](https://idtracker.ai/) | free | Identity tracks for up to ~100 unmarked animals (*eLife* 2026) |

Confidence: **verified live**.

---

### 7. De-identify / synthesise data so it can be shared

GDPR deposit of a survey, registry extract, clinic table, or interview
transcript. Distinct from transcription/CAQDAS and from Expected Parrot’s
*simulated respondents*.

Two sub-use-cases: formal k-anonymity on tables, and NLP redaction of
qualitative text *before* a cloud LLM.

| Tool | Provider | URL | Access | What a general assistant cannot do |
|---|---|---|---|---|
| Amnesia | OpenAIRE / Athena RC | [amnesia.openaire.eu](https://amnesia.openaire.eu/) · [what it is](https://amnesia.openaire.eu/about/what-is-amnesia.html) | free on-prem recommended; [online demo](https://amnesia.openaire.eu/demo/) is demo-only; paid support tiers | Formal k- / km-anonymity; data stays local |
| Textwash Pro | Bennett Kleinberg + jocapps GmbH | [textwash.eu](https://www.textwash.eu/) · OSS: [github.com/ben-aaron188/textwash](https://github.com/ben-aaron188/textwash) | 14-day trial, then $330/yr or **$130/yr student**; OSS CLI free | On-device contextual PII removal (EN/DE/NL/FR/ES/IT); then send only the redacted copy to Claude/ChatGPT |
| QualiAnon | Qualiservice / Universität Bremen FDZ | [github.com/pangaea-data-publisher/qualianon](https://github.com/pangaea-data-publisher/qualianon) · [Qualiservice tools](https://www.qualiservice.org/en/the-helpdesk/tools.html) | free OSS; v1.5.0 (2025); deliberately semi-automatic | Interview-text replacement with a human-in-the-loop codebook — the German FDZ standard |
| Presidio | Data Privacy Stack (ex-Microsoft) | [presidio.dataprivacystack.org](https://presidio.dataprivacystack.org/) · [HF demo](https://huggingface.co/spaces/presidio/presidio_demo) | free OSS | Local NER/regex PII pipeline for text (and images) |

Confidence: Amnesia, Textwash Pro, FAIR-Checker-adjacent pages, Presidio
**verified live**. QualiAnon **verified live** (GitHub + Qualiservice).

ChatGPT will invent redactions; it will not give a k-anonymity guarantee or an
offline GDPR path. If you add one EU-native *AI* (strict sense) tool to this
family: **Textwash**.

MOSTLY AI SDK exists for synthetic tabular data (`pip install 'mostlyai[local]'`);
academic adoption of the *platform* is a different question. Gretel synthetics
repo archived 2026-02-18.

---

### 8. Extract numerical data from published figures

Meta-analysis and reanalysis when authors did not share the points. Distinct
from Mathpix (LaTeX/OCR) and from Elicit table extraction.

r/labrats: “50 papers… my wrist is dying.” Reddit demand is already in lab
culture. Rank this higher than a “nice extra.”

| Tool | Provider | URL | Access | What a general assistant cannot do |
|---|---|---|---|---|
| WebPlotDigitizer v5 | Automeris LLC (Ankit Rohatgi) | [automeris.io](https://automeris.io/) · [docs](https://automeris.io/docs/) · [GitHub](https://github.com/automeris-io/WebPlotDigitizer) | freemium. Frontend AGPL; **“AI Assist” is closed-source cloud** (stated on GitHub) | Calibrate axes (incl. log) and recover x/y; overlay-and-correct points |

Confidence: **verified live** (docs + GitHub; homepage is a JS shell). Did not
check whether AI Assist is on the free tier, or whether images go to
OpenAI/Google. A VLM invents numbers.

Also live, not needed as a second core: PlotDigitizer.com (free web; Pro ~$40);
metaDigitise on CRAN (box/bar/scatter → means/SDs). graph2table: unknown legal
entity — do not list as recommendable.

---

### 9. Show that *your* work was cited in policy

REF impact, Horizon “pathways to impact,” CoARA, tenure. Distinct from Kudos
(you write a plain-language page) and from staying-current (new papers).

| Tool | Provider | URL | Access | What a general assistant cannot do |
|---|---|---|---|---|
| Sage Policy Profiles | Sage + Overton | [policyprofiles.sagepub.com](https://policyprofiles.sagepub.com/) | **free** researcher account. 2026 update: up to 3 policy-engagement matches/month | Search Overton’s policy-document index and resolve citations to *your* papers |

Confidence: product URL + Sage / Social Science Space pages **verified live**.
The app itself is JS-heavy — not logged in. **Seen referenced:** Nature 2023
tool note. Overton Index is institutional.

---

### 10. Reviewer-response / revision-check

**Empty edge, filled at candidate grade.** The decision letter is a structured
object (R1 comment 3b ↔ line 214).

| Tool | Provider | URL | Access | What a general assistant cannot do |
|---|---|---|---|---|
| RefereeBio | RefereeBio (independent; thin company identity) | [refereebio.com](https://refereebio.com/) | early access: 1 month Starter free, no card — 3 reviews, **3 revision checks**, 3 edits | Paste the real decision letter + revised MS; score each concern addressed / partial / open; draft a point-by-point rebuttal |

Confidence: **verified live**. Caveats: life-science primary papers only; sample
reports are fictional; early access; manuscript text “may be sent to configured
AI providers.” Pre-submission half overlaps Stanford Agentic Reviewer /
Reviewer3 / Manusights. The *new* task is the revision ledger.

Official `/deep-research` left this edge empty (did not see RefereeBio).
SciSpace “response to reviewers” agents are wrappers. r/AskAcademia threads are
etiquette, not tools. Treat as `candidate` until someone runs a real R&R
through it.

---

### 11. NIH Common Form biosketch

**Empty edge, partially filled.** NIH Common Forms via SciENcv are mandatory.
Personal Statement and Contributions are grant-specific and slow.

| Tool | Provider | URL | Access | What a general assistant cannot do |
|---|---|---|---|---|
| BioSketch Builder | BioSketch Builder / DVL Rao Holdings | [biosketchbuilder.com](https://biosketchbuilder.com/) | free drafts, no card; Chrome extension autofills SciENcv | Enforce Common Form limits, parse a CV into SciENcv fields, type into SciENcv |
| SciENcv | NCBI / NIH | [ncbi.nlm.nih.gov/sciencv](https://www.ncbi.nlm.nih.gov/sciencv/) | free | Produce the digitally certified PDF NIH will accept — **not AI** |

Confidence: BioSketch Builder **verified live**. Young indie product; AI
providers unnamed; contact `dvlraoholdings@gmail.com`. Fails the catalog’s
“recommendable to students” gate until there is a named organisation and
independent academic use. Official `/deep-research` correctly notes that a
third-party draft cannot become the certified SciENcv PDF.

**Narrative CV / R4RI / Résumé for Researchers is still empty** (UKRI / NWO /
Horizon templates + [PEP-CV](https://pep-cv.mariecuriealumni.eu/) mentoring only).

---

### 12. Forced alignment / phonetic annotation

Phonetics, oral-history editions, conversation analysis. noScribe gives words;
this gives phone/word time stamps.

| Tool | Provider | URL | Access | What a general assistant cannot do |
|---|---|---|---|---|
| WebMAUS / BAS Web Services | BAS / LMU Munich, CLARIN-D — **EU** | [clarin.phonetik.uni-muenchen.de/BASWebServices/interface/WebMAUSGeneral](https://clarin.phonetik.uni-muenchen.de/BASWebServices/interface/WebMAUSGeneral) | free academic web service | Forced alignment → Praat TextGrid / ELAN tiers |
| Montreal Forced Aligner | Montreal Corpus Tools | [montrealcorpustools.github.io/Montreal-Forced-Aligner](https://montrealcorpustools.github.io/Montreal-Forced-Aligner/) | free (`conda` / PyPI) | Train-your-own-corpus forced alignment |

Confidence: WebMAUS URL **verified live** (Angular shell; long-standing CLARIN
endpoint). MFA **seen referenced** / docs URL in the official run.

---

### 13. Controlled-vocabulary subject indexing

National libraries and repositories need terms from *their* SKOS vocabulary
(YSO, STW, GND, Deskryptory), not free-text keywords.

| Tool | Provider | URL | Access | What a general assistant cannot do |
|---|---|---|---|---|
| Annif | National Library of Finland | [annif.org](https://annif.org/) | free OSS + live demo | Rank terms from a production vocabulary with models trained on already-indexed national corpora |
| Finto AI | NatLibFi | [ai.finto.fi](https://ai.finto.fi/) | free web | Public Annif UI for Finnish thesauri |

Confidence: Annif **verified live**. Finto AI **seen referenced** (JS UI).
Used in production by DNB, National Library of Sweden, ZBW AutoSE, Finnish
repositories. Add only if you want a Nordic/DH slice.

---

## Still empty (reconfirmed 2026-08-18)

| Edge | What exists | Why it dies |
|---|---|---|
| **Press-release drafting for a paper** | EurekAlert / idw / AlphaGalileo (distribution); SciencePOD / Editage (human agencies); GlobeNewswire AI (corporate, demo); Prowly is now Semrush’s marketer PR toolkit | No self-serve paper → embargoed scientific newsroom product. **EurekAlert Content Eligibility Guidelines, last updated 1 July 2026:** “AI-generated text, images and other multimedia are not eligible for submission” ([eurekalert.org/releaseguidelines](https://www.eurekalert.org/releaseguidelines)). A dedicated product would be policy-hostile at the main science-news wire. Keep empty on purpose. |
| **AI conference matching** | [Thesify Conference Finder](https://www.thesify.ai/features/conference-finder) page exists; **“currently not available in app.”** IEEE Publication Recommender is keyword, not AI. WikiCFP / EasyChair Smart CFP are directories. Scholar Inbox is a poster-session planner at a meeting you already attend | No shipping “upload paper → ranked live CFPs with deadlines” |
| **Journal-figure alt-text** | FigurA11y: “not suitable for production” ([github.com/allenai/figura11y](https://github.com/allenai/figura11y)). Elsevier generates alt-text in *proofs*. MatplotAlt (`pip install matplotalt`) only does *your matplotlib object* | The empty edge as stated is still empty. No “upload this paper PDF, get journal-ready figure alt-text.” |
| **Narrative CV (R4RI / Horizon / NWO / CoARA)** | Official Word templates; PEP-CV is peer mentoring | No shipping AI builder |

---

## Named but not added

So the cuts are visible.

| Candidate | Why not a new map task / not a core slot |
|---|---|
| REDCap 15 AI | Real, inside the eCRF you already license (*JAMIA Open* 2026; 18 institutions). Task is “wordsmith/translate the instrument,” not protocol→eCRF. Institutional; admin must flip the switch. |
| Qualtrics Fraud Detection | Real bot/duplicate screening, distinct from ExpertReview. Not on all campus licences. CloudResearch Sentry is the specialist, primary CTA is Request a Demo. |
| cleanBib | [github.com/dalejn/cleanBib](https://github.com/dalejn/cleanBib) — citation-diversity audit (WW/MW/WM/MM) for journals that want a statement. Real task, R/Binder, not a product. |
| INCEpTION / Recogito Studio / NameTag 3 (ÚFAL/LINDAT) | DH NER and TEI/entity linking after Transkribus. Real EU task; add only for a digital-humanities slice. |
| Journal Checker Tool (cOAlition S) / Open Policy Finder (Jisc) | Plan S / funder OA compliance. Not AI. Adjacent to B!SON, not the same job. |
| Pl@ntNet | Field taxon ID from a photo. Real ecology task. CIRAD/Inria/INRAE. |
| GESTIS-Stoffenmanager / SEIRICH / ART | Gefahrstoff / COSHH / REACH exposure assessment. Statutory EU tools, not LLM. Real wet-lab task before the protocol. |
| Crowdhelix ReviewIQ | Horizon consortium / Pillar II idea check. Paid membership; Belgian-hosted LLM. Task barely exists in US catalogs. |
| Primo Research Assistant / Statista Research AI | Licensed-database Q&A. Sit inside **Publisher & Database AI Assistants**. |
| Lexis Protégé / West CoCounsel / Bloomberg Law AI | Real law-research task. Add only if you want a socio-legal slice. |
| Scinapse Expert Finder | Collaborator/expert finding (not Prophy’s editor-side matching). Freemium. Weaker than the tasks above. |
| DMPTool / DMPonline / EasyDMP | Live wizards, not models. Do not list as AI. |
| Code Ocean Aqua | AI inside a reproducibility capsule. Demo / VPC / biotech. Fails usable-this-week. |

---

## Empty-edge scorecard

| Edge (from `task-coverage.md`) | Official `/deep-research` | Coordinated fetch (this file) |
|---|---|---|
| Instrument-data interpretation | **SIRIUS** | same + MetFrag |
| Power analysis | still empty (N-Power preprint only) | **PowerGPT** live, 0 users today |
| Reviewer-response letters | still empty | **RefereeBio** live, candidate-grade |
| NIH biosketch / CV | SciENcv only | **BioSketch Builder** live, not recommendable; narrative CV still empty |
| Conference matching | Thesify “not in app” | same |
| Figure alt-text | FigurA11y not production | same |
| Press-release drafting | Prowly is Semrush marketing | plus EurekAlert **bans AI text** (1 Jul 2026) |

---

## What this hunt did not check

- Did not run a PowerGPT calculation, a SIRIUS job, a DSW/ARGOS plan, or a
  RefereeBio R&R on a real manuscript.
- Did not log into TERA, Sage Policy Profiles, or Overton.
- Did not test whether a given campus Qualtrics licence includes Fraud Detection,
  or whether UJEP / UK / AV ČR REDCap has 15.0 AI enabled.
- Did not verify WebPlotDigitizer AI Assist paywall or image-routing.
- Did not independently re-verify every arXiv/DOI cited by vendors beyond
  Clark 2025, PowerGPT arXiv:2509.12471, and the EurekAlert guidelines page.
- Japanese / Chinese / SciELO primary product pages were not exhaustively
  fetched. CNKI AI was blocked.
- Ithaka S+R GenAI Product Tracker Airtable did not return readable rows.
- This file does not add tools to `tools/` or change `categories.yml`.

---

## Library-guide sources (search-strategy and RDM)

Fetched 2026-08-18; used to confirm that the *task* is named, not to endorse tools.

- [Toronto Gerstein — Can ChatGPT write a comprehensive search strategy?](https://guides.library.utoronto.ca/c.php?g=577919&p=5332074)
- [McGill — Tools for search strategy development](https://libraryguides.mcgill.ca/text-mining/search-tools)
- [KCL — AI tools in evidence synthesis](https://libguides.kcl.ac.uk/systematicreview/ai)
- [Edinburgh — Using ELM to develop a search strategy](https://edinburgh-uk.libguides.com/gen-AI/literature-searching)
- [Stanford Lane — AI Tools in Action](https://laneguides.stanford.edu/AI/tools)
- [Utrecht — AI Tools](https://libguides.library.uu.nl/Artificial_Intelligence/tools)
- [NTK Praha — AI nástroje pro výzkum](https://www.techlib.cz/cs/84764-ai-nastroje-pro-vyzkum-umela-inteligence)
- [UNB — AI and Research Data Management](https://lib.unb.ca/guides/artificial-intelligence-ai-and-research-data-management) (updated 17 Aug 2026)
- [UNC — GenAI for research, including Engage & Measure Impact](https://guides.lib.unc.edu/genai_for_research)

---

## Next gate

If any of these become catalog categories, that is a `categories.yml` change and
needs explicit approval. Proposed first three, if wanted:

1. `instrument-data-interpretation` — core: SIRIUS
2. Search-strategy as a use-case (or split) under systematic review — core: Polyglot / Yale MeSH Analyzer
3. `data-management-fair` — core: Data Stewardship Wizard (+ F-UJI for the deposit-time slot)

Textwash is the strongest fourth if the criterion is “EU-native and AI in the
strict sense.”
