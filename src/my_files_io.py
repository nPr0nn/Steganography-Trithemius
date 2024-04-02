
####################################################
#    Module to deal with read and write files      #
####################################################

import os
import numpy as np 

# Read file into bytes
def read_file_into_bytes(file_path):
    with open(file_path, 'rb') as file:
        binary_data = file.read()
    return binary_data

# Write bytes into file
def write_bytes_into_file(binary_data, file_size, extension, file_path):
    file_path = file_path + '.' + extension
    with open(file_path, 'wb') as file:
        file.write(binary_data[:file_size])
    return file_path

# Create folder if it doesn't exist
def create_folder_if_not_exists(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"Folder '{folder_path}' created successfully.")
        
#------------------------------------------------------------------------------------------------

# Checks if the path exists and is a folder
def check_folder_path(folder_path):
    if folder_path == "":
        return folder_path
    if not os.path.exists(folder_path):
        print(f"  \033[2;31;43m [ERROR] \033[0;0m The path {folder_path} does not exist.")
        return None
    if not os.path.isdir(folder_path):
        print(f"  \033[2;31;43m [ERROR] \033[0;0m The path {folder_path} exists, but it's not a folder.")
        return None
    return folder_path

# Checks if the path exists and is a file
def check_file_path(file_path):
    if not os.path.exists(file_path):
        print(f"  \033[2;31;43m [ERROR] \033[0;0m The path {file_path} does not exist.")
        return None
    if not os.path.isfile(file_path):
        print(f"  \033[2;31;43m [ERROR] \033[0;0m The path {file_path} exists, but it's not a file.")
        return None
    return file_path

# Checks if the path exists and is a PNG image
def check_file_path_PNG(file_path):
    file_path = check_file_path(file_path)
    if not file_path:
        return None
    if not file_path.lower().endswith(".png"):
        print(f"  \033[2;31;43m [ERROR] \033[0;0m The path {file_path} exists, but it's not a PNG image.")
        return None
    return file_path

# Reads file content into string
def read_file_into_string(file_path, encoding='utf-8'):
    try:
        with open(file_path, 'r', encoding=encoding) as file:
            file_contents = file.read()
            return file_contents
    except FileNotFoundError:
        print("File not found.")
        return None
    except Exception as e:
        print("An error occurred:", e)
        return None

# Get the parent folder of the given file
def get_path_parent(file_path):
    return os.path.dirname(file_path)

# Get the file name
def get_file_name(file_path):
    return os.path.basename(file_path)

#------------------------------------------------------------------------------------------------

# Read binary input from user
def read_expected_int_input(user_input, expected_inputs):
    try:
        user_input = int(user_input)
        for expected_input in expected_inputs:
            if user_input == expected_input:
                return user_input
        else:
            print(f"  \033[2;31;43m [ERROR] \033[0;0m Please enter one of the following numbers: {expected_inputs}.")
            return None
    except:
        print(f"  \033[2;31;43m [ERROR] \033[0;0m Please enter a number.") 
        return None

# Reads a list of integers ensuring values are between 0 and 7 inclusive.
def read_bounded_integer_list(lower_bound, upper_bound, input):
    max_numbers = upper_bound - lower_bound + 1
    try:
        input_list = [int(x) for x in input.split()]
        if len(input_list) == 0:
            print(f"  \033[2;31;43m [ERROR] \033[0;0m Please enter at least one number.")
            return None
        if len(input_list) > max_numbers:
            print(f"  \033[2;31;43m [ERROR] \033[0;0m Please enter at most " + str(max_numbers) + " numbers.")
            return None
        if all(lower_bound <= num <= upper_bound for num in input_list):
            return input_list
        else:
            error_message = str(lower_bound) + " and " + str(upper_bound) + " inclusive."
            print(f"  \033[2;31;43m [ERROR] \033[0;0m Numbers must be between " + error_message)
            return None
    except ValueError:
        print(f"  \033[2;31;43m [ERROR] \033[0;0m Please enter only integers separated by spaces.")
        return None
