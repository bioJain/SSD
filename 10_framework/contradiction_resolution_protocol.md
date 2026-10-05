# Contradiction-resolution and evidence-history protocol

**Authorizing issue:** [JHA-145](https://linear.app/jha-res/issue/JHA-145/create-source-quality-and-contradiction-protocol)
**Version:** v0.1, 2026-10-06; proposed baseline pending PR review

Use the [source-quality rubric](source_quality_rubric.md) and
[verification checklist](verification_checklist.md). Field names and values follow
the [Evidence Ledger schema](evidence_ledger_schema.md). This protocol implements
the schema's conflict and history rules without changing its CSV format.

## 1. Preserve and compare before choosing

1. **Capture each source separately.** Preserve exact wording/numbers, source ID,
   URL, date/version, evidence location and data cutoff. Give conflicting rows a
   shared `contradiction_id` and neutral `contradiction_summary`. Record the
   affected claim IDs, gate/input/artifact and high-impact flag in `notes`.
2. **Normalize transparently.** Compare disease, primary/secondary Sjögren,
   diagnosed/total population, geography, case definition, intervention/dose,
   comparator, endpoint, units, numerator/denominator, analysis set, missing-data
   rule, follow-up, study/cohort ID and data cutoff. Keep raw values; record any
   unit conversion formula in a separate `analyst_inference` row. Do not normalize
   away a difference in meaning.
3. **Check provenance and versions.** Determine whether sources share a cohort,
   release or filing, and check registry history, supplements, corrections and
   retractions. Publication date, data cutoff and event date are distinct.
4. **Classify the explanation** using the controlled table below. Identify the
   evidence that actually demonstrates the explanation; recency or source rank
   alone does not resolve a mismatch.
5. **Record the disposition.** Put the selected narrow claim, retained alternative,
   rationale, limitations, reviewer/date, confidence and next verification action
   in `notes` or its linked record. Use a synthesis row when the conclusion differs
   from either source's wording. Apply the chosen resolution to the relevant group
   members; keep subgroups when more than one explanation is needed.
6. **Propagate to artifacts.** Recheck every member of the group and all dependent
   inferences, calculations and artifact mappings. Disclose material alternatives
   in the memo/deck/article where they affect interpretation.

Never average conflicting numbers to create an apparently agreed result. A
separately justified synthesis or sensitivity analysis must preserve the source
estimates, compatible definitions, formula/weights and limitations. It does not
erase the contradiction group.

## 2. Controlled resolution values

| `contradiction_resolution` | Evidence needed | Disposition |
|---|---|---|
| `scope_difference` | Demonstrated population, geography, intervention, subgroup or analysis-set mismatch | Retain both scoped claims. Select only the one matching the decision population; do not supersede a valid different-scope result. |
| `definition_difference` | Different case, endpoint, response, denominator or financial-term definition | Retain definitions and estimates; harmonize only when a documented transformation is valid. |
| `time_update` | Same scoped proposition with explicit new event, follow-up, data cut or status version | Preserve old as-of evidence; apply new evidence only within its date/cutoff and scope. |
| `source_precedence` | Competent authority or better primary evidence answers the same proposition and explains why the alternative is weaker | Retain the losing source and a claim-specific rationale; rank alone is insufficient. |
| `error_corrected` | Public correction/retraction or demonstrated transcription/calculation error | Record error, correcting evidence and before/after values; preserve prior ledger/artifact versions. |
| `other` | Explanation not covered above, stated explicitly with supporting evidence | Document why existing values do not fit; require second review for high-impact use. |
| `unresolved` | No supported explanation or justified precedence | Retain alternatives, bound the decision and set a named next-verification action. |

An unexplained difference remains `unresolved`. A sponsor's explanation of an
error is attributed until verified. `mixed` is an evidence-status value for
evaluable divergent findings; it is not a substitute for a contradiction record.

## 3. Unresolved high-impact conflicts

If a credible alternative could change the recommendation, gate or ranking, use
`confidence=low` on the integrated conclusion. Moderate is allowed only when a
documented sensitivity/bound shows the discrepancy cannot reverse the narrow
conclusion; never assign high to an unresolved material conflict.

Show both values or interpretations, their scopes/dates and the reason unresolved.
Carry the alternatives through affected calculations. If the critical gate cannot
be validly assessed, use the charter's `not evaluable` gate state and name the
evidence/catalyst needed for defer. Do not select a convenient source to force a
pass. Assign the responsible downstream issue/reviewer and observable trigger.

## 4. Supersession and archival procedure

1. Create a new stable `claim_id` when approved meaning, data or interpretation
   changes. Set its `parent_claim_id` to the predecessor; for splits, each new row
   links to that predecessor. Give a changed source version a new `source_id` and
   record its relationship to the prior version. Never recycle IDs.
2. Preserve the old quotation, URL, dates, locator, confidence and review metadata.
   Append the replacement ID(s), reason, date, reviewer and affected artifacts to
   old-row `notes`; mark `verification_state=superseded` only where the old row is
   replaced for that claim use. Historical or different-scope evidence can remain
   valid and must not be globally retired just because something newer exists.
3. Start the new row at `draft`, then source-check, second-review where required
   and approve it. A replacement does not inherit approval. If old evidence has
   become invalid before replacement is ready, flag dependent artifacts for
   correction and withhold their release rather than keeping invalid support.
4. Update the repeatable artifact-mapping table for each new artifact version.
   Retain prior mapping rows; use `mapping_status=archived` for replaced uses and
   `active` for current ones (these are project mapping conventions). Preserve
   artifact version/anchor and a commit permalink. Current release claims cannot
   map to superseded rows; historical releases remain inspectable at their commits.
5. Retain a versioned audit entry containing old/new IDs, source-version URLs,
   reason, resolution, reviewer/date, gate/model impact and artifact corrections.
   Ledger `notes` may hold this entry or link to a versioned Markdown record.
   Preserve public archive/registry-history URLs when available; keep minimal
   quotations and precise locators rather than downloaded third-party files.
6. If a live URL fails or changes without history, retain the original URL, access
   date and captured quotation/locator. Add a public archive URL only after checking
   it. Record any inability to recover the exact evidence and reduce confidence or
   suspend use when verification cannot be supported. Git history preserves our
   record, not the external page itself. Never modify immutable `00_source/` files.

The baseline cutoff remains 2026-10-04. Evidence accessed later can establish the
baseline only if its relevant version/event was available by the cutoff. Later
evidence belongs in a labeled post-cutoff update or requires a logged charter
cutoff change. Never backdate publication/access dates or silently rewrite a
released artifact. Unknown publication precision remains explicit.

## 5. Re-verification triggers and ownership

| Trigger | Required action |
|---|---|
| New full paper, conference version, longer follow-up or registry results | Compare scope, analysis set and data cut; recheck result, confidence and family independence. |
| Correction, retraction, regulator safety action or credible contradictory source | Immediately flag affected release claims; inspect source integrity and all related rows before reuse. |
| Registry/pipeline, enrollment, discontinuation, filing or transaction update | Recheck exact asset, indication, geography and event; do not infer study status from program status. |
| New cutoff, population/geography, endpoint or artifact reuse | Reassess fit and all dependent assumptions; make post-cutoff changes visible. |
| URL/version failure or due `next_review_date` | Recover evidence/version or document the gap; re-verify before release. |

Record the owner issue/reviewer, trigger, target source and review date in `notes`
and `reverification_trigger`; fill `next_review_date` for time-sensitive claims.
Review at the earliest observed event or scheduled date and always before release.
Use the existing JHA-144 dates for its program-status rows. For new rows without a
specific catalyst, default to 30 days after verification for preliminary,
conflicting or unclear status claims, and 90 days for confirmed current status;
these are project review cadences, not scientific validity thresholds. Stable
historical facts may use `none_expected` only with a rationale and a correction/
retraction check at reuse. Changing one member forces review of its whole group.

## 6. Worked handling examples

These examples are synthetic process illustrations, not clinical evidence or
production ledger rows.

| Situation | Correct handling |
|---|---|
| Abstract reports 12/20 responses; paper reports 18/30 at a later data cut | Check cohort/definition/timepoint first. Use `time_update` only if the later cohort explains the difference; preserve both. No mean of 60% and 60% and no claim of independent replication. |
| Registry says recruiting; recent sponsor release says indication discontinued | Confirm exact program and dates. Document `time_update` if the event is explicit; keep study and program status distinct. If the apparent conflict cannot be explained, use `unresolved` and exclude an unconfirmed program from verified-active counts. |
| US prevalence studies use diagnosed primary Sjögren versus all Sjögren | Use `scope_difference` and/or `definition_difference` in separate groups as needed; retain estimates, do not average them or feed both into one market denominator. |
| New paper corrects a previously released response denominator | New source/claim IDs, `error_corrected`, predecessor link, old row `superseded`, old mappings `archived`; review new row and issue affected artifact corrections. |

For a concrete ID chain, suppose synthetic row `JHA-145-EX-001` used source
`SRC-EX-v1`. Its replacement `JHA-145-EX-002` uses `SRC-EX-v2`, sets
`parent_claim_id=JHA-145-EX-001`, and enters `draft`. Both share `CTR-EX-001` with
`error_corrected` and the before/after denominator in the resolution notes. The
old row retains its original verifier/date and adds “replaced by EX-002” with a
dated audit entry. Once the replacement is approved, archive the v1 artifact use
and add an active mapping to EX-002 for v2. No ID or historical citation disappears.
