from math import sqrt

import helpers
import export

def make_line(from_point, to_point, thickness=1):
    slope = (to_point[1] - from_point[1])/(to_point[0] - from_point[0])
    points = []
    curr_point = from_point
    
    while not approx_equals(curr_point, to_point):
        central_location = (curr_point[0], int(curr_point[1]))
        points.append(central_location)
        
        thickness_applied = 1
        direction = True # true = north, south = false
        while thickness_applied < thickness:
            if direction:
                points.append((central_location[0], central_location[1] + thickness_applied))
            else:
                points.append((central_location[0], central_location[1] - thickness_applied))
                thickness_applied += 1
            direction = not direction
        
        next_point = (curr_point[0] + 1, curr_point[1] + slope)
        curr_point = next_point
    print(points)
    return points

def approx_equals(point1, point2, tolerance=1):
    if sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) < tolerance:
        return True
    return False

pixels = helpers.init_pixel_grid(512, 512, (255, 255, 255))

line = make_line((10, 10), (100, 100), 4)

for point in line:
    pixels[point[1]][point[0]] = (255, 0, 0)

export.pixel_arr_to_img("test_data/line.png", pixels)