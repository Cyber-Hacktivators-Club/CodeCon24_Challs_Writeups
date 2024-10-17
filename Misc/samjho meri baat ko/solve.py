def hex_to_image(hex_file, output_image):
    try:
    
        with open(hex_file, 'r') as file:
            hex_data = file.read()
        image_data = bytes.fromhex(hex_data)

        with open(output_image, 'wb') as image:
            image.write(image_data)

        print(f"Image has been successfully created as {output_image}.")

    except FileNotFoundError:
        print(f"File {hex_file} not found. Please check the path.")


hex_file = "path to given file"  
output_image = 'image.jpg'  

hex_to_image(hex_file, output_image)
