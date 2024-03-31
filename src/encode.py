
from . import my_files_io
from . import my_bits
from . import my_cv

import numpy as np

########### Message Encoding Protocol ###############
# [ size of file - 64 bits] [ extension - 24 bits ] #
# [              file bits - variable             ] #
#####################################################

# Entry point, encodes the file into the image 
def encode_file(image_path, file_path, bit_planes, output_path):
    # Read both image and file binary into numpy arrays
    image        = my_cv.read(image_path)
    file_bits = my_bits.read_file_to_binary_array(file_path)
   
    # Encode the file into an image and return encoded image matrix
    encoded_img = encode(image, file_bits, bit_planes)

    # Save the encoded image into the specified path
    image_output_path = output_path + "/encoded_" + my_files_io.get_file_name(image_path)
    my_cv.write(encoded_img, image_output_path) 
    return image_output_path
   
# Encodes file bits into the image bit planes 
# and returns the encoded image
def encode(img, file_bits, bit_planes):
    # Get number of bit planes and image dimensions
    num_bit_planes                 = len(bit_planes)
    h, w, number_of_color_channels = img.shape
   
    # Lets "divide" the file bits into bits buffers of the same size as the image
    # to be able to encode it efficiently

    # Check if the image specified bit planes are enough to store the file information
    buffer_size      = (w * h) 
    max_buffers      = number_of_color_channels * len(bit_planes)  
    total_image_size = max_buffers * buffer_size 
    if(len(file_bits) > total_image_size):
        raise ValueError("The message is too long to be encrypted in the image.")

    # Number of buffers needed to store the file information
    number_of_needed_buffers = int(np.ceil(len(file_bits) / buffer_size)) 

    # Create a mask to help on encoding the file information
    mask = np.zeros(number_of_needed_buffers * buffer_size, dtype=np.bool_)
    mask[:len(file_bits)] = 1
   
    # Resize file bits and auxiliary mask to the buffer size 
    file_bits.resize((number_of_needed_buffers*h, w), refcheck=False)
    mask.resize((number_of_needed_buffers*h, w), refcheck=False) 

    # Split image into color channels
    color_channels_array = my_cv.extract_color_channels(img) # np.array([r, g, b])
  
    # Generate combination of color channels and bit planes to iterate
    # Cartesian product
    color_channels_indices       = np.arange(len(color_channels_array)) 
    bit_plane_mesh, channel_mesh = np.meshgrid(bit_planes, color_channels_indices)
    combinations   = np.stack((bit_plane_mesh, channel_mesh), axis=-1).flatten().reshape(-1, 2) 
   
    # Encode the message
    for i in range(number_of_needed_buffers):
        # Get the correct bit plane number and color channel index combination
        # to encode the current buffer of file bits
        bit_plane_number, channel_index = combinations[i]

        # Get the correct color channel
        color_channel      = color_channels_array[channel_index] # grayscale channel

        # Get the correct buffer chunks
        file_bits_buffer   = file_bits[i*h:(i+1)*h, 0:w] 
        mask_buffer        = mask[i*h:(i+1)*h, 0:w]
        
        # Extract the correct bit plane and edit with the file bits
        bit_plane      = my_cv.extract_bit_plane(color_channel, bit_plane_number)
        new_bit_plane  = np.where(mask_buffer, file_bits_buffer, bit_plane)

        # Replace the bit plane on the correct color channel
        color_channels_array[channel_index] = my_cv.replace_bit_plane(color_channel, new_bit_plane, bit_plane_number)
    
    # Group color channels back together
    encoded_img = np.stack((color_channels_array), axis=-1)    
    return encoded_img
