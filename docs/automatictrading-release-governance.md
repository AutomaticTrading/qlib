# AutomaticTrading Qlib fork — Release trigger governance

**Status:** Review proposal, **not effective on main**. No package build, upload, release or workflow execution occurred during this change.

## Verified upstream-derived workflow capability

The baseline `.github/workflows/release.yml` at Qlib fork `main` commit `54355232463878d2eebb91fe0ee5fa7fa1f5976c` triggered on **push to main**. Its release job invoked `release-please-action` using a secret named `PAT`. When the release action returned `release_created=true`, the dependent jobs could build wheels and use a `TESTPYPI` secret to upload them to **TestPyPI**. The workflow file does **not** demonstrate a production PyPI upload; do not mislabel this TestPyPI path as production PyPI.

Actual Actions enablement, token presence, release history, environment protections and effective Rulesets remain **UNVERIFIED**.

## Proposed mitigation

Replace automatic `push(main)` trigger with `workflow_dispatch`. Add a guard requiring the job to run from `refs/heads/main`. Leave build and package upload steps unchanged. GitHub owner/maintainer must separately review the security and release process before ever dispatching it.

Manual trigger ≠ authorization. Restrict dispatch actors and PAT/TESTPYPI credentials through effective GitHub controls and independent approval. No actor is authorized by this file to publish.

## Required checks before merge or release

1. Check exact-head workflow static diff; ensure no unreviewed `push` release trigger.
2. Verify no other workflow, tag publishing tool or GitHub App can release automatically.
3. Review whether `release-please` still performs the intended release process under `workflow_dispatch`; compatibility is **not tested**.
4. Verify the fork's test suite, permissions and branch Rulesets. No secret values must be output.
5. Any future TestPyPI upload or release needs separately approved exact artifact/source SHA.
6. Independently review this PR, run safe non-publishing CI and only then request explicit owner approval to merge.

## Boundaries

No changes to Qlib dataset, qlib/model packages, environment dependencies, PyPI/TestPyPI credentials, RD-Agent, Optuna, LightRAG, NautilusTrader, OpenClaw Panel, existing RAG, PostgreSQL, ELK or production services. No snapshots. No trading or live execution.

Mapped to central **INT-025**; status `PARTIAL_PATCH_IN_DRAFT_PR` pending CI, review, merge and effective settings verification.
