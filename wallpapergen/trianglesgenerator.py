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

# 'triangulation' generator

import random
import typing

import cairo
import numpy
import scipy.spatial

from wallpapergen.generator import Generator
from wallpapergen.rgb import RGB


class TrianglesGenerator(Generator):
    def draw(self, surface: cairo.ImageSurface, colors: typing.List[RGB]) -> None:
        tri = scipy.spatial.Delaunay(
            numpy.array(TrianglesGenerator.generate_points(surface.get_width(), surface.get_height()))
        )

        # compute triangle colors, trying to find distinct colors for neighboring
        # triangles
        triangle_colors = TrianglesGenerator.compute_colors(tri, colors)

        # draw triangles
        dc = cairo.Context(surface)
        lines = set()
        for index, triangle in enumerate(tri.points[tri.simplices]):
            color = triangle_colors[index]
            assert color is not None
            dc.set_source_rgb(*color)
            dc.new_path()
            for p in triangle:
                dc.line_to(*p)
            dc.close_path()
            dc.fill()

            # over draw edges to avoid antialiasing artifacts
            for i, _ in enumerate(triangle):
                a = tuple(triangle[i])
                b = tuple(triangle[(i + 1) % len(triangle)])
                if (a, b) not in lines:
                    lines.add((a, b))
                    lines.add((b, a))
                    dc.new_path()
                    dc.move_to(*a)
                    dc.line_to(*b)
                    dc.stroke()

    @staticmethod
    def compute_colors(triangulation: scipy.spatial.Delaunay, colors: typing.List[RGB]) -> typing.List[RGB]:
        triangle_colors: typing.List[RGB] = []
        for index, _ in enumerate(triangulation.simplices):
            used_colors = {
                triangle_colors[neighbor_index]
                for neighbor_index in triangulation.neighbors[index]
                if 0 <= neighbor_index < len(triangle_colors)
            }
            triangle_colors.append(TrianglesGenerator.get_unused_color(colors, used_colors))
        return triangle_colors

    @staticmethod
    def generate_points(width: int, height: int) -> typing.List[typing.Tuple[int, int]]:
        min_allowed_dist = max(width, height) // random.randint(10, 20)
        w2 = width // 2
        h2 = height // 2

        # add points outside the surface to get a full triangulation of the surface
        points = [
            (-w2, -h2),
            (width + w2, -h2),
            (-w2, height + h2),
            (width + w2, height + h2),
        ]

        # place points randomly with minimum distance; stop when no minimum distance
        # point can be found in 20 tries.
        tries = 20
        while True:
            point_placed = False
            for _ in range(tries):
                x = random.randint(-w2, width + w2)
                y = random.randint(-h2, height + h2)

                min_dist = (
                    min_allowed_dist if len(points) == 0 else min([Generator.get_distance((x, y), p2) for p2 in points])
                )
                if min_dist >= min_allowed_dist:
                    points.append((x, y))
                    point_placed = True
                    break
            if not point_placed:
                break

        return points

    @staticmethod
    def get_unused_color(colors: typing.List[RGB], used: typing.Set[typing.Optional[RGB]],) -> RGB:
        remaining_colors = [color for color in colors if color not in used]
        if len(remaining_colors) == 0:
            remaining_colors = colors
        return random.choice(remaining_colors)
