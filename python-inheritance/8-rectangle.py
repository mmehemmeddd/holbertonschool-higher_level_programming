#!/usr/bin/python3
"""Module that defines a Rectangle class inheriting from BaseGeometry."""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class with private width and height."""

    def __init__(self, width, height):
        """Initialize Rectangle with width and height validated as positive integers."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
