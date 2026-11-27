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
from kirugram import raw, types

from ..object import Object
from ..update import Update


class ManagedBotUpdated(Object, Update):
    """This object contains information about the creation or token update of a bot that is managed by the current bot.

    Parameters:
        user (:obj:`~kirugram.types.User`):
            User that created the bot.

        bot (:obj:`~kirugram.types.User`):
            Information about the bot.
            Token of the bot can be fetched using the method :meth:`~kirugram.Client.get_managed_bot_token`.
    """

    def __init__(
        self,
        *,
        user: types.User,
        bot: types.User,
    ):
        super().__init__()

        self.user = user
        self.bot = bot

    @staticmethod
    async def _parse(
        client: kirugram.Client,
        managed_bot_updated: raw.types.UpdateManagedBot,
        users: dict[int, raw.types.User],
    ) -> ManagedBotUpdated:
        if not isinstance(managed_bot_updated, raw.types.UpdateManagedBot):
            return

        return ManagedBotUpdated(
            user=await types.User._parse(client, users.get(managed_bot_updated.user_id)),
            bot=await types.User._parse(client, users.get(managed_bot_updated.bot_id)),
        )
