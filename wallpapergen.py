#! /usr/bin/env python

# Random geometric wallpaper generator

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

import random
import cairo
from generators import circles, squares, stripes
from colourlovers import ColourLovers

def hex_to_rgb(value):
  value = value.lstrip('#')
  if not len(value) == 6:
    return (0, 0, 0)
  return tuple(int(value[i:i + 2], 16) / 256.0 for i in xrange(0, 3))

def get_colors():
  palette = []
  
  try:
    palette = ColourLovers().palettes('random')[0].colours
  except:
    print 'error accessing colourlovers.com'
    fallback_colors = [
      ['#0e376f', '#3a6ba5', '#fdfdfd', '#f9d401', '#f99f00'], 
      ['#3e0f45', '#624466', '#6f848f', '#999388', '#807373'], 
      ['#a07b69', '#7b5759', '#6f4559', '#4e3258', '#3a254c'],
      ['#443c2b', '#757a65', '#7edcce', '#b6eaaa', '#f8f79e'],
      ['#c9f77a', '#a7fc38', '#7ad12e', '#39423d', '#282b34'],
      ['#05285e', '#316cc4', '#4796e9', '#d6eaee', '#ffffff'],
      ['#1c273d', '#2a2f42', '#49455e', '#616a8b', '#7fabff'],
      ['#5a8365', '#646754', '#b4bb63', '#504e48', '#b8bb9e'],
      ['#525454', '#566466', '#698b91', '#bcced1', '#e8e5d3'],
      ]
    palette = random.choice(fallback_colors)
  
  return [hex_to_rgb(color_string) for color_string in palette]
  

def main():
  import argparse
  
  modes = { 'circles' : circles, 'squares' : squares, 'stripes' : stripes }
  
  command_line_parser = argparse.ArgumentParser(version='0.0.1')
  
  class CheckDimensionAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        if values < 16:
            parser.error("Value of {0} must be larger than 16.".format(option_string))
        setattr(namespace, self.dest, values)
  
  command_line_parser.add_argument('--width', metavar='VALUE', type=int, action=CheckDimensionAction, default=1024, help='Width of generated image.')
  command_line_parser.add_argument('--height', metavar='VALUE', type=int, action=CheckDimensionAction, default=768, help='Height of generated image.')
  command_line_parser.add_argument('--mode', metavar='MODE', choices=['random'] + modes.keys(), default='random', help='Type of wallpaper to generate.')
  command_line_parser.add_argument('output', metavar='FILE', help='Name of generated PNG image file.')
  command_line_args = command_line_parser.parse_args()
    
  width = command_line_args.width
  height = command_line_args.height
  surface = cairo.ImageSurface(cairo.FORMAT_RGB24, width, height)
  
  mode = random.choice(modes.keys()) if command_line_args.mode is 'random' else command_line_args.mode
  modes[mode].draw(surface, get_colors())
  
  surface.write_to_png(command_line_args.output)


if __name__ == '__main__':
  main()
