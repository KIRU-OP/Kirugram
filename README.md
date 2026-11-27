<!--
  Kirugram — Telegram MTProto API framework for Python
  Community-maintained rebrand of Kurigram.
  Original copyright notices and LGPL-3.0-or-later terms are preserved.
-->

<p align="center">
  <a href="https://github.com/KIRU-OP/Kirugram">
    <img src="https://raw.githubusercontent.com/kurigram-org/artwork/master/kurigram_logo_github.png" width="128" alt="Kirugram project artwork">
  </a>
</p>

<h1 align="center">Kirugram</h1>

<p align="center">
  <strong>Telegram MTProto API Framework for Python</strong>
  <br>
  A community-maintained rebrand of Kurigram, built on the Pyrogram project lineage.
</p>

<p align="center">
  <a href="https://github.com/KIRU-OP/Kirugram/actions/workflows/python.yml">
    <img src="https://img.shields.io/github/actions/workflow/status/KIRU-OP/Kirugram/python.yml?branch=main&label=tests&logo=github" alt="Python workflow status">
  </a>
  <a href="https://github.com/KIRU-OP/Kirugram/blob/main/COPYING">
    <img src="https://img.shields.io/github/license/KIRU-OP/Kirugram?color=blue" alt="LGPL-3.0-or-later license">
  </a>
  <a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/python-3.10%2B-3776AB?logo=python&logoColor=white" alt="Python 3.10 and newer">
  </a>
  <a href="https://github.com/KIRU-OP/Kirugram">
    <img src="https://img.shields.io/github/stars/KIRU-OP/Kirugram?style=social" alt="GitHub stars">
  </a>
</p>

<p align="center">
  <a href="#overview">Overview</a> ·
  <a href="#features">Features</a> ·
  <a href="#installation">Installation</a> ·
  <a href="#quick-start">Quick start</a> ·
  <a href="#migration-from-kurigram">Migration</a> ·
  <a href="#development">Development</a> ·
  <a href="#license-and-attribution">License</a>
</p>

---

## Overview

**Kirugram** is an asynchronous Python framework for working with Telegram's MTProto API. It provides a high-level interface for building Telegram clients and bot applications while retaining access to lower-level Telegram API functionality.

This repository is a **community-maintained rebrand of Kurigram**, which is itself part of the Pyrogram project lineage. Kirugram establishes a distinct project identity under **KIRU-OP** and uses the dedicated Python import namespace:

```python
from kirugram import Client, filters
```

The rebrand does not claim original authorship of Pyrogram or Kurigram, nor does it imply that the underlying implementation was independently rewritten. Upstream copyright notices, attribution and applicable license terms are retained.

## Features

- **Telegram MTProto API** — interact with Telegram through its MTProto client interface.
- **User and bot sessions** — build applications around user accounts or bot identities.
- **Asynchronous design** — write non-blocking applications with Python's async and await syntax.
- **Convenient handlers and filters** — organize incoming updates with a readable event-handling API.
- **Typed interfaces** — benefit from type hints and editor assistance.
- **Low-level access** — use the exposed raw API types and functions when higher-level helpers are not enough.
- **Optional performance dependencies** — install Kuricrypt and uvloop through the fast extra where supported.
- **QR-code login support** — use the optional qrcode extra for QR-based authorization functionality.

## Installation

Kirugram requires **Python 3.10 or newer**.

### Install from the Python package index

```bash
python -m pip install kirugram
```

### Install the latest source from GitHub

```bash
python -m pip install "https://github.com/KIRU-OP/Kirugram/archive/refs/heads/main.zip"
```

### Optional dependencies

Install optional performance dependencies:

```bash
python -m pip install "kirugram[fast]"
```

Install QR-code login dependencies:

```bash
python -m pip install "kirugram[qrcode]"
```

> Optional extras are not required for a basic installation. The fast extra includes Kuricrypt and, on supported platforms, uvloop.

## Quick start

The following example creates a client, registers a private-message handler and starts the application.

```python
from kirugram import Client, filters

app = Client("my_account")


@app.on_message(filters.private)
async def hello(client, message):
    await message.reply_text("Hello from Kirugram!")


app.run()
```

For production applications, consult the relevant Telegram API requirements and the framework's source and examples before configuring authentication, sessions or deployment.

## Core concepts

| Component | Purpose |
| --- | --- |
| `Client` | Creates and manages a Telegram client session. |
| `filters` | Selects updates that match handler conditions. |
| `handlers` | Defines how incoming updates are processed. |
| `types` | Provides Telegram objects used by the high-level API. |
| `raw` | Exposes lower-level MTProto API functions and types. |
| `enums` | Provides enumerations used throughout the library. |

## Migration from Kurigram

Kirugram introduces a dedicated import namespace. Existing applications that import the library through the previous namespace should update their imports when moving to the Kirugram package.

**Before:**

```python
from pyrogram import Client, filters
```

**After:**

```python
from kirugram import Client, filters
```

Review your dependency declarations and deployment environment as part of the migration. Test your application's authentication, handlers, session storage and integrations before deploying the migrated version.

The namespace and distribution name are different from the upstream project. Do not install both distributions into the same environment without checking for overlapping files and dependencies.

## Compatibility and project status

Kirugram follows the existing Kurigram implementation and aims to preserve its API behavior while maintaining a separate project identity and import namespace.

- **Python:** 3.10+
- **Import package:** `kirugram`
- **Distribution:** `kirugram`
- **Source branch:** `main`
- **License:** LGPL-3.0-or-later

Compatibility with a particular upstream release, Telegram API change or third-party integration should be verified against the current source and tests. The rebrand alone is not a guarantee of compatibility with every existing application.

## Development

Contributions, bug reports and improvements are welcome.

### Get the source

```bash
git clone https://github.com/KIRU-OP/Kirugram.git
cd Kirugram
```

### Set up a development environment

The repository uses a `pyproject.toml` configuration and a `uv.lock` lockfile. With uv installed, sync the development dependencies:

```bash
uv sync
```

You can also install the project in editable mode in an appropriately prepared Python environment:

```bash
python -m pip install -e .
```

### Run tests

```bash
uv run pytest
```

Please run the relevant tests before submitting a change. See [CONTRIBUTING.md](CONTRIBUTING.md) for contribution guidelines and repository conventions.

## Reporting issues

Before opening an issue:

1. Check whether the issue has already been reported.
2. Include the Python version and Kirugram version.
3. Provide a minimal reproducible example where possible.
4. Remove API credentials, session files, phone numbers and other private information from logs.

Use the [GitHub issue tracker](https://github.com/KIRU-OP/Kirugram/issues) to report bugs or request improvements.

## Project lineage and attribution

Kirugram acknowledges the projects and maintainers whose work forms its technical foundation:

- **Pyrogram** — the original project lineage and foundational work.
- **Kurigram** — the upstream project from which this repository is rebranded.
- **Kuricrypt** — the optional Rust-based cryptography dependency used by the fast extra.
- **Open-source contributors** — everyone whose work, reviews and reports help improve the ecosystem.

Kirugram is maintained as a community rebrand under the KIRU-OP repository. It is not an official Telegram project and is not affiliated with or endorsed by Telegram.

## License and attribution

Kirugram is distributed under the **GNU Lesser General Public License v3.0 or later (LGPL-3.0-or-later)**.

Original copyright holders retain their respective rights. Existing copyright headers, notices and license files are preserved. The repository includes the applicable license texts and attribution in:

- [COPYING](COPYING)
- [COPYING.lesser](COPYING.lesser)
- [NOTICE](NOTICE)

When using, modifying or redistributing this project, review these files and comply with the license terms.

---

<p align="center">
  <strong>Kirugram</strong>
  <br>
  A dedicated identity for the next chapter of this project lineage.
  <br><br>
  Maintained by <a href="https://github.com/KIRU-OP">KIRU-OP</a>
  <br>
  <a href="https://github.com/KIRU-OP/Kirugram">GitHub Repository</a>
  ·
  <a href="https://github.com/KIRU-OP/Kirugram/issues">Issues</a>
</p>
