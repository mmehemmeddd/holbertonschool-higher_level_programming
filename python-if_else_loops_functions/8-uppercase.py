#!/usr/bin/python3
def uppercase(str):
    for char in str:
        # Convert to ASCII number
        ascii_val = ord(char)
        
        # Check if it's in the lowercase range (a-z)
        if 97 <= ascii_val <= 122:
            # Subtract 32 to get the uppercase version
            char = chr(ascii_val - 32)
        
        print("{}".format(char), end="")
    print("")  # This prints the required new line at the very end
