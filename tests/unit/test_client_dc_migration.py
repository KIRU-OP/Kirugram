#  Kirugram - Telegram MTProto API Client Library for Python
#
#  Copyright (C) 2017-present Dan <https://github.com/delivrance>
#  Copyright (C) 2024-present KurimuzonAkuma <https://github.com/KurimuzonAkuma>
#
#  This file is part of Kirugram.
#
#  Kirugram is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Kirugram is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with Kirugram. If not, see <https://www.gnu.org/licenses/>.

"""DC migration rollback tests without Telegram credentials or network access."""

from __future__ import annotations as _annotations

from types import SimpleNamespace

import pytest

from kirugram import Client


class MigrationStorage:
    """Storage double with the same getter/setter shape used by Client."""

    def __init__(self) -> None:
        self.values = {
            "dc_id": 2,
            "server_address": "149.154.167.51",
            "port": 443,
            "auth_key": b"old-auth-key",
        }
        self.failed_field: str | None = None
        self.failure_raised = False

    async def _access(self, field: str, value):
        if value is not None:
            if field == self.failed_field and not self.failure_raised:
                self.failure_raised = True
                raise OSError(f"cannot persist {field}")

            self.values[field] = value

        return self.values[field]

    async def dc_id(self, value: int | None = None) -> int:
        return await self._access("dc_id", value)

    async def server_address(self, value: str | None = None) -> str:
        return await self._access("server_address", value)

    async def port(self, value: int | None = None) -> int:
        return await self._access("port", value)

    async def auth_key(self, value: bytes | None = None) -> bytes:
        return await self._access("auth_key", value)


class FakeSession:
    def __init__(self, dc_id: int, auth_key: bytes, *, fail_stop: bool = False) -> None:
        self.dc_id = dc_id
        self.auth_key = auth_key
        self.fail_stop = fail_stop
        self.stop_calls = 0

    async def stop(self) -> None:
        self.stop_calls += 1
        if self.fail_stop:
            raise RuntimeError("transport cleanup failed")


@pytest.mark.parametrize(
    "failed_field",
    ["dc_id", "server_address", "port", "auth_key"],
)
async def test_dc_migration_rolls_back_each_storage_write_failure(
    monkeypatch: pytest.MonkeyPatch,
    *,
    failed_field: str,
) -> None:
    client = Client("dc_migration_rollback", in_memory=True)
    storage = MigrationStorage()
    storage.failed_field = failed_field

    old_values = dict(storage.values)
    old_session = FakeSession(2, b"old-auth-key")
    migrated_session = FakeSession(3, b"new-auth-key")

    async def get_dc_option(dc_id: int, **kwargs) -> SimpleNamespace:
        assert dc_id == 3
        return SimpleNamespace(ip_address="149.154.167.91", port=8443)

    async def get_session(**kwargs) -> FakeSession:
        assert kwargs == {
            "dc_id": 3,
            "server_address": "149.154.167.91",
            "port": 8443,
            "export_authorization": False,
            "temporary": True,
        }
        return migrated_session

    client.storage = storage
    client.session = old_session
    client.sessions = {2: old_session}
    monkeypatch.setattr(client, "get_dc_option", get_dc_option)
    monkeypatch.setattr(client, "get_session", get_session)

    with pytest.raises(OSError, match=f"cannot persist {failed_field}"):
        await client._migrate_to_dc(3)

    assert storage.failure_raised
    assert storage.values == old_values
    assert client.session is old_session
    assert client.sessions == {2: old_session}
    assert old_session.stop_calls == 0
    assert migrated_session.stop_calls == 1


async def test_dc_migration_preserves_storage_error_when_new_session_cleanup_fails(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    client = Client("dc_migration_cleanup_failure", in_memory=True)
    storage = MigrationStorage()
    storage.failed_field = "auth_key"

    old_session = FakeSession(2, b"old-auth-key")
    migrated_session = FakeSession(3, b"new-auth-key", fail_stop=True)

    async def get_dc_option(dc_id: int, **kwargs) -> SimpleNamespace:
        return SimpleNamespace(ip_address="149.154.167.91", port=443)

    async def get_session(**kwargs) -> FakeSession:
        return migrated_session

    client.storage = storage
    client.session = old_session
    client.sessions = {2: old_session}
    monkeypatch.setattr(client, "get_dc_option", get_dc_option)
    monkeypatch.setattr(client, "get_session", get_session)

    with pytest.raises(OSError, match="cannot persist auth_key"):
        await client._migrate_to_dc(3)

    assert storage.values == {
        "dc_id": 2,
        "server_address": "149.154.167.51",
        "port": 443,
        "auth_key": b"old-auth-key",
    }
    assert client.session is old_session
    assert client.sessions == {2: old_session}
    assert old_session.stop_calls == 0
    assert migrated_session.stop_calls == 1
