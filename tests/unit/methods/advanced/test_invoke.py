from __future__ import annotations

from typing import Any

import pytest

from kirugram.methods.advanced.invoke import Invoke


class RecordingSession:
    def __init__(self) -> None:
        self.kwargs: dict[str, Any] | None = None

    async def invoke(self, **kwargs: Any) -> object:
        self.kwargs = kwargs
        return object()


class InvokeClient:
    is_connected = True
    no_updates = False
    takeout_id = None
    retries = 5
    timeout = 20.0
    sleep_threshold = 10.0
    retry_delay = 1.0

    def __init__(self) -> None:
        self.session = RecordingSession()

    async def fetch_peers(self, peers: list[object]) -> None:
        pass

    async def get_session(self, **kwargs: Any) -> RecordingSession:
        return self.session


@pytest.mark.parametrize(
    ("explicit_retries", "expected"),
    [
        pytest.param(0, 0, id="explicitly-disable-retries"),
        pytest.param(2, 2, id="override-default"),
        pytest.param(None, 5, id="use-client-default"),
    ],
)
async def test_invoke_respects_explicit_retry_count(
    explicit_retries: int | None,
    expected: int,
) -> None:
    client = InvokeClient()

    await Invoke.invoke(client, object(), retries=explicit_retries)  # type: ignore[arg-type]

    assert client.session.kwargs is not None
    assert client.session.kwargs["retries"] == expected
