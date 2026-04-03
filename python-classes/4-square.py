#!/usr/bin/python3
"""This module defines a Square class with getter and setter."""


class Square:
    """A class that defines a square."""

    def __init__(self, size=0):
        """Initialize the square with a specific size."""
        # Burada self.size yazırıq ki, birbaşa setter metodunu işə salsın
        # və yoxlamalardan (if şərtlərindən) keçsin.
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation."""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of the square."""
        return self.__size * self.__size
