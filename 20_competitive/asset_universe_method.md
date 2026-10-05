# Preliminary asset-universe validation

**Authorizing issue:** JHA-144

**Evidence cutoff:** 2026-10-04

**Access date:** 2026-10-05
**Status:** source-checked preliminary universe; not a final competitive-landscape assessment

## Decision use

This package defines the first auditable competitive set for deciding whether
continued diligence on B-cell reset strategies in Sjögren disease should advance,
defer or stop. It is deliberately broader than a list of successful trials. Active,
completed, terminated and unclear programs remain visible when they establish a
benchmark, identify a failed path or change the amount of apparent whitespace.

The package contains:

- `preliminary_asset_universe.csv`: one current classification per included asset
  or trial-bound regimen;
- `program_status_log.csv`: dated evidence supporting the program-status call;
- `initial_evidence_gaps.csv`: unresolved questions and the action needed to close
  them;
- `evidence_ledger_jha_144.csv`: claim-level sources using the JHA-143 schema.
- `evidence_ledger_artifact_mapping_jha_144.csv`: explicit links from ledger
  claims to asset rows and method statements.

## Inclusion boundary

An entry is included when it meets at least one of the following tests:

1. **Sjögren-direct:** the asset or regimen has a public Sjögren trial, regulatory
   decision or sponsor-confirmed Sjögren program.
2. **Modality-defining adjacent program:** the asset is in clinical development in
   another autoimmune disease and materially informs feasibility, depth,
   durability, delivery or competitive timing for a modality named in JHA-153 to
   JHA-162.
3. **Historical benchmark:** a completed, withdrawn or terminated Sjögren program
   is necessary to interpret the current benchmark or avoid false whitespace.
4. **Decision-relevant transaction:** a public transaction changes ownership,
   commitment or platform validation for a modality in scope.

Ocular-only, symptomatic-only, dietary, device and unrelated immunology programs
are excluded from this B-cell-reset competitive universe. The wider non-reset
systemic comparator sweep remains owned by JHA-161. Registry-only academic cell
therapy entries are retained only when Sjögren is explicitly named and the
construct is sufficiently identifiable to re-verify.

## Program-status protocol

This protocol resolves scope-register item U-08.

| Status value | Minimum evidence |
|---|---|
| `approved_geography_specific` | Dated regulator or sponsor disclosure identifies an approval and geography. Approval is never generalized beyond that geography. |
| `confirmed_active` | Sponsor or regulator evidence dated within 12 months of the cutoff confirms an ongoing program; a current registry is also required for clinical-stage programs when one should exist. |
| `completed_advancing` | The cited study is complete and the sponsor explicitly states that the asset is advancing, filing or entering another study. |
| `registry_active_unconfirmed` | A current registry is active/recruiting, but a dated sponsor disclosure was not found or does not identify the exact program. This is not treated as proof of an active corporate program. |
| `planned_not_started` | The registry is not yet recruiting and no study-start confirmation is available. Planned dates do not establish activity. |
| `unknown_stale_registry` | Registry status is unknown or stale; study start and completion are unverified. Planned completion dates establish neither completion nor discontinuation. |
| `completed_status_unclear` | The study completed, but current indication-level intent was not found. Completion is not interpreted as continuation or discontinuation. |
| `terminated` / `withdrawn` | The registry or sponsor explicitly uses that status. The cause is recorded only when explicitly reported. |
| `adjacent_activity_unconfirmed` | Sponsor evidence describes adjacent clinical development, but exact trial mapping or current registry activity is unverified. Exclude from verified-active counts. |
| `adjacent_completed_status_unclear` | A cited adjacent study is complete, but current program intent is unverified. Retain as a historical benchmark. |
| `adjacent_active` | Current sponsor and registry evidence confirms clinical development in an adjacent autoimmune disease; it remains indirect for Sjögren. |

The latest qualifying evidence wins only when the difference is a time update.
Conflicts that cannot be explained by date, geography, population or study scope
remain unresolved and cap confidence at `low` or `moderate`.

## Interpretation guardrails

- `confirmed_active` describes program activity, not efficacy, likelihood of
  approval or commercial value.
- A positive company release is captured as `company_interpretation` unless the
  underlying result is independently verified.
- Positive evidence for a termination or withdrawal claim supports that administrative event; it is not a positive or negative efficacy result.
- Each asset may map to multiple atomic claims. Direct historical and adjacent current claims require separate sources and mappings.
- A trial may be completed while the program is active; study status and program
  status are separate fields.
- Sjögren-direct and adjacent-autoimmune evidence are never pooled.
- Company use of “reset” does not qualify an asset as immune reset. Biological
  classification requires the D–T–O–R framework in
  `10_framework/b_cell_reset_taxonomy.md`.
- Trial-bound cell products without a stable nonproprietary or sponsor code retain
  a descriptive canonical name and `low` status confidence.

## Preliminary readout

The current set contains direct late-stage competition across BAFF/BAFF-R/APRIL,
CD40/CD40L, FcRn and TYK2, plus early direct depletion programs spanning T-cell
engagers, NK-cell combinations and trial-bound CAR-cell approaches. The adjacent
watchlist shows that autologous, allogeneic and in-vivo CAR programs are already
clinical in other autoimmune diseases, so lack of a Sjögren cohort is not evidence
of technical inactivity.

The most consequential uncertainty is not whether the field is active; it is
which programs can demonstrate disease-relevant tissue reach and durable clinical
control after B-cell reconstitution. Those fields remain evidence gaps for the
modality deep dives rather than being inferred from target or peripheral depletion.

## Re-verification cadence

Re-run the status check at the earliest of:

- a registry status, enrollment, completion-date or results update;
- a sponsor pipeline, discontinuation, transaction or regulatory disclosure;
- a Phase 2/3 readout or first Sjögren cohort disclosure;
- 2027-01-15 for `confirmed_active` and `adjacent_active` entries;
- 2026-11-15 for `registry_active_unconfirmed`, `planned_not_started`,
  `unknown_stale_registry`, `adjacent_activity_unconfirmed` and unclear entries.

## Review correction audit

Review of commit `3735525047` corrected GAP-016–018 column alignment,
separated planned and unknown registry states from active/completed states, and
removed uncorroborated adjacent activity from verified-active counts. The same
registry requirement applies to A026/A027 and to the adjacent component of A037.
CLM-0023–0025 now encode support for termination facts rather than negative
efficacy. CLM-0037 is retained as superseded; CLM-0039 and CLM-0040 separately
map the direct withdrawal and sponsor-reported adjacent tibulizumab activity.
GAP-019 tracks missing registry corroboration in addition to existing gaps.

The evidence cutoff remains 2026-10-04. These are corrections to the existing
source-checked package, not a new source-access pass or post-cutoff status update.

Reproduce structural and review regression checks with
`python3 scripts/validate_jha_144.py`.
