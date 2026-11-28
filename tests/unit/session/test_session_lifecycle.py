from __future__ import annotations

import asyncio

import pytest

from kirugram import Client
from kirugram.session.session import Result, Session, SessionState


class FakeConnection:
    def __init__(self) -> None:
        self.close_calls = 0

    async def close(self) -> None:
        self.close_calls += 1


async def test_stop_fails_pending_waiters_and_drains_tracked_tasks(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(Session, "STOP_TIMEOUT", 0)
    client = Client("session_stop_lifecycle", in_memory=True)
    session = Session(
        client,
        dc_id=2,
        server_address="149.154.167.51",
        port=443,
        auth_key=b"test-auth-key",
        test_mode=False,
    )
    connection = FakeConnection()
    session.connection = connection
    await session._set_state(SessionState.STARTED)
    session.is_started.set()

    waiter = Result()
    session.results[123] = waiter

    never_finish = asyncio.Event()
    tracked_task = session._create_tracked_task(never_finish.wait())

    await session.stop()

    assert session.state is SessionState.STOPPED
    assert session._must_stay_stopped is True
    assert session.is_started.is_set() is False
    assert waiter.event.is_set()
    assert isinstance(waiter.exception, TimeoutError)
    assert session.results == {}
    assert tracked_task.cancelled()
    assert session.pending_tasks == set()
    assert connection.close_calls == 1


async def test_stop_is_idempotent_after_the_session_is_stopped() -> None:
    client = Client("session_stop_idempotent", in_memory=True)
    session = Session(
        client,
        dc_id=2,
        server_address="149.154.167.51",
        port=443,
        auth_key=b"test-auth-key",
        test_mode=False,
    )
    connection = FakeConnection()
    session.connection = connection

    await session.stop()
    await session.stop()

    assert session.state is SessionState.STOPPED
    assert connection.close_calls == 0


async def test_restart_does_not_reopen_a_session_after_stop_was_requested(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    client = Client("session_restart_after_stop", in_memory=True)
    session = Session(
        client,
        dc_id=2,
        server_address="149.154.167.51",
        port=443,
        auth_key=b"test-auth-key",
        test_mode=False,
    )
    start_calls = 0

    async def unexpected_start() -> None:
        nonlocal start_calls
        start_calls += 1

    monkeypatch.setattr(session, "start", unexpected_start)

    await session.stop()
    await session.restart()

    assert start_calls == 0
    assert session.state is SessionState.STOPPED
    assert session._must_stay_stopped is True
