import logging
import random
import re
import typing

from colourlovers import clapi

from wallpapergen.lib.rgb import RGB


class Palettes:
    def __init__(self) -> None:
        self.__colourlovers = clapi.ColourLovers()
        self.__log = logging.getLogger("Palettes")
        self.__color_re = re.compile(
            "^#?([0-9a-f]{2})([0-9a-f]{2})([0-9a-f]{2})$", re.IGNORECASE
        )

    def get_palette(self, palette_id: int) -> typing.List[RGB]:
        self.__log.info(
            "trying to get palette (id=%d) from colourlovers.com", int(palette_id)
        )
        try:
            palette = self.__colourlovers.search_palette(id=palette_id)[0]
            self.__log.info(
                'received palette: id=%d, title="%s"', palette.id, palette.title
            )
            return self.__strings_to_rgbs(palette.colors)
        except Exception as e:
            logging.exception(e)
            self.__log.warning(
                "cannot access colourlovers.com; using random static palette"
            )
            return self.__get_random_static_palette()

    def get_random_palette(self) -> typing.List[RGB]:
        self.__log.info("trying to get random palette from colourlovers.com")
        try:
            palette = random.choice(
                self.__colourlovers.search_palettes(request="top", numResults=20)
            )
            self.__log.info(
                'received palette: id=%d, title="%s"', palette.id, palette.title
            )
            return self.__strings_to_rgbs(palette.colors)
        except Exception as e:
            logging.exception(e)
            self.__log.warning(
                "cannot access colourlovers.com; using random static palette"
            )
            return self.__get_random_static_palette()

    def __get_random_static_palette(self) -> typing.List[RGB]:
        static_palettes = [
            ["#0e376f", "#3a6ba5", "#fdfdfd", "#f9d401", "#f99f00"],
            ["#3e0f45", "#624466", "#6f848f", "#999388", "#807373"],
            ["#a07b69", "#7b5759", "#6f4559", "#4e3258", "#3a254c"],
            ["#443c2b", "#757a65", "#7edcce", "#b6eaaa", "#f8f79e"],
            ["#c9f77a", "#a7fc38", "#7ad12e", "#39423d", "#282b34"],
            ["#05285e", "#316cc4", "#4796e9", "#d6eaee", "#ffffff"],
            ["#1c273d", "#2a2f42", "#49455e", "#616a8b", "#7fabff"],
            ["#5a8365", "#646754", "#b4bb63", "#504e48", "#b8bb9e"],
            ["#525454", "#566466", "#698b91", "#bcced1", "#e8e5d3"],
        ]
        return self.__strings_to_rgbs(random.choice(static_palettes))

    def __hex_to_rgb(self, color_string: str) -> RGB:
        match = self.__color_re.match(color_string)
        if not match:
            self.__log.warning("cannot parse color string: %s", color_string)
            return 0, 0, 0

        r = int(match.group(1), 16) / 256.0
        g = int(match.group(2), 16) / 256.0
        b = int(match.group(3), 16) / 256.0
        return r, g, b

    def __strings_to_rgbs(self, color_strings: typing.List[str]) -> typing.List[RGB]:
        return [self.__hex_to_rgb(color_string) for color_string in color_strings]
