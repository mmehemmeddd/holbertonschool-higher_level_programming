#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Pad the tuples with zeros and slice only the first two elements
    a = (tuple_a + (0, 0))[:2]
    b = (tuple_b + (0, 0))[:2]
    
    # Add the corresponding elements together
    return (a[0] + b[0], a[1] + b[1])
