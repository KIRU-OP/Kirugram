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
from kirugram.file_id import FileType


class ReplaceStickerInSet:
    async def replace_sticker_in_set(
        self: kirugram.Client,
        user_id: int | str,
        old_sticker: str,
        sticker: types.InputSticker,
    ) -> types.StickerSet:
        """Use this method to replace an existing sticker in a sticker set with a new one.
        The method is equivalent to calling :meth:`kirugram.Client.delete_sticker_from_set`, then :meth:`kirugram.Client.add_sticker_to_set`, then :meth:`kirugram.Client.set_sticker_position_in_set`.

        .. include:: /_includes/usable-by/users-bots.rst

        Parameters:
            user_id (``int`` | ``str``):
               Unique identifier (int) or username (str) of sticker set owner.

            old_sticker (``str``):
                File identifier of the replaced sticker.

            sticker (:obj:`~kirugram.types.InputSticker`):
                Sticker to be replaced in the set.

        Returns:
            :obj:`~kirugram.types.StickerSet`: A updated sticker set is returned.
        """
        r = await self.invoke(
            raw.functions.stickers.ReplaceSticker(
                sticker=utils.get_input_media_from_file_id(
                    file_id=old_sticker, expected_file_type=FileType.STICKER
                ).id,
                new_sticker=await sticker.write(client=self, chat_id=user_id),
            )
        )

        return await types.StickerSet._parse(self, r)
