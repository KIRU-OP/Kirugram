#  Kirugram - Telegram MTProto API Client Library for Python
#  Copyright (C) 2017-present Dan <https://github.com/delivrance>
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
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with Kirugram.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import annotations as _annotations

import kirugram
from kirugram import raw, types, utils

from ..object import Object


class ProximityAlertTriggered(Object):
    """Information about a proximity alert.

    Parameters:
        traveler (:obj:`~kirugram.types.Chat`):
            User or channel that triggered the proximity alert, or ``None`` when the update does
            not include it.

        watcher (:obj:`~kirugram.types.Chat`):
            User or channel that subscribed for the proximity alert, or ``None`` when the update
            does not include it.

        distance (``int``):
            The distance between the two sides, in meters.
    """

    def __init__(
        self,
        *,
        traveler: kirugram.types.Chat | None,
        watcher: kirugram.types.Chat | None,
        distance: int,
    ) -> None:
        super().__init__()

        self.traveler = traveler
        self.watcher = watcher
        self.distance = distance

    @staticmethod
    async def _parse(
        client: kirugram.Client,
        action: raw.types.MessageActionGeoProximityReached,
        users: dict[int, raw.base.User],
        chats: dict[int, raw.base.Chat],
    ) -> ProximityAlertTriggered:
        from_id = utils.get_raw_peer_id(action.from_id)
        to_id = utils.get_raw_peer_id(action.to_id)

        return ProximityAlertTriggered(
            traveler=await types.Chat._parse_chat(client, users.get(from_id) or chats.get(from_id)),
            watcher=await types.Chat._parse_chat(client, users.get(to_id) or chats.get(to_id)),
            distance=action.distance,
        )
