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
from kirugram import enums, raw, types, utils


class OpenWebApp:
    async def open_web_app(
        self: kirugram.Client,
        chat_id: int | str,
        bot_user_id: int | str,
        url: str | None = None,
        message_thread_id: int | None = None,
        direct_messages_topic_id: int | None = None,
        reply_parameters: types.ReplyParameters | None = None,
        platform: enums.ClientPlatform | None = None,
    ) -> str:
        """Informs kirugram that a Web App is being opened from the attachment menu,
        a :obj:`~kirugram.types.MenuButton`, an url,
        or an :obj:`~kirugram.types.InlineKeyboardButton` button.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.

            bot_user_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target bot.

            url (``str``, *optional*):
                The URL from an :obj:`~kirugram.types.InlineKeyboardButton` or a :obj:`~kirugram.types.MenuButton`.

            message_thread_id (``int``, *optional*):
                If not None, the message thread identifier to which the message will be sent.

            direct_messages_topic_id (``int``, *optional*):
                If not None, unique identifier of the topic of channel direct messages chat to which the message will be sent.

            reply_parameters (:obj:`~kirugram.types.ReplyParameters`, *optional*):
                Information about the message or story to be replied in the message sent by the Web App.

            platform (:obj:`~kirugram.enums.ClientPlatform`, *optional*):
                The platform on which the link will be opened.

        Returns:
            ``str``: On success, returns the url of a Web App.

        Example:
            .. code-block:: python

                link = await app.open_web_app(chat_id, bot_user_id)
        """
        if platform is None:
            platform = self.client_platform

        r = await self.invoke(
            raw.functions.messages.RequestWebView(
                peer=await self.resolve_peer(chat_id),
                bot=await self.resolve_peer(bot_user_id),
                platform=platform.value,
                from_bot_menu=True if url is None else None,
                url=url,
                reply_to=await utils.get_reply_to(
                    client=self,
                    reply_parameters=reply_parameters,
                    message_thread_id=message_thread_id,
                    direct_messages_topic_id=direct_messages_topic_id,
                ),
            )
        )

        return r.url
