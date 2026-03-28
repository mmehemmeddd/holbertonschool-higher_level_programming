#!/usr/bin/python3
"""Module to safely print elements from a list."""


def safe_print_list(my_list=[], x=0):
    """Prints x elements of a list, safely handling out of bounds."""
    count = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            count += 1
        except IndexError:
            break
    print("")
    return count
