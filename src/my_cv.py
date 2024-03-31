
####################################################
# Computer Vision Module with additional functions #
####################################################

# Works as a layer of abstraction between the OpenCV library and the rest of the code

import cv2
import numpy as np 

# Resize the requested image by a scale factor (e.g. 0.5)
def resize_by(image, scale_factor):
    width, height = image.shape[1], image.shape[0]
    new_width  = int(width * scale_factor)
    new_height = int(height * scale_factor)
    dimensions = (new_width, new_height)
    return cv2.resize(image, dimensions, interpolation=cv2.INTER_AREA)

# Show the requested image
def show(image, title='Image', scale=1.0):
    cv2.namedWindow(title)
    cv2.moveWindow(title, 40,30)
    image = resize_by(image, scale)
    cv2.imshow(title, image)
    wait_time = 1000
    while cv2.getWindowProperty(title, cv2.WND_PROP_VISIBLE) >= 1:
        keyCode = cv2.waitKey(wait_time)
        if(keyCode & 0xFF) == ord("q"):
            break
    cv2.destroyAllWindows()

# Read the requested image 
def read(image_path, scale=1.0):
    image = cv2.imread(image_path)
    image = resize_by(image, scale) 
    return image

# Write the requested image 
def write(image, image_output_path, scale=1.0):
    image = resize_by(image, scale)
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    cv2.imwrite(image_output_path, image) 

#---------------------------------------------------

# Split image into color channels in the RGB order
def extract_color_channels(image):
    b, g, r = cv2.split(image)
    return np.array([r, g, b])

# Extract the bit at the specified position for each pixel
# MSB == 7 and LSB == 0 
def extract_bit_plane(image_gray, bit_plane_number):
    bit_image = (image_gray & (1 << bit_plane_number))
    return bit_image.astype(np.bool_)

# Extract the bit at the specified position for each pixel but passing a tuple as argument
def tup_extract_bit_plane(info, image):
    image_channel_index, bit_plane_number = info
    return extract_bit_plane(image[image_channel_index], bit_plane_number)

# Replace the specified bitplane with the new bitplane
def replace_bit_plane(image_gray, new_bit_plane, bit_plane_number):
    image_gray = np.bitwise_and(image_gray, ~(1 << bit_plane_number)) 
    image_gray = image_gray | (new_bit_plane.astype(np.uint8) << bit_plane_number)  
    return image_gray.astype(np.uint8)

