
####################################################
#   Command Line Interface Module for User Input   #
####################################################

from . import my_files_io

# Banner and welcome message
def start():
    banner = my_files_io.read_file_into_string("src/banner.txt")
    print(banner) 
    print("Welcome to Trithemius.py, an Steganography tool to hide any type of file inside a PNG image of your choice!")
    print("Its works by enconding the file bits inside the bit planes of the input image color channels.")
    print("Encodes and Decodes blazingly fast :D\n")

# End use of the CLI
def end():
    print("\nThanks for using Trithemius.py! ;P")
       
#------------------------------------------------------------------------------------------------

# Get user input to determine if he wants to encode or decode a file
def user_input_for_encoding_or_decoding(): 
    user_input = None  
    while(user_input == None):
        print("\nDo you want to encode or decode a file ? Or inspect ? (0 for encode, 1 for decode, 2 for inspect): ", end='')
        user_input = my_files_io.read_expected_int_input(input().strip(), [0, 1, 2])
    return user_input

# Get user input for message encoding
def user_input_for_encoding():
    image_path = None
    while(image_path == None): 
        print("\nEnter the path of the PNG image you want to hide the message in: ", end='')
        image_path = my_files_io.check_file_path_PNG(input().strip())
   
    file_path = None
    while(file_path == None): 
        print("\nEnter the path of the file you want to hide in the image: ", end='')
        file_path = my_files_io.check_file_path(input().strip())
    
    output_path = None
    while(output_path == None): 
        print("\nWhere do you want to save the encoded image ? (leave blank to save on same folder of the input image): ", end='')
        output_path = my_files_io.check_folder_path(input().strip())    
    if(output_path == ""):
        output_path = my_files_io.get_path_parent(image_path)

    bit_planes = None
    while(bit_planes == None): 
        print("\nWhich bit planes do you want to use to encode the message ? Order matters! (e.g 0 1 2): ", end='')
        bit_planes = my_files_io.read_bounded_integer_list(0, 7, input().strip()) 
    bit_planes = list(dict.fromkeys(bit_planes))
        
    return image_path, file_path, output_path, bit_planes

# Get user input for message decoding
def user_input_for_decoding():
    image_path = None
    while(image_path == None): 
        print("\nEnter the path of the PNG image you want to reveal the secrets in: ", end='')
        image_path = my_files_io.check_file_path_PNG(input().strip())

    output_path = None
    while(output_path == None): 
        print("\nWhere do you want to save the decoded file ? (leave blank to save on same folder of the input image): ", end='')
        output_path = my_files_io.check_folder_path(input().strip())    
    if(output_path == ""):
        output_path = my_files_io.get_path_parent(image_path)

    bit_planes = None
    while(bit_planes == None): 
        print("\nWhich bit planes do you want to use to decode the message ? Order matters! (e.g 2 0 1): ", end='')
        bit_planes = my_files_io.read_bounded_integer_list(0, 7, input().strip()) 
    bit_planes = list(dict.fromkeys(bit_planes))
        
    return image_path, output_path, bit_planes

# Get user input for inspecting a image
def user_input_for_inspecting():
    image_path = None
    while(image_path == None): 
        print("\nEnter the path of the PNG image you want to inspect: ", end='')
        image_path = my_files_io.check_file_path_PNG(input().strip())

    color_channels = None
    while(color_channels == None):
        print("\nAvailable color channels - 0: Red, 1: Green, 2: Blue") 
        print("Which color channels do you want to inspect ? (e.g 0 1 2): ", end='')
        color_channels = my_files_io.read_bounded_integer_list(0, 2, input().strip()) 
    color_channels = list(dict.fromkeys(color_channels))
        
    bit_planes = None
    while(bit_planes == None): 
        print("\nWhich bit planes do you want to inspect ? (e.g 0 1 2): ", end='')
        bit_planes = my_files_io.read_bounded_integer_list(0, 7, input().strip()) 
    bit_planes = list(dict.fromkeys(bit_planes))

    return image_path, color_channels, bit_planes
