from __future__ import annotations

import asyncio

import pytest

from kirugram.errors import PersistentTimestampOutdated
from kirugram.methods.advanced.recover_gaps import RecoverGaps


class RetryProbe(RecoverGaps):
    def __init__(self, failures: int) -> None:
        self.failures = failures
        self.calls = 0

    async def invoke(self, request):
        self.calls += 1
        if self.calls <= self.failures:
            raise PersistentTimestampOutdated
        return "recovered"


@pytest.mark.asyncio
async def test_difference_retry_recovers_after_transient_timestamp_errors(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    async def no_sleep(delay: float) -> None:
        pass

    monkeypatch.setattr(asyncio, "sleep", no_sleep)
    probe = RetryProbe(failures=2)

    result = await probe._invoke_difference(object(), state_id=0)

    assert result == "recovered"
    assert probe.calls == 3


@pytest.mark.asyncio
async def test_difference_retry_stops_after_bounded_attempts(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    async def no_sleep(delay: float) -> None:
        pass

    monkeypatch.setattr(asyncio, "sleep", no_sleep)
    probe = RetryProbe(failures=99)

    with pytest.raises(PersistentTimestampOutdated):
        await probe._invoke_difference(object(), state_id=0)

    assert probe.calls == probe.MAX_TIMESTAMP_RETRIES + 1


class SerializedRecovery(RecoverGaps):
    def __init__(self) -> None:
        self.recover_gaps_lock = asyncio.Lock()
        self.active = 0
        self.max_active = 0

    async def _recover_gaps(self, ids=None) -> tuple[int, int]:
        self.active += 1
        self.max_active = max(self.max_active, self.active)
        await asyncio.sleep(0)
        self.active -= 1
        return (0, 0)


@pytest.mark.asyncio
async def test_concurrent_gap_recovery_requests_are_serialized() -> None:
    recovery = SerializedRecovery()

    await asyncio.gather(
        recovery.recover_gaps(),
        recovery.recover_gaps(),
        recovery.recover_gaps(),
    )

    assert recovery.max_active == 1
