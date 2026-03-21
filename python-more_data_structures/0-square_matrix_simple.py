#!/usr/bin/python3
"""Module that computes the square of a matrix."""


def square_matrix_simple(matrix=[]):
    """Returns a new matrix with squared values."""
    return [[x ** 2 for x in row] for row in matrix]
