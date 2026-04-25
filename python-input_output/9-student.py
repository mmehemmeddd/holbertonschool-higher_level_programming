#!/usr/bin/python3
"""Student class definition."""


class Student:
    """Defines a student."""

    def __init__(self, first_name, last_name, age):
        """Initializes student instances."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns dictionary representation."""
        return self.__dict__
