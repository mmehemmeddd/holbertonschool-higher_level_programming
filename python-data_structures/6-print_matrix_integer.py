#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i in range(len(row)):
            if i == len(row) - 1:
                # If it's the last number in the row, don't add a space
                print("{:d}".format(row[i]), end="")
            else:
                # Otherwise, print the number followed by a space
                print("{:d} ".format(row[i]), end="")
        # Print a newline at the end of each row
        print()
