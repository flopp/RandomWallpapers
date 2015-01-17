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

You may want to run the generator at regular intervals to constantly get new wallpapers. On a unix/linux system, this can achieved via a cronjob or the `watch` command line tool, e.g.

    watch -n 600 ~/RW/wallpapergen.py --width 1920 --height 1080 --out ~/RW/wallpaper.png

This command assumes that you have cloned the repository to `~/RW`, that your screen resolution in 1920x1080, and that you want to generate a wallpaper every 600 seconds. The reulting image ist stored in `~/RW/wallpaper.png` which you can set as your desktop wallpaper. Any respectable desktop environment should reload the wallpaper as soon as the file changes.

## Examples

### Circles mode:
![Circles mode](https://raw.githubusercontent.com/flopp/RandomWallpapers/master/examples/circles.png)

### Squares mode:
![Squares mode](https://raw.githubusercontent.com/flopp/RandomWallpapers/master/examples/squares.png)

### Stripes mode:
![Stripes mode](https://raw.githubusercontent.com/flopp/RandomWallpapers/master/examples/stripes.png)

### Triangles mode:
![Triangles mode](https://raw.githubusercontent.com/flopp/RandomWallpapers/master/examples/triangles.png)

