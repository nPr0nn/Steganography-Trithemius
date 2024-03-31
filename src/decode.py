
from . import my_files_io
from . import my_bits
from . import my_cv

import numpy as np

### Message Encoding Protocol ###
# [ number of bit planes used - 3 bits ] [ bit planes info - máx 24 bits ] [ size of file - 64 bits] 
# [ extension - 24 bits ] [                       message bits - variable                          ]

def decode_file(image_path, output_path, bit_planes): 
    encoded_img      = my_cv.read(image_path) 
    file_bits        = decode(encoded_img, bit_planes)
     
    file_output_name = my_files_io.get_file_name(image_path)
    file_output_name = file_output_name.replace('.png', '').replace('encoded_', '')
   
    file_output_path = output_path + "/decoded_" + file_output_name 
    file_output_path = my_bits.save_binary_array_to_file(file_bits, file_output_path)
    
    return file_output_path

def decode(encoded_img, bit_planes):    
    # Split image into color channels
    color_channels = my_cv.extract_color_channels(encoded_img)

    # Genereate combination of color channels and bit planes to iterate
    color_channels_indices       = np.arange(len(color_channels)) 
    bit_plane_mesh, channel_mesh = np.meshgrid(bit_planes, color_channels_indices)
    combinations   = np.stack((channel_mesh, bit_plane_mesh), axis=-1).flatten().reshape(-1, 2) 

    # Extract bit planes
    all_bit_planes = np.apply_along_axis(my_cv.tup_extract_bit_plane, axis=1, arr=combinations, image=color_channels)  
    all_bit_planes = all_bit_planes.flatten()
       
    # Use header to get message size
    msg_number_of_bits = my_bits.convert_bits_to_int(all_bit_planes[:64]) + 64 + 24

    # Get only message bits
    msg_bits = all_bit_planes[:msg_number_of_bits] 
    
    return msg_bits.astype(np.uint8)
