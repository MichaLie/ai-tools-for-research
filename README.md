# AI Tools for Scientific Research

A curated list of AI tools that are actually useful in research work. I keep it
for my courses and workshops on AI in science, which makes it opinionated on
purpose: for each research task you get a handful of tools people really use,
not everything that exists.

Right now: 161 tools across 35 task areas. Latest successful public-source check: 15 October 2026.
Individual verification dates vary; flagged entries still need review.

This space moves fast. Tools rename, merge and die constantly, so if something
you need is missing, check back in a week or open an issue. For real depth in
three areas (biological foundation models, autonomous science agents,
privacy-first coding and data tools) I keep separate indexes at
[michalie.github.io](https://michalie.github.io/).

The searchable version, with the task map up top, is at
**[michalie.github.io/ai-tools-for-research](https://michalie.github.io/ai-tools-for-research/)**.

## How the list works

Every tool belongs to one task category and is either shown directly (the few
worth putting on a course slide) or folded into "more tools for this task"
in its section. Entries marked \* are flagged for re-verification. Dead tools
are not deleted; they move to the Retired section at the bottom, because the
history is part of the story.

## The map

Tasks grouped by research stage:

- **Everyday AI** · [General-Purpose AI Assistants](#general-purpose-ai-assistants) (8) · [Office Suite AI Integrations](#office-suite-ai-integrations) (2) · [Browser Automation Agents](#browser-automation-agents) (2)
- **Discover & Learn** · [AI-Powered Search Engines](#ai-powered-search-engines) (1) · [Deep Research Agents](#deep-research-agents) (5) · [Literature Discovery & Analysis](#literature-discovery-analysis) (8) · [Publisher & Database AI Assistants](#publisher-database-ai-assistants) (4) · [Citation Networks & Reference Management](#citation-networks-reference-management) (3) · [Grounded Knowledge & Specialized Databases](#grounded-knowledge-specialized-databases) (1) · [Systematic Review & Evidence Synthesis](#systematic-review-evidence-synthesis) (10) · [Staying Current](#staying-current) (5)
- **Plan & Design** · [Ideation & Grant Funding](#ideation-grant-funding) (5) · [Survey & Experiment Design](#survey-experiment-design) (4) · [Data Management & FAIR](#data-management-fair) (4)
- **Collect & Analyze** · [Data Analysis](#data-analysis) (4) · [Autonomous Research Agents](#autonomous-research-agents) (7) · [Code Assistants](#code-assistants) (5) · [Transcription & Qualitative Analysis](#transcription-qualitative-analysis) (8) · [OCR & Document Digitization](#ocr-document-digitization) (6) · [Lab Bench & Protocols](#lab-bench-protocols) (4) · [Instrument Data Interpretation](#instrument-data-interpretation) (2) · [Bioimage Analysis](#bioimage-analysis) (3) · [Behavioral Video Analysis](#behavioral-video-analysis) (3) · [De-identification & Data Sharing](#de-identification-data-sharing) (4)
- **Write & Illustrate** · [Writing & Translation](#writing-translation) (6) · [Visual & Presentation Creation](#visual-presentation-creation) (4) · [Scientific Image Generation](#scientific-image-generation) (3) · [LaTeX & Academic Language](#latex-academic-language) (5)
- **Review & Publish** · [AI Manuscript Review & Disclosure](#ai-manuscript-review-disclosure) (10) · [Integrity Screening & Forensics](#integrity-screening-forensics) (5) · [Journal Selection & Publishing](#journal-selection-publishing) (1)
- **Share & Impact** · [Conference Prep — Posters & Talk Practice](#conference-prep-—-posters-talk-practice) (6) · [Research Communication & Accessibility](#research-communication-accessibility) (6) · [Patents & Tech Transfer](#patents-tech-transfer) (6) · [Impact & Policy Tracking](#impact-policy-tracking) (1)

## General-Purpose AI Assistants

*The task: an everyday thinking partner — drafting, summarizing, coding help, quick analysis at any stage of research.*

| Tool | Provider | Access | Description |
|---|---|---|---|
| [ChatGPT](https://chatgpt.com/) | OpenAI | Freemium | Draft, research, analyze uploaded data, and create images in ChatGPT. Deep Research produces source-linked reports; free access includes limited file and image capabilities, with higher usage limits on paid plans. |
| [Claude](https://claude.ai/) | Anthropic | Freemium | Read and draft documents, search the web, create files, and run code with Claude. Free access has usage limits; paid plans add Claude Code, Claude Science, and integrations with Chrome and Microsoft 365. |
| [Gemini](https://gemini.google.com/) | Google | Freemium | Analyze documents and multimodal inputs, draft text, and research questions with Google’s AI assistant. Deep Research combines web sources and optional connected Workspace content into reports; free and paid plans have different limits. |
| [Microsoft Copilot](https://copilot.com/) | Microsoft | Freemium | Ask questions and create images, documents, spreadsheets, and presentations with Microsoft Copilot. Available capabilities depend on the signed-in account, subscription, and organizational settings; work and school accounts can connect organizational content. |

<details><summary>More tools for this task (4)</summary>

| Tool | Provider | Access | Description |
|---|---|---|---|
| [Google AI Studio](https://aistudio.google.com/) | Google | Free | Experiment with Gemini prompts and models in a browser, prototype applications, and obtain code for API integration. Web-workspace access and API usage have separate limits and pricing considerations. |
| [Grok](https://grok.com/) | SpaceXSI | Freemium | Ask questions, write code, and create images with an assistant that draws on the web and X for current information. Free access and paid subscriptions offer different usage limits. |
| [LM Council](https://lmcouncil.ai/) | — | Freemium | Compare responses from multiple language models and let models discuss a question with one another. Useful for examining how different systems approach the same research or writing task. |
| [Vibe (Mistral, formerly Le Chat)](https://chat.mistral.ai/) | Mistral AI | Freemium | Mistral’s Vibe, formerly Le Chat, supports chat, connected work tasks, and coding. Free access includes limited web searches and coding sessions; paid plans raise limits and add document creation capabilities. |

</details>

## Office Suite AI Integrations

*The task: AI inside the documents, spreadsheets and slides you already work in.*

| Tool | Provider | Access | Description |
|---|---|---|---|
| [Microsoft Copilot — editing in Office](https://www.microsoft.com/microsoft-365/copilot) | Microsoft | Paid | Create and revise editable Word documents, Excel workbooks, and PowerPoint presentations directly in Office with Copilot. Formerly called Agent Mode; available editing features depend on the app, subscription, rollout, and organizational settings. |

<details><summary>More tools for this task (1)</summary>

| Tool | Provider | Access | Description |
|---|---|---|---|
| [Claude for Microsoft 365](https://claude.com/claude-for-microsoft-365) | Anthropic | Paid | Revise Office files with shared context across applications: analyze Excel workbooks, edit Word text with tracked changes, build PowerPoint slides from templates, and draft Outlook replies. Requires a paid Claude plan; Outlook remains beta. |

</details>

## Browser Automation Agents

*The task: let AI operate the browser — forms, portals, repetitive web work.*

| Tool | Provider | Access | Description |
|---|---|---|---|
| [Claude in Chrome](https://claude.com/claude-in-chrome) | Anthropic | Paid | Let Claude read web pages, navigate across tabs, fill forms, and perform browser tasks. The extension connects with Claude and Claude Code; available on paid plans, with controls over the actions it can take. |
| [Comet](https://www.perplexity.ai/comet) | Perplexity AI | Freemium | Browse and research with Perplexity’s AI assistant in a Chromium-based browser. The assistant uses the current page and tabs as context for questions and web tasks; available on desktop and mobile. |

## AI-Powered Search Engines

*The task: ask the web a question and get a sourced answer instead of a list of links.*

| Tool | Provider | Access | Description |
|---|---|---|---|
| [Perplexity](https://www.perplexity.ai/) | Perplexity AI | Freemium | Use an AI answer engine to research questions on the web and follow the sources behind its answers. Free access is available, with paid plans for higher limits and additional capabilities. |

## Deep Research Agents

*The task: delegate a multi-hour literature synthesis and get back a cited report.*

| Tool | Provider | Access | Description |
|---|---|---|---|
| [ChatGPT Deep Research](https://openai.com/index/introducing-deep-research/) | OpenAI | Freemium | Delegate a multi-step investigation across the web, uploaded files, and supported connected sources, then inspect a report with citations. Source availability and usage limits depend on your plan and workspace settings. |
| [STORM](https://storm.genie.stanford.edu/) | Stanford OVAL Lab | Free | Explore a topic through perspective-guided questions and cited outlines. Co-STORM lets you steer an expert-agent discussion and inspect an evolving mind map; this MIT-licensed research prototype offers a web preview and customizable local setup. |

<details><summary>More tools for this task (3)</summary>

| Tool | Provider | Access | Description |
|---|---|---|---|
| [Claude Research](https://claude.com/resources/articles/research) | Anthropic | Paid | Investigate a question through successive searches across the web and connected sources, then inspect a cited report in Claude. Research is available on paid plans; connected-source access depends on permissions and configuration. |
| [Edison Literature (formerly Falcon)](https://platform.edisonscientific.com/) \* | Edison Scientific | Freemium | Search scientific literature and synthesize findings with citations on the Edison Scientific platform. The platform displayed a temporary service-outage notice during this check; availability needs re-verification. |
| [Gemini Deep Research](https://gemini.google/overview/deep-research/) | Google | Freemium | Plan and delegate an investigation using the web, uploaded files, and optionally connected Google Workspace sources, then inspect a cited report. Available sources and usage limits depend on your account and plan. |

</details>

## Literature Discovery & Analysis

*The task: find, screen and synthesize papers beyond what you can read yourself.*

| Tool | Provider | Access | Description |
|---|---|---|---|
| [Consensus](https://consensus.app/) | Consensus | Freemium | Ask a research question, compare paper-level answers, and inspect how selected studies agree or disagree using the Consensus Meter. Research Agent handles deeper searches; the meter’s conclusions depend on the retrieved studies. |
| [Elicit](https://elicit.com/) | Elicit | Freemium | Find papers, screen studies, extract data, and produce research reports with AI-assisted evidence workflows. Researchers can customize covered studies and extraction questions; free access and paid plans serve different workloads. |
| [SciSpace (Typeset)](https://scispace.com/) | SciSpace | Freemium | Search scientific literature, chat with PDFs, compare study findings, and synthesize evidence with Deep Review. Writing and citation tools are available; the journal-formatting editor has a separate plan structure. |
| [Scite](https://scite.ai/) | Research Solutions | Paid | Smart Citations platform showing whether later papers support, contrast, or merely mention cited work. 1.6B+ citations from 317M+ full-text articles, classified by deep learning to evaluate how a claim, paper, or author has been received. |
| [Semantic Scholar](https://www.semanticscholar.org/) | Allen Institute for AI (Ai2) | Free | Find scholarly literature with AI-assisted search, TLDR summaries, citation relationships, and Semantic Reader for supported papers. Free access and a developer API support literature discovery and research applications. |

<details><summary>More tools for this task (3)</summary>

| Tool | Provider | Access | Description |
|---|---|---|---|
| [AlphaXiv](https://www.alphaxiv.org/) | alphaXiv | Free | Discover and discuss arXiv papers, ask questions grounded in the literature, and explore related researchers and organizations. Browser-extension and MCP access connect the service to research workflows. |
| [AnswerThis](https://answerthis.io/) | AnswerThis | Freemium | Generates literature reviews with line-by-line citations over 300M+ papers, trials and PDFs; includes research-gap identification, citation mapping, systematic-review tools and an AI writer with 2,000+ citation styles. Free starter tier. |
| [Paperclip by GXL](https://gxl.ai/paperclip) | Generative Expert Labs, Inc. | Freemium | Give research agents searchable, line-citable evidence from papers, patents, trials, and scientific databases via browser, CLI, or MCP. Free and paid tiers; terms permit training on submitted content, so use public research material. |

</details>

## Publisher & Database AI Assistants

*The task: interrogate the curated scholarly databases your library already licenses.*

| Tool | Provider | Access | Description |
|---|---|---|---|
| [JSTOR AI Research Tool](https://about.jstor.org/products/jstor-platform/features-and-tools/research-tool/) | Ithaka (JSTOR) | Institutional | Free to JSTOR-participating institutions. Surfaces key points and arguments from articles, book chapters and research reports; recommends related topics and content; supports natural-language Q&A grounded in the document with inline references. Particularly strong for humanities, arts and social sciences. |
| [Scopus with AI](https://www.elsevier.com/products/scopus/scopus-ai) | Elsevier | Institutional | GenAI research assistant integrated into Scopus (now branded 'Scopus with AI'), drawing on content from 7,000+ publishers. Delivers referenced summaries, concept maps, emerging themes, foundational papers, and downloadable Deep Research agentic reports; RAG grounded only in curated Scopus content. |
| [Web of Science Research Assistant](https://clarivate.com/academia-government/scientific-and-academic-research/research-discovery-and-referencing/web-of-science/web-of-science-research-assistant/) \* | Clarivate | Institutional | AI assistant for exploring topics, finding journals, and reviewing literature using Web of Science content. Provides guided workflows, visualizations, and referenced responses; live product-page verification was blocked during this check. |

<details><summary>More tools for this task (1)</summary>

| Tool | Provider | Access | Description |
|---|---|---|---|
| [LeapSpace (formerly ScienceDirect AI)](https://www.elsevier.com/products/leapspace) | Elsevier | Paid | Search and compare scholarly evidence in Elsevier’s LeapSpace workspace, with document chat, Trust Cards, Claim Radar, and Writing Coach. Available through individual and institutional access routes. |

</details>

## Citation Networks & Reference Management

*The task: map citation networks and keep your reference library organized.*

| Tool | Provider | Access | Description |
|---|---|---|---|
| [ResearchRabbit](https://www.researchrabbit.ai/) | Litmaps | Freemium | Explore related papers through citation networks and recommendations, organize collections, and import references from Zotero. Free discovery features are complemented by a paid RR+ plan. |
| [Zotero](https://www.zotero.org/) | Digital Scholar | Free | Collect, organize, annotate, and cite sources with a free open-source reference manager. Browser capture and Word, LibreOffice, and Google Docs integrations support reference management; third-party extensions provide optional AI features. |

<details><summary>More tools for this task (1)</summary>

| Tool | Provider | Access | Description |
|---|---|---|---|
| [Litmaps](https://www.litmaps.com/) | Litmaps | Freemium | Interactive citation network visualizations showing papers by publication year and citation relationships. Automated monitoring alerts when new relevant papers are published. Integrates OpenAlex, Semantic Scholar, and Crossref. |

</details>

## Grounded Knowledge & Specialized Databases

*The task: chat with your own sources — grounded answers from documents you trust.*

| Tool | Provider | Access | Description |
|---|---|---|---|
| [Gemini Notebook (formerly NotebookLM)](https://notebook.google/) | Google | Freemium | Upload papers and notes, ask questions with citations back to your sources, and turn the collection into podcast-style Audio Overviews or presentations. Gemini Notebook, formerly NotebookLM, offers free access with higher limits on paid plans. |

## Systematic Review & Evidence Synthesis

*The task: screen thousands of abstracts, extract evidence, and keep a review living — PRISMA-style.*

| Tool | Provider | Access | Description |
|---|---|---|---|
| [ASReview](https://asreview.nl/) | Utrecht University (open source) | Free | Runs active-learning screening locally: the model learns from your include/exclude decisions and reorders remaining records, with simulation mode to benchmark savings on your own dataset. Fully open source; data never leaves your machine. |
| [citationchaser](https://estech.shinyapps.io/citationchaser/) | Neal R. Haddaway (with M.J. Grainger, C.T. Gray) | Free | Forward and backward citation chasing via the Lens.org API: input known relevant articles, retrieve everything they reference and everything citing them, and download all lists as RIS for systematic-review identification. |
| [Covidence](https://www.covidence.org/) | Covidence (not-for-profit, Cochrane partnership) | Institutional | Manages the full PRISMA pipeline in one workspace: import, dedupe, dual screening, full-text review, data extraction, and quality assessment, with team roles and export to analysis. De-facto standard licensed by many university libraries. |
| [Nested Knowledge](https://nested-knowledge.com/) | Nested Knowledge, Inc. | Freemium | Combines screening (Robot Screener), smart tagging, meta-analytical extraction, and PRISMA reporting with living-review updates: searches re-run automatically and interactive evidence maps and synthesis visualizations stay current and shareable. |
| [Polyglot (TERA)](https://tera-tools.com/) | Institute for Evidence-Based Healthcare (IEBH), Bond University | Freemium | Translates a PubMed or Ovid MEDLINE search string into syntax for Embase, CINAHL, PsycINFO, Scopus, Web of Science, Cochrane and more. Part of Bond IEBH's TERA evidence-synthesis suite (SearchRefiner, Deduplicator, Screenatron, Disputatron). |
| [Rayyan](https://www.rayyan.ai/) | Rayyan Systems, Inc. | Freemium | Screen abstracts and full texts independently with blinded reviewer decisions, AI relevance ranking, and conflict resolution; deduplicate records and extract study data within a shared review. A free tier supports basic screening. |

<details><summary>More tools for this task (4)</summary>

| Tool | Provider | Access | Description |
|---|---|---|---|
| [DistillerSR](https://www.distillersr.com/) | DistillerSR Inc. (Evidence Partners) | Paid | Runs audit-trailed literature reviews at regulatory grade: AI reranking of references, automatic study classifiers, generative extraction linked back to source text, and error-checking of human screening decisions, all with traceable human-in-the-loop validation. |
| [Laser AI](https://www.laser.ai/) | Evidence Prime (makers of GRADEpro) | Paid | Extracts data from study PDFs by suggesting text passages and table values for reviewer confirmation, deduplicates references, and standardizes screening with reusable guides and vocabularies; built for living evidence synthesis feeding guideline pipelines. |
| [PubReMiner](https://hgserver2.amc.nl/cgi-bin/miner/miner2.cgi) | Jan Koster, AMC (Amsterdam UMC) | Free | Runs a PubMed query and returns frequency tables of journals, authors and words in the result set — for refining search terms, finding active experts, or choosing a target journal. |
| [Yale MeSH Analyzer](https://mesh.med.yale.edu/) | Harvey Cushing/John Hay Whitney Medical Library, Yale University | Free | Paste up to 20 PMIDs to get a side-by-side grid of each article's MeSH headings, subheadings, major-topic flags and author keywords; exports Excel or HTML for building search strategies. |

</details>

## Staying Current

*The task: keep up with new papers without reading feeds all day — trained, personalized monitoring.*

| Tool | Provider | Access | Description |
|---|---|---|---|
| [LitSuggest](https://www.ncbi.nlm.nih.gov/research/litsuggest/) | NCBI / National Library of Medicine (NIH) | Free | Train a personal machine-learning classifier by marking PubMed articles relevant or irrelevant; the system then scores new PubMed papers, sends an automated weekly digest per project, and supports shared collaborative curation. |
| [R Discovery](https://discovery.researcher.life/) | Cactus Communications (Editage) | Freemium | Personalized reading feed over 250M+ papers: set research interests, get daily article recommendations and new-paper alerts, listen to audio versions, translate papers into 30+ languages, and chat with PDFs on mobile or web. |
| [Scholar Inbox](https://www.scholar-inbox.com/) | University of Tübingen (Autonomous Vision Group / Tübingen AI Center) | Free | Daily or weekly digest of new arXiv, bioRxiv, chemRxiv and medRxiv papers ranked by a recommender trained on the user's own ratings; includes semantic search, figure-preview skimming, collections, and a conference poster-session planner. |

<details><summary>More tools for this task (2)</summary>

| Tool | Provider | Access | Description |
|---|---|---|---|
| [Paper Digest](https://www.paperdigest.org/daily-paper-digest/) | Paper Digest (New York, US) | Freemium | Daily email digest of new papers from arXiv, PubMed, bioRxiv, medRxiv and ClinicalTrials.gov, filtered by user-set areas, keywords and authors, with a machine-generated one-sentence summary per paper and impact-based ranking. |
| [Stork](https://www.storkapp.me/) | Xu Cui (indie) | Freemium | Enter keywords and authors once; receive daily or weekly email alerts of matching new papers and preprints from PubMed and other sources, plus NIH grant-award alerts, with optional in-email translation of titles and abstracts. |

</details>

## Ideation & Grant Funding

*The task: find the gap, find the call, draft the proposal.*

| Tool | Provider | Access | Description |
|---|---|---|---|
| [ChatAcademia (formerly Research Kick)](https://www.chatacademia.com/) | ChatAcademia | Paid | Develop research questions, assess gaps and novelty, find literature and grants, and organize evidence in ChatAcademia. The workspace also offers data-analysis planning, claim checks, and manuscript-review tools; a free trial is available. |
| [Granted AI](https://grantedai.com/) | Granted AI | Freemium | Find funding opportunities and funder profiles, track applications, and draft proposals from uploaded requirements. AI coaching, compliance checks, and simulated review support application preparation; free and paid access are available. |
| [Instrumentl](https://www.instrumentl.com/) | Instrumentl | Paid | Find grants matched to a project, refine results with the AI Prospecting Assistant, and track funding opportunities. Paid plans and a free trial are available; grant-writing capabilities depend on the subscription. |

<details><summary>More tools for this task (2)</summary>

| Tool | Provider | Access | Description |
|---|---|---|---|
| [Grantable](https://grantable.co/) | Grantable | Freemium | Find relevant funders, assess opportunities, and draft grant proposals using your organization’s documents and past applications. The platform supports proposal checklists and grant tracking, with free and paid access. |
| [GrantBoost](https://www.grantboost.io/) | GrantBoost | Freemium | Discover matched grants, organize a funding pipeline, and draft proposals using templates and your organization’s voice. A permanent limited free plan is available; paid plans separate discovery from proposal-writing features. |

</details>

## Survey & Experiment Design

*The task: design instruments and experiments well before collecting a single data point — including simulated piloting.*

| Tool | Provider | Access | Description |
|---|---|---|---|
| [Expected Parrot](https://www.expectedparrot.com) | Expected Parrot, Inc. | Freemium | Open-source Python DSL for building surveys and experiments, running them on panels of LLM-simulated respondents across many models, then re-fielding the identical instrument to real humans ('Humanize') and analyzing both in one results object. |
| [NC3Rs Experimental Design Assistant](https://eda.nc3rs.org.uk/) | NC3Rs (UK) | Free | Free web tool where researchers diagram an in vivo experiment and receive automated bespoke critique: statistical-method recommendations, randomization and blinding support, sample-size calculation, and a shareable design report for funders and ethical review. |
| [Qualtrics AI](https://www.qualtrics.com/support/survey-platform/distributions-module/synthetic-panels/) | Qualtrics | Institutional | Create and evaluate surveys in Qualtrics, including simulated responses through Synthetic Panels. The documented panel represents the United States general population; availability depends on institutional licensing and enabled features. |

<details><summary>More tools for this task (1)</summary>

| Tool | Provider | Access | Description |
|---|---|---|---|
| [Synthetic Users](https://www.syntheticusers.com/) | Synthetic Users Inc. | Paid | Runs no-code simulated qualitative studies: multi-agent AI participants with persistent persona profiles answer interviews, concept tests, and usability-style questions in minutes, at $2-60 per interview instead of recruiting humans. |

</details>

## Data Management & FAIR

*The task: funder-compliant, machine-actionable data management plans and FAIR checks on what you deposit.*

| Tool | Provider | Access | Description |
|---|---|---|---|
| [ARGOS (OpenAIRE)](https://argos.openaire.eu/portal/) | OpenAIRE | Freemium | Creates data and software management plans from funder and institutional templates, produces machine-actionable DMPs, and publishes finished plans to Zenodo. OpenAIRE service integrated with EOSC; free for individual researchers. |
| [Data Stewardship Wizard](https://ds-wizard.org/) | ELIXIR CZ / Czech Technical University in Prague | Free | Builds collaborative, machine-actionable data management plans via guided knowledge-model questionnaires, with FAIR guidance, versioning, and funder-compliant exports including Horizon Europe. Open-source ELIXIR Recommended Interoperability Resource. |
| [F-UJI](https://www.f-uji.net/) | PANGAEA (Devaraju & Huber), developed under FAIRsFAIR (H2020 grant 831558) | Free | Scores a published dataset's FAIRness from its identifier, programmatically evaluating the actual harvested metadata against the FAIRsFAIR data object assessment metrics, via web interface and web service. |

<details><summary>More tools for this task (1)</summary>

| Tool | Provider | Access | Description |
|---|---|---|---|
| [FAIR-Checker](https://fair-checker.france-bioinformatique.fr/) \* | Institut Français de Bioinformatique (IFB) / ELIXIR France | Free | Assesses FAIRness of a web resource or dataset by extracting its metadata and validating it against DataCite, OpenAIRE, Wikidata, Linked Open Vocabularies, and Bioschemas community profiles, to help providers improve resource quality. |

</details>

## Data Analysis

*The task: analyze data conversationally — upload, ask, get code and plots back.*

**Going deeper:** [Coding & Data Agents index (privacy-first, 60 entries)](https://michalie.github.io/research-coding-agents-wiki/) →

| Tool | Provider | Access | Description |
|---|---|---|---|
| [Benchling AI](https://www.benchling.com/ai) | Benchling | Freemium | Query Benchling records, import PDFs and external reports as structured data, draft notebook entries and study reports, and run protein structure models within the notebook. Free access is available to academic scientists. |
| [ChatGPT Data Analysis (Code Interpreter)](https://help.openai.com/en/articles/8437071-data-analysis-with-chatgpt) | OpenAI | Freemium | Upload data to ChatGPT for cleaning, calculations, statistical analysis, and charts. For suitable tasks it executes Python in a notebook environment and exposes results and analysis details for review; usage varies by plan. |
| [Julius](https://julius.ai/) | Julius AI | Freemium | Analyze data and spreadsheets through conversational requests, then create charts, reports, and presentations. Julius also supports data connections and app-building tools; review its current plans for usage and access limits. |

<details><summary>More tools for this task (1)</summary>

| Tool | Provider | Access | Description |
|---|---|---|---|
| [Claude Code Interpreter](https://claude.com/resources/articles/create-files) | Anthropic | Freemium | Create and edit spreadsheets, documents, presentations, and PDFs, or analyze data by running code within Claude. File creation and code execution are included in the free plan with usage limits; paid plans offer more capacity. |

</details>

## Autonomous Research Agents

*The task: hand an agent a research question and let it plan, execute and report autonomously.*

**Going deeper:** [Autonomous Science Agents index (438 entries)](https://michalie.github.io/autonomous-stem-agents-wiki/) →

| Tool | Provider | Access | Description |
|---|---|---|---|
| [BIOS / BioAgents](https://ai.bio.xyz/) | bio.xyz (Bio Protocol) | Free | Ask research questions and receive cited answers from a system that searches literature and scientific databases and performs analyses. The broader BIOS platform also advertises drug-discovery services. |
| [Kosmos](https://edisonscientific.com/) \* | Edison Scientific | Paid | Run scientific investigations that combine literature review, data analysis, and hypothesis development, with options to steer ongoing work. Edison’s platform displayed a temporary outage during this check; current access needs re-verification. |

<details><summary>More tools for this task (5)</summary>

| Tool | Provider | Access | Description |
|---|---|---|---|
| [AIVA](https://chat.aivaportal.com/) | Mamidi Health | Freemium | Query genomic datasets, annotate variants, search literature, and create visualizations through a conversational interface. A free account offers limited use; uploading samples requires trial or paid access. |
| [Heureka Bench](https://www.heurekalabs.co/) | Heureka Labs | Free | Heureka Bench: local-first desktop notebook with the ARC research agent and a proprietary biology model (Archimedes) for multi-omics data analysis, hypothesis generation, experiment design, QC and literature curation. Free macOS/Windows download, no subscription; optional cloud compute. |
| [K-Dense](https://www.k-dense.ai/) | K-Dense Inc. | Freemium | Plan and execute scientific research tasks with agents that search literature, run analyses, and produce reports. Hosted plans include a free Instant level; separate open-source tools support user-provided models and research workflows. |
| [Pipette.bio](https://pipette.bio/) | Variome Analytics | Freemium | Bioinformatics AI agent that plans and runs genomics, transcriptomics, single-cell, ChIP-seq, variant-calling and metagenomics analyses from natural-language requests, on 150+ open-source tools with reproducibility bundles. Free tier (20 credits/month); paid packs and lab plans. |
| [Potato](https://potato.ai/) | Happy Potato, Inc. | Freemium | AI co-scientist for wet-lab work: generates protocols from stated intent, explores related literature and reviews papers on a free individual workspace; paid Optimizer tiers add guided and Bayesian experimental-design rounds and robot-ready outputs. |

</details>

## Code Assistants

*The task: write and debug research code with an AI pair programmer or agent.*

**Going deeper:** [Coding & Data Agents index (privacy-first, 60 entries)](https://michalie.github.io/research-coding-agents-wiki/) →

| Tool | Provider | Access | Description |
|---|---|---|---|
| [Claude Code](https://claude.com/product/claude-code) | Anthropic | Paid | Terminal-based agentic coding tool for code generation, debugging, and repository-wide modifications through natural language, also available in IDEs, Slack and the web. CLAUDE.md configuration for project conventions. |
| [Cursor](https://cursor.com/) | Anysphere (SpaceX) | Freemium | Write and revise code with an AI editor and agents that can work across files, run checks, and prepare changes for review. A free tier and paid plans offer different completion and agent limits. |
| [GitHub Copilot](https://github.com/features/copilot) | GitHub (Microsoft) | Freemium | Get code suggestions and delegate repository tasks to coding agents across supported development environments. Copilot offers free and paid plans, with features and model access varying by plan; eligible students have a dedicated program. |

<details><summary>More tools for this task (2)</summary>

| Tool | Provider | Access | Description |
|---|---|---|---|
| [Codex](https://openai.com/codex/) | OpenAI | Freemium | Delegate coding tasks through the Codex app, CLI, IDE integrations, or cloud environments. Agents can edit repositories, run checks, and prepare changes for review; access and usage allowances depend on the ChatGPT plan. |
| [Google Antigravity](https://antigravity.google/) | Google | Freemium | Develop software with Google’s agents across an app, CLI, and IDE, using terminal and browser tools. Projects, parallel workspaces, and scheduled tasks support longer development workflows. |

</details>

## Transcription & Qualitative Analysis

*The task: turn interviews and focus groups into text, then into coded themes — with sensitive data kept safe.*

| Tool | Provider | Access | Description |
|---|---|---|---|
| [Evidano](https://www.evidano.com/) | Evidano | Freemium | Uploads interview transcripts, documents, audio/video and runs thematic analysis with supporting quotes, frequency and cross-segment analysis, plus a chatbot over the data. Also fields an AI avatar that conducts semi-structured voice interviews in 100+ languages. Free tier available. |
| [MAXQDA AI Assist](https://www.maxqda.com/products/ai-assist) | VERBI GmbH (Germany) | Institutional | AI add-on inside the MAXQDA CAQDAS: suggests codes and subcodes for text passages with explanatory comments, summarizes documents and coded segments, and answers questions about coded data with responses linked to text sections. Claims zero data retention and EU-based processing. |
| [noScribe](https://noscribe.de/en/) | Kai Dröge (open-source, GPL-3.0) | Free | Transcribes interview audio fully offline on the researcher's own computer using Whisper plus pyannote speaker diarization; marks pauses, overlaps and filler words per qualitative-research conventions; includes an audio-aligned correction editor. ~60 languages; Windows/macOS/Linux. |
| [QualCoder](https://qualcoder.org/) | Colin Curtain (open-source, LGPLv3) | Free | Code and analyze qualitative text, PDFs, images, audio, and video in an open-source desktop tool. Optional AI-assisted coding and data chat use configurable model backends and an editable prompt library. |

<details><summary>More tools for this task (4)</summary>

| Tool | Provider | Access | Description |
|---|---|---|---|
| [Amberscript](https://www.amberscript.com/en/business-solutions-use-cases/transcription-services-qualitative-research/) | Amberscript (Netherlands) | Paid | Cloud transcription for research interviews: machine drafts in minutes (90+ languages, ~85% accuracy) or human-verified transcripts (>99%, 18+ languages) with NDA-bound transcribers. Data stored only in Western Europe; GDPR, ISO 27001/9001. Word/TXT export, speech-to-text API. |
| [aTrain](https://business-analytics.uni-graz.at/en/research/atrain/) | University of Graz (BANDAS Center) | Free | Offline transcription of speech recordings with speaker detection (faster-whisper, 57 languages); exports transcripts with clickable timestamps directly importable into ATLAS.ti and MAXQDA. Installs from the Microsoft Store; no data ever sent to the internet. |
| [Montreal Forced Aligner](https://github.com/MontrealCorpusTools/Montreal-Forced-Aligner) | Montreal Corpus Tools (Michael McAuliffe et al.) | Free | Command-line forced aligner built on Kaldi: time-aligns transcripts to audio at word and phone level using pretrained or self-trained acoustic models. MIT-licensed; installed via conda-forge; v3.0 cited (2026). |
| [WebMAUS](https://clarin.phonetik.uni-muenchen.de/BASWebServices/interface/WebMAUSGeneral) | Bavarian Archive for Speech Signals (BAS), LMU Munich / CLARIN | Free | Web service for forced alignment: upload audio plus transcript, receive phone- and word-level time-aligned Praat TextGrid output. Munich Automatic Segmentation (MAUS) engine within the BAS/CLARIN speech-tools suite. |

</details>

## OCR & Document Digitization

*The task: turn handwriting, archives, equations and PDFs into editable, analyzable text and LaTeX.*

| Tool | Provider | Access | Description |
|---|---|---|---|
| [Marker](https://github.com/datalab-to/marker) | Datalab | Free | Open-source pipeline converting PDF, DOCX, PPTX, EPUB, and images to Markdown, JSON, or HTML with equations, tables, and reading order preserved — for building searchable or LLM-ready corpora from paper collections; runs locally. |
| [Mathpix](https://mathpix.com/) | Mathpix Inc. | Freemium | Screenshot-to-LaTeX OCR: converts images of equations, handwriting, chemistry structures, tables, and full PDFs into LaTeX, Markdown, DOCX, or CSV via the Snip desktop tool and editor. One keyboard shortcut turns any on-screen formula into paste-ready code. |
| [Transkribus](https://www.transkribus.org/pricing) | READ-COOP SCE (European cooperative, Austria) | Freemium | Uploads scans of handwritten or printed historical documents and gets searchable transcriptions; trains custom recognition models for a specific hand, script, or language; recognizes tables and form fields. |
| [WebPlotDigitizer](https://automeris.io/) | Automeris LLC (Ankit Rohatgi) | Free | Extract numerical data from chart images and PDFs using manual tools, computer vision, and AI assistance. Supports several plot types through a browser interface; review the extracted data against the original figure. |

<details><summary>More tools for this task (2)</summary>

| Tool | Provider | Access | Description |
|---|---|---|---|
| [eScriptorium](https://escriptorium.eu/about/) | École Pratique des Hautes Études (EPHE) + Inria ALMAnaCH (France) | Free | Open-source web platform for segmenting and transcribing manuscripts and archival documents using the kraken HTR engine; researchers train or fine-tune their own recognition models and export ALTO/PAGE XML; self-hostable, IIIF-compatible. |
| [Handwriting OCR](https://www.handwritingocr.com/research-handwriting-ocr) | Handwriting OCR Ltd (UK) | Freemium | Uploads pages of contemporary handwriting — lab notebooks, field observation sheets, questionnaires, cursive letters — and returns searchable editable text; handles mixed hands, faded ink, and converts embedded equations to LaTeX. |

</details>

## Lab Bench & Protocols

*The task: draft, troubleshoot and execute protocols at the bench — hands-free, robot-ready, reagent-smart.*

| Tool | Provider | Access | Description |
|---|---|---|---|
| [BenchSci / EMET](https://www.benchsci.com/) | BenchSci (Toronto) | Free | Find evidence about antibodies, reagents, and experimental models in BenchSci’s EMET workspace to inform laboratory resource selection. Limited access is free for academic, nonprofit, and government researchers. |
| [OpentronsAI](https://opentrons.com/ai) | Opentrons | Free | Generates executable, inspectable Python protocols for Opentrons liquid-handling robots from a natural-language description of the experiment, with in-chat simulation, verification, and deck-map visualization. Sign-up works even without owning a robot. |
| [protocols.io AI](https://group.springernature.com/gp/group/media/press-releases/new-ai-capabilities-on-protocolsio/27837624) | Springer Nature | Freemium | Drafts structured protocols from prompts or Word/PDF uploads, suggests error-reduction and troubleshooting fixes, translates private protocols across 36 languages, and summarizes reviewer feedback — inside the standard platform for publishing versioned, citable methods. |

<details><summary>More tools for this task (1)</summary>

| Tool | Provider | Access | Description |
|---|---|---|---|
| [SciNote AI](https://www.scinote.net/product/ai-and-automations/) | SciNote LLC (Middleton, WI, USA; EU hub in Slovenia; owned by Gilson) | Freemium | Electronic lab notebook whose AI converts PDF-based SOPs and protocols into structured, reusable ELN templates and auto-updates task/project progress from user activity; includes inventory management and compliance tools. Core ELN is open source; free plan for individuals. |

</details>

## Instrument Data Interpretation

*The task: turn raw instrument output into identifications — what is this peak, this spectrum, this unknown.*

| Tool | Provider | Access | Description |
|---|---|---|---|
| [SIRIUS](https://github.com/sirius-ms/sirius) | Böcker group (FSU Jena) + Bright Giant GmbH | Free | Identifies small molecules from LC-MS/MS data: molecular formula annotation, CSI:FingerID structure ranking, CANOPUS compound-class prediction, MSNovelist de-novo structures. Desktop app (Win/Mac/Linux); web services free for academics via institutional email. |

<details><summary>More tools for this task (1)</summary>

| Tool | Provider | Access | Description |
|---|---|---|---|
| [MetFrag](https://msbi.ipb-halle.de/MetFrag/) | IPB Halle (Leibniz Institute of Plant Biochemistry) | Free | In-silico fragmentation for identifying metabolite MS/MS spectra: paste a peak list, screen candidates from PubChem, KEGG, HMDB, LipidMaps, ChEBI, COCONUT and more. Free web tool, no login. |

</details>

## Bioimage Analysis

*The task: segment, classify and count in your own microscopy and histology — cells, nuclei, whole slides.*

| Tool | Provider | Access | Description |
|---|---|---|---|
| [Cellpose](https://www.cellpose.org/) | Stringer & Pachitariu labs, HHMI (MouseLand) | Free | Generalist deep-learning instance segmentation of cells and nuclei in microscopy images, with human-in-the-loop training on your own channels; Cellpose-SAM model, GUI, free web demo, and Python API. |
| [ilastik](https://www.ilastik.org/) | Kreshuk lab, EMBL | Free | Interactive machine-learning toolkit for bioimage analysis: train pixel and object classifiers with brush strokes to segment, classify, track, and count cells in 2D/3D. No deep-learning expertise required. |
| [QuPath](https://qupath.github.io/) | Pete Bankhead group, University of Edinburgh | Free | Open-source desktop software for whole-slide image and digital pathology analysis: annotate gigapixel microscopy images, detect and classify cells, and script reproducible batch analyses. |

## Behavioral Video Analysis

*The task: track animals and quantify behavior from your own videos — markerless pose, identities, ethograms.*

| Tool | Provider | Access | Description |
|---|---|---|---|
| [DeepLabCut](https://deeplabcut.github.io/DeepLabCut/README.html) | Mathis Group & Mathis Lab, EPFL | Free | Markerless pose estimation for animal behavior: train deep-learning keypoint models on your own videos or apply pretrained SuperAnimal foundation models; single- and multi-animal, PyTorch backend. |
| [idtracker.ai](https://idtracker.ai/) | de Polavieja lab, Champalimaud Foundation | Free | Tracks up to 100 unmarked animals in laboratory videos while preserving individual identities, using deep-learning identification networks; free open-source GUI and Python tools. |

<details><summary>More tools for this task (1)</summary>

| Tool | Provider | Access | Description |
|---|---|---|---|
| [SLEAP](https://sleap.ai/) | Talmo Lab, Salk Institute | Free | Estimate animal poses and track individuals in video using a graphical labeling workflow and trainable neural networks. Supports single- and multi-animal analyses, with tools for training, inference, and reviewing predictions. |

</details>

## De-identification & Data Sharing

*The task: anonymize tables and transcripts so data can be shared or sent to a cloud model — with formal guarantees, GDPR in mind.*

| Tool | Provider | Access | Description |
|---|---|---|---|
| [Amnesia](https://amnesia.openaire.eu/) | OpenAIRE / ATHENA Research Center | Free | Anonymize tabular datasets through a graphical interface using formal privacy models such as k-anonymity. Local deployment and a REST API support data-sharing workflows; suitability depends on the dataset and disclosure risks. |
| [Textwash](https://www.textwash.eu/) | Bennett Kleinberg + jocapps GmbH (OSS original: Kleinberg, Tilburg/UCL) | Freemium | Removes personal data from interviews, documents, and logs using a small on-device AI model (16 configurable entity types, contextual not keyword-based), in English, German, Dutch, French, Spanish, Italian. Free GPL-3.0 Python CLI covers English and Dutch. |

<details><summary>More tools for this task (2)</summary>

| Tool | Provider | Access | Description |
|---|---|---|---|
| [Presidio](https://presidio.dataprivacystack.org/) | Data Privacy Stack (community-owned; originally Microsoft) | Free | Detects and anonymizes PII (names, credit cards, SSNs, and custom entities) in text and images via configurable NER/regex pipelines that run locally. MIT-licensed; originally built at Microsoft, now community-maintained under Data Privacy Stack. |
| [QualiAnon](https://github.com/pangaea-data-publisher/qualianon) | Qualiservice research data center, University of Bremen (with TU Munich and PANGAEA) | Free | Anonymizes or pseudonymizes qualitative text data such as interview transcripts, with user-controlled replacements and separation of identifiers, original data, and edited materials — the German FDZ (Qualiservice) archival workflow. |

</details>

## Writing & Translation

*The task: draft, polish and translate scholarly text, and get the manuscript into the journal's shape. No mature dedicated reformatting tool exists yet; a coding agent given the author-guidelines URL does the job under your supervision.*

| Tool | Provider | Access | Description |
|---|---|---|---|
| [DeepL](https://www.deepl.com/en/translator) | DeepL SE | Freemium | Translate text or whole documents while preserving document layout, and use glossaries to maintain terminology across research materials. Free and paid plans differ in document translation limits and available features. |
| [Grammarly](https://www.grammarly.com/) | Superhuman | Freemium | Correct grammar, spelling, clarity, and tone as you write emails, forms, proposals, and drafts across applications. Free and paid plans offer different features; institutional settings may restrict generative assistance. |
| [Paperpal](https://paperpal.com/) | Cactus Communications | Freemium | Draft academic manuscripts using saved sources, predictive writing, and insertable citations, then check language and submission readiness. Reference-library imports and journal-oriented preflight checks connect drafting with publication preparation; features vary by plan. |

<details><summary>More tools for this task (3)</summary>

| Tool | Provider | Access | Description |
|---|---|---|---|
| [Deepwriter AI](https://deepwriter.com/) \* | Deepwriter | Paid | Produce long-form drafts from research questions and source material using a multi-agent writing workflow. Official documentation remains online, but the product website’s certificate failed validation during this check. |
| [Jenni](https://jenni.ai/) | Jenni AI | Freemium | Draft incrementally with AI autocomplete grounded in uploaded sources or imported reference libraries, insert traceable citations, and export to Word or LaTeX. Free and paid plans support this integrated research-writing workflow. |
| [QuillBot](https://quillbot.com/) | Learneo | Freemium | Paraphrase, check grammar, summarize text, and generate citations in a writing workspace. Free access has limits, while Premium expands the available modes and usage. |

</details>

## Visual & Presentation Creation

*The task: turn text into diagrams, posters and slide decks.*

| Tool | Provider | Access | Description |
|---|---|---|---|
| [Gamma](https://gamma.app/) | Gamma Tech, Inc. | Freemium | Turn outlines or source content into presentations, documents, and websites, then revise their layout and visuals with AI assistance. Free and paid plans provide different creation and export limits. |
| [Napkin](https://www.napkin.ai/) | Napkin AI | Freemium | Turn text into editable diagrams, flowcharts, mind maps, infographics, and charts. Napkin Slides also creates presentations; a free plan provides weekly generation credits, with higher allowances on paid plans. |

<details><summary>More tools for this task (2)</summary>

| Tool | Provider | Access | Description |
|---|---|---|---|
| [Beautiful.ai](https://www.beautiful.ai/) | Beautiful Slides, Inc. | Paid | AI applying design principles in real-time with Smart Slide technology automatically adjusting layouts. Free access for students with verified .edu emails. Integrates with PowerPoint, Google Slides, Slack, and Dropbox. |
| [Gemini Notebook (Slide Decks)](https://notebook.google/) | Google | Freemium | Generate presentations from sources in Gemini Notebook, customize the deck, and revise individual slides. Export as PDF or PowerPoint; feature access and generation limits depend on the account. |

</details>

## Scientific Image Generation

*The task: generate scientific illustrations and publication figures.*

| Tool | Provider | Access | Description |
|---|---|---|---|
| [BioRender](https://www.biorender.com/) | BioRender | Freemium | Create scientific illustrations, graphs, and slides with BioRender’s icon and template libraries. Leo by BioRender adds AI-assisted figure creation with editable elements; free access and paid publication-oriented plans serve different needs. |

<details><summary>More tools for this task (2)</summary>

| Tool | Provider | Access | Description |
|---|---|---|---|
| [ChatGPT Images (gpt-image-2.5)](https://openai.com/index/introducing-chatgpt-images-2-5/) | OpenAI | Freemium | ChatGPT's native image model (gpt-image-2.5, released 2026-09-08): generates and edits images with accurate text rendering, reference-image preservation and multi-turn editing; usable for annotated scientific figures and infographics. Instant mode on all ChatGPT tiers including free. |
| [Nano Banana Pro (Gemini)](https://deepmind.google/models/gemini-image/pro/) | Google DeepMind | Paid | State-of-the-art image generation with legible text in multiple languages, up to 4K resolution, and real-time Google Search integration for accurate diagrams and educational visuals. SynthID watermarked. |

</details>

## LaTeX & Academic Language

*The task: AI inside the scholarly writing toolchain — LaTeX editing, published-language feedback.*

| Tool | Provider | Access | Description |
|---|---|---|---|
| [OpenAI Prism](https://prism.openai.com/) | OpenAI | Free | Write and collaborate on scientific documents in a browser-based LaTeX workspace with integrated AI. Supports document-level editing, equations, references, and shared projects; available free with a personal ChatGPT account. |
| [Overleaf AI Assist](https://www.overleaf.com/about/ai-features) | Overleaf (Digital Science) | Freemium | AI built into the standard collaborative LaTeX editor: explains and fixes LaTeX compile errors, generates tables and equations from images or prompts (TeXGPT), and gives Writefull-powered language feedback trained on published papers. Free daily allowances on all plans. |
| [Writefull](https://www.writefull.com/) | Digital Science (sister company of Overleaf) | Freemium | Language feedback for scientific text from models trained on millions of published journal articles, delivered inside Overleaf (edits in LaTeX source), Word, or a standalone Revise uploader. Adds paraphrasing, abstract/title generation, and TeXGPT table/equation code generation. |

<details><summary>More tools for this task (2)</summary>

| Tool | Provider | Access | Description |
|---|---|---|---|
| [Papers AI](https://papers.ai/) | Digital Science (built by the Overleaf team) | Freemium | Offline-first AI research workspace: write in LaTeX, Typst, Markdown or Word alongside Jupyter notebooks and CSVs, with a context-aware assistant that reads drafts, data and references together. Compiles locally in-browser; can run entirely on local models via Ollama/LM Studio/vLLM. |
| [Trinka](https://www.trinka.ai/features/latex-grammar-checker) | Trinka AI (Enago / Crimson Interactive) | Freemium | Upload a .tex file and get it proofread with LaTeX commands untouched: returns a corrected LaTeX file plus a Word file with tracked changes, a language-quality score, and revision breakdown. Style-guide aware (APA, AMA, IEEE). |

</details>

## AI Manuscript Review & Disclosure

*The task: stress-test a manuscript before submission — reviews, integrity checks, AI disclosure.*

| Tool | Provider | Access | Description |
|---|---|---|---|
| [Enago AI Disclosure](https://www.enago.com/ai-disclosure-statement-generator/) | Enago | Free | Generate an AI Disclosure Statement for your manuscript that you can use while submitting your manuscript to a publisher. |
| [Proofig + PubShield](https://www.proofig.com/pubshield/) | Proofig AI / Turnitin | Institutional | Screen manuscripts through PubShield’s institutional quality-assurance workflow, combining Proofig image-integrity checks with text-similarity screening and additional manuscript checks. Helps authors and institutions identify issues before journal submission. |
| [Prophy](https://www.prophy.ai/) \* | Prophy | — | Find potential manuscript or grant reviewers, identify conflicts, and assemble expert panels from scholarly profiles. Prophy serves publishers, funders, and research offices; public access remains demo-led with no listed price. |
| [RegCheck](https://regcheck.app/) | Psychology of Digitalisation group, University of Bern (SNSF-funded) | Free | Upload a preregistration (or ClinicalTrials.gov link) plus the final paper; an LLM compares them dimension-by-dimension and flags deviations, quoting verbatim text from both documents so every judgement is checkable. Free, with API. |
| [SciScore](https://sciscore.com/) | SciCrunch, Inc. | Paid | Check a manuscript’s methods for reported blinding, randomization, power analysis, and research-resource identifiers (RRIDs), then review missing items against reporting guidelines. Paid author reports are available through Aseda Sciences; the score assesses reporting completeness. |
| [Stanford Agentic Reviewer](https://paperreview.ai/) | Stanford ML Group | Free | Submit a research paper to Stanford Agentic Reviewer for AI-generated review feedback. The interface supports venue context and returns suggestions for revision; researchers should evaluate the feedback themselves. |

<details><summary>More tools for this task (4)</summary>

| Tool | Provider | Access | Description |
|---|---|---|---|
| [Manusights](https://manusights.com/) | Manusights | Freemium | Check a manuscript’s submission readiness, methods, figures, and citation support, then prioritize revisions. A free Readiness Scan and paid Full Review are available; the service publishes manuscript-handling controls in its Trust Center. |
| [QED Science](https://www.qedscience.com/) | QED Science | Freemium | Examine manuscript or grant claims, identify logical and methodological gaps, and assess novelty against related work. Academic researchers can request a free account; enterprise access serves commercial research teams. |
| [Review-it](https://review-it.ai/) | Review-it AI | Paid | Review academic documents for strengths, weaknesses, structural improvements, and suitable journals. The service offers AI-assisted feedback for manuscript revision; consult its current plans before uploading a document. |
| [Reviewer3](https://reviewer3.com/) | Reviewer3 | Paid | Check manuscripts for reference problems, unsupported claims, methodological issues, and other submission risks. Separate workflows support authors, reviewers, and editorial teams; findings are organized for human review. |

</details>

## Integrity Screening & Forensics

*The task: screen the literature — and your own reference list — for fabrication, manipulation and AI-generated text.*

| Tool | Provider | Access | Description |
|---|---|---|---|
| [Argos](https://www.scitility.com/) | Scitility PBC | Freemium | Check references for retractions and other integrity concerns, monitor citation-related risks, and investigate flagged publications. Scitility provides interfaces and API access for researchers and organizations. |
| [Pangram](https://www.pangram.com/) | Pangram Labs (Brooklyn, NY, founded 2023) | Freemium | Classifies text as human- or AI-written with per-document and per-sentence results via web dashboard and API; 20 free checks daily. Reports a 1-in-10,000 false-positive rate, with an independent University of Chicago evaluation. |
| [Problematic Paper Screener](https://www.irit.fr/~Guillaume.Cabanac/problematic-paper-screener) | Guillaume Cabanac, IRIT / Universite de Toulouse (with Labbe & Magazinov) | Free | Browsable dashboard screening the literature with detectors for tortured phrases, SCIgen/Mathgen text, citejacking, Seek & Blastn nucleotide errors, problematic cell lines, and retracted or concerning references. Check a DOI before citing it, or trawl your field for flagged papers. |
| [statcheck](https://statcheck.io/) | Michele Nuijten & Sacha Epskamp (Tilburg University) | Free | Upload a PDF, DOCX, or HTML manuscript; it recomputes every APA-style statistical result (t, F, r, chi-square, Z, Q) and flags p-values inconsistent with the reported test statistic and degrees of freedom. |

<details><summary>More tools for this task (1)</summary>

| Tool | Provider | Access | Description |
|---|---|---|---|
| [Imagetwin](https://imagetwin.ai/pricing) | ImageTwin AI GmbH | Paid | Scans figures (western blots, microscopy, photos) for duplications, manipulations, and AI-generated images; matches against a 150M+ published-figure database to catch cross-paper reuse. Pay-per-scan from EUR 29 makes lab-level pre-submission screening feasible. |

</details>

## Journal Selection & Publishing

*The task: pick the right venue — open-access options, fit, and legitimacy.*

| Tool | Provider | Access | Description |
|---|---|---|---|
| [B!SON](https://service.tib.eu/bison/) | TIB Hannover & SLUB Dresden | Free | Paste a manuscript's title, abstract, and references; machine-learning similarity against DOAJ article and citation data ranks quality-assured open-access journals publishing similar work, with transparent per-journal reasoning and an open API. |

## Conference Prep — Posters & Talk Practice

*The task: get from accepted paper to poster, slides rehearsed, and delivery polished.*

| Tool | Provider | Access | Description |
|---|---|---|---|
| [Paper2Poster](https://github.com/Paper2Poster/Paper2Poster) | Paper2Poster (open-source, NeurIPS 2025) | Free | Multi-agent pipeline that converts a paper PDF into an editable PowerPoint conference poster: parses the paper into assets, plans a panel layout, renders and self-corrects with VLM feedback. Runs locally or via API models; Docker supported. |
| [Paper2Video](https://github.com/showlab/Paper2Video) | Show Lab, NUS (open-source) | Free | Convert LaTeX paper sources into a conference-talk video with slides, narration, subtitles, and synchronized cursor movements. Open-source local software; setup and model compute are required, with a 48GB GPU recommended and an optional talking-head presenter. |
| [Yoodli](https://yoodli.ai/use-cases/public-speaking) | Yoodli | Freemium | Records a practice talk via webcam or uploaded video and scores filler words, pacing, eye contact, clarity, and structure, benchmarking each rehearsal against the last; AI follow-up questions simulate audience Q&A after a conference talk. |

<details><summary>More tools for this task (3)</summary>

| Tool | Provider | Access | Description |
|---|---|---|---|
| [ChatSlide](https://www.chatslide.ai/guides/research-poster-presentation-ai-guide) | ChatSlide AI | Freemium | Upload a paper or paste an abstract; generates a single-page academic poster (A0 or 36x48 in) with sectioned layout, charts rendered from your data, and PubMed/Scholar citation lookup. Exports print-locked PDF or editable pptx. |
| [PowerPoint Speaker Coach](https://support.microsoft.com/en-us/powerpoint/rehearse-your-slide-show-with-speaker-coach) | Microsoft | Free | Rehearse a talk against your actual slide deck inside PowerPoint (web, Windows, Mac, mobile); flags pacing, pitch, filler words, monotone delivery, and reading text off slides, then produces a rehearsal report with statistics. |
| [VirtualSpeech](https://virtualspeech.com/platform/public-speaking) | VirtualSpeech Ltd | Paid | Practice presentations in simulated settings using your slides, then receive feedback on content and delivery and answer AI-generated audience questions. Browser and VR options support individual or organizational training. |

</details>

## Research Communication & Accessibility

*The task: consume research by ear and communicate it beyond the paper — audio, podcast, plain language.*

| Tool | Provider | Access | Description |
|---|---|---|---|
| [Audemic Scholar](https://audemic.io/) | Audemic | Paid | Reads uploaded or reference-manager-imported papers aloud with synchronized text highlighting; reorder sections, capture highlights and notes. Dyslexia-friendly fonts, background color options, and adjustable pacing support researchers with dyslexia, ADHD, or visual impairment. |
| [Cassyni](https://cassyni.com/) | Cassyni (founders of Mendeley, Publons, Kopernio) | Freemium | Runs and records research seminars, then AI-enhances them: transcripts, slide extraction, semantic chapters, resolved references to cited papers, and a DOI per talk — turning seminars into citable, searchable scholarly objects researchers can browse. |
| [Kudos](https://www.growkudos.com/) | Kudos Innovations Ltd | Freemium | Researcher creates a free showcase page explaining a publication in plain language; Kudos's AI service drafts the summary and a paid campaign promotes it via email, social media, and themed showcases, with tracked views, Altmetric scores, and citations. |
| [Listening](https://www.listening.com/) | Listening (listening.com) | Paid | Converts paper PDFs into natural-sounding audio that automatically skips citations, references, and footnotes; listen by section (abstract, results) at up to 4x speed. Mobile apps and Chrome extension for consuming a reading backlog while commuting. |
| [Wondercraft](https://www.wondercraft.ai/tools/research-paper-to-podcast-generator) | Wondercraft Limited | Freemium | Turns an uploaded paper or URL into a conversational podcast episode; edit the script word-by-word, choose or clone voices, add team review flows, then export WAV or publish toward Spotify and Apple Podcasts. Free tier includes starter credits. |

<details><summary>More tools for this task (1)</summary>

| Tool | Provider | Access | Description |
|---|---|---|---|
| [ElevenReader](https://elevenreader.io/) | ElevenLabs | Freemium | Free reader app from ElevenLabs that voices PDFs, preprints, and web articles with realistic neural voices, reading abbreviations naturally ('e.g.' as 'for example'). 10 free hours monthly; Ultra ($99/yr) adds smart imports that strip headers and footers. |

</details>

## Patents & Tech Transfer

*The task: prior-art checks, patent landscapes and invention disclosures. Caution: unfiled inventions are confidential — check your TTO's policy before pasting disclosure text into third-party AI.*

| Tool | Provider | Access | Description |
|---|---|---|---|
| [Google Patents](https://patents.google.com/) | Google | Free | Free worldwide patent full-text search with ML features: machine-classified CPC code suggestions, 'Similar' documents ranked by a full-text model, one-click 'Find prior art' scoped to before the priority date, SMILES chemical-structure search, and Google Scholar non-patent literature integration. |
| [PQAI](https://projectpq.ai/) | Project PQAI (nonprofit initiative, AT&T / Georgia IP Alliance) | Free | Paste a plain-language invention description; deep-learning models trained on examiner citation data return ranked prior art from USPTO, EPO and open-access journals, plus concept extraction and CPC/IPC code suggestions. Open-source (MIT); free web search, paid API tiers. |
| [The Lens](https://about.lens.org/) | The Lens Limited (Australian non-profit, wholly owned subsidiary of SPIE; formerly Cambia) | Freemium | Links 155M+ patent records with 270M+ scholarly works: landscape dashboards, patent-to-paper citation mapping, PatSeq search for DNA/protein sequences inside patents, freedom-to-operate style filtering. Free personal accounts for academic researchers (exports up to 50,000 records); institutional toolkit for universities. |

<details><summary>More tools for this task (3)</summary>

| Tool | Provider | Access | Description |
|---|---|---|---|
| [CAS SciFinder Prior Art](https://www.cas.org/resources/cas-insights/prior-art-search-and-analysis-scientific-ip-strategies) | CAS (American Chemical Society) | Institutional | Inside CAS SciFinder: paste 200+ characters of invention text (claims or abstract) and AI algorithm streams return similar patents and non-patent literature published before your priority date, drawing on CAS's human-curated chemistry collection including Markush structures. |
| [InventGenie](https://www.inventgenie.com/for-researchers) | InventGenie (Calgary, Canada) | Paid | Turns research papers, notes and technical input into structured invention-disclosure building blocks: draft patent claims, specification text and figure suggestions, formatted for tech-transfer review, with multi-inventor collaboration. Pay-per-draft or monthly seat pricing (free trial); attorney review still required before filing. |
| [PatSnap](https://www.patsnap.com/) | PatSnap | Paid | AI innovation-intelligence platform: patent landscape maps, novelty and FTO search agents (Eureka), drafting agents, litigation and market data, biosequence and chemical structure search. Tech transfer offices use it to judge whether an invention's space is commercially active before funding proof-of-concept. |

</details>

## Impact & Policy Tracking

*The task: show where your work landed beyond academia — policy documents, impact cases.*

| Tool | Provider | Access | Description |
|---|---|---|---|
| [Sage Policy Profiles](https://policyprofiles.sagepub.com/) | Sage (powered by Overton) | Free | Track where research is mentioned or cited in policy using Overton data, visualize and export results, and discover policy-engagement opportunities. Free for individual researchers and academics. |

## Watchlist

Noticed but not properly vetted yet — waitlisted, too young, or missing a privacy policy.

- [AlphaEvolve + ERA](https://labs.google/science) — [sweep 2026-08-18] Fetched labs.google/science and research.google ERA blog. 'Computational Discovery' built with AlphaEvolve+ERA; ERA Nature paper May 19 2026 and CDC-forecasting claim confirmed. Access via 'Express interest' / gradual trusted-tester rollout.
[sweep 2026-09-11] Still 'Express interest' only (gate 2, usable this week, fails); Nature paper and CDC-forecasting claim reconfirmed. Keep candidate until self-serve access opens.

[sweep 2026-10-15] The live Google Labs page still offers Express interest. Gate 2 fails; retained candidate. Removed the historical disease-forecasting result from the short product description. Sources: https://labs.google/science
- [Gemini Co-Scientist](https://labs.google/science) — [sweep 2026-08-18] description flagged: Fetched labs.google/science and blog.google I/O 2026 post: Co-Scientist Nature paper confirmed, but Stanford liver-fibrosis/Vorinostat result was published in Advanced Science, not Nature. Access via 'Express interest' waitlist. Google-branded (blog.google/labs.google), not DeepMind.
[sweep 2026-09-11] Gate 2 fails: still 'Express interest' waitlist on labs.google/science (gradual rollout, no open access as of Sept 2026) — keep candidate. Description fix: Stanford vorinostat result is Advanced Science 2025, not Nature; Co-Scientist paper itself is in Nature (blog.google).

[sweep 2026-10-15] The live Google Labs page still offers Express interest. Gate 2 fails; retained candidate. Simplified the description to current advertised capabilities. Sources: https://labs.google/science
- [Literature Insights (Gemini for Science)](https://labs.google/science) — [sweep 2026-08-18] Fetched labs.google/science: Literature Insights listed, built with Gemini Notebook; tables, reports, slide decks, infographics confirmed. Access is 'Express interest' only — no open availability. Audio/video overviews not confirmed.
[sweep 2026-09-11] Gate 2 fails: still 'Express interest' waitlist, gradual rollout — keep candidate. Audio/video overviews now confirmed on blog.google I/O post (previous caveat resolved). Description accurate.

[sweep 2026-10-15] Live Google Labs page confirms literature search, extraction tables, and generated artifacts, but access is still Express interest. Gate 2 fails; retained candidate. Sources: https://labs.google/science
- [Nature Research Assistant](https://natureresearchassistant.com/) — [sweep 2026-08-18] Fetched site: Springer Nature confirmed, still beta; new users must join waiting list, no pricing disclosed. Summaries, paper chat, figure descriptions with audio all confirmed on page.
[sweep 2026-09-11] Still beta + waiting list, no pricing: fails gate 2 (usable this week). Keep candidate; re-check next sweep. New 'Manuscript Adviser' feature and publisher-agnostic scope now on page.

[sweep 2026-10-15] The product explicitly requires new users to join the waiting list. Gate 2 still fails; retained candidate. Sources: https://natureresearchassistant.com/
- [PowerGPT](https://power-gpt.net/) — [grok-gap-hunt 2026-08-18, independently verified] CONFIRMED: no privacy policy, ToS, or data-handling statement on homepage or /others (footer = contacts only) -> candidate. '0 daily users' still shown. arXiv:2509.12471 real, matches (94.1% vs 55.4%).
[sweep 2026-09-11] candidate re-vetted: gates 1,2,3,5 pass; gate 4 (recommendable - privacy policy/transparent terms) still fails, '0 daily users' counter unchanged. Keep candidate; promote only if a privacy/data statement appears.

[sweep 2026-10-15] Homepage and institution-entry guidance remain live. No privacy policy or data-handling terms were found among the inspected page links. Retained candidate because gate 4 remains unresolved; absence is limited to inspected surfaces. Sources: https://power-gpt.net/
- [Protocol Builder](https://protocolbuilderpro.com/) — [discovery 2026-08-18] Unique use case: structured IRB protocol and consent-form authoring with compliance templates Adoption: Sold to IRBs and GME programs; BRANY is an established IRB/compliance services organization; site current (screenshots dated March 2026) Demo-only, no public pricing — hence candidate. US clinical-research centric; EU ethics-committee fit unverified.
[sweep 2026-09-11] Still demo-only with no public pricing or self-serve trial — fails gate 2 (usable this week); gates 1, 3, 4, 5 pass. Keep candidate until a trial or institutional purchase path is verifiable.

[sweep 2026-10-15] Current BRANY product page still routes new users to Schedule a Demo and does not publish self-serve pricing or trial access. Retained candidate under the existing usable-this-week gate. Sources: https://protocolbuilderpro.com/
- [Faraday](https://www.ascentbio.ai/) — [sweep 2026-08-18] ascent.bio rendered empty; live site is ascentbio.ai (fetched): Faraday AI scientist, 40+ institutions, signup via accounts.platform.ascentbio.ai. platform.ascentbio.ai/faraday showed 'down for maintenance'. No pricing found; public beta per blog.
[sweep 2026-09-11] Access is request/invite-gated per Ascent Bio docs (alpha program) and blog (request an access link); no public pricing. Per gate 2 waitlist tools are candidate, not active. Revert to active if self-serve signup is confirmed.

[sweep 2026-10-15] The homepage still ends with Request Access; the account endpoint returned a bot challenge. No self-serve trial or published pricing was verified. Retained candidate, with no claim of a shutdown. Sources: https://www.ascentbio.ai/
- [Genemod](https://genemod.net/) — [discovery 2026-08-18] Unique use case: Conversational agent acting over lab inventory and sample records (the inventory/ordering AI slot), or null if judged too close to generic ELN AI Adoption: Capterra and FitGap listings; own academic-labs pricing packages Weakest vetting: genemod.net pages repeatedly failed direct fetch (oversized pages); AI-agent and pricing claims come from genemod.net snippets via search. ~$199/month, 14-day trial, annual contract; no confirmed permanent free tier.
[sweep 2026-09-11] Still cannot fetch genemod.net directly. Alive, but Capterra now shows contact-for-pricing with no trial/free version; fails gate 4 (transparent pricing) and gate 2 is unverified. Keep candidate.

[sweep 2026-10-15] Product, pricing, company, and privacy pages now fetch successfully, resolving the old fetch uncertainty. Pricing is a tailored quote after a demo; the linked public signup URL returns 404. Retained candidate because immediate access and transparent prices remain unresolved. Sources: https://genemod.net/; https://genemod.net/pricing; https://genemod.net/solutions/academia; https://app.genemod.net/signup; https://genemod.net/privacy-policy
- [Paper Pivot](https://paperpivot.com/) — [capture 2026-09-11] Fetched paperpivot.com: landing page + terms of service only; "currently in development", waitlist signup, no company name, /pricing and /privacy 404 (privacy-policy link exists on the landing page, not checked). Closest thing to a dedicated journal-reformatting tool after FormatMyPaper turned out to be satire. Fails gate 2 (usable this week) and gate 4 (no named organisation) today; re-vet at next sweep. CheckMyManuscript ($5/manuscript, 95 compliance checks, anonymous operator) rejected as a checker, not a reformatter.

[sweep 2026-10-15] Fetched the previously unchecked privacy policy: it covers waitlist email collection. Terms explicitly say no product is sold. Gate 2 fails; organization identity remains unclear, so candidate status is retained. Sources: https://paperpivot.com/; https://paperpivot.com/privacy-policy; https://paperpivot.com/terms-of-service
- [RefereeBio](https://refereebio.com/) — [grok-gap-hunt 2026-08-18, independently verified] All section-10 claims confirmed on homepage (free Starter month: 3 reviews/3 revision checks/3 edits, no card; AI-provider clause). No legal entity or team named; keep candidate.
[sweep 2026-09-11] Still no legal entity, founders, address or jurisdiction on /about, /legal or /security; self-described 'early access'. Fails gate 4 (recommendable to students). Keep candidate.

[sweep 2026-10-15] Current pages add non-expiring introductory credits and specify Connecticut governing law, correcting the previous no-jurisdiction note. A clearly named operating legal entity was still not found in the inspected About/Legal content; retained candidate under gate 4. Sources: https://refereebio.com/; https://refereebio.com/about; https://refereebio.com/legal
- [AI Reference Checker (RefCheckAI)](https://sydney-informatics-hub.github.io/RefCheckAI/) — [discovery 2026-08-18] Unique use case: Semantic citation verification — whether the cited paper supports the claim, not merely whether the reference exists (scite shows citation context but does not classify your own manuscript's claims) Adoption: University-built (Sydney Informatics Hub, NCI/NVIDIA-supported CodeFest); model weights and training data published for download Early access — web app via registration/email only. Classification accuracy not independently benchmarked. CC BY-NC 4.0.
[sweep 2026-09-11] Alive, unchanged. Still early-access via registration/email only, so fails gate 2 (usable this week). Keep candidate; page brands it 'AI Reference Checker'.

[sweep 2026-10-15] The official page brands the tool AI Reference Checker. Early-adopter access still requires contact/registration; downloadable research assets are available, but general hosted access is not verified. Retained candidate. Sources: https://sydney-informatics-hub.github.io/RefCheckAI/
- [PaperTok](https://www.papertok.com) — [discovery 2026-08-18] Unique use case: Paper to short-form social video for public science communication Adoption: CHI 2026 paper (Barcelona, April 2026); TechXplore coverage June 2026 Academic prototype, live site with generate button; requires user's paid Google Gemini subscription. Privacy policy and durability unverified.
[sweep 2026-09-11] Candidate vetted: passes gates 1, 3, 5; gate 2 marginal (needs user's paid Gemini subscription); FAILS gate 4 — no privacy policy on site, academic prototype with no durability commitment. Keep candidate; re-check if a privacy policy appears.

[sweep 2026-10-15] The previously recorded paid-Gemini requirement was not confirmed on the inspected page; its Add credits step means author attribution. No price was established, so changed paid to unknown. Generated material and feedback may support research/model improvement; retained candidate pending clear access and manuscript-data terms. Sources: https://www.papertok.com

## Retired

Kept for the record.

- **ChatGPT Atlas** (deprecated) — Discontinued by OpenAI around 2026-08-09; the standalone Atlas browser was folded into the ChatGPT desktop app. Kept for the historical record.

[sweep 2026-10-15] Official OpenAI support confirms Atlas shut down on 9 August 2026. The old URL now serves the generic ChatGPT interface, which is not evidence of a browser relaunch. Sources: https://chatgpt.com/atlas; https://help.openai.com/en/articles/20001371
- **You.com** (deprecated) — [sweep 2026-08-18] description flagged: Fetched you.com twice: now an enterprise/developer API platform (Search, Contents, Research, Finance APIs); no ARI or consumer answer engine mentioned. 2026 reporting confirms pivot; consumer plans gone. Usage-billed with one-time trial credits.
[sweep 2026-09-11] Resolved needs-review: the consumer AI search/ARI product the entry described no longer exists; you.com is a usage-billed retrieval/research API for developers (pivot confirmed 2026). Deprecated with epitaph — not usable by students as an AI search engine. If a developer-API category ever exists, it could be re-listed there.

[sweep 2026-10-15] The current product page still presents APIs rather than the former consumer product. Retained deprecated status and replaced the obsolete consumer description. Sources: https://you.com/
- **Transcription Pearl** (deprecated) — [discovery 2026-08-18] Unique use case: Peer-review-backed LLM transcription workflow: the accompanying study found LLMs beat specialized HTR (Transkribus) on 18th/19th-c. English documents — the easter egg of this area Adoption: Companion paper published in Historical Methods (2025, DOI 10.1080/01615440.2025.2500309) and arXiv:2411.03340; GitHub repo public Beta; last commit Nov 2024 — maintenance uncertain. Requires own API keys and Python. CC BY-NC 4.0. Candidate until freshness confirmed.
[sweep 2026-09-11] Candidate rejected on gate 5 (alive/maintained): no commits since 2024-11-11 (22 months), still 1.0 beta, and superseded by the same authors' Archive Studio (May 2025). Suggest capturing Archive Studio as the candidate for this use case instead; its own maintenance cadence not yet verified.

[sweep 2026-10-15] Corrected a prior maintenance note: GitHub’s latest repository commit is 29 April 2025, not 11 November 2024. No newer maintenance was found; retained the existing retired status. Sources: https://github.com/mhumphries2323/Transcription_Pearl; https://github.com/mhumphries2323/Transcription_Pearl/commit/5fc5157a2070742cb6b4db64cf05a28d505e5b9b
- **FormatMyPaper** (deprecated) — Core as sole representative of the journal-reformatting use case (Michaela, 2026-08-18): no other tool in the catalog covers submission-requirements formatting.
[sweep 2026-09-11] Epitaph: FormatMyPaper is a satire site by Ubadah Sabbagh (Oct 2025), not a product — no formatting happens, testimonials are fabricated. Fails gate 4 (real organization) and gate 3 (does nothing). Was core as sole journal-reformatting representative; that use case now has no representative — Michaela to decide on a replacement (e.g. SciSpace/Typeset journal templates, Overleaf journal templates) or drop the task.

[sweep 2026-10-15] The live formatting button still links to the preprint advocacy page. Retained deprecated status and shortened the existing 42-word description. Sources: https://formatmypaper.com/; https://formatmypaper.com/prestige/

---

\* = flagged for re-verification.

Corrections and suggestions are welcome as issues or PRs. The maintenance rules
live in [AGENTS.md](AGENTS.md); every entry needs a working URL and has to pass
`scripts/validate.py`. This README is generated from [`tools/`](tools/) by
`scripts/build.py` — edit the YAML, not this file.

Data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Code: MIT.
