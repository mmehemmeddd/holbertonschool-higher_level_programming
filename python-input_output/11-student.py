#!/usr/bin/python3
"""Student class with reload functionality."""


class Student:
    """Defines a student with save and reload capabilities."""

    def __init__(self, first_name, last_name, age):
        """Initializes student instances."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance."""
        if isinstance(attrs, list) and all(isinstance(s, str) for s in attrs):
            res = {}
            for k in attrs:
                if k in self.__dict__:
                    res[k] = self.__dict__[k]
            return res
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance from a dict."""
        for key, value in json.items():
            setattr(self, key, value)
