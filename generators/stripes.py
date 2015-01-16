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

# 'stripes' generator


def draw(surface, colors):
    import math
    import random
    import cairo

    dc = cairo.Context(surface)

    width = surface.get_width()
    height = surface.get_height()
    max_dim = max(width, height)

    angle = 5 * random.randint(1, 17)  # 5 deg - 85 deg in steps of 5 deg
    if random.randint(0, 1):
        angle *= -1

    stripe_widths = [random.randint(16, 256) for i in range(len(colors))]
    stripe_index = 0

    dc.translate(width / 2, height / 2)
    dc.rotate(angle * math.pi / 180.0)
    x = -2 * max_dim
    while x < 2 * max_dim:
        color = colors[stripe_index]
        stripe_width = stripe_widths[stripe_index]
        stripe_index = (stripe_index + 1) % len(colors)

        dc.set_source_rgb(color[0], color[1], color[2])
        dc.rectangle(x, -2 * max_dim, stripe_width + 2, 4 * max_dim)
        dc.fill()

        x += stripe_width
