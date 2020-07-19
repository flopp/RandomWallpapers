import math
import typing

import cairo

from wallpapergen.rgb import RGB


class Generator:
    def __init__(self) -> None:
        pass

    def draw(self, surface: cairo.ImageSurface, colors: typing.List[RGB]) -> None:
        pass

    @staticmethod
    def get_distance(p1: typing.Tuple[int, int], p2: typing.Tuple[int, int]) -> float:
        dx = p1[0] - p2[0]
        dy = p1[1] - p2[1]
        return math.sqrt(dx * dx + dy * dy)
