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

### squares
def draw(surface, colors):
  import math
  import random
  import cairo
  
  dc = cairo.Context(surface)
  
  width = surface.get_width()
  height = surface.get_height()  
  max_dim = max(width, height)
  
  angle = 5 * random.randint(0, 17) # 0 deg - 85 deg in steps of 5 deg
  
  dc.translate(width/2, height/2)
  dc.rotate(angle * math.pi / 180.0)
  
  min_side = 16
  max_side = min(width, height) // 2
  side = random.randint(min_side, max_side)
  
  dc.set_source_rgb(colors[0][0], colors[0][1], colors[0][2])
  dc.rectangle(0, 0, width, height)
  dc.fill()

  for x in xrange(-2*max_dim, 2*max_dim, side):
    for y in xrange(-2*max_dim, 2*max_dim, side):
      color = random.choice(colors)
      dc.set_source_rgb(color[0], color[1], color[2])
      # let the rectangles overlap to the top left in order to avoid antialiasing artifacts at the edges
      dc.rectangle(x-1, y-1, side+1, side+1)
      dc.fill()
