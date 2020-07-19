# Copyright (C) 2015 Florian Pigorsch <mail@florian-pigorsch.de>
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

# 'circles' generator

import math
import random
import typing

import cairo

from wallpapergen.generator import Generator
from wallpapergen.rgb import RGB


Circle = typing.Tuple[int, int, int]


class CirclesGenerator(Generator):
    def draw(self, surface: cairo.ImageSurface, colors: typing.List[RGB]) -> None:
        dc = cairo.Context(surface)

        width = surface.get_width()
        height = surface.get_height()
        max_radius = min(width, height) // 2

        dc.set_source_rgb(*colors[0])
        dc.rectangle(0, 0, width, height)
        dc.fill()

        circles: typing.List[Circle] = []
        while True:
            (x, y, radius) = CirclesGenerator.create_nonintersecting_circle(
                (0, width), (0, height), (8, max_radius), circles
            )
            if radius <= 0:
                break
            circles.append((x, y, radius))

            for color in colors[1:]:
                dc.set_source_rgb(*color)
                dc.arc(x, y, radius, 0, 2 * math.pi)
                dc.fill()
                if radius <= 16:
                    break
                radius = random.randint(8, radius - 4)

    @staticmethod
    def create_nonintersecting_circle(
        x_range: typing.Tuple[int, int],
        y_range: typing.Tuple[int, int],
        r_range: typing.Tuple[int, int],
        circles: typing.List[Circle],
    ) -> Circle:
        for _ in range(0, 20):
            x = random.randint(*x_range)
            y = random.randint(*y_range)
            r = random.randint(*r_range)
            if not CirclesGenerator.check_if_circle_intersects(x, y, r, circles):
                return x, y, r
        return 0, 0, 0

    @staticmethod
    def check_if_circle_intersects(x: int, y: int, r: int, circles: typing.List[Circle]) -> bool:
        for (x2, y2, r2) in circles:
            if Generator.get_distance((x, y), (x2, y2)) < (r + r2):
                return True
        return False
