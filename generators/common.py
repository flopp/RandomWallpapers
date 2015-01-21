def get_unused_color(colors, used):
    import random
    remaining_colors = [color for color in colors if color not in used]
    if len(remaining_colors) == 0:
        remaining_colors = colors
    return random.choice(remaining_colors)


def get_distance(p1, p2):
    from math import sqrt
    dx = p1[0] - p2[0]
    dy = p1[1] - p2[1]
    return sqrt(dx * dx + dy * dy)