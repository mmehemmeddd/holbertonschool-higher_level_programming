#!/usr/bin/python3
"""Module that checks if an object is an instance or inherits from a class."""


def is_kind_of_class(obj, a_class):
    """Returns True if obj is an instance of or inherits from a_class."""
    return isinstance(obj, a_class)
