# Copyright (C) 2015-2020 Florian Pigorsch <mail@florian-pigorsch.de>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import math
import typing

import cairo

from wallpapergen.rgb import RGB


class Generator:
    def __init__(self) -> None:
        pass

    def draw(self, surface: cairo.ImageSurface, colors: typing.List[RGB]) -> None:
        pass

    @staticmethod
    def get_distance(p1: typing.Tuple[int, int], p2: typing.Tuple[int, int]) -> float:
        dx = p1[0] - p2[0]
        dy = p1[1] - p2[1]
        return math.sqrt(dx * dx + dy * dy)
