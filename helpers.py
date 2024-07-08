
def init_pixel_grid(height, width, default_color=(0, 0, 0)):
    pixels = []
    
    for y in range(height):
        row = []
        for x in range(width):
            row.append(default_color)
        pixels.append(row)
    
    return pixels