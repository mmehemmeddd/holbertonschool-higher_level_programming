#!/usr/bin/python3
"""Module that checks if an object inherits from a class."""


def inherits_from(obj, a_class):
    """Returns True if obj is a subclass of a_class (not the same class)."""
    return isinstance(obj, a_class) and type(obj) is not a_class
