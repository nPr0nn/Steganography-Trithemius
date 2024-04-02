
from . import my_cv
from . import my_files_io

import numpy as np

# Display to the user the required bit planes for each color channel of the image
def inspect_image(image_path, color_channels, bit_planes):
    
    # Read image color channels
    image = my_cv.read(image_path)
    color_channels_array = my_cv.extract_color_channels(image) # np.array([r, g, b])    
    color_channels_names = ["Red", "Green", "Blue"]
  
    # Get folder path
    folder_path = my_files_io.get_path_parent(image_path) + "/inspected_images"
    my_files_io.create_folder_if_not_exists(folder_path)
    
    # Generate combination of color channels and bit planes to iterate
    # Cartesian product
    color_channels_indices       = color_channels
    bit_plane_mesh, channel_mesh = np.meshgrid(bit_planes, color_channels_indices)
    combinations = np.stack((bit_plane_mesh, channel_mesh), axis=-1).flatten().reshape(-1, 2) 
    combinations = sorted(combinations, key=lambda x: bit_planes.index(x[0]))

    # Display image of bit planes
    for combination in combinations:
        bit_plane_number, color_channel_index = combination
        color_channel = color_channels_array[color_channel_index]
         
        # If it's the first time displaying the color channel show it entirely
        if(bit_plane_number == bit_planes[0]):
            my_cv.show(color_channel, "Full Color Channel " + color_channels_names[color_channel_index])
            my_cv.write(color_channel, folder_path + "/color_channel_" + color_channels_names[color_channel_index] + ".png")

        # Extract bit plane
        bit_plane = my_cv.extract_bit_plane(color_channel, bit_plane_number) 

        # Display bit plane
        title = "Color Channel " + color_channels_names[color_channel_index] + " - Bit Plane " + str(bit_plane_number)
        bit_plane = bit_plane.astype(np.uint8) * 255
        my_cv.show(bit_plane, title)
        new_image_path=folder_path+"/color_channel_"+color_channels_names[color_channel_index]+"_bit_plane_"+str(bit_plane_number)
        my_cv.write(bit_plane, new_image_path + ".png")
        
