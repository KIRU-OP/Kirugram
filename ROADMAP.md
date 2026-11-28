# Kirugram Engineering Roadmap

Kirugram's long-term goal is to be a dependable, developer-first Python framework for building Telegram clients, bots, and automation. It communicates with Telegram through Telegram's documented MTProto and Bot API interfaces. Kirugram is an independent community-maintained project; it is not an official Telegram service and has no private or privileged access to Telegram's internal infrastructure.

This roadmap describes intended work, not features that are already shipped. A roadmap item is complete only when its implementation, tests, documentation, and compatibility notes are merged.

## Design principles

- **Protocol-first:** keep Telegram MTProto transport, authorization, session, update, and RPC behavior correct and testable.
- **Reliable by default:** bounded retries, clear timeout behavior, safe reconnects, and useful diagnostics; never hide permanent authentication or permission errors behind endless retries.
- **Developer-friendly:** stable public APIs, type hints, predictable exceptions, examples, and migration guides.
- **Secure sessions:** protect API credentials and authorization keys; never log session secrets, login codes, passwords, or tokens.
- **Compatibility with attribution:** preserve upstream notices and comply with the license of every inherited or third-party file.
- **No false affiliation:** do not imply Telegram endorsement, private server access, or guaranteed availability.

## Workstreams

### 1. MTProto core and transport

- Maintain the Telegram TL schema and generated raw API layer.
- Validate abridged, intermediate, padded-intermediate, and supported proxy transports against protocol fixtures.
- Add deterministic tests for connection lifecycle, partial reads/writes, timeouts, and transport shutdown.
- Keep data-center configuration current from supported Telegram configuration responses; avoid hard-coded assumptions about a single DC.
- Test DC migration and authorization export/import flows with mocked protocol responses.

### 2. Authentication and session reliability

- Cover user and bot authorization flows, QR login, 2FA, expired codes, and revoked sessions.
- Make session state transitions explicit and race-safe.
- Test reconnect behavior, DC migration, auth-key duplication, server salt refresh, and recovery after transient network failures.
- Use bounded exponential backoff with jitter for retryable transport failures; respect Telegram flood-wait responses and do not retry non-retryable errors blindly.
- Document secure session storage, backup, revocation, and deployment practices.

### 3. Updates and RPC engine

- Test update gap recovery, ordering, duplicate handling, acknowledgements, and graceful shutdown.
- Standardize RPC error mapping and expose actionable error context without leaking secrets.
- Add observability hooks for connection state, retries, RPC latency, and update lag, disabled or privacy-preserving by default.
- Keep raw MTProto access available while maintaining convenient high-level methods.

### 4. Media and voice integrations

- Test upload/download integrity, CDN redirects, file references, and large-file handling.
- Keep voice-chat calling support in a clearly separated optional integration layer (for example, compatible call libraries); do not claim the MTProto client alone provides a complete voice-chat stack.
- Publish tested dependency/version combinations for optional integrations.

### 5. Public developer experience

- Provide a stable kirugram import namespace and documented package installation.
- Publish quick-start guides for bots, user clients, handlers, raw API calls, sessions, proxies, and deployment.
- Add runnable examples and a compatibility matrix for supported Python versions and optional dependencies.
- Establish semantic versioning, changelog discipline, deprecation policy, and reproducible release workflows.
- Add a support policy that distinguishes verified features from experimental ones.

## Release gates

A feature is not advertised as stable until:

1. Unit tests cover success, failure, cancellation, and concurrency paths.
2. Protocol behavior is checked against Telegram's current documentation and fixtures.
3. CI passes on the supported Python versions.
4. Documentation and migration notes are included.
5. Security and licensing implications are reviewed.

## What Kirugram cannot promise

- It cannot connect to Telegram's private internal systems or bypass Telegram authorization.
- It cannot guarantee that Telegram will never change its protocol, impose rate limits, restrict an account, or make a service unavailable.
- It cannot make every third-party bot framework or voice-chat package compatible without explicit integration and testing.

## Current status

This is a planning document. Items above must not be described as implemented solely because they appear here. Track implementation through issues and merged pull requests in this repository.
