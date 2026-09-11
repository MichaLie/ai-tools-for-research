# AI Tools for Scientific Research

A curated list of AI tools that are actually useful in research work. I keep it
for my courses and workshops on AI in science, which makes it opinionated on
purpose: for each research task you get a handful of tools people really use,
not everything that exists.

Right now: 160 tools across 35 task areas. Last checked against the live web on 11 September 2026.

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
- **Share & Impact** · [Conference Prep — Posters & Talk Practice](#conference-prep-—-posters-talk-practice) (5) · [Research Communication & Accessibility](#research-communication-accessibility) (6) · [Patents & Tech Transfer](#patents-tech-transfer) (6) · [Impact & Policy Tracking](#impact-policy-tracking) (1)

## General-Purpose AI Assistants

*The task: an everyday thinking partner — drafting, summarizing, coding help, quick analysis at any stage of research.*

| Tool | Provider | Access | Description |
|---|---|---|---|
| [ChatGPT](https://chatgpt.com/) | OpenAI | Freemium | Conversational AI with Deep Research for multi-step source synthesis, Python-based data analysis, and reasoning models. Free tier; paid Go, Plus and Pro plans add image generation, file analysis and higher usage limits. |
| [Claude](https://claude.ai/) | Anthropic | Freemium | Advanced AI assistant with 200K token context window, Code Interpreter, and Claude for Life Sciences integrations (Benchling, BioRender, PubMed, 10x Genomics). Excels at long-document analysis and nuanced scientific writing. |
| [Gemini](https://gemini.google.com/) | Google | Freemium | Multimodal AI with 1M token context, Deep Research mode analyzing 100+ sources, and integration with Google Workspace. Supports PDFs, images, audio, and video analysis for comprehensive research workflows. |
| [Microsoft Copilot](https://copilot.microsoft.com/) | Microsoft | Freemium | Free consumer AI chat at copilot.microsoft.com. The Microsoft 365 Copilot add-on ($18/user/month academic offering for faculty, staff and students) adds the Researcher agent for grant proposals and policy analysis and the Analyst agent with Python execution for data queries. |

<details><summary>More tools for this task (4)</summary>

| Tool | Provider | Access | Description |
|---|---|---|---|
| [Google AI Studio](https://aistudio.google.com/) | Google | Free | Free browser-based platform for experimenting with Gemini models. Provides researchers direct API access to test prompts, build prototypes, and embed Deep Research capabilities into applications. |
| [Grok](https://grok.com/) | xAI | Freemium | xAI's assistant with real-time X/Twitter and web search plus DeepSearch multi-step research mode. Free tier on grok.com and inside X (lighter model, limited usage); SuperGrok subscriptions unlock the newest models (Grok 4.6 as of Aug 2026). |
| [LM Council](https://lmcouncil.ai/) | — | Freemium | Multi-model consensus tool that queries multiple AI models simultaneously (GPT-5, Claude, Gemini, Grok), with anonymous peer review and ranking. Reduces individual model biases through collective evaluation. |
| [Vibe (Mistral, formerly Le Chat)](https://chat.mistral.ai/) | Mistral AI | Freemium | Mistral's assistant, renamed from Le Chat to Vibe in May 2026: Chat (turn-based), Work (multi-step agent across Google Workspace, Outlook, SharePoint, Slack, GitHub) and Code (CLI, VS Code, web) modes. Free tier; Pro EUR 17.99/month, Team EUR 29.99/user/month; European alternative to US assistants. |

</details>

## Office Suite AI Integrations

*The task: AI inside the documents, spreadsheets and slides you already work in.*

| Tool | Provider | Access | Description |
|---|---|---|---|
| [Claude for Excel / Word / PowerPoint](https://claude.com/claude-for-microsoft-365) | Anthropic | Paid | Native sidebar add-ins for Excel, Word and PowerPoint (GA May 7, 2026; Outlook in public beta). Carries full conversation context across apps, reads templates/slide masters, generates native charts and tracked changes in Word. Install via Microsoft AppSource; included with paid Claude plans. |
| [Microsoft 365 Copilot — Agent Mode](https://www.microsoft.com/microsoft-365/copilot) | Microsoft | Paid | Agent Mode is now GA in Word, Excel and PowerPoint (April 2026): Copilot takes multi-step, app-native actions on documents, spreadsheets and decks. Users can choose Claude or ChatGPT as the underlying model. Included with Microsoft 365 Copilot, Premium, Personal and Family plans. |

## Browser Automation Agents

*The task: let AI operate the browser — forms, portals, repetitive web work.*

| Tool | Provider | Access | Description |
|---|---|---|---|
| [Claude in Chrome](https://claude.com/chrome) | Anthropic | Paid | Chrome extension in which Claude reads pages, clicks, types and fills forms with approval, works across tabs and runs background tasks; integrates with Claude Code (build in terminal, verify in browser). Generally available on all paid plans (Pro/Max/Team/Enterprise). |
| [Comet](https://www.perplexity.ai/comet) | Perplexity AI | Freemium | AI-powered Chromium browser with Background Assistants completing multiple research tasks asynchronously. Highlights any text for instant explanations; Email Assistant handles scheduling and drafts (Max subscribers). |

## AI-Powered Search Engines

*The task: ask the web a question and get a sourced answer instead of a list of links.*

| Tool | Provider | Access | Description |
|---|---|---|---|
| [Perplexity](https://www.perplexity.ai/) | Perplexity AI | Freemium | Answer engine with Deep Research achieving 93.9% factuality accuracy. Academic focus mode prioritizes peer-reviewed sources. Generates reports with inline citations in under 3 minutes. |

## Deep Research Agents

*The task: delegate a multi-hour literature synthesis and get back a cited report.*

| Tool | Provider | Access | Description |
|---|---|---|---|
| [ChatGPT Deep Research](https://openai.com/index/introducing-deep-research/) | OpenAI | Freemium | Built-in ChatGPT feature that conducts multi-step internet research, synthesizing hundreds of sources into comprehensive reports. Reduces hours of manual research to minutes with full source attribution. |
| [Claude Research](https://claude.com/blog/research) | Anthropic | Paid | Agentic research mode in Claude: runs many searches across the web and connected tools, then returns a cited report. Available on all paid plans (Pro, Max, Team, Enterprise) on web, desktop, and mobile. |
| [Gemini Deep Research](https://gemini.google/overview/deep-research/) | Google | Freemium | Google's agentic research mode that browses up to hundreds of websites and synthesizes a report within a 1M-token context; accepts uploaded files and Workspace data (Gmail, Drive, Chat). Included in the free Gemini tier with lower usage limits than Pro. |
| [STORM](https://storm.genie.stanford.edu/) | Stanford OVAL Lab | Free | LLM system that researches a topic and writes a Wikipedia-style, fully cited article by simulating multi-perspective expert conversations. Co-STORM mode lets you join the discussion for human-AI collaborative knowledge curation. Free web demo; MIT-licensed code. |

<details><summary>More tools for this task (1)</summary>

| Tool | Provider | Access | Description |
|---|---|---|---|
| [Edison Literature (formerly Falcon)](https://platform.edisonscientific.com/) | Edison Scientific | Freemium | Deep literature-research agent (PaperQA3) on the Edison Scientific platform: searches and reads full text, figures, and tables of 150M+ papers and patents and returns cited syntheses. Successor to FutureHouse's Falcon; academics get about 20 free calls per day. |

</details>

## Literature Discovery & Analysis

*The task: find, screen and synthesize papers beyond what you can read yourself.*

| Tool | Provider | Access | Description |
|---|---|---|---|
| [Consensus](https://consensus.app/) | Consensus | Freemium | AI academic search across 220M+ peer-reviewed papers with Consensus Meter visualizing study agreement/disagreement. Research Agent (formerly Scholar Agent, built on GPT-5) answers multi-step questions with citation-backed, paper-grounded output. |
| [Elicit](https://elicit.com/) | Elicit | Freemium | Automates systematic literature reviews across 125M+ papers: semantic search, AI screening and data extraction (users report up to 80% time savings; 99.4% extraction accuracy) with PRISMA 2020 support. Free tier; Pro $49/month, Scale $169/month. |
| [SciSpace (Typeset)](https://scispace.com/) | SciSpace | Freemium | All-in-one research platform: semantic literature search over 280M+ papers, Chat with PDF, AI comparison columns and Deep Review for systematic-review synthesis. Includes journal formatting templates (Typeset) and plagiarism/AI checks. Free tier; Premium from $12/month. |
| [Scite](https://scite.ai/) | Research Solutions | Paid | Smart Citations platform showing whether later papers support, contrast, or merely mention cited work. 1.6B+ citations from 317M+ full-text articles, classified by deep learning to evaluate how a claim, paper, or author has been received. |
| [Semantic Scholar](https://www.semanticscholar.org/) | Allen Institute for AI (Ai2) | Free | Free AI-powered discovery tool with 237M+ papers. Features TLDR summaries, Semantic Reader for augmented PDF reading, and Highly Influential Citations for identifying foundational works. Open API available. |

<details><summary>More tools for this task (3)</summary>

| Tool | Provider | Access | Description |
|---|---|---|---|
| [AlphaXiv](https://www.alphaxiv.org/) | alphaXiv | Free | Comment and chat layer over arXiv preprints: line-by-line discussion threads, AI chat grounded in the paper, one-click blog-style overviews, Chrome extension and MCP server. Free; $7M seed (Nov 2025) with Eric Schmidt and Sebastian Thrun among angels. |
| [AnswerThis](https://answerthis.io/) | AnswerThis | Freemium | Generates literature reviews with line-by-line citations over 300M+ papers, trials and PDFs; includes research-gap identification, citation mapping, systematic-review tools and an AI writer with 2,000+ citation styles. Free starter tier. |
| [GXL](https://gxl.ai/) | GXL (Generative Expert Labs) | — | Deep biomedical literature index covering 8M+ papers across bioRxiv, medRxiv and PubMed Central, including figures, tables and supplemental data. Its Paperclip CLI and MCP server expose the corpus to AI agents (e.g. Benchling notebooks via Benchling's AI Connectors). |

</details>

## Publisher & Database AI Assistants

*The task: interrogate the curated scholarly databases your library already licenses.*

| Tool | Provider | Access | Description |
|---|---|---|---|
| [JSTOR AI Research Tool](https://about.jstor.org/products/jstor-platform/features-and-tools/research-tool/) | Ithaka (JSTOR) | Institutional | Free to JSTOR-participating institutions. Surfaces key points and arguments from articles, book chapters and research reports; recommends related topics and content; supports natural-language Q&A grounded in the document with inline references. Particularly strong for humanities, arts and social sciences. |
| [Scopus with AI](https://www.elsevier.com/products/scopus/scopus-ai) | Elsevier | Institutional | GenAI research assistant integrated into Scopus (now branded 'Scopus with AI'), drawing on content from 7,000+ publishers. Delivers referenced summaries, concept maps, emerging themes, foundational papers, and downloadable Deep Research agentic reports; RAG grounded only in curated Scopus content. |
| [Web of Science Research Assistant](https://clarivate.com/academia-government/scientific-and-academic-research/research-discovery-and-referencing/web-of-science/web-of-science-research-assistant/) | Clarivate | Institutional | Agentic AI assistant grounded in 120+ years of Web of Science Core Collection data. Task-based guides (Topic Explorer, Find a Journal, Literature Review 2.0) walk researchers through multi-step workflows with interactive visualisations and referenced responses. Natural language search in multiple languages. |

<details><summary>More tools for this task (1)</summary>

| Tool | Provider | Access | Description |
|---|---|---|---|
| [LeapSpace (formerly ScienceDirect AI)](https://www.elsevier.com/products/leapspace) | Elsevier | Paid | Elsevier's AI research workspace (successor to ScienceDirect AI) over 100M+ academic records incl. 23M+ full-text articles: chat with documents, compare evidence across papers, Trust Cards and Claim Radar for provenance, Writing Coach. Individual subscription with free trial, or institutional licence. |

</details>

## Citation Networks & Reference Management

*The task: map citation networks and keep your reference library organized.*

| Tool | Provider | Access | Description |
|---|---|---|---|
| [ResearchRabbit](https://www.researchrabbit.ai/) | Litmaps | Freemium | AI-powered paper discovery through citation chains and semantic similarity over 310M+ articles, shown as visual network maps. Free plan with unlimited searches; Zotero importer (two-way sync in development); RR+ from $10/month adds larger seed sets and alerts. |
| [Zotero](https://www.zotero.org/) | Digital Scholar | Free | Free, open-source reference manager with browser integration and Word/LibreOffice/Google Docs plugins. AI plugins (Aria, Beaver) add GPT powered paper chat and agentic search with sentence-level citations. |

<details><summary>More tools for this task (1)</summary>

| Tool | Provider | Access | Description |
|---|---|---|---|
| [Litmaps](https://www.litmaps.com/) | Litmaps | Freemium | Interactive citation network visualizations showing papers by publication year and citation relationships. Automated monitoring alerts when new relevant papers are published. Integrates OpenAlex, Semantic Scholar, and Crossref. |

</details>

## Grounded Knowledge & Specialized Databases

*The task: chat with your own sources — grounded answers from documents you trust.*

| Tool | Provider | Access | Description |
|---|---|---|---|
| [Gemini Notebook (formerly NotebookLM)](https://notebook.google/) | Google | Freemium | Google's source-grounded research notebook (NotebookLM, renamed Gemini Notebook in July 2026): upload papers and notes, chat with automatic citations, Deep Research integration, and AI-generated podcast-style Audio Overviews. Free tier; Google AI Plus/Pro plans raise notebook and source limits. |

## Systematic Review & Evidence Synthesis

*The task: screen thousands of abstracts, extract evidence, and keep a review living — PRISMA-style.*

| Tool | Provider | Access | Description |
|---|---|---|---|
| [ASReview](https://asreview.nl/) | Utrecht University (open source) | Free | Runs active-learning screening locally: the model learns from your include/exclude decisions and reorders remaining records, with simulation mode to benchmark savings on your own dataset. Fully open source; data never leaves your machine. |
| [citationchaser](https://estech.shinyapps.io/citationchaser/) \* | Neal R. Haddaway (with M.J. Grainger, C.T. Gray) | Free | Forward and backward citation chasing via the Lens.org API: input known relevant articles, retrieve everything they reference and everything citing them, and download all lists as RIS for systematic-review identification. |
| [Covidence](https://www.covidence.org/) | Covidence (not-for-profit, Cochrane partnership) | Institutional | Manages the full PRISMA pipeline in one workspace: import, dedupe, dual screening, full-text review, data extraction, and quality assessment, with team roles and export to analysis. De-facto standard licensed by many university libraries. |
| [Nested Knowledge](https://nested-knowledge.com/) | Nested Knowledge, Inc. | Freemium | Combines screening (Robot Screener), smart tagging, meta-analytical extraction, and PRISMA reporting with living-review updates: searches re-run automatically and interactive evidence maps and synthesis visualizations stay current and shareable. |
| [Polyglot (TERA)](https://tera-tools.com/) | Institute for Evidence-Based Healthcare (IEBH), Bond University | Freemium | Translates a PubMed or Ovid MEDLINE search string into syntax for Embase, CINAHL, PsycINFO, Scopus, Web of Science, Cochrane and more. Part of Bond IEBH's TERA evidence-synthesis suite (SearchRefiner, Deduplicator, Screenatron, Disputatron). |
| [Rayyan](https://www.rayyan.ai/) | Rayyan Systems, Inc. | Freemium | Screen titles/abstracts in blinded reviewer pairs with AI relevance ranking, resolve up to 200k duplicates, run risk-of-bias assessment, and auto-generate PRISMA flow diagrams; free tier covers core screening. |

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
| [ChatAcademia (formerly Research Kick)](https://www.chatacademia.com/) | ChatAcademia | Paid | AI research-ideation workspace (formerly Research Kick): detects research gaps and scores novelty 0-10 with literature evidence across 300M+ papers from 8+ databases, searches US/EU/UK grants, and syncs with Zotero and Mendeley. 7-day trial, then $15-45/month. |
| [Granted AI](https://grantedai.com/) | Granted AI | Freemium | Full-lifecycle grant platform: discovery across 140,000+ grants from 144 sources, funder research over 133,000+ foundations, AI-coached drafting from uploaded RFPs, simulated committee review and compliance checks. Free tier available; paid plans from $29/month. |
| [Instrumentl](https://www.instrumentl.com/) | Instrumentl | Paid | Grant discovery, tracking and lightweight proposal support with a large funder database (interactive 990 reports) and a curated feed of active opportunities. Strong for academic researchers and larger nonprofits managing complex grant portfolios. Single-user plans from ~$179/month (billed annually); 14-day trial. |

<details><summary>More tools for this task (2)</summary>

| Tool | Provider | Access | Description |
|---|---|---|---|
| [Grantable](https://grantable.co/) | Grantable | Freemium | Chat-first AI grant 'coworker' that remembers your organisation, past proposals and funder context. GrantGraph prospecting screens 990 filings and giving histories; scheduled funder scans, RFP checklists, section drafting. Free tier (5 chats/day); Starter $50/month, $25 for nonprofits. |
| [GrantBoost](https://www.grantboost.io/) | GrantBoost | Paid | Template-based AI grant writing for nonprofit and research grants. Pick a grant type, fill in organisational details and the AI drafts proposal sections. Works best for common, well-known grant categories. Free trial; plans from $32/month. |

</details>

## Survey & Experiment Design

*The task: design instruments and experiments well before collecting a single data point — including simulated piloting.*

| Tool | Provider | Access | Description |
|---|---|---|---|
| [Expected Parrot](https://www.expectedparrot.com) | Expected Parrot, Inc. | Freemium | Open-source Python DSL for building surveys and experiments, running them on panels of LLM-simulated respondents across many models, then re-fielding the identical instrument to real humans ('Humanize') and analyzing both in one results object. |
| [NC3Rs Experimental Design Assistant](https://eda.nc3rs.org.uk/) | NC3Rs (UK) | Free | Free web tool where researchers diagram an in vivo experiment and receive automated bespoke critique: statistical-method recommendations, randomization and blinding support, sample-size calculation, and a shareable design report for funders and ethical review. |
| [Qualtrics AI](https://www.qualtrics.com/support/survey-platform/distributions-module/synthetic-panels/) | Qualtrics | Institutional | Survey platform most universities already license: ExpertReview audits draft questionnaires for methodology errors, PII risk, and accessibility before launch; Synthetic Panels answer a survey with a first-party AI model trained on real survey responses. |

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
| [FAIR-Checker](https://fair-checker.france-bioinformatique.fr/) | Institut Français de Bioinformatique (IFB) / ELIXIR France | Free | Assesses FAIRness of a web resource or dataset by extracting its metadata and validating it against DataCite, OpenAIRE, Wikidata, Linked Open Vocabularies, and Bioschemas community profiles, to help providers improve resource quality. |

</details>

## Data Analysis

*The task: analyze data conversationally — upload, ask, get code and plots back.*

**Going deeper:** [Coding & Data Agents index (privacy-first, 60 entries)](https://michalie.github.io/research-coding-agents-wiki/) →

| Tool | Provider | Access | Description |
|---|---|---|---|
| [Benchling AI](https://www.benchling.com/ai) | Benchling | Freemium | ELN-grounded AI agents for the lab: answer questions across your Benchling data, import PDFs and CRO reports as structured records, draft notebook entries and study reports, and run AlphaFold 2, Chai-1 and Boltz-2 structure prediction in-platform. Credit-based; free for academic scientists. |
| [ChatGPT Data Analysis (Code Interpreter)](https://help.openai.com/en/articles/8437071-data-analysis-with-chatgpt) | OpenAI | Freemium | Sandboxed Python environment inside ChatGPT (now branded 'data analysis', formerly Code Interpreter / Advanced Data Analysis) for data exploration, statistical analysis, and interactive charts. Uploads up to 512 MB per file; free plan capped at 3 file uploads per day. |
| [Julius](https://julius.ai/) | Julius AI | Freemium | AI data analysis platform handling datasets up to 32GB through natural language queries. Automatically determines appropriate statistical tests and generates publication-ready visualizations. 50% student/educator discount. |

<details><summary>More tools for this task (1)</summary>

| Tool | Provider | Access | Description |
|---|---|---|---|
| [Claude Code Interpreter](https://claude.com/blog/create-files) | Anthropic | Paid | Claude creates and edits Excel, Word, PowerPoint and PDF files and runs data analysis (cleaning, statistics, charts) by writing and executing code in a sandboxed container ('Claude's computer') inside Claude.ai and the desktop app; available on paid plans. |

</details>

## Autonomous Research Agents

*The task: hand an agent a research question and let it plan, execute and report autonomously.*

**Going deeper:** [Autonomous Science Agents index (438 entries)](https://michalie.github.io/autonomous-stem-agents-wiki/) →

| Tool | Provider | Access | Description |
|---|---|---|---|
| [BIOS / BioAgents](https://ai.bio.xyz/) | bio.xyz (Bio Protocol) | Free | AI scientist at chat.bio.xyz: a research agent plans literature questions and answers with citations across papers, patents and trials; its data-analysis agent ranked #1 on BixBench (Jan 2026). Landing page now also pitches prompt-to-protein-binder design with an autonomous wet lab. Free access. |
| [Kosmos](https://edisonscientific.com/) | Edison Scientific | Paid | AI scientist running autonomous multi-hour discovery campaigns with parallel data analysis and literature search; a single run reads ~1,500 papers and executes ~42,000 lines of analysis code. Validated discoveries in metabolomics, neuroscience, and genetics. $200 per run; some free credits for academics. |

<details><summary>More tools for this task (5)</summary>

| Tool | Provider | Access | Description |
|---|---|---|---|
| [AIVA](https://chat.aivaportal.com/) | Mamidi Health | — | Conversational AI platform for genomics enabling natural language queries on genomic data. Integrates LLMs for analysis, literature search, and evidence-based clinical interpretations from sequencing data. |
| [Heureka Bench](https://www.heurekalabs.co/) | Heureka Labs | Free | Heureka Bench: local-first desktop notebook with the ARC research agent and a proprietary biology model (Archimedes) for multi-omics data analysis, hypothesis generation, experiment design, QC and literature curation. Free macOS/Windows download, no subscription; optional cloud compute. |
| [K-Dense](https://www.k-dense.ai/) | K-Dense Inc. | Freemium | Multi-agent system that plans and executes end-to-end scientific analyses (literature, code in sandboxes, reports) across 250+ databases and 200+ scientific data formats. Free Instant tier, per-run caps of $9-29, Plus $199/mo; academic labs get the Team plan at 90% off; BYOK and agent-skills components are open source. |
| [Pipette.bio](https://pipette.bio/) | Variome Analytics | Freemium | Bioinformatics AI agent that plans and runs genomics, transcriptomics, single-cell, ChIP-seq, variant-calling and metagenomics analyses from natural-language requests, on 150+ open-source tools with reproducibility bundles. Free tier (20 credits/month); paid packs and lab plans. |
| [Potato](https://potato.ai/) | Happy Potato, Inc. | Freemium | AI co-scientist for wet-lab work: generates protocols from stated intent, explores related literature and reviews papers on a free individual workspace; paid Optimizer tiers add guided and Bayesian experimental-design rounds and robot-ready outputs. |

</details>

## Code Assistants

*The task: write and debug research code with an AI pair programmer or agent.*

**Going deeper:** [Coding & Data Agents index (privacy-first, 60 entries)](https://michalie.github.io/research-coding-agents-wiki/) →

| Tool | Provider | Access | Description |
|---|---|---|---|
| [Claude Code](https://claude.com/product/claude-code) | Anthropic | Paid | Terminal-based agentic coding tool for code generation, debugging, and repository-wide modifications through natural language, also available in IDEs, Slack and the web. CLAUDE.md configuration for project conventions. |
| [Cursor](https://cursor.com/) | Anysphere (SpaceX) | Freemium | AI-first code editor (VS Code fork) with natural-language code generation, Tab completion and parallel background agents; full VS Code extension compatibility. Free Hobby tier, Pro from $20/month. |
| [GitHub Copilot](https://github.com/features/copilot) | GitHub (Microsoft) | Freemium | AI pair programmer providing real-time code suggestions in VS Code, Visual Studio, JetBrains, Eclipse, Xcode and Vim/Neovim. Agent mode delegates multi-file tasks to Copilot, Claude or Codex agents; free tier with 2,000 completions/month; GitHub reports up to 55% faster coding. |

<details><summary>More tools for this task (2)</summary>

| Tool | Provider | Access | Description |
|---|---|---|---|
| [Codex](https://openai.com/codex/) | OpenAI | Freemium | Agentic coding platform that runs tasks in isolated cloud sandboxes on your GitHub repository, or locally via CLI, desktop app and IDE extensions. Writes features, fixes bugs, explains code and opens pull requests. Included with ChatGPT plans; limited trial on Free. |
| [Google Antigravity](https://antigravity.google/) | Google | Free | Agent-first development platform from Google that lets AI agents take actions across an IDE, terminal and browser. Hosts Science Skills for connecting research workflows to 30+ life-science databases. Launched alongside Gemini for Science (May 2026). |

</details>

## Transcription & Qualitative Analysis

*The task: turn interviews and focus groups into text, then into coded themes — with sensitive data kept safe.*

| Tool | Provider | Access | Description |
|---|---|---|---|
| [Evidano](https://www.evidano.com/) | Evidano | Freemium | Uploads interview transcripts, documents, audio/video and runs thematic analysis with supporting quotes, frequency and cross-segment analysis, plus a chatbot over the data. Also fields an AI avatar that conducts semi-structured voice interviews in 100+ languages. Free tier available. |
| [MAXQDA AI Assist](https://www.maxqda.com/ai-assist) | VERBI GmbH (Germany) | Institutional | AI add-on inside the MAXQDA CAQDAS: suggests codes and subcodes for text passages with explanatory comments, summarizes documents and coded segments, and answers questions about coded data with responses linked to text sections. Claims zero data retention and EU-based processing. |
| [noScribe](https://noscribe.de/en/) | Kai Dröge (open-source, GPL-3.0) | Free | Transcribes interview audio fully offline on the researcher's own computer using Whisper plus pyannote speaker diarization; marks pauses, overlaps and filler words per qualitative-research conventions; includes an audio-aligned correction editor. ~60 languages; Windows/macOS/Linux. |
| [QualCoder](https://qualcoder.org/) | Colin Curtain (open-source, LGPLv3) | Free | Free open-source CAQDAS (text, PDF, image, audio, video coding) with AI-assisted coding and AI chat over data. Uniquely, the underlying prompts are visible and editable; backends include OpenAI GPT-4 or Blablador, the Helmholtz Society's free no-data-stored academic LLM service. |

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
| [WebPlotDigitizer](https://automeris.io/) | Automeris LLC (Ankit Rohatgi) | Free | Extracts numerical x/y data from published chart images: calibrate axes (incl. log), digitize points manually or with computer-vision assist, export data. Sign-up required; frontend open source (AGPL v3), v5.2. |

<details><summary>More tools for this task (2)</summary>

| Tool | Provider | Access | Description |
|---|---|---|---|
| [eScriptorium](https://escriptorium.eu/about/) | École Pratique des Hautes Études (EPHE) + Inria ALMAnaCH (France) | Free | Open-source web platform for segmenting and transcribing manuscripts and archival documents using the kraken HTR engine; researchers train or fine-tune their own recognition models and export ALTO/PAGE XML; self-hostable, IIIF-compatible. |
| [Handwriting OCR](https://www.handwritingocr.com/handwritten-laboratory-notes-ocr) | Handwriting OCR Ltd (UK) | Freemium | Uploads pages of contemporary handwriting — lab notebooks, field observation sheets, questionnaires, cursive letters — and returns searchable editable text; handles mixed hands, faded ink, and converts embedded equations to LaTeX. |

</details>

## Lab Bench & Protocols

*The task: draft, troubleshoot and execute protocols at the bench — hands-free, robot-ready, reagent-smart.*

| Tool | Provider | Access | Description |
|---|---|---|---|
| [BenchSci](https://www.benchsci.com/) | BenchSci (Toronto) | Free | Finds validated antibodies and reagents by AI-decoding figures and usage evidence from millions of publications and commercial products; filter by application, species reactivity, and validation status before ordering. Free for verified academic and nonprofit researchers. |
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
| [SLEAP](https://sleap.ai/) | Talmo Lab, Salk Institute | Free | Multi-animal pose estimation and identity tracking from video: GUI labeling with human-in-the-loop training, deep-learning inference at 800+ FPS, PyTorch backend since v1.5. |

</details>

## De-identification & Data Sharing

*The task: anonymize tables and transcripts so data can be shared or sent to a cloud model — with formal guarantees, GDPR in mind.*

| Tool | Provider | Access | Description |
|---|---|---|---|
| [Amnesia](https://amnesia.openaire.eu/) | OpenAIRE / ATHENA Research Center | Free | Anonymizes tabular datasets with formal k-anonymity and km-anonymity guarantees via a graphical interface, so shared data no longer counts as personal data under GDPR. Runs entirely on-premise; REST API available. |
| [Textwash](https://www.textwash.eu/) | Bennett Kleinberg + jocapps GmbH (OSS original: Kleinberg, Tilburg/UCL) | Freemium | Removes personal data from interviews, documents, and logs using a small on-device AI model (16 configurable entity types, contextual not keyword-based), in English, German, Dutch, French, Spanish, Italian. Free GPL-3.0 Python CLI covers English and Dutch. |

<details><summary>More tools for this task (2)</summary>

| Tool | Provider | Access | Description |
|---|---|---|---|
| [Presidio](https://presidio.dataprivacystack.org/) | Data Privacy Stack (community-owned; originally Microsoft) | — | Detects and anonymizes PII (names, credit cards, SSNs, and custom entities) in text and images via configurable NER/regex pipelines that run locally. MIT-licensed; originally built at Microsoft, now community-maintained under Data Privacy Stack. |
| [QualiAnon](https://github.com/pangaea-data-publisher/qualianon) | Qualiservice research data center, University of Bremen (with TU Munich and PANGAEA) | Free | Anonymizes or pseudonymizes qualitative text data such as interview transcripts, with user-controlled replacements and separation of identifiers, original data, and edited materials — the German FDZ (Qualiservice) archival workflow. |

</details>

## Writing & Translation

*The task: draft, polish and translate scholarly text, and get the manuscript into the journal's shape. No mature dedicated reformatting tool exists yet; a coding agent given the author-guidelines URL does the job under your supervision.*

| Tool | Provider | Access | Description |
|---|---|---|---|
| [DeepL](https://www.deepl.com/en/translator) | DeepL SE | Freemium | AI translation service known for contextually accurate output, particularly strong for European languages. Free web translator; Pro glossary feature keeps terminology consistent across a manuscript or field. |
| [Grammarly](https://www.grammarly.com/) | Superhuman | Freemium | AI writing assistant with grammar checking, plagiarism detection (16B+ web pages), and academic tone detection trained on scholarly writing. 2025 AI agents help find credible sources and check originality. |
| [Jenni](https://jenni.ai/) | Jenni AI | Freemium | Integrated research, reference, and writing workspace with AI autocomplete grounded in uploaded sources or Zotero/Mendeley imports; traceable citations linked to PDF locations in 10,000+ citation styles; exports to .docx and LaTeX. Free tier, no card required. |
| [Paperpal](https://paperpal.com/) | Cactus Communications | Freemium | Academic writing AI trained on 250M+ research papers. AI Research Finder returns summarized answers with insertable citations. Offers 30+ pre-submission journal checks aligned with publisher guidelines. |

<details><summary>More tools for this task (2)</summary>

| Tool | Provider | Access | Description |
|---|---|---|---|
| [Deepwriter AI](https://deepwriter.com/) | Deepwriter | Paid | Multi-agent long-form writing system (Abraxas reasoning engine) that keeps documents coherent up to 275 pages, with optional web deep research, uploads of up to 20 source files, citation handling, and LaTeX export. Plans from $159.99/month. |
| [QuillBot](https://quillbot.com/) | Learneo | Freemium | Paraphrasing tool with dedicated Academic mode maintaining scholarly language. Features context-preserving rewrites, citation generator (APA, MLA, Chicago), and QuillBot Flow unified workspace. |

</details>

## Visual & Presentation Creation

*The task: turn text into diagrams, posters and slide decks.*

| Tool | Provider | Access | Description |
|---|---|---|---|
| [Gamma](https://gamma.app/) | Gamma Tech, Inc. | Freemium | AI presentation tool generating polished slides from outlines or raw content. 2025 Gamma Agent update added real-time web research with citations. Transforms research notes into presentations with GPT-Image-1 integration. |
| [Napkin](https://www.napkin.ai/) | Napkin AI | Freemium | Transforms text into professional diagrams, flowcharts, mind maps, and infographics, plus Napkin Slides for decks. AI interprets relationships and hierarchy to produce appropriate visuals. Generous free tier (500 weekly credits); Plus $9, Pro $22 per month. |

<details><summary>More tools for this task (2)</summary>

| Tool | Provider | Access | Description |
|---|---|---|---|
| [Beautiful.ai](https://www.beautiful.ai/) | Beautiful Slides, Inc. | Paid | AI applying design principles in real-time with Smart Slide technology automatically adjusting layouts. Free access for students with verified .edu emails. Integrates with PowerPoint, Google Slides, Slack, and Dropbox. |
| [Gemini Notebook (Slide Decks)](https://notebook.google/) | Google | Freemium | Built-in feature of Gemini Notebook (formerly NotebookLM) that turns uploaded sources into slide decks and infographics, with citations back to the sources; PPTX export and per-slide editing added Feb 2026. Free tier; higher limits with Google AI Pro/Ultra. |

</details>

## Scientific Image Generation

*The task: generate scientific illustrations and publication figures.*

| Tool | Provider | Access | Description |
|---|---|---|---|
| [BioRender](https://www.biorender.com/) | BioRender | Freemium | Web-based scientific illustration platform with 50,000+ peer-reviewed icons and 5,000+ templates for life sciences; 3D protein visualization from PDB structures or uploaded files; high-resolution JPEG/PNG/PDF export. Paid plan required for publication rights ($35/mo academic individual). |

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
| [OpenAI Prism](https://prism.openai.com/) | OpenAI | Free | Free AI-native LaTeX workspace on GPT-5.2: whole-document writing and proofreading assistance, reference management, image-to-LaTeX for photographed equations and whiteboard sketches, agentic literature search with citation suggestions, and real-time collaboration with unlimited collaborators. |
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
| [Proofig + PubShield](https://www.proofig.com/pubshield/) | Proofig AI / Turnitin | Institutional | Image integrity AI (Proofig) paired with iThenticate text-similarity screening via PubShield. Brings figure-duplication detection and plagiarism checks into a single pre-publication workflow used by publishers and institutions. |
| [Prophy](https://www.prophy.ai/) \* | Prophy | — | Semantic reviewer-matching platform used by publishers and funding agencies to find conflict-free referees for a manuscript or proposal, ranked across 101M+ researcher profiles and 196M+ papers; integrates with Editorial Manager. Demo-request access, no public pricing. |
| [RegCheck](https://regcheck.app/) | Psychology of Digitalisation group, University of Bern (SNSF-funded) | Free | Upload a preregistration (or ClinicalTrials.gov link) plus the final paper; an LLM compares them dimension-by-dimension and flags deviations, quoting verbatim text from both documents so every judgement is checkable. Free, with API. |
| [SciScore](https://sciscore.com/) | SciCrunch, Inc. | Freemium | Paste a methods section, get a 1-10 rigor score auditing blinding, randomization, power analysis, and resource identifiability (antibodies, cell lines, RRIDs) against NIH/ARRIVE guidelines. Ten free reports yearly via ORCID sign-in. |
| [Stanford Agentic Reviewer](https://paperreview.ai/) | Stanford ML Group | Free | Free AI peer review system by Andrew Ng's team providing rapid, actionable feedback. Grounds reviews in latest arXiv research; correlation with human reviewers (0.42) matches inter-human agreement (0.41). |

<details><summary>More tools for this task (4)</summary>

| Tool | Provider | Access | Description |
|---|---|---|---|
| [Manusights](https://manusights.com/) | Manusights | Freemium | Pre-submission manuscript diagnostic: free Readiness Scan in minutes plus a $39 Full Review in about 30 minutes. Verifies citations claim-by-claim against live databases with a retraction gate and analyses figures. Anthropic privacy partner; manuscripts not used for model training. |
| [QED Science](https://www.qedscience.com/) | QED Science | Freemium | Critical Thinking AI that breaks a manuscript or grant into its constituent claims, flags logical and methodological gaps, and ranks novelty against studies in the field (QED Score). Free for academic researchers; enterprise tier for pharma/biotech. In use at 1,500 institutions in 70+ countries. |
| [Review-it](https://review-it.ai/) | Review-it AI | Paid | Uploads a manuscript, thesis or proposal (PDF/DOCX) and returns an AI peer review with strengths, weaknesses and suggested fixes, plus a pre-submission checklist (scope, citations, desk-rejection risk), journal finder and a reference checker for fake or broken citations. Per-document from $6.99; unlimited $59/month. |
| [Reviewer3](https://reviewer3.com/) | Reviewer3 | Paid | AI peer review platform: integrity checks (hallucinated or retracted citations, AI-generated text), claim-by-claim evidence decomposition, and panel review of study design, data and scope, with modes for author self-review, reviewer support and editorial triage. Claims 98.5% accuracy separating real from fabricated citations. |

</details>

## Integrity Screening & Forensics

*The task: screen the literature — and your own reference list — for fabrication, manipulation and AI-generated text.*

| Tool | Provider | Access | Description |
|---|---|---|---|
| [Argos](https://www.scitility.com/) | Scitility PBC | Freemium | Screens a reference list for retracted and high-risk articles before submission and sends alerts when papers in your citation network are retracted; computes daily risk scores from author histories and retraction cascades across 50M+ articles. |
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
| [Yoodli](https://yoodli.ai/use-cases/public-speaking) | Yoodli | Freemium | Records a practice talk via webcam or uploaded video and scores filler words, pacing, eye contact, clarity, and structure, benchmarking each rehearsal against the last; AI follow-up questions simulate audience Q&A after a conference talk. |

<details><summary>More tools for this task (3)</summary>

| Tool | Provider | Access | Description |
|---|---|---|---|
| [ChatSlide](https://www.chatslide.ai/guides/research-poster-presentation-ai-guide) | ChatSlide AI | Freemium | Upload a paper or paste an abstract; generates a single-page academic poster (A0 or 36x48 in) with sectioned layout, charts rendered from your data, and PubMed/Scholar citation lookup. Exports print-locked PDF or editable pptx. |
| [PowerPoint Speaker Coach](https://support.microsoft.com/en-us/office/rehearse-your-slide-show-with-speaker-coach-cd7fc941-5c3b-498c-a225-83ef3f64f07b) | Microsoft | Free | Rehearse a talk against your actual slide deck inside PowerPoint (web, Windows, Mac, mobile); flags pacing, pitch, filler words, monotone delivery, and reading text off slides, then produces a rehearsal report with statistics. |
| [VirtualSpeech](https://virtualspeech.com/practice/presentation-skills) | VirtualSpeech Ltd | Paid | Rehearse a talk in simulated rooms (conference room, lecture hall, press conference — 13 environments) via browser or VR headset; AI scores body language, eye contact, pace, and filler words, and asks questions generated from your presentation content. |

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
| [Sage Policy Profiles](https://policyprofiles.sagepub.com/) | Sage (powered by Overton) | Free | Shows where your publications are cited in government policy documents via Overton's index; export, visualize, and share the matches. A matcher added 2026 surfaces up to three personalized policy-engagement opportunities monthly. |

## Watchlist

Noticed but not properly vetted yet — waitlisted, too young, or missing a privacy policy.

- [AlphaEvolve + ERA](https://labs.google/science) — [sweep 2026-08-18] Fetched labs.google/science and research.google ERA blog. 'Computational Discovery' built with AlphaEvolve+ERA; ERA Nature paper May 19 2026 and CDC-forecasting claim confirmed. Access via 'Express interest' / gradual trusted-tester rollout.
[sweep 2026-09-11] Still 'Express interest' only (gate 2, usable this week, fails); Nature paper and CDC-forecasting claim reconfirmed. Keep candidate until self-serve access opens.
- [Gemini Co-Scientist](https://labs.google/science) — [sweep 2026-08-18] description flagged: Fetched labs.google/science and blog.google I/O 2026 post: Co-Scientist Nature paper confirmed, but Stanford liver-fibrosis/Vorinostat result was published in Advanced Science, not Nature. Access via 'Express interest' waitlist. Google-branded (blog.google/labs.google), not DeepMind.
[sweep 2026-09-11] Gate 2 fails: still 'Express interest' waitlist on labs.google/science (gradual rollout, no open access as of Sept 2026) — keep candidate. Description fix: Stanford vorinostat result is Advanced Science 2025, not Nature; Co-Scientist paper itself is in Nature (blog.google).
- [Literature Insights (Gemini for Science)](https://labs.google/science) — [sweep 2026-08-18] Fetched labs.google/science: Literature Insights listed, built with Gemini Notebook; tables, reports, slide decks, infographics confirmed. Access is 'Express interest' only — no open availability. Audio/video overviews not confirmed.
[sweep 2026-09-11] Gate 2 fails: still 'Express interest' waitlist, gradual rollout — keep candidate. Audio/video overviews now confirmed on blog.google I/O post (previous caveat resolved). Description accurate.
- [Nature Research Assistant](https://natureresearchassistant.com/) — [sweep 2026-08-18] Fetched site: Springer Nature confirmed, still beta; new users must join waiting list, no pricing disclosed. Summaries, paper chat, figure descriptions with audio all confirmed on page.
[sweep 2026-09-11] Still beta + waiting list, no pricing: fails gate 2 (usable this week). Keep candidate; re-check next sweep. New 'Manuscript Adviser' feature and publisher-agnostic scope now on page.
- [PowerGPT](https://power-gpt.net/) — [grok-gap-hunt 2026-08-18, independently verified] CONFIRMED: no privacy policy, ToS, or data-handling statement on homepage or /others (footer = contacts only) -> candidate. '0 daily users' still shown. arXiv:2509.12471 real, matches (94.1% vs 55.4%).
[sweep 2026-09-11] candidate re-vetted: gates 1,2,3,5 pass; gate 4 (recommendable - privacy policy/transparent terms) still fails, '0 daily users' counter unchanged. Keep candidate; promote only if a privacy/data statement appears.
- [Protocol Builder](https://protocolbuilderpro.com/) — [discovery 2026-08-18] Unique use case: structured IRB protocol and consent-form authoring with compliance templates Adoption: Sold to IRBs and GME programs; BRANY is an established IRB/compliance services organization; site current (screenshots dated March 2026) Demo-only, no public pricing — hence candidate. US clinical-research centric; EU ethics-committee fit unverified.
[sweep 2026-09-11] Still demo-only with no public pricing or self-serve trial — fails gate 2 (usable this week); gates 1, 3, 4, 5 pass. Keep candidate until a trial or institutional purchase path is verifiable.
- [Faraday](https://www.ascentbio.ai/) — [sweep 2026-08-18] ascent.bio rendered empty; live site is ascentbio.ai (fetched): Faraday AI scientist, 40+ institutions, signup via accounts.platform.ascentbio.ai. platform.ascentbio.ai/faraday showed 'down for maintenance'. No pricing found; public beta per blog.
[sweep 2026-09-11] Access is request/invite-gated per Ascent Bio docs (alpha program) and blog (request an access link); no public pricing. Per gate 2 waitlist tools are candidate, not active. Revert to active if self-serve signup is confirmed.
- [Genemod](https://genemod.net/) — [discovery 2026-08-18] Unique use case: Conversational agent acting over lab inventory and sample records (the inventory/ordering AI slot), or null if judged too close to generic ELN AI Adoption: Capterra and FitGap listings; own academic-labs pricing packages Weakest vetting: genemod.net pages repeatedly failed direct fetch (oversized pages); AI-agent and pricing claims come from genemod.net snippets via search. ~$199/month, 14-day trial, annual contract; no confirmed permanent free tier.
[sweep 2026-09-11] Still cannot fetch genemod.net directly. Alive, but Capterra now shows contact-for-pricing with no trial/free version; fails gate 4 (transparent pricing) and gate 2 is unverified. Keep candidate.
- [Paper Pivot](https://paperpivot.com/) — [capture 2026-09-11] Fetched paperpivot.com: landing page + terms of service only; "currently in development", waitlist signup, no company name, /pricing and /privacy 404 (privacy-policy link exists on the landing page, not checked). Closest thing to a dedicated journal-reformatting tool after FormatMyPaper turned out to be satire. Fails gate 2 (usable this week) and gate 4 (no named organisation) today; re-vet at next sweep. CheckMyManuscript ($5/manuscript, 95 compliance checks, anonymous operator) rejected as a checker, not a reformatter.
- [RefereeBio](https://refereebio.com/) — [grok-gap-hunt 2026-08-18, independently verified] All section-10 claims confirmed on homepage (free Starter month: 3 reviews/3 revision checks/3 edits, no card; AI-provider clause). No legal entity or team named; keep candidate.
[sweep 2026-09-11] Still no legal entity, founders, address or jurisdiction on /about, /legal or /security; self-described 'early access'. Fails gate 4 (recommendable to students). Keep candidate.
- [RefCheckAI](https://sydney-informatics-hub.github.io/RefCheckAI/) — [discovery 2026-08-18] Unique use case: Semantic citation verification — whether the cited paper supports the claim, not merely whether the reference exists (scite shows citation context but does not classify your own manuscript's claims) Adoption: University-built (Sydney Informatics Hub, NCI/NVIDIA-supported CodeFest); model weights and training data published for download Early access — web app via registration/email only. Classification accuracy not independently benchmarked. CC BY-NC 4.0.
[sweep 2026-09-11] Alive, unchanged. Still early-access via registration/email only, so fails gate 2 (usable this week). Keep candidate; page brands it 'AI Reference Checker'.
- [Paper2Video](https://github.com/showlab/Paper2Video) — [discovery 2026-08-18] Unique use case: Automatic pre-recorded conference-talk video generation from a paper — relevant for virtual conferences requiring submitted videos Adoption: NeurIPS 2025 SEA workshop acceptance; 2.4k GitHub stars MIT license but demanding: LaTeX sources as input, Gemini/OpenAI keys, ~48GB-VRAM GPU for talking head (lighter slides-only mode exists). Research-grade, not turnkey.
[sweep 2026-09-11] vetted: alive (last commit 2026-03-05) but fails gate 2 (usable this week): needs LaTeX sources, two paid API keys and a 48GB GPU with no hosted demo; research artifact rather than a tool students can run. Keep candidate; revisit if a hosted service appears.
- [PaperTok](https://www.papertok.com) — [discovery 2026-08-18] Unique use case: Paper to short-form social video for public science communication Adoption: CHI 2026 paper (Barcelona, April 2026); TechXplore coverage June 2026 Academic prototype, live site with generate button; requires user's paid Google Gemini subscription. Privacy policy and durability unverified.
[sweep 2026-09-11] Candidate vetted: passes gates 1, 3, 5; gate 2 marginal (needs user's paid Gemini subscription); FAILS gate 4 — no privacy policy on site, academic prototype with no durability commitment. Keep candidate; re-check if a privacy policy appears.

## Retired

Kept for the record.

- **ChatGPT Atlas** (deprecated) — Discontinued by OpenAI around 2026-08-09; the standalone Atlas browser was folded into the ChatGPT desktop app. Kept for the historical record.
- **You.com** (deprecated) — [sweep 2026-08-18] description flagged: Fetched you.com twice: now an enterprise/developer API platform (Search, Contents, Research, Finance APIs); no ARI or consumer answer engine mentioned. 2026 reporting confirms pivot; consumer plans gone. Usage-billed with one-time trial credits.
[sweep 2026-09-11] Resolved needs-review: the consumer AI search/ARI product the entry described no longer exists; you.com is a usage-billed retrieval/research API for developers (pivot confirmed 2026). Deprecated with epitaph — not usable by students as an AI search engine. If a developer-API category ever exists, it could be re-listed there.
- **Transcription Pearl** (deprecated) — [discovery 2026-08-18] Unique use case: Peer-review-backed LLM transcription workflow: the accompanying study found LLMs beat specialized HTR (Transkribus) on 18th/19th-c. English documents — the easter egg of this area Adoption: Companion paper published in Historical Methods (2025, DOI 10.1080/01615440.2025.2500309) and arXiv:2411.03340; GitHub repo public Beta; last commit Nov 2024 — maintenance uncertain. Requires own API keys and Python. CC BY-NC 4.0. Candidate until freshness confirmed.
[sweep 2026-09-11] Candidate rejected on gate 5 (alive/maintained): no commits since 2024-11-11 (22 months), still 1.0 beta, and superseded by the same authors' Archive Studio (May 2025). Suggest capturing Archive Studio as the candidate for this use case instead; its own maintenance cadence not yet verified.
- **FormatMyPaper** (deprecated) — Core as sole representative of the journal-reformatting use case (Michaela, 2026-08-18): no other tool in the catalog covers submission-requirements formatting.
[sweep 2026-09-11] Epitaph: FormatMyPaper is a satire site by Ubadah Sabbagh (Oct 2025), not a product — no formatting happens, testimonials are fabricated. Fails gate 4 (real organization) and gate 3 (does nothing). Was core as sole journal-reformatting representative; that use case now has no representative — Michaela to decide on a replacement (e.g. SciSpace/Typeset journal templates, Overleaf journal templates) or drop the task.

---

\* = flagged for re-verification.

Corrections and suggestions are welcome as issues or PRs. The maintenance rules
live in [AGENTS.md](AGENTS.md); every entry needs a working URL and has to pass
`scripts/validate.py`. This README is generated from [`tools/`](tools/) by
`scripts/build.py` — edit the YAML, not this file.

Data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Code: MIT.
