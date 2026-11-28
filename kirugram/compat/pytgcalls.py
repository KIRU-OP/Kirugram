"""PyTgCalls compatibility for Kirugram clients.

This adapter keeps Pyrogram-compatibility details inside Kirugram rather than
requiring every application to monkey-patch PyTgCalls itself.
"""
from __future__ import annotations

import importlib
import importlib.util
import sys


_MODULES = (
    "errors",
    "raw.base",
    "raw.functions.auth",
    "raw.functions.channels",
    "raw.functions.messages",
    "raw.functions.phone",
    "raw.functions.updates",
    "raw.functions.upload",
    "raw.types",
    "raw.types.messages",
    "session",
)


def install() -> bool:
    """Install PyTgCalls' expected Pyrogram module aliases for Kirugram.

    Returns False when PyTgCalls is not installed; importing Kirugram remains
    supported without the optional voice-chat integration.
    """
    try:
        if importlib.util.find_spec("pytgcalls") is None:
            return False
    except (ImportError, ValueError):
        return False

    # Load Kirugram's equivalents before PyTgCalls imports its Pyrogram bridge.
    for module_name in _MODULES:
        importlib.import_module(f"kirugram.{module_name}")

    for module_name, module in tuple(sys.modules.items()):
        if module_name == "kirugram" or module_name.startswith("kirugram."):
            sys.modules["pyrogram" + module_name[len("kirugram"):]] = module

    try:
        from pytgcalls.mtproto.bridged_client import BridgedClient
    except ImportError:
        return False

    original_package_name = BridgedClient.package_name

    def package_name(client):
        if client.__class__.__module__.split(".", 1)[0] == "kirugram":
            return "pyrogram"
        return original_package_name(client)

    BridgedClient.package_name = staticmethod(package_name)
    return True
