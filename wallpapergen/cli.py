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
import logging
import random
import typing

import cairo

from wallpapergen.generators import circles, squares, stripes, triangles
from wallpapergen.lib import palettes


def main() -> None:
    modes: typing.Dict[str, typing.Any] = {
        "circles": circles,
        "squares": squares,
        "stripes": stripes,
        "triangles": triangles,
    }

    command_line_parser = argparse.ArgumentParser()

    class CheckDimensionAction(argparse.Action):
        def __call__(
            self,
            parser: argparse.ArgumentParser,
            namespace: argparse.Namespace,
            values: typing.Union[str, typing.Sequence[typing.Any], None],
            option_string: typing.Optional[str] = None,
        ) -> None:
            assert isinstance(values, int)
            if values < 16:
                parser.error(f"Value of {option_string} must be larger than 16.")
            setattr(namespace, self.dest, values)

    class CheckRandomOrIntAction(argparse.Action):
        def __call__(
            self,
            parser: argparse.ArgumentParser,
            namespace: argparse.Namespace,
            values: typing.Union[str, typing.Sequence[typing.Any], None],
            option_string: typing.Optional[str] = None,
        ) -> None:
            assert isinstance(values, str)
            if values == "random":
                setattr(namespace, self.dest, values)
            try:
                if int(values) <= 0:
                    parser.error(f"Value oof {option_string} must be 'random' or an int > 0.")
            except ValueError:
                parser.error(f"Value oof {option_string} must be 'random' or an int > 0.")
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
        "--mode", metavar="MODE", choices=modes_choices, default="random", help="Type of wallpaper to generate.",
    )
    command_line_parser.add_argument(
        "--palette",
        metavar="PALETTE",
        type=str,
        action=CheckRandomOrIntAction,
        default="random",
        help="Color palette to use. Numerical palette id from Colourlovers.com, or 'random'",
    )
    command_line_parser.add_argument("-v", "--verbose", action="store_true", help="Print verbose messages.")
    command_line_parser.add_argument("output", metavar="FILE", help="Name of generated PNG image file.")
    command_line_args = command_line_parser.parse_args()

    if command_line_args.verbose:
        logging.basicConfig(level=logging.DEBUG)

    if command_line_args.mode == "random":
        mode = random.choice(list(modes.keys()))
    else:
        mode = command_line_args.mode
    logging.info("using generator: %s", mode)

    if command_line_args.palette == "random":
        colors = palettes.Palettes().get_random_palette()
    else:
        palette_id = int(command_line_args.palette)
        colors = palettes.Palettes().get_palette(palette_id)

    surface = cairo.ImageSurface(cairo.FORMAT_RGB24, command_line_args.width, command_line_args.height)
    modes[mode].draw(surface, colors)

    logging.info("writing image file: %s", command_line_args.output)
    surface.write_to_png(command_line_args.output)


if __name__ == "__main__":
    main()
