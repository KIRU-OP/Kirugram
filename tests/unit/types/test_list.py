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

from kirugram import types


def test_a_list_of_plain_values_is_representable() -> None:
    assert repr(types.List([1, "two"])) == "kirugram.types.List([1,'two'])"


def test_a_nested_list_is_representable() -> None:
    assert repr(types.List([types.List([1])])) == "kirugram.types.List([kirugram.types.List([1])])"


def test_an_object_still_reports_its_own_shape() -> None:
    username = types.Username(username="someone", active=True)

    assert repr(types.List([username])) == f"kirugram.types.List([{username!r}])"
    assert "kirugram.types.Username(" in repr(username)
