
####################################################
# Additional functions to deal with bits and bytes #
####################################################

import os
import numpy as np
from . import my_files_io

# Functions to convert numpy bits array into a int
def convert_bits_to_int(binary_array): 
    powers_of_two = 1 << np.arange(len(binary_array))[::-1]
    return int(np.sum(binary_array * powers_of_two))

#------------------------------------------------------------------------------------------------
 
# Convert file binary data into numpy array of bits
# Using numpy.frombuffer() to interpret binary data as an array
def read_file_to_binary_array(file_path):
    # Read the file content
    binary_data  = my_files_io.read_file_into_bytes(file_path) 
    binary_array = np.unpackbits(np.frombuffer(binary_data, dtype=np.uint8)).astype(np.bool_)

    # Encode the number of bits of the file content + extension in the first 64 bits
    file_size       = len(binary_array)
    size_bits       = format(file_size, '064b')  # 64 bits for file size
    size_array      = np.array([int(bit) for bit in size_bits], dtype=np.bool_)
    binary_array    = np.concatenate((size_array, binary_array))

    # Encode the file extension into the numpy array
    extension       = os.path.splitext(file_path)[1][1:]  # Extract and remove leading '.'
    extension_bits  = ''.join(format(ord(char), '08b') for char in extension)
    extension_array = np.array([int(bit) for bit in extension_bits], dtype=np.bool_)
    binary_array    = np.concatenate((binary_array, extension_array))

    return binary_array

# Convert numpy bits array back to binary data and writes into a file
# Assumes that the first 64 bits are the encoded file size
# Assumes that the following 24 bits are the encoded file extension
def save_binary_array_to_file(binary_array, file_path):
    binary_array   = binary_array.astype(np.uint8)
   
    # Decode file size into an variable and remove the bits from the numpy array 
    file_size      = convert_bits_to_int(binary_array[:64])
    binary_array   = binary_array[64:]

    # Decode the file extension into a string and remove the bits from the numpy array
    extension_bits = ''.join(str(bit) for bit in binary_array[-24:])
    extension      = ''.join(chr(int(extension_bits[i:i+8], 2)) for i in range(0, len(extension_bits), 8))
    binary_array   = binary_array[:-24]

    # Convert the numpy array back to binary data and write into the file
    binary_data = np.packbits(binary_array.reshape(-1, 8))
    return my_files_io.write_bytes_into_file(binary_data, file_size, extension, file_path)
