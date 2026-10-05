# Source-quality rubric

**Authorizing issue:** [JHA-145](https://linear.app/jha-res/issue/JHA-145/create-source-quality-and-contradiction-protocol)
**Version:** v0.1, 2026-10-06; proposed baseline pending PR review
**Applies to:** all downstream research, models, decks and articles

This is a project operating standard, not a new scientific finding. Use it with
the [Evidence Ledger schema](evidence_ledger_schema.md),
[contradiction protocol](contradiction_resolution_protocol.md) and
[verification checklist](verification_checklist.md). The charter evidence cutoff
remains **2026-10-04**; today's authoring or access date does not extend it.

## 1. Prefer the source that can establish the exact claim

Primary means the origin of the relevant data or authoritative action. It does
not mean unbiased. Assess the underlying methods, incentives and claim fit before
using publication prestige or recency as a tie-breaker.

| Claim | Preferred primary source | Cross-check and limits |
|---|---|---|
| Approval, label, regulatory safety action | Regulator decision, current label or safety communication | Check exact indication, population, geography and effective date. Company announcements do not establish another country's approval. |
| Clinical efficacy or safety | Full peer-reviewed study with methods, tables and supplements; regulator assessment where applicable | Compare protocol/registry results, prespecified endpoint, analysis set and data cutoff. Review for corrections/retraction. A small uncontrolled study cannot establish comparative benefit or absence of rare harm. |
| Study design, enrollment, trial status | Versioned registry, public protocol or results record | Sponsor/investigator update for current activity; registry records may be sponsor entered and stale. Planned dates do not establish events. |
| Corporate program activity | Dated sponsor disclosure naming the exact program plus applicable current registry | Apply the [asset-universe status rules](../20_competitive/asset_universe_method.md). Trial completion, program continuation and indication intent are separate claims. |
| Epidemiology and addressable population | Original population study, public health dataset or official statistics with methods | Independent population estimate; match case definition, year, geography and denominator. Reviews are discovery aids; do not combine primary/secondary Sjögren or US/EU5 implicitly. |
| Treatment practice | Current jurisdiction-specific guideline and original practice/utilization evidence | A recommendation does not establish real-world uptake. Label, off-label use and common practice are distinct. |
| Transaction or ownership | Public filed agreement/filing; buyer and seller disclosures | Separate signing from closing, upfront from contingent milestones, licensed territory from worldwide rights. Maximum potential value is not cash paid. |
| Mechanism, tissue reach, durability, reset | Original experiments or longitudinal clinical evidence measuring the asserted property | Apply the [B-cell reset taxonomy](b_cell_reset_taxonomy.md). Peripheral depletion, adjacent-disease response and marketing terminology do not establish Sjögren immune reset. |

For other claims, document why the chosen origin can establish that proposition.
Trace reviews, news, databases and AI summaries back to original public evidence;
use them as context or discovery unless the claim is specifically about that
secondary source. Inaccessible full text is not verified by an abstract or snippet.
Record what was actually inspected and retain the resulting limitation.

## 2. Assess quality without a compensating numerical score

Record each dimension as **adequate**, **limited** or **unusable**, with the
reason in ledger `notes` or a linked verification record. A strong dimension
cannot compensate for a missing denominator or incompatible population.

| Dimension | Adequate | Limited | Unusable for the intended claim |
|---|---|---|---|
| Authority and provenance | Original record or competent authority; identity/version clear | Secondary account or incomplete version history | Origin cannot be identified or authenticated |
| Methods and evaluability | Design, endpoint, analysis set, denominator, timing and uncertainty available as relevant | Small/uncontrolled study, immature follow-up, abstract-only detail | Required result/denominator unavailable or design cannot answer the question |
| Claim fit | Same disease, population, intervention, comparator, outcome, time and geography | Explicitly bounded extrapolation | Mismatch makes the stated conclusion invalid |
| Integrity and transparency | Precise location, faithful transcription, corrections checked | Selective reporting, missing supplement or unresolved discrepancy | Retracted/invalid result used as valid evidence or irreconcilable transcription |
| Independence and incentives | Origin and funding disclosed; independent corroboration where needed | Sponsor-only or overlapping dataset | Apparent corroboration consists only of copied material |
| Currency and cutoff | Relevant version as of cutoff; update history checked | Stale status or uncertain date | Post-cutoff information represented as baseline evidence |

An unusable result cannot support the intended affirmative/negative conclusion.
It may support a narrower attributed statement or a documented evidence gap.
Do not manufacture a source for `not_found`: record the public search endpoint,
queries, scope, access date and search-record location using the schema's required
fields, with `source_type=other_public` and `publication_date=not_reported` when
appropriate. This documents the search, not evidence of biological absence.

## 3. High-impact claims and two-source requirements

A claim is **high impact** if a plausible change could alter an advance/defer/stop
recommendation, a G1–G6 gate, patient/modality ranking, an addressable population
input, a safety/efficacy comparison, program inclusion/activity, approval or
material transaction interpretation. Mark impact and its decision use in `notes`.

For high-impact claims, inspect the primary source and a second relevant source,
record separate ledger rows and identify whether their evidence origins are
independent. Require a second reviewer before `approved`. Two URLs, publications
or reviewers do not necessarily mean two independent bodies of evidence.

| High-impact claim class | Verification minimum |
|---|---|
| Efficacy, safety, durability or immune-reset conclusion | Full original result plus protocol/registry/regulator cross-check for fidelity. A broad claim of replicated efficacy or established reset also needs independent biological evidence; a same-trial publication and registry are not replication. |
| Epidemiology, segment size or market-driving input | Original estimate plus independent population source or methodologically distinct estimate; preserve incompatible estimates and test decision sensitivity. Derived calculations link every input row and formula. |
| Current clinical program activity | Dated exact-program disclosure plus registry when applicable, as required by JHA-144. Two sponsor-controlled records can corroborate identity/status but not independently verify efficacy. |
| Comparative superiority or cross-disease transfer | Original rows for both comparators or populations; explicit comparability and transfer rationale. Unadjusted cross-trial differences remain analyst inference, normally low confidence. |
| Approval, safety action or transaction fact | Competent authority/filing plus corroborating record where available; the narrow authoritative-fact exception below applies when a second origin does not exist. |

Syndicated news, a release and a slide quoting it, registry/publication from one
trial, and buyer/seller reports of one transaction belong to shared evidence
families. Record shared trial IDs, cohorts, data cutoffs and source ownership.
Editorial peer review enables external scrutiny; it does not create an independent
dataset or remove sponsor incentives. Never call a sponsor-reported number a
`fact` solely because media repeated it. Follow JHA-143: sponsor-only statements
remain `company_interpretation` until the underlying proposition is independently
verified; retain the sponsor framing separately after verification.

**Narrow authoritative-fact exception:** one public competent-authority record
may establish its own administrative act (for example, a geography-specific
approval), or one public filed contract may establish an explicitly disclosed
term. A second reviewer must record the missing corroboration search, authority,
exact narrow proposition, exception rationale and residual limitation. High
confidence is possible for that act/term, never for a resulting efficacy, safety,
commercial or platform-validation inference. This exception does not waive the
JHA-144 registry requirement for confirmed clinical activity.

If the standard cannot be met, narrow and attribute the claim, retain an evidence
gap and a next-verification trigger, and use low/moderate confidence as justified.
A reviewer may approve a clearly disclosed provisional claim, but it cannot serve
as the sole verified premise for a critical gate pass. No critical conclusion may
rest only on unverified company interpretation.

## 4. Company releases and conference evidence

- Capture company claims as attributed `company_interpretation`, including
  topline numbers pending independent verification. Split reported result,
  sponsor explanation and analyst implication into separate rows.
- Identify conference, abstract number, presentation date, poster/oral/full-paper
  version and exact locator. Label preliminary/unreviewed evidence explicitly.
  Sponsor-only conference claims follow the same attribution rule.
- Record analysis set, numerator/denominator, endpoint definition, follow-up,
  data cutoff and uncertainty if disclosed. Missing details are `not_reported`;
  reported but unusable results are `not_evaluable`. Neither means `negative`.
- Abstract, poster, release and paper from the same cohort are versions of one
  evidence family. A later paper can clarify or correct, but does not silently
  replace a different population, endpoint or follow-up.
- Do not infer significance from “positive,” absence of harm from no reported
  events, or durable reset from transient response. Recheck at full results,
  regulator review, correction or longer follow-up.

## 5. Confidence applies to the exact wording

| Ledger value | Operational rule |
|---|---|
| `high` | Direct, evaluable, strong evidence; relevant triangulation or documented narrow-authority exception; no unresolved contradiction likely to change the decision. Scope and uncertainty are explicit. |
| `moderate` | Credible support with a bounded limitation, indirect component or discrepancy that cannot plausibly reverse the stated narrow conclusion. Explain the bound. |
| `low` | Sparse, preliminary, sponsor-only, substantially indirect or conflicting evidence could plausibly change the conclusion. Use for unresolved decision-changing contradictions. |
| `unknown` | Judgment not yet possible; `draft` only. |

Company-only clinical conclusions, conference-only clinical findings and
adjacent-autoimmune extrapolations to Sjögren cannot receive high confidence.
An adequately documented adjacent-disease result may be high for its own disease;
the separate Sjögren inference remains indirect. Evidence quantity does not
override fit, bias or uncertainty. Verification state measures review completion,
not evidentiary strength; `approved` may still be low confidence with disclosure.

## 6. Ledger integration

Keep the canonical CSV header and controlled vocabularies unchanged. Store source
quality, impact, evidence-family independence, exceptions, rationale and review
history in `notes` or a versioned record linked from `notes`. For multiple sources,
use separate rows; a synthesis row uses `claim_type=analyst_inference`, lists all
supporting claim IDs in `analyst_interpretation`, and uses `parent_claim_id` for
one parent/predecessor. Do not put multiple IDs into that single-ID field.

Each row must retain URL, publication date with actual precision, access date,
location, quotation where applicable, directness, disease relevance, evidence
state, confidence, verifier/date and observable re-verification trigger. Use the
schema's distinctions among `not_found`, `not_reported`, `not_studied`,
`not_evaluable` and `negative`. Method-policy text does not assert new clinical
facts; future applications must create and review their own ledger rows.
