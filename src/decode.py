
from . import my_files_io
from . import my_bits
from . import my_cv

import numpy as np

########### Message Encoding Protocol ###############
# [ size of file - 64 bits] [ extension - 24 bits ] #
# [              file bits - variable             ] #
#####################################################

# Entry point, decodes the file hidden inside the image 
def decode_file(image_path, output_path, bit_planes): 
    # Read input image 
    encoded_img      = my_cv.read(image_path) 

    # Decode the file bits
    file_bits        = decode(encoded_img, bit_planes)
    
    # Sets decoded file name as the same name of the encoded image
    # just replacing the extension
    file_output_name = my_files_io.get_file_name(image_path)
    file_output_name = file_output_name.replace('.png', '').replace('encoded_', '') 
    file_output_path = output_path + "/decoded_" + file_output_name 

    # Save the decoded file into the specified path with its name  
    file_output_path = my_bits.save_binary_array_to_file(file_bits, file_output_path)  
    return file_output_path

# Decodes file bits hidden in the image bit planes 
# and returns the file bits
def decode(encoded_img, bit_planes):    
    # Split image into color channels
    color_channels_array = my_cv.extract_color_channels(encoded_img)

    # Generate combination of color channels and bit planes to iterate
    # Cartesian product
    color_channels_indices       = np.arange(len(color_channels_array)) 
    bit_plane_mesh, channel_mesh = np.meshgrid(bit_planes, color_channels_indices)
    combinations   = np.stack((bit_plane_mesh, channel_mesh), axis=-1).flatten().reshape(-1, 2) 

    # Extract bit planes
    all_bit_planes = np.apply_along_axis(my_cv.tup_extract_bit_plane, axis=1, arr=combinations, image=color_channels_array)  
    all_bit_planes = all_bit_planes.flatten()
       
    # Use header to get file number of bits
    # [ size of file - 64 bits] [ extension - 24 bits ]
    file_number_of_bits = my_bits.convert_bits_to_int(all_bit_planes[:64]) + 64 + 24

    # Get only message bits
    file_bits = all_bit_planes[:file_number_of_bits] 
    
    return file_bits.astype(np.uint8)
