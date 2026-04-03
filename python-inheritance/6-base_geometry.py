#!/usr/bin/python3
"""Module that defines a BaseGeometry class with an unimplemented area method."""


class BaseGeometry:
    """Base class for geometry objects."""

    def area(self):
        """Raises an exception because area() is not implemented."""
        raise Exception("area() is not implemented")
