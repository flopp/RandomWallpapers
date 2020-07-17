import math
import random
import typing

from wallpapergen.lib.rgb import RGB


def get_unused_color(
    colors: typing.List[RGB], used: typing.Set[typing.Optional[RGB]],
) -> RGB:
    remaining_colors = [color for color in colors if color not in used]
    if len(remaining_colors) == 0:
        remaining_colors = colors
    return random.choice(remaining_colors)


def get_distance(p1: typing.Tuple[int, int], p2: typing.Tuple[int, int]) -> float:
    dx = p1[0] - p2[0]
    dy = p1[1] - p2[1]
    return math.sqrt(dx * dx + dy * dy)
