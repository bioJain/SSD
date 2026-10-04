# LinkedIn article QA checklist

Complete this checklist for every article package. A failed release gate blocks
publication; it is not waived by good prose.

## 1. Stable source controls

- [ ] The exact deck version and stable session anchor are recorded.
- [ ] The mapped session has passed JHA-181 content and visual QA.
- [ ] Every material claim and number maps to final JHA-173 Evidence Ledger rows.
- [ ] JHA-174 claim-level citation QA is complete for those rows.
- [ ] The Evidence Ledger and deck use the 2026-10-04 cutoff, or a logged
      post-cutoff exception is visible in all three formats.
- [ ] The deck destination, version, access method and permissions were tested.

## 2. Content completeness

- [ ] The title leads with a quantified signal, tension or decision question.
- [ ] The standfirst frames the decision problem without a generic overview.
- [ ] The opening states one answer-first thesis.
- [ ] The body uses two to four evidence anchors.
- [ ] At least one material uncertainty, negative result or counterargument is
      included.
- [ ] One portfolio, clinical-development or market implication is explicit.
- [ ] The CTA states the additional value of the mapped deck session.
- [ ] The article is understandable without access to the deck.
- [ ] Complete matrices, models, sensitivities, scoring and methods remain in the
      deck rather than being duplicated.

## 3. Evidence language

- [ ] Sjögren-direct evidence is visibly distinguished from adjacent-disease
      extrapolation.
- [ ] Facts, company interpretations, analyst inferences, extrapolations and
      unknowns are distinguishable.
- [ ] not found, not reported, not studied, not evaluable and negative are used
      according to the project definitions.
- [ ] Population, geography, denominator, time point and comparator are supplied
      wherever they affect interpretation.
- [ ] Cross-trial differences are not presented as causal or head-to-head results.
- [ ] Clinical and commercial differentiation are stated separately.
- [ ] The conclusion is no stronger than the least certain evidence needed to
      support it.

## 4. Citation and numerical QA

- [ ] Each citation supports the immediately adjacent claim.
- [ ] All numbers match the Evidence Ledger and the mapped deck slide.
- [ ] Dates, units, currencies, price years and percentages are correct.
- [ ] Derived values show the calculation or point to the deck method.
- [ ] Source hierarchy favors primary, current and directly relevant evidence.
- [ ] Company claims are attributed and not rewritten as verified facts.
- [ ] Contradictory credible evidence is disclosed rather than averaged away.
- [ ] Every URL resolves and points to the intended source.

## 5. Length measurement

The public reference article was measured on 2026-10-04 from its rendered LinkedIn
page. The count begins with the standfirst (“What reciprocal collateral
sensitivity...”) and ends after the final call-to-action (“...let's talk.”).

Count whitespace-delimited words in:

- standfirst;
- body paragraphs; and
- body list items.

Exclude:

- article title, author and publication metadata;
- numbered section headings;
- image alt text and figure captions;
- LinkedIn recommendation widgets;
- hashtags; and
- references.

This method yields **1,552 reference words**. For each article:

- [ ] Narrative-body word count is recorded.
- [ ] Count is **699–853 words** inclusive.
- [ ] Percentage is calculated as article words / 1,552 × 100.
- [ ] Section headings, captions and references are excluded consistently.

## 6. Visual QA

- [ ] The visual advances the argument rather than decorating it.
- [ ] Text and labels are legible at LinkedIn article width and on mobile.
- [ ] The exhibit states measure, population, date and evidence class.
- [ ] Source line and ledger row identifiers are present.
- [ ] The visual contains no confidential, licensed or unsupported content.
- [ ] The article does not expose withheld full-deck matrices or methods.
- [ ] Alt text describes the decision-relevant content.

## 7. Public-use and overclaiming QA

- [ ] Only public information is used.
- [ ] No employer-confidential, personal, licensed or non-citable information is
      disclosed.
- [ ] The piece is not medical advice or an investment recommendation.
- [ ] No approval, efficacy, market-size or program-status claim extends beyond
      its source.
- [ ] The CTA does not promise access that is unavailable.
- [ ] Sponsor/product names and trademarks are used factually and neutrally.
- [ ] The feed post preserves the article's central caveat.

## 8. Release record

- [ ] article-to-deck-mapping.csv contains the final article, slide and ledger
      relationships.
- [ ] publication-register.csv contains the deck version and destination.
- [ ] Article URL and publication date are recorded after publication.
- [ ] Any correction or retirement is versioned and linked to its successor.
- [ ] JHA-179 cross-format QA is complete before the release is declared final.


