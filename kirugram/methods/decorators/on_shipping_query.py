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

import kirugram
from kirugram.filters import Filter
from .unbound_arguments import unbound_arguments

if TYPE_CHECKING:
    from collections.abc import Callable

    from .handler_type import HandlerType


class OnShippingQuery:
    def on_shipping_query(
        self: OnShippingQuery | Filter | None = None,
        filters: Filter | None = None,
        group: int = 0,
    ) -> Callable[[HandlerType], HandlerType]:
        """Decorator for handling shipping queries.

        This does the same thing as :meth:`~kirugram.Client.add_handler` using the
        :obj:`~kirugram.handlers.ShippingQueryHandler`.

        .. include:: /_includes/usable-by/bots.rst

        Parameters:
            filters (:obj:`~kirugram.filters`, *optional*):
                Pass one or more filters to allow only a subset of shipping queries to be passed
                in your function.

            group (``int``, *optional*):
                The group identifier, defaults to 0.

        """

        def decorator(func: HandlerType) -> HandlerType:
            if isinstance(self, kirugram.Client):
                self.add_handler(kirugram.handlers.ShippingQueryHandler(func, filters), group)
            elif isinstance(self, Filter) or self is None:
                if not hasattr(func, "handlers"):
                    func.handlers = []

                arguments = unbound_arguments(self, filters=filters, group=group)

                func.handlers.append(
                    (
                        kirugram.handlers.ShippingQueryHandler(func, arguments.filters),
                        arguments.group,
                    )
                )

            return func

        return decorator
