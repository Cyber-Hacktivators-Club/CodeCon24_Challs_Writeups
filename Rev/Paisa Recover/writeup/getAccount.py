def add_offset_to_string(input_string):
    result = ""
    for char in input_string:
        # Add 0x7 to the character's ASCII value
        new_char = chr(ord(char) + 0x7)
        result += new_char
    return result

# Example usage
input_string = "?:G@BLIKH))/2)+-./01"  
output_string = add_offset_to_string(input_string)
print(f"Modified string: {output_string}")
