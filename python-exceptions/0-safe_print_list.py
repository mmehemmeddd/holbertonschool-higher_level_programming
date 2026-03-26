#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    # Initialize a counter for the real number of printed elements
    count = 0
    
    # Loop x times
    for i in range(x):
        try:
            # Try to print the element at index i on the same line
            print("{}".format(my_list[i]), end="")
            # If successful, increment the counter
            count += 1
        except IndexError:
            # If we hit an index that doesn't exist, exit the loop
            break
            
    # Print a new line after all elements are printed
    print()
    
    # Return the actual number of elements printed
    return count
