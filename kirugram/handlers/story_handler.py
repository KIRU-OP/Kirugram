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

from collections.abc import Callable
from typing import TYPE_CHECKING, Any

from kirugram import types

from .handler import Handler

if TYPE_CHECKING:
    import kirugram
    from kirugram.filters import Filter

StoryCallbackType = Callable[["kirugram.Client", types.Story], Any]


class StoryHandler(Handler[StoryCallbackType]):
    """The Story handler class. Used to handle new stories.
    It is intended to be used with :meth:`~kirugram.Client.add_handler`

    For a nicer way to register this handler, have a look at the
    :meth:`~kirugram.Client.on_story` decorator.

    Parameters:
        callback (``Callable``):
            Pass a function that will be called when a new Stories arrives. It takes *(client, story)*
            as positional arguments (look at the section below for a detailed description).

        filters (:obj:`~kirugram.filters.Filter`):
            Pass one or more filters to allow only a subset of stories to be passed
            in your callback function.

    Other parameters:
        client (:obj:`~kirugram.Client`):
            The Client itself, useful when you want to call other API methods inside the story handler.

        story (:obj:`~kirugram.types.Story`):
            The received story.
    """

    def __init__(self, callback: StoryCallbackType, filters: Filter | None = None) -> None:
        super().__init__(callback, filters)
