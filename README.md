# RandomWallpapers
Random geometric wallpaper generator 

## Requirements
- python-cairo (install with `sudo apt-get inbstall python-cairo` on Debian/Ubuntu systems)
- python-colourlovers (install with `sudo pip install python-colourlovers`)

## Usage
    ./wallpapergen.py [--width VALUE] [--height VALUE] [--mode MODE] FILE
    
    positional arguments:
      FILE            Name of generated PNG image file
    
    optional arguments:
      --width VALUE   Width of generated image
      --height VALUE  Height of generated image
      --mode MODE     Type of wallpaper to generate; values: random, circles, squares, stripes
