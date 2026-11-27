# Contributing to Kirugram

Thank you for considering a contribution to Kirugram. Whether you are fixing a defect, improving documentation, adding tests, or suggesting an enhancement, your work is welcome.

This guide explains how this repository is developed and how to prepare a change for review. Please read it before opening a pull request.

## 1. Project and contribution basics

Kirugram is maintained in the `KIRU-OP/Kirugram` repository. It continues the technical lineage of Kurigram and Pyrogram while maintaining its own project identity and the `kirugram` Python namespace.

Contributions must respect the existing project history, retained copyright notices, and LGPL-3.0-or-later licensing. Do not remove or rewrite upstream attribution or license headers as part of an unrelated change.

Before starting substantial work:

1. Search the issue tracker and open pull requests for related discussions.
2. For a significant feature or behavior change, open an issue first so the approach can be discussed.
3. Keep each pull request focused on one understandable change.

## 2. Development environment

Kirugram supports Python 3.10 and newer. The repository uses [uv](https://docs.astral.sh/uv/) to manage its development environment and dependencies.

Install uv using its official installation guide, clone the repository, and enter the project directory:

```bash
git clone https://github.com/KIRU-OP/Kirugram.git
cd Kirugram
```

Synchronize the environment:

```bash
make sync
```

The Makefile runs project commands through uv. The first run creates the local `.venv` and installs the versions recorded in `uv.lock`.

If you change dependency declarations in `pyproject.toml`, regenerate the lock file and include both files in your change:

```bash
uv lock
```

Do not manually edit dependency entries in `uv.lock`.

## 3. Generated API files

Some parts of the Telegram API implementation are generated from the schema and compiler templates. These include:

- `kirugram/raw/types/`
- `kirugram/raw/functions/`
- `kirugram/raw/base/`
- `kirugram/raw/all.py`
- `kirugram/errors/exceptions/`

Generate these files with:

```bash
make api
```

Do not make manual fixes inside generated output. If generated code needs to change, investigate the source schema, compiler, templates, or handwritten code that consumes the generated API. Changes under `compiler/api/source` should be followed by another `make api` run.

A fresh checkout may not contain all generated files. Run the generator before type checking or when working on code that imports generated `kirugram.raw` modules.

## 4. Checks to run before a pull request

Run the relevant checks after making your changes:

```bash
make lint
make api
make typecheck
make test-unit
```

What these commands do:

| Command | Purpose |
| --- | --- |
| `make lint` | Runs Ruff checks and verifies formatting. |
| `make format` | Applies the repository's Ruff formatting. |
| `make api` | Regenerates Telegram API and exception modules. |
| `make typecheck` | Runs the configured `ty` type checker. |
| `make test-unit` | Runs the non-integration test suite, including guard tests, with coverage. |
| `make test-guards` | Runs repository-wide guard tests. |
| `make test` | Runs the full test suite, including integration tests. |

Run `make format` when formatting is needed, then run `make lint` again. Avoid formatting unrelated files.

### Integration tests

The integration suite can connect to real services and needs the relevant test configuration. Local values belong in the git-ignored `.env.test` file. Use `.env.test.example` to see which settings the suite expects.

Never commit real API credentials, Telegram session files, private endpoints, or personal data. Integration tests that do not have their required configuration are skipped by the test suite.

### Test placement

Place new tests in the directory that matches their purpose:

- `tests/unit/` for isolated behavior and module-level tests.
- `tests/guards/` for checks that enforce repository-wide rules.
- `tests/integrations/` for tests that communicate with Telegram or another live service.

Every test should belong to one of these test areas. Add or update tests whenever a change affects behavior.

### Dependency compatibility

The repository also provides two dependency-range checks:

```bash
make test-floor
make test-ceil
```

These test the lowest declared dependency versions and the newest compatible releases in separate environments. They are useful when changing dependency constraints or investigating compatibility issues. They do not replace the normal locked-environment checks.

## 5. Documentation

Documentation sources live in `docs/`. Generated API documentation is prepared by the documentation compiler.

Build the documentation:

```bash
make docs
```

Start the local documentation server with automatic rebuilds:

```bash
make docs-serve
```

When changing public behavior, update the relevant documentation and examples in the same pull request where practical. Keep examples consistent with the current `kirugram` import namespace.

## 6. Code quality and style

The project uses Ruff for linting and formatting, and `ty` for type checking. Their active rules are configured in `pyproject.toml`.

Please follow these conventions:

- Use modern built-in type annotations, such as `list[str]` and `int | None`.
- Add the repository's existing license header to new Python modules. Empty package `__init__.py` files are the exception where the surrounding package follows that pattern.
- Follow the module annotation conventions already used by the package, including `from __future__ import annotations as _annotations` where required.
- Prefer clear, specific exceptions for runtime validation. Do not rely on `assert` for checks that library users depend on.
- Keep public exports deliberate. When a module defines `__all__`, keep it complete and explicit.
- Add a short explanation to any `# noqa` or `# ty: ignore` suppression. Avoid adding suppressions simply to silence a new issue.
- Keep dependencies as broadly compatible as the project can safely support. If an upper version bound is necessary, explain the compatibility reason next to it.
- Use `Final` for module-level constants that are not meant to change.
- Avoid unrelated refactors, broad formatting changes, or speculative abstractions in a focused bug fix.

The repository contains guard tests for selected conventions. If a guard reports a violation, fix the underlying code rather than weakening the guard to make the check pass.

## 7. Commit messages

Use [Conventional Commits](https://www.conventionalcommits.org/) for commit messages. Include a scope that describes the affected area.

Examples:

```text
fix(session): handle reconnect timeout
feat(client): add message helper
docs(readme): clarify installation steps
test(filters): cover empty input
```

Keep the subject concise and describe the actual change.

## 8. Pull request checklist

Before requesting review, make sure that:

- [ ] The pull request addresses one main purpose.
- [ ] The description explains the problem and the chosen solution.
- [ ] Related issues are linked.
- [ ] Tests cover changed or newly added behavior.
- [ ] `make lint` passes.
- [ ] `make api` and `make typecheck` pass when generated API or typed code is involved.
- [ ] `make test-unit` passes.
- [ ] Documentation and examples are updated when needed.
- [ ] No credentials, session files, generated local artifacts, or unrelated changes are included.
- [ ] Commit messages follow Conventional Commits.
- [ ] Existing copyright and license notices remain intact.

A pull request may need changes before it can be merged. Please respond to review feedback and keep the discussion focused on the technical change.

## 9. Reporting bugs and requesting features

When reporting a bug, include:

- The Kirugram version or commit you are using.
- Your Python version and operating system.
- A short description of the expected and actual behavior.
- A minimal reproduction, traceback, or relevant test where possible.

Remove secrets and private account information from all logs before sharing them.

For feature requests, explain the use case and the behavior you would expect. This helps maintainers evaluate the change without guessing at the intended result.

## 10. Community and project identity

For project discussions and announcements, use the Kirugram community spaces:

- [Community chat](https://t.me/kirugram_chat)
- [News and announcements](https://t.me/kirugram_news)
- [GitHub issues](https://github.com/KIRU-OP/Kirugram/issues)

Kirugram is an independent community-maintained project. It is not affiliated with or endorsed by Telegram.

Thank you for helping make Kirugram better.
