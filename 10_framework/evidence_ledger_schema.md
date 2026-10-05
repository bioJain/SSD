# Evidence Ledger schema and claim taxonomy

**Linear issue:** JHA-143  
**Purpose:** keep every material claim, number, and interpretation traceable, auditable, and re-verifiable from source to memo.

## 1. Operating rules

1. Record one atomic claim per row. Split claims that depend on different sources, populations, outcomes, or confidence judgments.
2. Assign a stable `claim_id` before a claim enters a memo, table, model, deck, or article. Do not recycle identifiers.
3. Link every material claim use to a ledger row through `claim_id` in the repeatable artifact-mapping table; one claim may map to many artifact locations.
4. Preserve source wording in `quoted_evidence`; place synthesis or judgment only in `analyst_interpretation`.
5. Use public information only. Store a stable URL and precise evidence location instead of downloaded third-party files.
6. Treat absence labels as findings about the search or source, not as proof that an effect does not exist.
7. Create a new row or mark a row `superseded` when the claim meaning changes. Do not silently overwrite approved evidence.

## 2. Controlled vocabularies

### 2.1 Claim type (`claim_type`)

| Value | Meaning | Test |
|---|---|---|
| `fact` | A directly checkable statement reported by a source, including a number, event, design feature, or result. | A reviewer can verify the claim without accepting the source author's explanation. |
| `company_interpretation` | A sponsor's, developer's, or other interested party's explanation, framing, forecast, or conclusion. | The statement is attributable to that party and is not promoted to independent fact. |
| `analyst_inference` | The research team's synthesis, comparison, implication, estimate, or judgment. | The reasoning and supporting rows are explicit and another reviewer could disagree. |

Do not combine multiple types in one row. A statement or number found only in a sponsor/company source remains `company_interpretation` until independently verified. After independent verification, the verified underlying result may be a `fact`, while the sponsor's framing remains a separate `company_interpretation`. An analyst conclusion based on either is a separate `analyst_inference` row.

### 2.2 Evidence directness (`evidence_directness`)

| Value | Meaning |
|---|---|
| `direct` | The source measures or documents the same disease, population, intervention, comparator, outcome, timepoint, geography, or transaction element asserted by the claim. |
| `indirect` | One or more material elements differ and the claim requires extrapolation, analogy, triangulation, or mechanistic reasoning. |

For indirect evidence, identify the mismatch in `analyst_interpretation` or `notes` and reduce confidence when appropriate. Directness is independent of source quality: a direct company statement may still carry bias, while a high-quality adjacent-disease study remains indirect for a Sjögren-specific claim.

### 2.3 Evidence status (`evidence_status`)

Choose exactly one value.

| Value | Use when | Do not use when |
|---|---|---|
| `positive` | The evaluable evidence supports the stated direction or threshold. | The result is only the analyst's preference. |
| `negative` | The relevant outcome was studied, reported, evaluable, and did not support the stated direction or met the defined null/negative rule. | Nothing was found or the outcome was omitted. |
| `mixed` | Evaluable findings materially differ across endpoints, subgroups, timepoints, or credible sources. | The only problem is uncertainty or missing detail. |
| `not_found` | A documented, reasonable search did not locate evidence addressing the claim. | A located source omits the item. |
| `not_reported` | A relevant located source exists, but it does not disclose the required result or detail. | The outcome was explicitly not studied. |
| `not_studied` | The design, protocol, or authoritative description shows the question or outcome was not investigated. | Study status is merely unknown. |
| `not_evaluable` | Evidence exists but cannot support a valid judgment because of data quality, incompatible definitions, immature follow-up, missing denominator, or similar limitation. | The source simply omits the result. |
| `not_applicable` | The field or question does not logically apply to this claim. | The information is missing but should exist. |

Absence-classification decision tree:

```text
Is the field/question logically applicable?
  no  -> not_applicable
  yes -> Was relevant evidence located?
           no  -> not_found
           yes -> Was the question/outcome studied?
                    explicitly no -> not_studied
                    yes/unclear -> Was the needed result reported?
                                     no  -> not_reported
                                     yes -> Can it be validly assessed?
                                              no  -> not_evaluable
                                              yes -> positive / negative / mixed
```

`negative` is an observed evaluable result and must never be used as an absence label.

### 2.4 Confidence (`confidence`)

| Value | Minimum interpretation |
|---|---|
| `high` | Direct, internally consistent evidence from strong source(s), with no unresolved contradiction likely to change the decision. |
| `moderate` | Credible evidence with a material but bounded limitation, indirect component, or minor unresolved discrepancy. |
| `low` | Sparse, indirect, biased, immature, or conflicting evidence; the claim may change with plausible new information. |
| `unknown` | Confidence cannot yet be assigned; use only while the row is `draft`. |

Confidence is a reasoned judgment, not a substitute for source type, directness, or verification state. Explain non-obvious ratings in `notes`.

### 2.5 Verification state (`verification_state`)

| Value | Meaning |
|---|---|
| `draft` | Entered but not yet checked against the cited location. |
| `source_checked` | Source, dates, quotation, and evidence location were checked by one reviewer. |
| `second_reviewed` | A second reviewer checked claim fidelity, taxonomy, and contradiction handling. |
| `approved` | Ready for use in a released deliverable. |
| `superseded` | Retained for audit history but replaced by a newer row or evidence state. |

## 3. Field dictionary

Requirement codes: **R** = required for every row; **C** = conditionally required; **O** = optional.

| # | Field | Req. | Definition and validation |
|---:|---|:---:|---|
| 1 | `claim_id` | R | Stable unique identifier, recommended format `JHA-143-CLM-0001`. |
| 2 | `parent_claim_id` | C | Parent or predecessor claim when the row decomposes, qualifies, or supersedes another row. |
| 3 | `claim_text` | R | One complete, atomic claim written as it may appear in a deliverable. |
| 4 | `claim_type` | R | One of `fact`, `company_interpretation`, `analyst_inference`. |
| 5 | `evidence_status` | R | One controlled status from section 2.3. |
| 6 | `evidence_directness` | R | `direct` or `indirect`. |
| 7 | `disease_relevance` | R | `sjogren_direct`, `adjacent_autoimmune`, `general_mechanistic`, or `not_disease_specific`. |
| 8 | `source_id` | R | Stable source identifier; multiple sources supporting one claim should use separate rows linked by `parent_claim_id` or a shared claim family. |
| 9 | `source_type` | R | Controlled source class such as `peer_reviewed`, `registry`, `regulatory`, `guideline`, `company`, `conference`, `transaction`, or `other_public`. |
| 10 | `source_title` | R | Full source or record title. |
| 11 | `source_publisher` | R | Journal, registry, regulator, company, conference, database, or publisher. |
| 12 | `source_url` | R | Public stable URL, DOI resolver, registry URL, or archived public page. |
| 13 | `publication_date` | R | Source publication or last-update date at the precision actually supported: `YYYY`, `YYYY-MM`, or `YYYY-MM-DD`; use `not_reported` if the source provides no date. Do not invent a day. |
| 14 | `publication_date_precision` | R | `year`, `month`, `day`, or `not_reported`; must agree with `publication_date`. |
| 15 | `access_date` | R | Date the source was accessed, ISO `YYYY-MM-DD`. |
| 16 | `evidence_location` | R | Precise page, section, table, figure, record field, timestamp, or paragraph locator. |
| 17 | `quoted_evidence` | C | Minimal exact excerpt or faithful data transcription; required for `fact` and `company_interpretation` unless copyright or format prevents capture. |
| 18 | `analyst_interpretation` | C | Reasoning that connects evidence to the claim; required for `analyst_inference` and indirect evidence. |
| 19 | `contradiction_id` | C | Shared identifier grouping rows that conflict, recommended format `CTR-0001`. |
| 20 | `contradiction_summary` | C | Neutral description of the disagreement; required when `contradiction_id` is populated. |
| 21 | `contradiction_resolution` | C | `unresolved`, `scope_difference`, `time_update`, `source_precedence`, `definition_difference`, `error_corrected`, or `other`; required when `contradiction_id` is populated. |
| 22 | `confidence` | R | `high`, `moderate`, `low`, or `unknown`. |
| 23 | `verification_state` | R | One state from section 2.5. |
| 24 | `verified_by` | C | Reviewer name or identifier; required from `source_checked` onward. |
| 25 | `verified_date` | C | ISO date of the latest verification; required from `source_checked` onward. |
| 26 | `next_review_date` | O | Planned ISO review date for time-sensitive claims. |
| 27 | `reverification_trigger` | R | Concrete event that forces review, or `none_expected` for stable historical facts. |
| 28 | `geography` | R | Geography to which the claim applies, or `global`/`not_applicable`. |
| 29 | `population` | R | Study or decision population, or `not_applicable`. |
| 30 | `denominator` | R | Numeric base and its definition for quantitative claims (for example, `n=42 randomized participants`); use `not_applicable` for non-quantitative claims or a specific missing-evidence value such as `not_reported` when applicable. |
| 31 | `intervention` | R | Intervention, modality, asset, exposure, or `not_applicable`. |
| 32 | `comparator` | R | Comparator/control, or `none`/`not_applicable`. |
| 33 | `outcome` | R | Outcome, measure, event, or decision variable. |
| 34 | `timepoint` | R | Observation horizon/date, or `not_applicable`. |
| 35 | `notes` | O | Search scope, limitations, confidence rationale, date precision detail, or audit notes. |

## 4. Contradiction protocol

1. Preserve each conflicting source as its own ledger row; never average away disagreement.
2. Assign the same `contradiction_id` to all relevant rows and state the conflict neutrally.
3. Check whether population, definition, endpoint, timepoint, geography, version, or source incentives explain the difference.
4. Record a controlled `contradiction_resolution`; keep `unresolved` when evidence does not justify precedence.
5. An unresolved material contradiction normally caps confidence at `low` or `moderate` and must be visible in the consuming memo.
6. Re-verify all rows in the group when one member is updated or superseded.

## 5. Re-verification triggers

Use event-based triggers that a reviewer can observe, for example:

- trial registry, protocol, publication, abstract, or data-cut update;
- regulatory decision, label change, safety communication, or guideline revision;
- company pipeline-status, enrollment, discontinuation, or transaction update;
- new primary evidence that conflicts with or materially narrows the claim;
- evidence cutoff change, memo reuse in a new geography/population, or scheduled review date;
- source URL failure or correction/retraction notice.

## 6. Row integrity and release checks

Before a row becomes `approved`:

- all **R** fields and applicable **C** fields are populated;
- `source_url`, `publication_date`, `access_date`, and `evidence_location` resolve to the cited evidence;
- claim wording does not overstate the quotation or data;
- claim type, directness, disease relevance, evidence status, and confidence are independently assessed;
- `negative` is supported by an evaluable reported result;
- missing-evidence states follow the decision tree and include search/source context in `notes`;
- contradictions are grouped, explained, and carried into the memo where material;
- analyst inferences link to the factual rows that support them;
- memo linkage is stable and the consuming artifact exposes the `claim_id` or an unambiguous claim map;
- dates use ISO format and the row has a concrete re-verification trigger.

Pre-publication ledger checks:

1. Every material statement and number in each artifact maps to at least one non-superseded row through `claim_id` in the artifact-mapping table.
2. Every approved row used by an artifact maps back to each exact artifact anchor through that same table.
3. No row used in the release remains `draft` or has `confidence=unknown`.
4. All due review dates and triggered re-verifications are resolved.
5. Contradiction groups and low-confidence conclusions are disclosed rather than hidden.

## 7. Template use

`evidence_ledger_template.csv` contains the canonical claim-level fields and one clearly marked removable example row. `evidence_ledger_artifact_mapping_template.csv` is the repeatable relation between stable claim IDs and every memo, deck, article, table, or model location that uses them. Add one mapping row for each claim/artifact/anchor use; multiple rows may reference the same `claim_id`. Delete example rows before production use and retain header order in both files.

