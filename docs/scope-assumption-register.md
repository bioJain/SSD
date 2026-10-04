# Scope and assumption register

## Purpose

This register makes resolved scope, working assumptions, open choices and evidence
controls explicit for JHA-141 and its downstream workstreams. It is a control
document, not a source of scientific facts.

## Resolved decisions

| ID | Decision | Baseline | Consequence |
|---|---|---|---|
| S-01 | Decision form | Advance, defer or stop continued portfolio diligence | Every workstream must explain its effect on that recommendation |
| S-02 | Evidence cutoff | 2026-10-04 | Later evidence is excluded or labeled as a logged post-cutoff update |
| S-03 | Primary geography | United States | US definitions and assumptions anchor market conclusions |
| S-04 | Secondary geography | EU5: France, Germany, Italy, Spain and UK | EU5 is reported separately and used for comparison |
| S-05 | Core population | Primary Sjögren | Core disease, segment, pathway and opportunity conclusions use this population |
| S-06 | Secondary Sjögren | Separate contextual stratum | Do not pool silently with primary Sjögren |
| S-07 | Adjacent autoimmune evidence | Indirect only | May inform mechanism or feasibility, not establish Sjögren efficacy or size |
| S-08 | Source restriction | Public information only | No employer-confidential or non-citable proprietary evidence is required |
| S-09 | Evidence unit | Claim-level ledger row | Material claims and numbers require traceable source fields |
| S-10 | Source directory | Any future `00_source/` is immutable by default | Changes require separate explicit authorization |
| S-11 | Missing evidence | Controlled five-state vocabulary | Missingness is not converted to zero, absence or failure |
| S-12 | Deliverable logic | Question → workstream → output → final decision | Context without a decision mapping is non-critical |

## Working assumptions and falsification tests

Working assumptions enable progress but are not facts. Each must be revised when
its falsification test is met.

| ID | Working assumption | Why it is needed | Falsification or revision test | Affected output |
|---|---|---|---|---|
| A-01 | A portfolio-level decision can be made from public evidence with explicit uncertainty | Defines the project method | Critical gates remain not evaluable after the defined search and no bounded scenario resolves them | Final recommendation |
| A-02 | Primary Sjögren contains decision-relevant subsegments not captured by a single severity label | Enables segmentation | Evidence shows proposed segments cannot be consistently defined or measured | Patient framework |
| A-03 | Secondary Sjögren evidence is not directly exchangeable with primary Sjögren evidence | Prevents population leakage | A source supplies validated, separable evidence demonstrating equivalence for the specific claim | Segment and evidence rules |
| A-04 | Depth, tissue reach, off-treatment durability and reconstitution are separable modality attributes | Enables taxonomy | Operational definitions cannot classify representative edge cases without contradiction | Reset taxonomy |
| A-05 | Marketing use of “reset” is insufficient for classification | Protects analytical independence | Public evidence meets the operational category criteria irrespective of terminology | Claim-boundary rules |
| A-06 | Adjacent-autoimmune evidence may inform feasibility but requires a transfer rationale | Permits bounded extrapolation | Sjögren-direct evidence becomes available or biology/population differences invalidate transfer | Modality profiles |
| A-07 | Registry status alone does not prove an active program | Prevents stale-status errors | Recent corroborating sponsor or regulatory evidence validates activity | Asset universe |
| A-08 | US and EU5 evidence should not be pooled by default | Preserves geographic meaning | Compatible definitions, dates and denominators support a documented pooled analysis | Epidemiology and commercial work |
| A-09 | Patient segments may overlap while remaining decision-useful | Avoids false mutually exclusive bins | Overlap prevents reproducible interpretation or double counting cannot be controlled | Segmentation and sizing |
| A-10 | A useful commercial view can be scenario-based without false precision | Supports early decisions | Key denominator, adoption or access ranges are so unconstrained that scenarios are non-informative | Gate G6 |
| A-11 | Defer is a temporary evidence state with a named catalyst | Keeps recommendations actionable | No realistic evidence or catalyst could change the failed or unknown gate | Final recommendation |
| A-12 | Negative and missing evidence lead to different decisions | Prevents semantic errors | The underlying study and reporting context show the states were misclassified | Evidence Ledger |

## Unresolved choices

These choices remain open until the named trigger or downstream analysis resolves
them. They must not be silently converted into assumptions.

| ID | Open choice | Current handling | Resolution trigger | Owner |
|---|---|---|---|---|
| U-01 | Final decision sponsor and meeting date | Use portfolio-research audience; do not infer approval authority | Named sponsor and decision calendar recorded in Linear | JHA-141 owner |
| U-02 | Quantitative gate weights | Use qualitative pass/conditional/fail/not evaluable | Scoring rubric approval and sensitivity analysis | Downstream decision work |
| U-03 | Commercial time horizon | Report assumptions explicitly; no single default forecast | Final valuation or sizing brief specifies horizon | Market workstream |
| U-04 | Currency and price year | Preserve source currency/year; do not normalize silently | Commercial model convention is approved | Market workstream |
| U-05 | Exact EU5 aggregation rule | Report country-level evidence when comparability is uncertain | Compatible definitions and denominators are validated | Disease/market workstream |
| U-06 | Biomarker-enriched target segments | Treat as hypotheses | Reproducible clinical or translational evidence supports selection | JHA-146 |
| U-07 | Minimum durability threshold for reset | Leave taxonomy parameter explicit | JHA-142 operational criteria and edge cases are approved | JHA-142 |
| U-08 | Minimum evidence for active program status | Require dated corroboration and record unclear otherwise | JHA-144 status protocol is approved | JHA-144 |
| U-09 | Final integrated synthesis issue | Map framework to JHA-141 until assigned | Linear creates or designates synthesis issue | Project owner |
| U-10 | Post-cutoff monitoring cadence | Do not update baseline automatically | Catalyst-watch process specifies cadence and owner | Competitive workstream |

## Evidence controls

### Required source fields

Every material ledger row must contain, when applicable:

- Stable claim or evidence identifier
- Exact claim or number
- Source title and source URL
- Publisher or sponsor
- Publication or disclosure date
- Access date
- Precise evidence location (page, section, table, figure or registry field)
- Geography, population and denominator
- Study or source type
- Sjögren-direct or indirect status
- Fact, company interpretation, analyst inference, extrapolation or unknown
- Confidence and rationale
- Contradiction links
- Evidence state
- Re-verification trigger and last-checked date

### Controlled evidence states

| State | Use when | Do not interpret as |
|---|---|---|
| not found | A documented search did not locate evidence | Proof of absence |
| not reported | An identified source omits the item | Not studied or negative |
| not studied | The design did not assess the item | Negative result |
| not evaluable | Evidence cannot support a valid assessment | Zero effect |
| negative | The item was assessed and the relevant result was unfavorable | Missing evidence |

### Evidence hierarchy and transfer

- Prefer primary, current and directly relevant sources for decision-critical claims.
- Preserve conflicting credible evidence and explain differences in population,
  definition, time, design or source incentives.
- Label company statements as company interpretation unless independently verified.
- Use adjacent-disease, non-US/EU5 or modality-analog evidence only with a written
  transfer rationale and limitation.
- Never upgrade indirect evidence to direct evidence through repetition.

## Change management

A register change is required when any of the following changes:

- Root decision or advance/defer/stop definitions
- Geography or population boundary
- Evidence cutoff or public-data restriction
- Required deliverables or downstream issue mapping
- Gate definitions or completion rules
- Controlled evidence-state meanings

For each change:

1. Add or revise a register row with the date and authorizing Linear issue.
2. State the reason and affected questions, workstreams and deliverables.
3. Reassess any conclusion that depended on the prior baseline.
4. Preserve prior versions in Git history.
5. Add the commit or pull-request URL to Linear.

## Baseline approval

This register and the linked charter and research-question tree constitute the
JHA-141 approved baseline. Open choices remain intentionally unresolved and do not
block downstream work unless a dependent workstream identifies them as
decision-critical.
