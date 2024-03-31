
from . import my_files_io
from . import my_bits
from . import my_cv

import numpy as np

### Message Encoding Protocol ###
# [ number of bit planes used - 3 bits ] [ bit planes info - máx 24 bits ] [ size of file - 64 bits] 
# [ extension - 24 bits ] [                       message bits - variable                          ]

def encode_file(image_path, file_path, bit_planes, output_path):
    image        = my_cv.read(image_path)
    message_bits = my_bits.read_file_to_binary_array(file_path)
    
    encoded_img = encode(image, message_bits, bit_planes)

    image_output_path = output_path + "/encoded_" + my_files_io.get_file_name(image_path)
    my_cv.write(encoded_img, image_output_path)
    
    return image_output_path
    
def encode(img, msg_bits, bit_planes):
    num_bit_planes                 = len(bit_planes)
    h, w, number_of_color_channels = img.shape
    
    # Size check
    buffer_size      = (w * h) 
    max_buffers      = number_of_color_channels * len(bit_planes)  
    total_image_size = max_buffers * buffer_size 
    if(len(msg_bits) > total_image_size):
        raise ValueError("The message is too long to be encrypted in the image.")

    # Number of buffers needed to store the message
    number_of_needed_buffers = int(np.ceil(len(msg_bits) / buffer_size)) 

    # Mask to do vectorized operation while encrypting the message
    mask = np.zeros(number_of_needed_buffers * buffer_size, dtype=np.bool_)
    mask[:len(msg_bits)] = 1
   
    # Resize message bits and mask
    msg_bits.resize((number_of_needed_buffers*h, w), refcheck=False)
    mask.resize((number_of_needed_buffers*h, w), refcheck=False) 

    # Split image into color channels
    color_channels = my_cv.extract_color_channels(img)
    channel_index  = 0

    # Encrypt message
    for i in range(number_of_needed_buffers):
        # get the bit plane number and color channel index combination to be altered
        bit_plane_number  = bit_planes[i % len(bit_planes)]
        channel_index     += (i % len(bit_planes) == 0 and i != 0)
 
        # get the correct buffer chunks
        msg_bits_chunk = msg_bits[i*h:(i+1)*h, 0:w] 
        mask_chunk     = mask[i*h:(i+1)*h, 0:w]
        
        # get the correct bit plane
        bit_plane      = my_cv.extract_bit_plane(color_channels[channel_index], bit_plane_number)
        new_bit_plane  = np.where(mask_chunk, msg_bits_chunk, bit_plane)

        # replace bit plane
        color_channels[channel_index] = my_cv.replace_bit_plane(color_channels[channel_index], new_bit_plane, bit_plane_number)
        
    encoded_img = np.stack((color_channels), axis=-1)    
    return encoded_img
