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

MessageReactionCountCallbackType = Callable[
    ["kirugram.Client", types.MessageReactionCountUpdated], Any
]


class MessageReactionCountHandler(Handler[MessageReactionCountCallbackType]):
    """The MessageReactionCount handler class.
    Used to handle changes in the anonymous reaction of a message.

    It is intended to be used with :meth:`~kirugram.Client.add_handler`.

    For a nicer way to register this handler, have a look at the
    :meth:`~kirugram.Client.on_message_reaction_count` decorator.

    Parameters:
        callback (``Callable``):
            Pass a function that will be called when a new MessageReactionCount event arrives. It takes
            *(client, reactions)* as positional arguments (look at the section below for a detailed
            description).

        filters (:obj:`~kirugram.filters.Filter`):
            Pass one or more filters to allow only a subset of updates to be passed in your callback function.

    Other parameters:
        client (:obj:`~kirugram.Client`):
            The Client itself, useful when you want to call other API methods inside the handler.

        reactions (:obj:`~kirugram.types.MessageReactionCountUpdated`):
            The received message reaction count update.
    """

    def __init__(
        self,
        callback: MessageReactionCountCallbackType,
        filters: Filter | None = None,
    ) -> None:
        super().__init__(callback, filters)
