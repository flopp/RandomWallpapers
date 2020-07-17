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

import argparse
import random
import logging
import cairo
from wallpapergen.generators import circles, squares, stripes, triangles
from wallpapergen.lib import palettes


def main():
    modes = {
        "circles": circles,
        "squares": squares,
        "stripes": stripes,
        "triangles": triangles,
    }

    command_line_parser = argparse.ArgumentParser()

    class CheckDimensionAction(argparse.Action):
        def __call__(self, parser, namespace, values, option_string=None):
            if values < 16:
                parser.error(f"Value of {option_string} must be larger than 16.")
            setattr(namespace, self.dest, values)

    command_line_parser.add_argument(
        "--width",
        metavar="VALUE",
        type=int,
        action=CheckDimensionAction,
        default=1024,
        help="Width of generated image.",
    )
    command_line_parser.add_argument(
        "--height",
        metavar="VALUE",
        type=int,
        action=CheckDimensionAction,
        default=768,
        help="Height of generated image.",
    )
    modes_choices = ["random"] + list(modes.keys())
    command_line_parser.add_argument(
        "--mode",
        metavar="MODE",
        choices=modes_choices,
        default="random",
        help="Type of wallpaper to generate.",
    )
    command_line_parser.add_argument(
        "--palette",
        metavar="PALETTE",
        type=str,
        default="random",
        help="Color palette to use. Numerical palette id from Colourlovers.com, or 'random'",
    )
    command_line_parser.add_argument(
        "-v", "--verbose", action="store_true", help="Print verbose messages."
    )
    command_line_parser.add_argument(
        "output", metavar="FILE", help="Name of generated PNG image file."
    )
    command_line_args = command_line_parser.parse_args()

    if command_line_args.verbose:
        logging.basicConfig(level=logging.DEBUG)

    width = command_line_args.width
    height = command_line_args.height
    surface = cairo.ImageSurface(cairo.FORMAT_RGB24, width, height)

    mode = (
        random.choice(list(modes.keys()))
        if command_line_args.mode == "random"
        else command_line_args.mode
    )
    logging.info("using generator: %s", mode)

    pal = palettes.Palettes()
    colors = (
        pal.get_palette(command_line_args.palette)
        if command_line_args.palette.isdigit()
        else pal.get_random_palette()
    )
    modes[mode].draw(surface, colors)

    logging.info("writing image file: %s", command_line_args.output)
    surface.write_to_png(command_line_args.output)


if __name__ == "__main__":
    main()
