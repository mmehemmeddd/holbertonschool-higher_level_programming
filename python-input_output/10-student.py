#!/usr/bin/python3
"""Student class with filter definition."""


class Student:
    """Defines a student with filtering capability."""

    def __init__(self, first_name, last_name, age):
        """Initializes student instances."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns dictionary representation with optional filtering."""
        if isinstance(attrs, list) and all(isinstance(s, str) for s in attrs):
            res = {}
            for k in attrs:
                if k in self.__dict__:
                    res[k] = self.__dict__[k]
            return res
        return self.__dict__
