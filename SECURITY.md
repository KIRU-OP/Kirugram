# Security Policy

## Supported versions

Security fixes are developed against the latest code on the `main` branch.
Older commits and unpublished development builds may not receive security fixes.
When a release is published, its support status will be stated in the release notes.

## Reporting a vulnerability

Please do not publish exploitable vulnerability details in a public issue.

Use GitHub's **Report a vulnerability** option in the repository's Security tab to send a private report, if it is available. Include:

- The affected Kirugram version or commit.
- The affected component and Python version.
- A concise description of the security impact.
- Reproduction steps or a minimal proof of concept, avoiding real credentials and private session data.
- Any suggested mitigation, if known.

Do not include Telegram API credentials, phone numbers, session strings, authorization keys, private chat data, or other secrets in a report.

## Response expectations

The maintainers will acknowledge reports when practical, investigate the affected code, and coordinate a fix and disclosure timeline with the reporter. No fixed response or resolution time is guaranteed.

Please allow maintainers time to investigate and prepare a fix before sharing vulnerability details publicly.

## Scope

Reports involving authentication, MTProto transport, cryptography, session storage, authorization, DC migration, update processing, dependency vulnerabilities, or release integrity are especially relevant.

Kirugram is derived from Kurigram/Pyrogram code. If a report also affects upstream projects or third-party dependencies, maintainers may coordinate with those projects.
