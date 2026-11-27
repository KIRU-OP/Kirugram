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


class RemoveProfileAudio:
    async def remove_profile_audio(self: kirugram.Client, file_id: str) -> bool:
        """Removes an audio file from the profile audio files of the current user.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            file_id (``str``):
                Identifier of the audio file to be removed.

        Returns:
            ``bool``: On success, True is returned.

        Example:
            .. code-block:: python

                # Remove audio file from profile
                await app.remove_profile_audio(file_id)
        """
        r = await self.invoke(
            raw.functions.account.SaveMusic(
                id=(utils.get_input_media_from_file_id(file_id, FileType.AUDIO)).id, unsave=True
            )
        )

        return r
