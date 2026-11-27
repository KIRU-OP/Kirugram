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
from kirugram import raw, utils
from kirugram.file_id import FileType


class RemoveRecentSticker:
    async def remove_recent_sticker(
        self: kirugram.Client,
        sticker: str,
        is_attached: bool | None = None,
    ) -> bool:
        """Removes a sticker from the list of recently used stickers.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            sticker (``str``):
                File identifier of the sticker.

            is_attached (``bool``, *optional*):
                Pass *True* to remove the sticker from the list of stickers recently attached to photo or video files.
                Pass *False* to remove the sticker from the list of recently sent stickers.

        Returns:
            ``bool``: True, on success.
        """
        r = await self.invoke(
            raw.functions.messages.SaveRecentSticker(
                id=utils.get_input_media_from_file_id(
                    file_id=sticker, expected_file_type=FileType.STICKER
                ).id,
                unsave=True,
                attached=is_attached,
            )
        )

        return bool(r)
