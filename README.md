# SSD — Sjögren B-cell Reset CI & Decision Map

Canonical repository for the public-data, decision-oriented Sjögren B-cell reset
competitive-intelligence project.

- Linear project: [Sjögren B-cell Reset CI & Decision Map](https://linear.app/jha-res/project/sjogren-b-cell-reset-ci-and-decision-map-3f6211aa8691)
- Repository: [bioJain/SSD](https://github.com/bioJain/SSD)
- Repository setup issue: [JHA-180](https://linear.app/jha-res/issue/JHA-180/initialize-ssd-github-repository-and-linear-codex-workflow)

## Working model

Linear is the source of truth for scope, priority, status, and acceptance criteria.
GitHub is the source of truth for versioned files, reviews, and releases. Codex
works from a Linear issue and records its issue identifier in the branch, commit,
and pull request.

```text
Linear issue (JHA-###)
  -> issue branch (owner/jha-###-short-description)
  -> commit(s) containing JHA-###
  -> pull request linking JHA-###
  -> merge to main
  -> Linear status update
```

See [CONTRIBUTING.md](CONTRIBUTING.md) for the detailed workflow.

## Evidence principles

- Use public information only.
- Trace every material claim and number to its source.
- Separate Sjögren-direct evidence from adjacent-autoimmune extrapolation.
- Distinguish verified fact, company interpretation, analyst inference, and unknown.
- Do not commit credentials, protected data, or large analysis binaries.

## Evidence framework

- [Evidence Ledger schema and claim taxonomy](10_framework/evidence_ledger_schema.md)
- [Source-quality rubric](10_framework/source_quality_rubric.md)
- [Contradiction-resolution and history protocol](10_framework/contradiction_resolution_protocol.md)
- [Claim verification and release checklist](10_framework/verification_checklist.md)

## Status

The repository is initialized. Research deliverables will be added through
issue-linked branches and reviewed pull requests.
