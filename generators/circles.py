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

### circles
def draw(surface, colors):
  import math
  import random
  import cairo
  dc = cairo.Context(surface)
  
  width = surface.get_width()
  height = surface.get_height()  
  max_radius = min(width, height) // 2
  
  (r,g,b) = colors[0]
  dc.set_source_rgb(r, g, b)
  dc.rectangle(0, 0, width, height)
  dc.fill()
  
  circles = []
  while True:
    (x, y, radius) = create_nonintersecting_circle(0, width, 0, height, 8, max_radius, circles)
    if radius <= 0:
      break
    circles.append((x, y, radius))
    
    for color in colors[1:]:
      dc.set_source_rgb(color[0], color[1], color[2])
      dc.arc(x, y, radius, 0, 2 * math.pi)
      dc.fill()
      if radius <= 16:
        break
      radius = random.randint(8, radius - 4)

def nonintersecting_circle(minx, maxx, miny, maxy, minr, maxr, circles):
  for try_index in xrange(0, 20):
    x = random.randint(minx, maxx)
    y = random.randint(miny, maxy)
    r = random.randint(minr, maxr)
    if not check_if_circle_intersects(x, y, r, circles):
      return (x, y, radius)
  return (0, 0, 0)

def check_if_circle_intersects(x, y, r, circles):
  for (x2, y2, r2) in circles:
    if (x-x2)*(x-x2) + (y-y2)*(y-y2) < (r+r2)*(r+r2):
      return True
  return False
