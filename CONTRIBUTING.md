# Contributing

## Linear -> GitHub -> Codex workflow

1. Start from a Linear issue in the
   [Sjögren project](https://linear.app/jha-res/project/sjogren-b-cell-reset-ci-and-decision-map-3f6211aa8691).
2. Use Linear's suggested branch name when available. The branch must contain the
   issue key, for example `joehalee/jha-180-initialize-ssd-repository`.
3. Ask Codex to work from that issue and the current repository checkout.
4. Include the issue key in every commit subject, for example
   `JHA-180 Initialize repository workflow`.
5. Open a pull request whose title or description contains the issue key and the
   full Linear issue URL.
6. Merge through a pull request after checks and review. Update the Linear issue
   with the resulting pull request or commit URL and move it to the appropriate
   status.

## Branch and commit conventions

- Default branch: `main`
- Work branches: `<owner>/jha-<number>-<short-description>`
- Commit subject: `JHA-<number> <imperative summary>`
- Keep commits focused on one Linear issue when practical.
- Do not push unreviewed research work directly to `main` after repository setup.

## Repository hygiene

- Do not commit tokens, API keys, `.env` files, or private credentials.
- Do not commit large single-cell or model artifacts such as `*.h5ad` and `*.loom`.
- Record external artifact locations and checksums in an inventory file instead.
- Prefer reproducible scripts and source citations over manually edited outputs.
