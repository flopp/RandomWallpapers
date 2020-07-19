import cairo

from wallpapergen.circlesgenerator import CirclesGenerator
from wallpapergen.squaresgenerator import SquaresGenerator
from wallpapergen.stripesgenerator import StripesGenerator
from wallpapergen.trianglesgenerator import TrianglesGenerator
from wallpapergen.palettes import Palettes


def test_generators() -> None:
    surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 300, 200)
    for gen in [CirclesGenerator, SquaresGenerator, StripesGenerator, TrianglesGenerator]:
        gen().draw(surface, [(255, 0, 0), (0, 255, 0), (0, 0, 255)])


def test_palettes() -> None:
    assert len(Palettes().get_random_palette()) > 0
    assert len(Palettes().get_palette(123)) > 0
