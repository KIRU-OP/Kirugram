# Upstream Maintenance Policy

Kirugram is a community-maintained rebrand based on [Kurigram](https://github.com/kurigram-org/kurigram).
It is not an independent rewrite of the Telegram MTProto client implementation.

## Canonical upstream

- Repository: https://github.com/kurigram-org/kurigram
- Upstream branch: `main`
- Kirugram branch: `main`
- Package namespace: `kirugram` (upstream namespace: `pyrogram`)

The upstream revision checked when this policy was added (2026-11-28) was
`b44c9ba7cf5c44fa666921ea7b365c047ee1b92e`. This is an audit reference, not a
claim that Kirugram is synchronized with that revision.

## Rules for every upstream update

1. Record the new upstream commit SHA and review its changelog and commit history.
2. Map upstream `pyrogram/` paths to Kirugram's `kirugram/` paths. Do not treat
   the package rename as an independent implementation.
3. Review upstream changes file by file. Preserve Kirugram-only changes only when
   their behavior is understood and covered by tests.
4. Pay special attention to MTProto authentication, authorization keys, session
   storage, DC migration, message sequencing, update state recovery, encryption,
   and generated Telegram TL schema files.
5. Regenerate generated API files using the repository's documented build commands
   when the upstream TL schema changes. Do not hand-edit generated output.
6. Run the full offline test suite, lint, type checks, package build, and dependency
   floor/ceiling checks. Run live integration tests only when their required test
   credentials and services are configured.
7. Review the complete diff and package contents before merging. Never force-push
   over `main`, blindly merge upstream, or publish a release just because CI passed.
8. Document Kirugram-specific behavior and migration impact in `CHANGELOG.md`.

## Release gate

A release is ready only after:

- The upstream revision and the Kirugram-specific patch set have been reviewed.
- Required CI jobs pass on the exact commit intended for release.
- The wheel and source distribution build successfully and contain the expected
  `kirugram` package, license notices, and generated API files.
- Authentication, session handling, raw API imports, and supported integrations
  have regression coverage.
- The version, changelog, installation instructions, and published artifact agree.

A green CI run is evidence that the configured checks passed; it is not proof of
security, complete Telegram compatibility, or production readiness.

## Ownership and attribution

Keep inherited copyright notices and the applicable upstream LGPL-3.0-or-later
terms intact. Kirugram-specific changes must be clearly identified without
relabeling inherited upstream work as original Kirugram authorship. Review
`NOTICE`, `COPYING`, and `COPYING.lesser` before changing licensing or
redistributing modified files.
