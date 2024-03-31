
import time 

from src import my_cli
from src import encode
from src import decode
from src import inspect

def main():
    # Start CLI and show application banner
    my_cli.start()

    # Get user input for encoding or decoding or inspecting
    user_choice = my_cli.user_input_for_encoding_or_decoding()
   
    # Start encoding
    if(int(user_choice) == 0):
        image_path, file_path, output_path, bit_planes = my_cli.user_input_for_encoding()
         
        print("\nImage path:  ", image_path)
        print("File path:   ", file_path)
        print("Output path: ", output_path)
        print("Bit planes to use: ", bit_planes) 
        
        start_time = time.time()
        print("\nEncoding...")
        image_output_path = encode.encode_file(image_path, file_path, bit_planes, output_path)
        print("Encoding time: %s seconds" % (time.time() - start_time))
        print("Image encoded and saved at: ", image_output_path)
    
    # Start decoding
    elif(int(user_choice) == 1):
        image_path, output_path, bit_planes = my_cli.user_input_for_decoding() 

        print("Decoding...")
        start_time = time.time()
        file_output_path = decode.decode_file(image_path, output_path, bit_planes)
        print("Decoding time: %s seconds" % (time.time() - start_time))
        print("File decoded and saved at: ", file_output_path)
       
    # Start inspecting
    elif(int(user_choice) == 2):
        image_path, color_channels, bit_planes = my_cli.user_input_for_inspecting()
       
        print("\nImage path:  ", image_path)
        print("Color channels to inspect: ", color_channels)
        print("Bit planes to inspect: ", bit_planes)
        
        print("Inspecting...")
        inspect.inspect_image(image_path, color_channels, bit_planes)

    # End CLI and show goodbye message
    my_cli.end()
        
if __name__ == "__main__":
    main()
