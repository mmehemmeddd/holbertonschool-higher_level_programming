#!/usr/bin/python3
"""Module that defines a MyList class."""


class MyList(list):
    """Custom list that can print itself sorted."""

    def print_sorted(self):
        """Prints the list in ascending sorted order."""
        print(sorted(self))
