from PIL import Image
import numpy as np

def pixel_arr_to_img(output, pixels):
    array = np.array(pixels, dtype=np.uint8)
    img = Image.fromarray(array)
    img.save(output)