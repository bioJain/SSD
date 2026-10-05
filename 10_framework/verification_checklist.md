# Claim verification and release checklist

**Authorizing issue:** [JHA-145](https://linear.app/jha-res/issue/JHA-145/create-source-quality-and-contradiction-protocol)
**Version:** v0.1, 2026-10-06; proposed baseline pending PR review

Use this checklist for each claim family and consuming artifact, alongside the
[source rubric](source_quality_rubric.md),
[contradiction protocol](contradiction_resolution_protocol.md) and
[canonical schema](evidence_ledger_schema.md). Store completed records in the
relevant workstream, linked from ledger `notes`; no new CSV columns are required.
Unchecked required items block approval/release. Record justified non-applicability
explicitly rather than checking an item that was not performed.

## 1. Source and atomic claim

- [ ] Claim has a stable ID, one proposition and a named decision use; high-impact
  classification and affected gate/ranking/model input are documented.
- [ ] Original public source inspected; URL, publisher/title, version, actual
  publication-date precision, access date and exact location recorded. No source
  access or verification is claimed solely from a summary/snippet.
- [ ] Quotation/transcription preserves units and source wording. Result,
  company framing and analyst inference occupy separate rows.
- [ ] Relevant source version/event is within the 2026-10-04 cutoff, or explicitly
  logged as a post-cutoff update under charter change control.
- [ ] Population, disease, geography, intervention, comparator, endpoint, timepoint,
  analysis set, numerator/denominator and uncertainty checked where applicable.
- [ ] Six quality dimensions assessed with limitations; direct/indirect and
  Sjögren/adjacent relevance assigned independently of publication type.
- [ ] `not_found`, `not_reported`, `not_studied`, `not_evaluable` and `negative`
  correctly distinguished; search scope/queries and dates recorded for not found.

## 2. Triangulation and judgment

- [ ] High-impact minimum met for the claim class: primary source and relevant
  second source, or the rubric's documented narrow-authoritative-fact exception.
- [ ] Separate rows identify each source and supporting claim IDs. Shared
  cohort/trial/release/contract families, incentives and independence are explicit.
- [ ] Sponsor-only clinical numbers remain `company_interpretation`; conference
  findings remain preliminary. Same-study cross-checks are not called replication.
- [ ] Derived numbers include input IDs, formula/units, assumptions and sensitivity;
  comparisons and extrapolations have a stated fit/transfer rationale.
- [ ] Confidence rationale obeys caps; high-impact unresolved decision-changing
  contradictions are low, and draft-only unknown confidence is not released.
- [ ] Reviewer actually inspected source fidelity before `source_checked`; a
  distinct second reviewer checked high-impact claims before `second_reviewed`/
  `approved`. Repeating the same author's check is not a second review.

## 3. Conflicts, history and future checks

- [ ] Every conflicting source retained; shared contradiction ID/neutral summary,
  controlled resolution, evidence for the explanation and alternatives recorded.
- [ ] No conflict silently averaged; unresolved alternatives and their decision
  sensitivity appear in all consuming artifacts where material.
- [ ] Replacement uses new IDs/predecessor link; old evidence, verification history
  and archived mapping/version anchors remain traceable through commit permalinks.
- [ ] All group members and dependent inferences/models/artifacts rechecked after
  an update, correction or supersession. Invalid evidence is withheld from reuse.
- [ ] Concrete trigger, target source and owner issue/reviewer recorded; dated
  next review assigned where time-sensitive. Due checks resolved before release.

## 4. Artifact release

- [ ] All required/conditional schema fields populated; IDs/links/controlled values
  valid. Every material claim/number maps to non-superseded approved ledger rows.
- [ ] Current artifact version and precise anchors appear in the repeatable mapping
  table; historical mappings retained as archived where replaced.
- [ ] No used row is draft, source-checked-only, second-reviewed-only or unknown;
  low/moderate approved claims visibly retain limitations and uncertainty.
- [ ] Critical gate passes do not rely solely on unverified interpretation;
  unassessable critical gates follow the charter's not-evaluable/defer rules.
- [ ] Deck and article use the same approved rows, cutoff and terminology; shortening
  prose preserves caveats needed to interpret the claim.
- [ ] Reviewer/date and remaining gaps/catalysts recorded in the release record.

## 5. Copyable verification record

```text
Record ID / version / authorizing issue:
Claim IDs / supporting input IDs / source IDs:
Artifact IDs, versions and anchors:
Decision use / high impact and reason / affected gates:
Evidence cutoff / post-cutoff handling:
Source URLs, versions, publication/access dates and locations:
Quality: authority; methods; fit; integrity; independence; currency:
Evidence families / shared datasets / funding and incentives:
Triangulation performed / independence limits:
Narrow-authority exception (if any): search, rationale, residual limit:
Claim type / directness / disease relevance / evidence status:
Confidence / rationale / decision sensitivity:
Contradiction IDs / raw alternatives / resolution evidence:
Predecessor and replacement IDs / archived versions and mappings:
Source checker and date:
Second reviewer and date (distinct person/agent; if pending, say pending):
Approval/release reviewer and date (if pending, say pending):
Outstanding gaps / owner issue or reviewer:
Target source / observable trigger / next review date:
Checklist exceptions with reason / release disposition:
```

A completed policy document or successful structural check does not verify any
clinical claim. Do not mark future research rows second-reviewed or approved until
the corresponding evidence review actually occurs.
