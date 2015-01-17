# RandomWallpapers
Random geometric wallpaper generator. The generator has different modes (currently 'circles', 'squares', 'stripes', 'triangles'), which produce different image styles. Visually appealing color palettes are retrieved from http://ColourLovers.com.

## Requirements
- python-cairo (install with `sudo apt-get install python-cairo` on Debian/Ubuntu systems)
- python-numpy (install with `sudo apt-get install python-numpy` on Debian/Ubuntu systems)
- python-scipy (install with `sudo apt-get install python-scipy` on Debian/Ubuntu systems)
- python-colourlovers (install with `sudo pip install python-colourlovers`)

## Usage
    ./wallpapergen.py [--width VALUE] [--height VALUE] [--mode MODE] 
                      [--palette PALETTE] FILE
    
    positional arguments:
      FILE            Name of generated PNG image file
    
    optional arguments:
      --width VALUE   Width of generated image
      --height VALUE  Height of generated image
      --mode MODE     Type of wallpaper to generate; 
                      values: 'random', 'circles', 'squares', 'stripes', triangles'; 
                      default: 'random'
      --palette PALETTE  Color palette to use. Numerical palette id from
                      Colourlovers.com, or 'random'; default: 'random'

## Examples

### Circles mode:
![Circles mode](https://raw.githubusercontent.com/flopp/RandomWallpapers/master/examples/circles.png)

### Squares mode:
![Squares mode](https://raw.githubusercontent.com/flopp/RandomWallpapers/master/examples/squares.png)

### Stripes mode:
![Stripes mode](https://raw.githubusercontent.com/flopp/RandomWallpapers/master/examples/stripes.png)

### Triangles mode:
![Triangles mode](https://raw.githubusercontent.com/flopp/RandomWallpapers/master/examples/triangles.png)

