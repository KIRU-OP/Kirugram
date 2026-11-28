# MTProto Authentication and Session Audit

## Scope

This is a source-level maintenance review of the current `main` branch. It is not a penetration test, a cryptographic verification, or a claim that every runtime path has been exercised.

Reviewed components:

- `kirugram/session/auth.py` — MTProto authorization-key exchange.
- `kirugram/session/session.py` — encrypted session transport and lifecycle.
- `kirugram/client.py` — session creation, authorization import, and DC migration.
- `kirugram/storage/storage.py` and `kirugram/storage/sqlite_storage.py` — persisted credentials and session strings.
- `kirugram/connection/connection.py` — DC-specific transport parameters.

## Findings and follow-up

### 1. Validate server DH parameters before expensive or state-changing operations

**Priority: hardening recommendation; requires a focused code change and regression tests.**

In `Auth.create()`, the current sequence parses the server DH parameters, calculates `g_b`, sends `SetClientDHParams`, calculates the authorization key from `g_a`, and only then performs the DH range, fixed-prime, hash, and nonce checks.

The same ordering is present in the reviewed upstream Kurigram `pyrogram/session/auth.py` implementation. This review therefore does not classify it as a Kirugram-only regression.

Before changing this security-critical handshake, prepare tests proving that invalid DH parameters are rejected before modular exponentiation and before `SetClientDHParams` is sent. Preserve Telegram's documented parameter, hash, and nonce checks. Do not weaken or remove any existing checks. Validate against Telegram's current MTProto security guidance and upstream behavior.

### 2. Session strings are credentials, not encrypted backups

**Priority: documentation and operational handling.**

`Storage.export_session_string()` packs the DC, API ID, test-mode flag, 256-byte authorization key, user ID, and bot flag, then URL-safe-base64 encodes the result. Base64 is an encoding, not encryption. Anyone obtaining a valid session string may be able to reuse the account authorization represented by it.

Treat session strings and SQLite session files as secrets:
- Never paste them into issues, logs, screenshots, CI output, or chat.
- Keep session files out of source control and public artifacts.
- Restrict filesystem and backup access.
- Rotate/revoke the affected Telegram authorization if a session string is exposed.

### 3. DC migration has explicit rollback and cleanup paths

**Priority: add focused regression tests.**

`Client._migrate_to_dc()` captures the prior DC ID, server address, port, and auth key; creates a temporary session for the target DC; persists the new values; then swaps the active session and stops stale sessions. If persistence fails, it attempts to restore the previous values and stop the new session.

`Client.get_session()` also removes a partially initialized cached session and attempts to stop it if startup or authorization import fails.

These are useful safeguards, but source inspection alone cannot establish that every cancellation, storage failure, failed stop, or concurrent migration interleaving is safe. Add deterministic tests for:
- target session startup failure;
- storage write failure at each migration field;
- authorization import failure;
- cancellation during migration;
- cleanup failure while preserving the original exception;
- repeated or concurrent migration requests.

Tests should use fake sessions and storage; they must not require real Telegram credentials.

### 4. Session shutdown and restart need lifecycle regression coverage

**Priority: add deterministic tests.**

`Session` tracks pending tasks, fails pending request waiters when stopping, and serializes restart operations with a lock. These safeguards are security- and reliability-sensitive because stale tasks must not continue using a stopped transport.

Add tests for stop during connect/start, stop during restart, pending request cancellation, worker failure, and repeated stop/restart calls. Assert that no task or transport is left running after the operation completes.

## Upstream comparison

The reviewed MTProto DH parameter-check ordering in Kirugram's `auth.py` matches the corresponding upstream Kurigram file at the time of review. No change to the handshake was made in this audit PR. A future fix should be proposed with tests and reviewed as a protocol change, not applied as a cosmetic refactor.

## Validation status

- Source-level inspection completed for the files listed above.
- Compared the authorization DH-check ordering with upstream Kurigram.
- Existing gap-recovery tests were inspected separately.
- No local test suite or live Telegram login was run as part of this source review.
- This document records review findings and follow-up work; it is not a security certification.
