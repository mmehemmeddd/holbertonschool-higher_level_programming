#!/usr/bin/python3
"""Test file for Square class."""

Square = __import__('0-square').Square  # import the Square class

my_square = Square()
print(type(my_square))
print(my_square.__dict__)
