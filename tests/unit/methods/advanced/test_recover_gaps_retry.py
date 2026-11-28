from __future__ import annotations

import asyncio

import pytest

from kirugram.errors import PersistentTimestampInvalid, PersistentTimestampOutdated
from kirugram.methods.advanced.recover_gaps import RecoverGaps


class TimestampRetryProbe(RecoverGaps):
    def __init__(self, error: type[Exception], failures: int) -> None:
        self.error = error
        self.failures = failures
        self.calls = 0

    async def invoke(self, request):
        self.calls += 1
        if self.calls <= self.failures:
            raise self.error()
        return "recovered"


@pytest.mark.parametrize(
    "error",
    [PersistentTimestampOutdated, PersistentTimestampInvalid],
    ids=["outdated", "invalid"],
)
async def test_difference_retry_handles_both_timestamp_error_variants(
    monkeypatch: pytest.MonkeyPatch,
    *,
    error: type[Exception],
) -> None:
    delays: list[float] = []

    async def record_sleep(delay: float) -> None:
        delays.append(delay)

    monkeypatch.setattr(asyncio, "sleep", record_sleep)
    probe = TimestampRetryProbe(error, failures=2)

    result = await probe._invoke_difference(object(), state_id=42)

    assert result == "recovered"
    assert probe.calls == 3
    assert delays == [
        probe.TIMESTAMP_RETRY_DELAY,
        probe.TIMESTAMP_RETRY_DELAY * 2,
    ]


@pytest.mark.parametrize(
    "error",
    [PersistentTimestampOutdated, PersistentTimestampInvalid],
    ids=["outdated", "invalid"],
)
async def test_difference_retry_is_bounded_for_both_timestamp_errors(
    monkeypatch: pytest.MonkeyPatch,
    *,
    error: type[Exception],
) -> None:
    delays: list[float] = []

    async def record_sleep(delay: float) -> None:
        delays.append(delay)

    monkeypatch.setattr(asyncio, "sleep", record_sleep)
    probe = TimestampRetryProbe(error, failures=99)

    with pytest.raises(error):
        await probe._invoke_difference(object(), state_id=7)

    assert probe.calls == probe.MAX_TIMESTAMP_RETRIES + 1
    assert len(delays) == probe.MAX_TIMESTAMP_RETRIES
    assert delays == [
        probe.TIMESTAMP_RETRY_DELAY * (2**attempt)
        for attempt in range(probe.MAX_TIMESTAMP_RETRIES)
    ]


async def test_difference_retry_propagates_cancellation_during_backoff(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    sleep_started = asyncio.Event()

    async def cancel_during_sleep(delay: float) -> None:
        sleep_started.set()
        raise asyncio.CancelledError

    monkeypatch.setattr(asyncio, "sleep", cancel_during_sleep)
    probe = TimestampRetryProbe(PersistentTimestampInvalid, failures=99)

    with pytest.raises(asyncio.CancelledError):
        await probe._invoke_difference(object(), state_id=9)

    assert probe.calls == 1
    assert sleep_started.is_set()
