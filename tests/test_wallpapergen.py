import cairo

from wallpapergen.generators import circles, squares, stripes, triangles
from wallpapergen.lib import palettes


def test_generators() -> None:
    surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 300, 200)
    for gen in [circles, squares, stripes, triangles]:
        gen.draw(surface, [(255, 0, 0), (0, 255, 0), (0, 0, 255)])


def test_palettes() -> None:
    assert len(palettes.Palettes().get_random_palette()) > 0
    assert len(palettes.Palettes().get_palette(123)) > 0
