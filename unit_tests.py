
import time 
import os

from src import my_cli
from src import encode
from src import decode
from src import inspect

# Compare two binary files to see if they are equal
def compare_binaries(file1, file2):
    with open(file1, 'rb') as f1, open(file2, 'rb') as f2:
        return f1.read() == f2.read()

#------------------------------------------------------------------------------

def create_folder_if_not_exists(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"Folder '{folder_path}' created successfully.")

def generic_test(test_id, image_path, file_path, image_output_path, file_output_path, bit_planes):
  
    print("\nRunning test: ", test_id)

    create_folder_if_not_exists(image_output_path)
    create_folder_if_not_exists(file_output_path)

    # Encoding
    start_time = time.time()
    print("Encoding...")
    image_output_path = encode.encode_file(image_path, file_path, bit_planes, image_output_path)
    print("Encoding time: %s seconds" % (time.time() - start_time)) 
    print("Image encoded and saved at: ", image_output_path)

    # Decoding
    print("Decoding...")
    start_time = time.time()
    file_output_path = decode.decode_file(image_output_path, file_output_path, bit_planes)
    print("Decoding time: %s seconds" % (time.time() - start_time))
    print("File decoded and saved at: ", file_output_path)

    # Compare original and decoded files 
    result = compare_binaries(file_path, file_output_path)
    if result:
        print("\033[2;32;40m [OK] \033[0;0m")
    else:
        print("\033[2;31;40m [FAIL] \033[0;0m")

#------------------------------------------------------------------------------ 

# Test small txt encoded into small png 

def test1():
    # Encoding variables
    image_path        = "data/images/baboon.png"
    file_path         = "data/messages/highway.txt"
    image_output_path = "data/encoded_images"
    bit_planes        = [0, 1, 2]
    bit_planes        = list(dict.fromkeys(bit_planes))

    # Decoding variables
    file_output_path  = "data/decoded_messages"

    # Compare original and decoded files
    generic_test(1, image_path, file_path, image_output_path, file_output_path, bit_planes)

#------------------------------------------------------------------------------

# Test big txt encoded into small png using more bit planes

def test2():
    # Encoding variables
    image_path        = "data/images/lenna.png"
    file_path         = "data/messages/frankenstein.txt"
    image_output_path = "data/encoded_images"
    bit_planes        = [0, 1, 2, 3, 4]
    bit_planes        = list(dict.fromkeys(bit_planes))

    # Decoding variables
    file_output_path  = "data/decoded_messages"

    # Compare original and decoded files
    generic_test(2, image_path, file_path, image_output_path, file_output_path, bit_planes)

#------------------------------------------------------------------------------
    
# Test big txt encoded into small png using more bit planes but different order

def test3():
    # Encoding variables
    image_path        = "data/images/watch.png"
    file_path         = "data/messages/frankenstein.txt"
    image_output_path = "data/encoded_images"
    bit_planes        = [2, 0, 5, 1]
    bit_planes        = list(dict.fromkeys(bit_planes))

    # Decoding variables
    file_output_path  = "data/decoded_messages"

    # Compare original and decoded files
    generic_test(3, image_path, file_path, image_output_path, file_output_path, bit_planes)
    
#------------------------------------------------------------------------------

# Test big txt encoded into big png different

def test4():
    # Encoding variables
    image_path        = "data/images/big.png"
    file_path         = "data/messages/big.txt"
    image_output_path = "data/encoded_images"
    bit_planes        = [0, 1, 2]
    bit_planes        = list(dict.fromkeys(bit_planes))

    # Decoding variables
    file_output_path  = "data/decoded_messages"

    # Compare original and decoded files
    generic_test(4, image_path, file_path, image_output_path, file_output_path, bit_planes)

#------------------------------------------------------------------------------

# Test small image encoded into big image

def test5():
    # Encoding variables
    image_path        = "data/images/big.png"
    file_path         = "data/messages/monalisa.png"
    image_output_path = "data/encoded_images"
    bit_planes        = [0, 1, 2]
    bit_planes        = list(dict.fromkeys(bit_planes))

    # Decoding variables
    file_output_path  = "data/decoded_messages"

    # Compare original and decoded files
    generic_test(5, image_path, file_path, image_output_path, file_output_path, bit_planes)
    
#------------------------------------------------------------------------------

# Test audio encoded into big image

def test6():
    # Encoding variables
    image_path        = "data/images/big.png"
    file_path         = "data/messages/music.mp3"
    image_output_path = "data/encoded_images"
    bit_planes        = [1, 3]
    bit_planes        = list(dict.fromkeys(bit_planes))

    # Decoding variables
    file_output_path  = "data/decoded_messages"

    # Compare original and decoded files
    generic_test(6, image_path, file_path, image_output_path, file_output_path, bit_planes)

#------------------------------------------------------------------------------

# Test text with different characters encoded into big image

def test7():
    # Encoding variables
    image_path        = "data/images/big.png"
    file_path         = "data/messages/01 - The Fellowship Of The Ring.txt"
    image_output_path = "data/encoded_images"
    bit_planes        = [0, 1, 2]
    bit_planes        = list(dict.fromkeys(bit_planes))

    # Decoding variables
    file_output_path  = "data/decoded_messages"

    # Compare original and decoded files
    generic_test(7, image_path, file_path, image_output_path, file_output_path, bit_planes)

#------------------------------------------------------------------------------

# Test gif encoded into big image

def test8():
    # Encoding variables
    image_path        = "data/images/big.png"
    file_path         = "data/messages/mario.gif"
    image_output_path = "data/encoded_images"
    bit_planes        = [0, 1, 2]
    bit_planes        = list(dict.fromkeys(bit_planes))

    # Decoding variables
    file_output_path  = "data/decoded_messages"

    # Compare original and decoded files
    generic_test(8, image_path, file_path, image_output_path, file_output_path, bit_planes)

#------------------------------------------------------------------------------
    
# Test mp4 encoded into big image

def test9():
    # Encoding variables
    image_path        = "data/images/big.png"
    file_path         = "data/messages/rick_roll.mp4"
    image_output_path = "data/encoded_images"
    bit_planes        = [3, 1, 2]
    bit_planes        = list(dict.fromkeys(bit_planes))

    # Decoding variables
    file_output_path  = "data/decoded_messages"

    # Compare original and decoded files
    generic_test(9, image_path, file_path, image_output_path, file_output_path, bit_planes)
 
    
#------------------------------------------------------------------------------

# Run all unit tests
def unit_tests():
    my_cli.start()
    print("\033[2;31;43m [WARNING] \033[0;0m")
    print("Unit tests just test the encoding and decoding functions, not the whole CLI. Edit this file carefully")

    test1()
    test2()
    test3()
    test4()
    test5()
    test6()
    test7()
    test8()
    test9()
    
    my_cli.end()

if __name__ == "__main__":
    unit_tests()
