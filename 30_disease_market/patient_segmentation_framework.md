# Sjögren patient-segmentation framework

**Authorizing issue:** [JHA-146](https://linear.app/jha-res/issue/JHA-146/map-sjogren-patient-segmentation)
**Version:** v0.1, 2026-10-06 — working draft for review; not release-approved
**Evidence cutoff:** 2026-10-04; access date 2026-10-06 does not extend cutoff
**Decision scope:** primary Sjögren core; US primary market, EU5 country-level secondary comparisons; associated/secondary disease contextual only.

## Decision answer

Anchor the patient–modality map on **systemic activity, symptom burden and
organ-specific threat**, with separate glandular-function, biomarker, treatment-history,
lymphoma-risk and delivery-feasibility overlays. Use overlapping clinical views
for research and a separate counting partition for market sizing. Do not rank
modalities or calculate segment shares from this framework alone.

This is an analyst operational proposal grounded in the linked working evidence,
not a validated diagnostic algorithm, treatment selection tool or market estimate.
The [verification record](segmentation_verification_jha_146.md) distinguishes
actually inspected material from indexed excerpts and lists release requirements.
All evidence remains `draft` or `source_checked`; none is `approved`.

## 1. Population and diagnosis gates

Keep the following fields independent:

- **Population:** source-defined primary, associated/secondary or unresolved;
  record the coexisting autoimmune disease and attribution of manifestations.
- **Diagnosis:** established clinical diagnosis, suspected disease, or
  model-estimated undiagnosed disease. The latter two must not be pooled.
- **Research classification:** criteria version, criteria met/not met/not evaluable,
  entry/exclusion assessment and source. Clinical diagnosis is a separate field.
- **Geography:** study geography versus market geography; UK/France/Norway evidence
  does not establish a US proportion. EU5 countries remain distinct.

The 2016 weighted classification threshold is ≥4 under its entry/exclusion
conditions (JHA-146-CLM-0001, original excerpt only). Its distinction from a
stand-alone diagnosis is explicitly described by the inspected Johns Hopkins
summary (CLM-0002). Retain anti-SSA-negative disease as evaluable rather than
automatically excluding it; original criteria item/footnote verification is
pending. Do not implement a complete classification calculator from this draft.

**Undiagnosed disease is a funnel stratum, not currently confirmed treatment
eligibility.** Source-estimated undiagnosed prevalence belongs to JHA-147/148;
sicca suspicion alone cannot establish Sjögren. Associated disease is SEG-08,
kept outside the primary core denominator. These are charter scope rules, not
new epidemiological observations.

## 2. Clinical axes

### Activity and symptoms

The inspected activity-state abstract defines ESSDAI low <5, moderate 5–13 and
high ≥14 (CLM-0003); ESSPRI <5 is its patient-acceptable symptom boundary
(CLM-0004). Record raw scores, assessment date, domains/components and source.
These are measurement boundaries, not automatic treatment eligibility rules.

| Systemic activity | ESSPRI <5 | ESSPRI ≥5 |
|---|---|---|
| ESSDAI <5 | Low measured activity / acceptable symptoms | Low measured activity / unsatisfactory symptoms |
| ESSDAI 5–13 | Moderate activity / acceptable symptoms | Moderate activity / unsatisfactory symptoms |
| ESSDAI ≥14 | High activity / acceptable symptoms | High activity / unsatisfactory symptoms |

Unknown scores remain unknown; never put them into the low/acceptable cells.
At exactly ESSPRI=5, use the ≥5 cell under this source definition. Keep alternative
protocol definitions separate rather than silently changing the boundary.
This cross-tab is our operational inference (CLM-0009), not a newly validated scale.

### Glandular function and history

Record objective salivary and ocular measurements separately from perceived
symptoms. Preserve **unstimulated versus stimulated** flow and collection protocol;
do not substitute one for the other. Low flow does not alone prove irreversible
damage. Record symptom onset, diagnosis date and residual function separately;
“early disease” has no universal cutoff in this proposal and does not mean
reversible disease. Any trial reserve/duration threshold must come from its protocol.

### Organ involvement and severe systemic disease

For each relevant pulmonary, renal, neurological, cutaneous, articular,
haematological or other manifestation, retain source diagnosis, activity,
attribution, severity and fixed damage separately. ESSDAI's activity/damage
boundary requires original user-guide verification (CLM-0005); do not infer that
all historical impairment is currently active inflammation.

SEG-05 is an **analyst-defined organ-threat overlay**: a named current,
Sjögren-attributed active manifestation with documented threat to organ function
or life and specialist/protocol adjudication. It is not ESSDAI≥14 by definition.
High total activity can occur without organ threat; documented organ threat may
require attention at other totals. Specify the actual organ criteria rather than
using an unverified universal threshold. Cases lacking that assessment are unknown,
not organ-threat negative.

### Biomarkers, lymphoma and treatment feasibility

- Retain anti-SSA/Ro assay status separately from clinical activity and response.
  B-cell-related measurements are exploratory enrichment inputs, not proven reset
  response predictors (CLM-0011).
- **Lymphoma risk is not a general severity proxy.** BSR's risk-factor discussion
  supports a distinct risk flag (CLM-0006); separating it from current organ threat
  is our safeguard (CLM-0010). Record risk factors, suspected lymphoma and confirmed
  lymphoma separately. Do not convert risk-factor counts to individual probabilities
  or treat lymphoma prevention as a demonstrated reset benefit.
- Define refractory disease from actual therapy, dose, duration, adherence, response
  and intolerance. Treatment intolerance alone is not biological refractoriness;
  no universal failed-agent count is assumed.
- One-time-reset candidacy and intensive-therapy ineligibility are **modality/protocol
  specific**. Record actual infection, immune, comorbidity, conditioning and monitoring
  assessments; no blanket age or IgG cutoff is proposed. Severe need does not prove
  intensive treatment suitability or reset efficacy.

## 3. Segment dictionary and overlaps

The machine-readable [segment dictionary](patient_segments_jha_146.csv) supplies
stable IDs, operational criteria, caveats, clinical variables and commercial uses.
All composite inclusion rules are explicit analyst proposals; the ESSDAI/ESSPRI
boundaries have their separate working source rows.

| ID | Decision view | Boundary or role |
|---|---|---|
| SEG-01 | Glandular-dominant / low systemic activity | Objective ocular/oral involvement; ESSDAI<5; no current documented organ threat |
| SEG-02 | High symptoms / low systemic activity | ESSDAI<5 and ESSPRI≥5; may overlap SEG-01 |
| SEG-03 | Moderate active systemic disease | ESSDAI 5–13; report domains and attribution |
| SEG-04 | High active systemic disease | ESSDAI≥14; report domains and attribution |
| SEG-05 | Active organ-threatening disease | Organ-specific adjudicated overlay; not a score-only bin |
| SEG-06 | Other evaluable low systemic activity | ESSDAI<5 without documented glandular predominance after adequate evaluation |
| SEG-07 | Incompletely evaluable phenotype | Required activity/glandular/organ-threat inputs unavailable |
| SEG-08 | Associated/secondary disease | Contextual population stratum; separate underlying disease |
| SEG-09 | Undiagnosed/suspected funnel stratum | Separate estimated disease from suspicion; outside diagnosed core |

Biomarker positivity, refractory status, duration/reserve, lymphoma risk and
protocol-specific feasibility are overlays, not additional populations to add.
SEG-01/02 can overlap; SEG-05 can overlap systemic bands; SEG-08/09 are outside
the diagnosed primary counting population. Unresolved primary/associated status
is quarantined with its own reported denominator, not assigned to either by default.

## 4. Counting rules for JHA-148/167

These rules govern a future dataset/model; no patient-level data or population
estimates were obtained here.

1. Fix geography, year, case definition and diagnosed-primary denominator. Keep
   source-estimated undiagnosed disease and associated disease in separate strata.
2. Require a common assessment window. If organ-threat assessment is missing,
   assign the counting record to **unknown phenotype**; keep any known activity
   and symptom tags for descriptive analyses.
3. Among adequately assessed records, assign **organ-threatening** first. For the
   remainder, assign **high activity**, then **moderate activity**, then **low
   activity/glandular-dominant**, then **other low activity**. Missing necessary
   activity or glandular inputs go to unknown phenotype. Every core record has
   exactly one counting bin, including unknown.
4. Report ESSPRI, biomarker, refractory and feasibility cross-tabs within bins.
   Never sum overlapping clinical views. The partition's priority is a counting
   convention, not a validated medical severity order.
5. Count the union of clinically eligible groups using intersections or individual
   records. With aggregate sources lacking overlap data, retain bounds/scenarios
   and mark exact union `not_evaluable`; do not assume independence or zero overlap.
6. Propagate **conditional**, source-linked diagnosis, specialist, therapy-eligibility
   and delivery-reach transitions. Do not multiply marginal subgroup rates from
   incompatible populations. Already restricted denominators must not be restricted
   again for the same criterion.

For two compatible groups A and B within core denominator N, a descriptive union
is A+B−intersection(A,B). Without intersection data, the union lies between
max(A,B) and min(N,A+B); preserve why those bounds may still be too broad to be
useful. Fractions, eligibility and uptake remain for JHA-147/148/167 to establish.

### Synthetic interpretation checks

These are invented examples to test the proposed rules, not patient records or
population estimates. Assume diagnosed primary disease and adequate assessments
unless stated otherwise.

| Example | Clinical view | Counting disposition |
|---|---|---|
| ESSDAI=4, ESSPRI=7, objective glandular involvement, no organ threat | SEG-01 and SEG-02 | Low activity/glandular-dominant; counted once |
| ESSDAI=5, ESSPRI=5, no organ threat | SEG-03; unsatisfactory symptom cell | Moderate activity |
| ESSDAI=14, ESSPRI=2, no organ threat | SEG-04; acceptable symptom cell | High activity; no automatic organ-threat label |
| ESSDAI=7 with documented current organ threat | SEG-03 and SEG-05 | Organ-threatening; counted once |
| Low C4, high lymphoma-risk flag, missing ESSDAI/organ assessment | Risk overlay retained; SEG-07 | Unknown phenotype; risk does not supply severity |
| Historical organ damage without current activity | Damage recorded separately | Use current evaluated phenotype; history does not itself assign SEG-05 |

## 5. Measurement and commercial interface

[Measurement dictionary](segmentation_variables_jha_146.csv) records 15 variables
with distinct trial and commercial roles. Clinical evidence supplies phenotype,
activity and outcomes. Commercial relevance is an **analyst use case**, not a
clinical observation or quantified uptake estimate.

| Clinical question | Measurable trial variables | Separate commercial question |
|---|---|---|
| Is disease systemically active? | ESSDAI total/domain and attribution | What fraction reaches specialist care and actual therapy eligibility? |
| Is glandular function recoverable? | Flow type/protocol, ocular measures, baseline reserve | Is the hypothesized eligible population accessible and large enough? |
| Are symptoms improved? | ESSPRI total/components plus defined meaningful benefit | Does benefit support adoption/access under a given setting? |
| Is organ disease active and threatening? | Organ severity, function, damage, rescue/background therapy | Can referral centres and monitoring deliver the modality? |
| Does biomarker enrichment predict benefit? | Assay, prespecified threshold and treatment interaction | What independently sourced fraction qualifies? |

No segment share, price, uptake, peak sales, response rate or rNPV is inferred.
UK guidance is contextual evidence, not a US practice/utilization estimate.

## 6. Enrichment hypotheses and falsification

[Hypothesis register](biomarker_hypotheses_jha_146.csv) supplies four proposed tests:
B-cell-active enrichment, glandular reserve, refractory active systemic study
wedge, and symptom endotype stratification. Each records a candidate rule,
clinical validation test, separate commercial interpretation and disconfirming
result. None is a demonstrated predictive selection rule. HYP-02 maps to its dedicated
analyst-proposal row CLM-0012 and reserve-validation gap GAP-08; HYP-03 maps to
CLM-0013 and the refractory/safety/feasibility gap GAP-09. The issue scope authorizes
these research questions but is not clinical evidence for either hypothesis.
CLM-0009 describes only the two-axis measurement framework and does not support
glandular recovery or a reset study wedge.

The symptom study identifies groups using five symptom inputs, including anxiety
and depression (CLM-0007; author abstract). Its trial subgroup findings are
reanalyses (CLM-0008); they do not establish prospective response to a new reset
modality. Use the actual published classifier only after inspecting full methods;
ESSPRI alone cannot reconstruct it. Cohort-derived proportions are not US shares.

Link any reset hypothesis to the existing [D–T–O–R taxonomy](../10_framework/b_cell_reset_taxonomy.md):
cell depletion, clinical response and durable off-treatment control after
reconstitution are different observations. No patient phenotype alone proves reset.

## 7. Downstream handoff and review

| Owner | Handoff |
|---|---|
| JHA-148 | Population/diagnosis strata, counting partition, overlap and missingness controls |
| JHA-151 | Symptom/activity discordance, glandular reserve and organ-specific outcome needs |
| JHA-164 | Separate clinical, commercial, evidence-confidence and feasibility dimensions |
| JHA-166 | Stable segment IDs and hypothesis tests; no modality winner assigned here |
| JHA-147/167 | Source-compatible country-level denominators and conditional rates required |

[Evidence Ledger](evidence_ledger_jha_146.csv) and
[artifact mappings](evidence_ledger_artifact_mapping_jha_146.csv) preserve claim
provenance. [Owned gaps](segmentation_gaps_jha_146.csv) record original access,
second review, sizes/intersections and predictive validity work. No credible
contradictory numerical population estimates were synthesized; none was collected
for sizing. Distinguish definition differences from empirical contradictions.

Review checks:

- [x] Interpretable clinical views with explicit overlap and counting rules
- [x] Clinical measures separated from commercial hypotheses and missing inputs
- [x] Lymphoma risk kept separate from general severity
- [x] Population, geography, denominator, dates and inference labels retained
- [ ] Original-source gaps and JHA-145 high-impact verification minimum completed
- [ ] Distinct second review and claim approval before external release

Structural validation does not approve clinical evidence. This PR supplies a
reviewable research framework; downstream work must retain these limitations until
required source checks and approval are complete.
