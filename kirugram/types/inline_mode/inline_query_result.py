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

from typing import TYPE_CHECKING
from uuid import uuid4

from ..object import Object

if TYPE_CHECKING:
    import kirugram
    from kirugram import types


class InlineQueryResult(Object):
    """One result of an inline query.

    - :obj:`~kirugram.types.InlineQueryResultCachedAudio`
    - :obj:`~kirugram.types.InlineQueryResultCachedDocument`
    - :obj:`~kirugram.types.InlineQueryResultCachedAnimation`
    - :obj:`~kirugram.types.InlineQueryResultCachedPhoto`
    - :obj:`~kirugram.types.InlineQueryResultCachedSticker`
    - :obj:`~kirugram.types.InlineQueryResultCachedVideo`
    - :obj:`~kirugram.types.InlineQueryResultCachedVoice`
    - :obj:`~kirugram.types.InlineQueryResultArticle`
    - :obj:`~kirugram.types.InlineQueryResultAudio`
    - :obj:`~kirugram.types.InlineQueryResultContact`
    - :obj:`~kirugram.types.InlineQueryResultDocument`
    - :obj:`~kirugram.types.InlineQueryResultAnimation`
    - :obj:`~kirugram.types.InlineQueryResultLocation`
    - :obj:`~kirugram.types.InlineQueryResultPhoto`
    - :obj:`~kirugram.types.InlineQueryResultVenue`
    - :obj:`~kirugram.types.InlineQueryResultVideo`
    - :obj:`~kirugram.types.InlineQueryResultVoice`
    """

    def __init__(
        self,
        type: str,
        id: str,
        input_message_content: types.InputMessageContent,
        reply_markup: types.InlineKeyboardMarkup,
    ):
        super().__init__()

        self.type = type
        self.id = str(uuid4()) if id is None else str(id)
        self.input_message_content = input_message_content
        self.reply_markup = reply_markup

    async def write(self, client: kirugram.Client):
        pass
