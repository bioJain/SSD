# Deck-linked LinkedIn article series

## Document control

- **Authorizing issue:** [JHA-182 — Create deck-linked LinkedIn article series](https://linear.app/jha-res/issue/JHA-182/create-deck-linked-linkedin-article-series)
- **Upstream deck:** [JHA-181 — Build report-style full decision deck](https://linear.app/jha-res/issue/JHA-181/build-report-style-full-decision-deck)
- **Evidence cutoff:** 2026-10-04
- **Permitted evidence:** Public information only
- **Current release state:** Architecture complete; article drafting is gated

## Purpose

This directory controls the public article layer for the Sjögren B-cell Reset CI
& Decision Map. Each released article must be a concise, evidence-led entry point
to one approved deck session. It must stand on its own without reproducing the
deck's complete matrices, models, scoring, methods or final cross-session
recommendation.

The full deck remains the canonical long-form artifact. The article series does
not create a parallel evidence base or an independent numerical model.

## Current gate

No article title, brief or draft may be created until all of the following are
true for its mapped session:

1. JHA-181 has assigned a stable session anchor and deck version.
2. The session's Evidence Ledger rows are final under JHA-173.
3. Claim-level source and citation QA is complete under JHA-174.
4. The deck destination, access method and permissions have been validated.
5. The session is suitable for public external use.

As of 2026-10-04, JHA-181, JHA-173 and JHA-174 remain Todo. The map and
registers therefore contain no invented article placeholders. This is a release
control, not missing work.

## Reference length baseline

The style reference is [The RAS-Resistant Atlas](https://www.linkedin.com/pulse/ras-resistant-atlas-five-drug-resistant-cell-lines-one-tj-bing-essfc/).
Its narrative body measures **1,552 whitespace-delimited words** under the method
defined in qa-checklist.md. The required 45–55% range is therefore:

- **Minimum:** 699 words
- **Maximum:** 853 words
- **Drafting target:** 775 words

The word-count range applies to the article narrative body. It excludes the
title, author/date metadata, section headings, figure captions or alt text,
hashtags and reference list.

## Files

| File | Purpose |
|---|---|
| article-series-map.md | Controlled workflow and session-to-article map |
| article-template.md | Reusable brief, article and feed-post template |
| qa-checklist.md | Factual, citation, confidentiality, length and release QA |
| article-to-deck-mapping.csv | Machine-readable article/slide/ledger mapping register |
| publication-register.csv | Deck-version and publication record |

## Release sequence

1. Add only approved JHA-181 session anchors to article-series-map.md.
2. Create a brief from article-template.md and identify exact ledger rows.
3. Draft to 699–853 narrative-body words.
4. Complete qa-checklist.md and the mapping CSV.
5. Validate deck URL, version and access method.
6. Produce the final article and feed post.
7. Publish only after approval; record the URL and date in the publication
   register.


