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


class ManagedBotCreated(Object):
    """This object contains information about the bot that was created to be managed by the current bot.

    Parameters:
        bot (:obj:`~kirugram.types.User`):
            Information about the bot.
            The bot's token can be fetched using the method :meth:`~kirugram.Client.get_managed_bot_token`.
    """

    def __init__(
        self,
        *,
        bot: types.User,
    ):
        super().__init__()

        self.bot = bot

    @staticmethod
    async def _parse(
        client: kirugram.Client,
        managed_bot_created: raw.types.MessageActionManagedBotCreated,
        users: dict[int, raw.types.User],
    ) -> ManagedBotCreated:
        if not isinstance(managed_bot_created, raw.types.MessageActionManagedBotCreated):
            return

        return ManagedBotCreated(
            bot=await types.User._parse(client, users.get(managed_bot_created.bot_id))
        )
