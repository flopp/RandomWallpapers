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


def get_unused_color(colors, used):
    import random
    remaining_colors = [color for color in colors if color not in used]
    if len(remaining_colors) == 0:
        remaining_colors = colors
    return random.choice(remaining_colors)


def get_distance(p1, p2):
    from math import sqrt
    dx = p1[0] - p2[0]
    dy = p1[1] - p2[1]
    return sqrt(dx * dx + dy * dy)


def draw(surface, colors):
    import numpy
    import scipy.spatial
    import random
    import cairo

    dc = cairo.Context(surface)

    width = surface.get_width()
    height = surface.get_height()
    min_allowed_dist = max(width, height) // 10

    w2 = width // 2
    h2 = height // 2
    # add points outside the surface to get a full triangulation of the surface
    points = [(-w2, -h2), (width + w2, -h2), (-w2, height + h2), (width + w2, height + h2)]

    # place points randomly with minimum distance
    while True:
        point_placed = False
        for i in range(20):
            x = random.randint(-width // 2, width + width // 2)
            y = random.randint(-height // 2, height + height // 2)

            min_dist = min_allowed_dist if len(points) == 0 else min([get_distance((x, y), p2) for p2 in points])
            if min_dist >= min_allowed_dist:
                points.append((x, y))
                point_placed = True
                break
        if not point_placed:
            break

    lines = set()
    numpy_points = numpy.array(points)
    tri = scipy.spatial.Delaunay(numpy_points)

    # compute triangle colors, trying to find distinct colors for neighboring triangles
    triangle_colors = [None] * len(tri.simplices)
    for index in range(len(tri.simplices)):
        used_colors = {triangle_colors[neighbor_index] for neighbor_index in tri.neighbors[index]}
        triangle_colors[index] = get_unused_color(colors, used_colors)

    # draw triangles
    for index, triangle in enumerate(tri.points[tri.simplices]):
        dc.set_source_rgb(*triangle_colors[index])
        dc.new_path()
        for p in triangle:
            dc.line_to(*p)
        dc.close_path()
        dc.fill()

        # over draw edges to avoid antialiasing artifacts
        for i in range(len(triangle)):
            a = tuple(triangle[i])
            b = tuple(triangle[(i+1)%len(triangle)])
            if (a, b) not in lines:
                lines.add((a, b))
                lines.add((b, a))
                dc.new_path()
                dc.move_to(*a)
                dc.line_to(*b)
                dc.stroke()