# Operational B-cell reset taxonomy

**Linear issue:** JHA-142

**Evidence cutoff:** 2026-10-04

**Scope:** modality-neutral classification for Sjögren portfolio research, with adjacent-autoimmune evidence explicitly labeled as indirect

**Status:** prospective analyst framework; not a validated regulatory endpoint or clinical surrogate

## 1. Purpose and governing rule

This taxonomy separates what a therapy **does to B-lineage biology** from what a
company calls it. It is designed to classify antibodies, small molecules, cell
therapies, engagers, combination regimens and future modalities by the same
evidence rules.

The governing rule is:

> **Depletion is an observed cell-state change. Reset is a composite claim that
> additionally requires off-treatment clinical durability after immune
> reconstitution.**

No single observation—undetectable blood B cells, an autoantibody decline, a
clinical response, a drug-free interval, or a naive-dominant returning B-cell
population—proves immune reset by itself. Classification requires the four-axis
assessment below and an explicit account of missing evidence. Clinical benefit
and biological depletion must be assessed separately [E-06].

The numeric thresholds in this document are prospective analyst cutoffs chosen
to make comparisons reproducible. They are not validated regulatory surrogates,
and they must be revised if later evidence shows that a cutoff is misleading for
a disease, assay or modality.

## 2. Classification categories

Assign exactly one primary category at the evidence cutoff. A secondary
descriptor may be added, but it must not replace the primary category.

| Category | Operational definition | Minimum evidence | Exclusions and cautions |
|---|---|---|---|
| **Functional control** | Disease-relevant B-cell activity is modulated or suppressed without evidence that the regimen meets depletion criteria, or control depends on continuing exposure. | Evaluable pharmacodynamic or clinical evidence showing control of B-cell signaling, survival, trafficking, antibody recycling, cytokine support or downstream activity. | A response during ongoing therapy is not reset. Reduced biomarkers without cell-count evidence are not depletion. |
| **Transient depletion** | A measurable fall in the prespecified B-cell population meets at least `D1`, but depletion is brief, incomplete, limited to blood, or followed by return without qualifying durable off-treatment control. | Serial cellular measurements with baseline and at least one post-treatment timepoint. | Do not infer tissue effects from blood. Do not infer reconstitution quality from total B-cell return. |
| **Deep depletion** | The regimen meets `D2` or `D3` and at least `T1`; durability or reconstitution evidence is insufficient for immune reset. | Prespecified sensitive assay, serial confirmation and at least `T1`; `T2` is preferred. | Blood-only evidence (`T0`) does not meet this category, even when blood depletion is profound. Deep depletion can occur without clinical benefit, tissue clearance, plasma-cell effect or immune reset. |
| **Immune reset** | A finite treatment produces deep depletion, followed by documented immune reconstitution and sustained disease control after B-cell return while the patient remains off the reset therapy and protocol-defined rescue/background intensification. | `D2+`, `T2+`, `O3` and `R2+`, plus clinically meaningful control. Evidence must include observations both before and after B-cell reconstitution. | Persistent aplasia alone is not reset. Ongoing maintenance, scheduled redosing, unwithdrawn high-intensity background therapy or absent post-reconstitution follow-up prevents this classification. |
| **Unproven reset claim** | “Reset,” “reboot,” “reconstitution” or equivalent language is used, but available evidence does not satisfy the immune-reset rule. | A traceable company or investigator claim and an axis-by-axis assessment showing the unmet requirements. | This category is not a negative efficacy judgment. It records a claim-evidence gap. |
| **Insufficient evidence** | Available public evidence cannot support a defensible assignment to the other biological categories. | Completed documented search and mandatory missing-evidence codes. | Never convert missing evidence into poor performance, no effect or evidence of absence. |

### 2.1 Category precedence

Apply the following decision order:

1. If core observations are missing or not evaluable, assign **insufficient
   evidence** unless a reset claim is being adjudicated.
2. If a reset claim exists and the immune-reset minimum is unmet, assign
   **unproven reset claim**.
3. If the mechanism controls function without qualifying cellular depletion, or
   requires ongoing exposure, assign **functional control**.
4. If cellular depletion is demonstrated, assign **deep depletion** only when
   both `D2+` and `T1+` are met. Otherwise assign **transient depletion** when
   the observed cellular reduction meets `D1+`.
5. Upgrade to **immune reset** only when all reset requirements are met. Never
   infer the category by modality class.

## 3. D–T–O–R four-axis framework

Record every axis independently. A higher score on one axis cannot compensate
for an unknown or failed requirement on another.

### 3.1 D — depletion depth

Depth is assessed against the prespecified disease-relevant population and assay.
Report absolute counts and assay lower limit whenever available; percentages alone
can be distorted by changes in other leukocytes.

| Score | Operational criterion |
|---|---|
| `D0` | Evaluable cellular evidence shows less than 50% reduction from baseline or otherwise shows no qualifying depletion. |
| `D1` | Partial depletion: at least 50% but less than 95% reduction from baseline, or a single profound-depletion observation without serial confirmation. |
| `D2` | Profound depletion: at least 95% reduction from baseline **or** below the assay lower limit/5 cells per µL, confirmed at two observations at least 28 days apart. |
| `D3` | Lineage-extending deep depletion: `D2` plus direct depletion evidence for relevant memory B cells and at least one additional pathogenic B-lineage population, such as plasmablasts or a defined autoreactive clone. Plasma-cell and LLPC effects require the separate rules in section 5. |

Rules:

- State the marker panel. `CD19+`, `CD20+`, memory B cells, plasmablasts and
  antibody-secreting cells are not interchangeable.
- A result at the assay floor is reported as “below the assay limit,” not zero.
- If no cellular measurement was made, do not assign `D0`; score the field with
  the applicable missing-evidence state (`NF`, `NR`, `NS`, `NE` or `UNK`). Missing
  core depletion evidence makes the primary classification **insufficient
  evidence** unless a reset claim is under review, in which case it is
  **unproven reset claim**. A supported functional-control signal may be recorded
  as a secondary descriptor while the primary category remains insufficient
  evidence.
- A percentage reduction calculated from an already-low baseline is `NE` unless
  the absolute count and assay performance support interpretation.
- Profound peripheral depletion and later repopulation dominated by naive or
  immature cells have been observed after rituximab, but those blood findings do
  not establish tissue depletion or reset [E-01, E-02].
- Depletion caused by conditioning, corticosteroids or another combination
  component must be attributed to the **regimen** unless component contribution
  is separately demonstrated.

### 3.2 T — disease-relevant tissue reach

This axis evaluates observed cellular effects outside peripheral blood.

| Score | Operational criterion |
|---|---|
| `T0` | Peripheral blood evidence only, or evaluable evidence shows no relevant tissue effect. |
| `T1` | Indirect tissue evidence: imaging, soluble biomarkers, modeled exposure, tissue-function change or serology without direct cellular measurement. |
| `T2` | Direct paired cellular evidence in at least one disease-relevant tissue, lymphoid organ or bone-marrow compartment, using biopsy, aspirate or validated cell-resolved method. |
| `T3` | Direct paired cellular evidence in two or more relevant non-blood compartments, or in one affected tissue plus a pathogenic niche/clone assessment that addresses residual disease biology. |

Rules:

- Blood depletion never stands in for gland, lymph-node, spleen or bone-marrow
  depletion; blood, tonsil, marrow and salivary-gland measurements have shown
  compartment-specific findings [E-02, E-03, E-04].
- Salivary flow, ultrasound or serum biomarkers can support `T1`; they do not
  establish cellular depletion.
- A tissue biopsy must report sampling site, timing, method and evaluability.
  Changes in focus score or cell density must not be interpreted without noting
  sampling variability. Paired Sjögren salivary-gland biopsies illustrate the
  value and small-sample limits of direct tissue assessment [E-04].
- Evidence from another autoimmune disease is **indirect for Sjögren**, even when
  it is direct for the measured compartment in that disease.

### 3.3 O — off-treatment durability

Start the clock at the later of: last dose of the putative reset therapy, end of
protocol conditioning, or last scheduled depletion-directed dose. Report exposure
half-life or cellular persistence where relevant.

| Score | Operational criterion |
|---|---|
| `O0` | No interpretable off-treatment window: ongoing continuous therapy, scheduled maintenance/redosing, rescue treatment, or follow-up shorter than 3 months. |
| `O1` | Clinical control for at least 3 but less than 6 months off the reset therapy, without prohibited rescue/background intensification. |
| `O2` | Clinical control for at least 6 but less than 12 months off the reset therapy, including at least one assessment after B-cell return when return has occurred. |
| `O3` | Clinical control for at least 12 months off the reset therapy and at least 6 months after documented B-cell reconstitution, without prohibited rescue/background intensification. |

Rules:

- “Treatment-free” must list what was stopped and what continued. Stable low-dose
  symptomatic or standard background care is allowed only if predefined and
  unchanged; otherwise assign `NE`.
- Persistent CAR or antibody exposure does not automatically make durability
  uninterpretable. If active drug or effector cells remain at biologically
  meaningful levels, describe the state as **exposure-associated control** and do
  not award `O3` without a justified sensitivity analysis.
- Redosing before relapse censors durability. Redosing after documented relapse
  records the first off-treatment interval but does not support reset.
- Drug-free control and the return of B cells are separate observations; both
  need explicit follow-up before durability after reconstitution is claimed
  [E-07, E-08].

### 3.4 R — immune-reconstitution quality

Reconstitution begins when total circulating B cells recover above the protocol
threshold or laboratory lower limit. Quality requires phenotype, function and/or
repertoire evidence; total count alone is not enough.

| Score | Operational criterion |
|---|---|
| `R0` | No B-cell return during observation, or reconstitution was not assessed. Persistent aplasia is reported separately. |
| `R1` | Quantitative B-cell return documented, but phenotype, repertoire and immune competence are missing or not evaluable. |
| `R2` | Qualitative renewal: returning cells are predominantly transitional/naive rather than memory-dominant, with at least one additional favorable measure such as reduced pathogenic clones, normalized repertoire diversity, or sustained disease control after return. |
| `R3` | Multidomain renewal: `R2` plus orthogonal evidence across at least two of repertoire/clonality, pathogenic autoantibodies, total immunoglobulins or vaccine/pathogen antibody preservation, functional immune response, and stable clinical remission after return. |

Rules:

- A naive-dominant population is compatible with renewal, not proof of tolerance;
  post-depletion repopulation patterns and clinical courses can differ [E-01,
  E-02].
- Stable total immunoglobulin or vaccine antibodies can demonstrate preserved
  humoral memory; it does not prove removal of pathogenic clones.
- Autoantibody decline is supportive only when antigen, assay, kinetics and the
  responsible cell source are interpretable.
- Hypogammaglobulinemia, recurrent infection or failed vaccine response is not a
  favorable reconstitution signal even if disease control persists.

## 4. Non-equivalence rules

The following substitutions are prohibited:

| Observation | Must not be treated as |
|---|---|
| Undetectable circulating B cells | Tissue clearance, plasma-cell depletion or immune reset |
| Clinical response on therapy | Off-treatment durability |
| Long drug-free interval before B-cell return | Durable control after immune reconstitution |
| B-cell return | High-quality immune reconstitution |
| Naive/transitional predominance | Restored tolerance or elimination of autoreactive clones |
| Autoantibody decline | Direct proof of plasma-cell or LLPC depletion |
| Total Ig decline | Selective removal of pathogenic humoral memory |
| Stable vaccine/pathogen antibody titers | Failure to affect pathogenic antibody-secreting cells |
| Company use of “reset” | Analyst classification as immune reset |
| Evidence in SLE, RA or another disease | Sjögren-direct evidence |
| No located evidence | Negative result or absence of an effect |

These distinctions are supported by observed differences among peripheral and
lymphoid compartments, B-cell repopulation phenotypes, and autoantibody versus
extrinsic-antigen antibody kinetics [E-01, E-02, E-03, E-05].

## 5. Plasma-cell, LLPC and serology rules

### 5.1 Required labels

Record plasma-cell evidence separately for:

- circulating plasmablasts;
- short-lived plasma cells;
- tissue-resident plasma cells;
- bone-marrow long-lived plasma cells (`LLPC`);
- antigen-specific or autoreactive antibody-secreting clones.

Do not collapse these populations into “plasma cells.” Marker definitions, tissue,
assay, timepoint and antigen specificity are required.

### 5.2 Direct versus indirect evidence

**Direct cellular evidence** includes paired cell-resolved measurement of the
named population in blood, affected tissue, spleen or bone marrow. Valid methods
may include flow cytometry, immunohistochemistry, single-cell profiling, ELISpot
or repertoire/clonal tracking when the population assignment is explicit.

**Indirect evidence** includes serum autoantibody change, total immunoglobulin,
complement, disease activity, imaging or a mechanism-based expectation. These can
support an interpretation but cannot establish depletion of LLPCs.

### 5.3 Target-specific rules

- For a CD20-directed regimen, mature plasma cells and LLPCs must be presumed
  **not directly targeted** unless direct evidence demonstrates an effect. CD20
  biology or an autoantibody fall alone is insufficient: mature plasma cells
  lacking CD20 are not directly depleted by anti-CD20 treatment, while measured
  autoantibody titers can fall [E-05].
- For CD19-directed regimens, do not assume coverage of CD19-low/negative plasma
  cells or LLPCs without direct population-level evidence; dual CD19/BCMA
  targeting has been studied specifically in a small SLE phase 1 cohort [E-09].
- For BCMA-, CD38- or dual-targeted regimens, target expression and depletion of
  the relevant pathogenic population must still be measured; target choice alone
  is not outcome evidence [E-09].
- A fall in one autoantibody with preservation of vaccine/pathogen antibodies may
  indicate selective effects or different source-cell kinetics. Record the mixed
  result; do not force a global plasma-cell conclusion [E-05].

## 6. Missing-evidence states

Every unscored required field must use one of these states. Blank cells are not
allowed in a completed assessment.

| Code | State | Use when | Must not mean |
|---|---|---|---|
| `NF` | not found | A documented, reasonable search found no relevant evidence. | Proof the effect is absent. |
| `NR` | not reported | A relevant source exists but omits the required result or detail. | The item was not studied. |
| `NS` | not studied | The design or authoritative description shows the item was not assessed. | A negative result. |
| `NE` | not evaluable | Evidence exists but cannot support a valid judgment because of assay, denominator, timing, confounding or data-quality limits. | Zero or no effect. |
| `NEG` | negative | The item was studied, reported and evaluable, and the prespecified favorable criterion was not met or a contrary effect was observed. | Missing evidence. |
| `UNK` | unknown | The state cannot yet be distinguished among `NF`, `NR`, `NS` or `NE`. Temporary only; include a resolution action. | A favorable or unfavorable assumption. |

Absence decision rule:

```text
Was relevant evidence located?
  no  -> NF (document the search)
  yes -> Was the question studied?
           explicitly no -> NS
           yes/unclear -> Was the needed result reported?
                            no  -> NR
                            yes -> Is it validly assessable?
                                     no  -> NE
                                     yes -> measured result, including NEG if unfavorable
Unable to determine which branch applies -> UNK + named resolution action
```

## 7. Company-claim adjudication

Treat company language as a claim to test, not a classification input.

1. Capture the exact claim, speaker/publisher, source URL, publication date,
   access date and precise evidence location.
2. Record the statement type as `company_interpretation` unless the sentence is a
   directly checkable fact, an analyst conclusion, an extrapolation, or unknown.
3. Decompose compound claims. “Deep tissue depletion and durable immune reset”
   creates separate D, T, O and R claims.
4. Populate each axis from public evidence. A corporate slide that repeats a
   claim without data is not independent support.
5. Apply the category rules without regard to modality or brand.
6. Record the gap: missing axis, inadequate duration, ongoing therapy,
   unmeasured tissue, absent post-return follow-up, or indirect disease evidence.
7. Reclassify only when new evidence changes an axis; never upgrade because the
   same wording appears in more sources.

Permitted language:

- “The company describes the regimen as a reset.”
- “Available evidence supports deep peripheral depletion; tissue and
  post-reconstitution durability remain `NR`.”
- “The reset claim is unproven at the 2026-10-04 evidence cutoff.”

Prohibited language:

- “Reset therapy” as an unqualified modality label.
- “Eradicates autoreactive immunity” without direct clone/population evidence.
- “Durable” without a stated clock, therapy status and follow-up range.

## 8. Standard assessment record

### 8.1 Required sentence

> In **[population]**, **[intervention and regimen]** is classified as
> **[category]** at **[cutoff date]**, with **D# / T# / O# / R#**; evidence is
> **[direct or indirect for Sjögren; grade; confidence]** because **[one-sentence
> rationale]**. Missing or limiting evidence: **[codes and named gaps]**.

### 8.2 Record template

```yaml
assessment_id: JHA-142-ASMT-0001
asset_or_regimen:
population:
disease:
evidence_cutoff: 2026-10-04
primary_category:
secondary_descriptor:
D_score:
T_score:
O_score:
R_score:
depletion_population_and_assay:
tissue_compartments:
off_treatment_clock_start:
background_and_rescue_therapy:
b_cell_return_definition_and_date:
plasma_cell_or_LLPC_evidence:
clinical_control_definition:
missing_evidence_codes:
sjogren_directness: direct | indirect
statement_type: fact | company_interpretation | analyst_inference | extrapolation | unknown
evidence_grade: A | B | C | D
confidence: high | moderate | low
decision_relevant_limitations:
reverification_trigger:
```

### 8.3 Evidence grade

| Grade | Minimum basis |
|---|---|
| `A` | Replicated or controlled human evidence in the target disease, with fit-for-purpose measurements for the assessed axes. |
| `B` | Prospective human target-disease evidence that is uncontrolled, small, incomplete on an axis or not replicated. |
| `C` | Human adjacent-disease, mechanistic or retrospective evidence requiring a written transfer rationale. |
| `D` | Preclinical, modeled, single anecdotal report, or uncorroborated company interpretation. |

Grade is not confidence. Confidence also considers consistency, precision,
directness, bias, follow-up and the importance of missing evidence.

## 9. Worked examples

These examples illustrate the method; they are not asset recommendations.

### 9.1 Intermittent anti-CD20 with blood depletion only

Observed: profound serial peripheral B-cell depletion; B cells return after
several months; no paired gland or marrow cellular data; response assessed while
background therapy continues.

Classification: **transient depletion**, `D2 / T0 / O0 / R1`. The depth axis is
profound in blood, but `T0` is below the minimum `T1` required for the primary
deep-depletion category. Tissue effect is `NS` or `NR` depending on the
protocol/source. It is not immune reset even if returning cells are largely
naive, because target-tissue and off-treatment evidence are missing [E-01,
E-03].

### 9.2 Finite CD19 CAR-T in adjacent autoimmune disease

Observed: deep depletion after one infusion, drug-free clinical remission,
B-cell return with naive/transitional predominance, and remission maintained
after return. Tissue evidence is limited and the disease is not Sjögren.

Classification for the studied disease may meet **immune reset** if `T2` and the
full timing criteria are documented. For a Sjögren decision the evidence remains
**indirect** and cannot establish Sjögren immune reset. If tissue evidence is only
indirect, classify **deep depletion with reset-compatible reconstitution**, not
immune reset [E-07, E-08].

### 9.3 Continuous BAFF/APRIL-pathway inhibition

Observed: clinical and B-cell functional control during continuous dosing;
serial cellular measurements show less than 50% change, and there is no
off-treatment interval.

Classification: **functional control**, `D0 / T0–T1 / O0 / R0`. The
classification does not imply weak efficacy; it distinguishes pharmacologic
control from finite immune reset.

### 9.4 Dual B-cell/plasma-cell targeting with single-arm evidence

Observed: deep blood depletion, autoantibody declines, medication-free follow-up
and B-cell return; direct LLPC measurement is absent and the study is small,
uncontrolled and outside Sjögren.

Classification: at most **unproven reset claim** or **deep depletion with
reset-compatible features** for a Sjögren assessment. Autoantibody negativity is
not direct LLPC-depletion evidence [E-05, E-09].

### 9.5 Apparent remission during persistent effector-cell activity

Observed: disease control for 12 months, but CAR cells remain detectable at a
level plausibly capable of ongoing B-cell suppression and B cells have not
returned.

Classification: **deep depletion with exposure-associated control**, `R0` and no
`O3`, provided `T1+` is met. If tissue reach is `T0`, classify as **transient
depletion** with exposure-associated control. Persistent aplasia plus remission
is not equivalent to reset [E-07, E-08].

## 10. Edge-case rules

| Edge case | Required handling |
|---|---|
| Persistent antibody, engager or CAR activity | State whether exposure is pharmacologically/biologically meaningful. Use exposure-associated control when continuing activity could explain remission. |
| Scheduled maintenance or pre-emptive redosing | `O0`; do not call the interval off-treatment durability. Record why redosing occurred. |
| Rescue medication or background intensification | Censor the durability interval at first rescue/intensification unless a prespecified analysis establishes non-confounding. |
| Stable background therapy | List drug and dose. Allow only if stable and predefined; run a sensitivity classification that treats it as confounded. |
| Lymphodepletion/conditioning | Attribute early cellular and clinical effects to the regimen unless component-specific evidence exists. |
| Mixed autoantibody or serotype response | Record each analyte separately and classify the global humoral conclusion as mixed; do not average unlike antibodies. |
| Disease fluctuation or regression to the mean | Require serial objective control and an appropriate comparator or strong longitudinal context before attributing durability. |
| Delayed tissue sampling | Align tissue timing with the biological claim; otherwise use `NE` rather than carrying forward an earlier result. |
| B-cell return definition changes across studies | Preserve each protocol threshold and assay. Do not pool return times without harmonization. |
| Loss to follow-up | Do not count unobserved time as durable remission. Report observed minimum and censoring. |
| Infections or hypogammaglobulinemia | Record as reconstitution-quality and benefit-risk evidence; disease control does not erase immune incompetence [E-05]. |
| Mixed patients in a cohort | Classify at patient level when possible. If only aggregates exist, use `NE` for claims obscured by heterogeneity. |

## 11. Public evidence register

The register anchors the framework to public human observations. It does not
validate the analyst cutoffs. Evidence from non-Sjögren diseases is deliberately
labeled indirect for a Sjögren decision. The approved evidence cutoff remains
2026-10-04. Access dates of 2026-10-05 record retrieval for PR verification;
they do not extend the cutoff or add post-cutoff evidence. Every publication
listed below predates the cutoff.

| ID | Public source | Publication date | Access date | Evidence location | Sjögren directness | Statement type | Grade | Confidence | Framework use |
|---|---|---:|---:|---|---|---|:---:|---|---|
| E-01 | [Leandro et al., *Reconstitution of peripheral blood B cells after depletion with rituximab in patients with rheumatoid arthritis*](https://pubmed.ncbi.nlm.nih.gov/16447239/) | 2006-02 | 2026-10-05 | PubMed abstract, Results and Conclusion | indirect | fact | C | moderate | Demonstrates profound blood depletion, later repopulation dominated by naive/immature cells, and the need to separate depletion from reconstitution quality. |
| E-02 | [Anolik et al., *Delayed memory B cell recovery in peripheral blood and lymphoid tissue in systemic lupus erythematosus after B cell depletion therapy*](https://pubmed.ncbi.nlm.nih.gov/17763423/) | 2007-09 | 2026-10-05 | PubMed abstract, Methods and Results | indirect | fact | C | moderate | Supports separate assessment of blood, lymphoid tissue and memory-B-cell recovery. |
| E-03 | [Nakou et al., *Rituximab therapy reduces activated B cells in both the peripheral blood and bone marrow of patients with rheumatoid arthritis*](https://pubmed.ncbi.nlm.nih.gov/19715572/) | 2009-08-28 | 2026-10-05 | PubMed abstract, Methods and Results | indirect | fact | C | moderate | Shows that blood and marrow effects can differ and must be measured by compartment. |
| E-04 | [Pijpe et al., *Clinical and histologic evidence of salivary gland restoration supports the efficacy of rituximab treatment in Sjögren's syndrome*](https://pubmed.ncbi.nlm.nih.gov/19877054/) | 2009-11 | 2026-10-05 | PubMed abstract, paired parotid-biopsy Methods and Results | direct | fact | B | low | Provides Sjögren-direct paired tissue evidence, with a very small sample and sampling limitations. |
| E-05 | [Ferraro et al., *Levels of autoantibodies, unlike antibodies to all extrinsic antigen groups, fall following B cell depletion with Rituximab*](https://pubmed.ncbi.nlm.nih.gov/18085668/) | 2008-01 | 2026-10-05 | PubMed abstract, rationale and Results | indirect | fact | C | moderate | Supports separating autoantibody kinetics from direct LLPC measurement and from preserved extrinsic-antigen antibodies. |
| E-06 | [Bowman et al., *Randomized Controlled Trial of Rituximab and Cost-Effectiveness Analysis in Treating Fatigue and Oral Dryness in Primary Sjögren's Syndrome*](https://pubmed.ncbi.nlm.nih.gov/28296257/) | 2017-07 | 2026-10-05 | PubMed abstract, Methods, Results and Conclusion | direct | fact | A | high | Demonstrates that biological depletion or biomarker change cannot substitute for clinically meaningful target-disease benefit. |
| E-07 | [Mackensen et al., *Anti-CD19 CAR T cell therapy for refractory systemic lupus erythematosus*](https://pubmed.ncbi.nlm.nih.gov/36109639/) | 2022-09-15 | 2026-10-05 | PubMed abstract, treatment, follow-up and B-cell return | indirect | fact | C | moderate | Supports measuring finite therapy, drug-free control and remission after B-cell reappearance as distinct elements. |
| E-08 | [Müller et al., *CD19 CAR T-Cell Therapy in Autoimmune Disease — A Case Series with Follow-up*](https://pubmed.ncbi.nlm.nih.gov/38381673/) | 2024-02-22 | 2026-10-05 | PubMed abstract, Methods, Results and Conclusions | indirect | fact | C | moderate | Supports explicit B-cell-aplasia duration, post-treatment medication status, clinical follow-up and controlled-trial caveats. |
| E-09 | [Wang et al., *BCMA-CD19 compound CAR T cells for systemic lupus erythematosus: a phase 1 open-label clinical trial*](https://pubmed.ncbi.nlm.nih.gov/38777376/) | 2024-09-30 | 2026-10-05 | PubMed abstract, Methods and Results | indirect | fact | C | low | Illustrates dual-target, autoantibody, reconstitution and long follow-up claims while retaining single-arm and disease-transfer limitations. |

## 12. Completion and update rules

An asset assessment is complete only when:

- a primary category and all four axis entries are present;
- every missing element has a controlled code and resolution action;
- treatment exposure, background therapy, rescue use and B-cell return are dated;
- blood, tissue, plasma-cell/LLPC, serology and clinical evidence are not
  conflated;
- every material claim has source URL, publication date, access date, evidence
  location, directness, statement type, grade and confidence;
- adjacent-autoimmune evidence includes a written Sjögren transfer limitation;
- the assessment names a re-verification trigger.

Reassess when any of the following occurs: longer post-reconstitution follow-up,
new tissue or marrow data, updated clone/repertoire analysis, rescue/redosing,
material safety or immune-competence findings, a controlled target-disease study,
or a change to the project's evidence cutoff.

