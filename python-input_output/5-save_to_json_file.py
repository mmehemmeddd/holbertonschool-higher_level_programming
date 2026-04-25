#!/usr/bin/python3
"Salam bu text json ucundur"
import json


def save_to_json_file(my_obj, filename):
    """Python obyektini (my_obj) JSON formatına salıb fayla (filename) yazır."""
    with open(filename, mode="w", encoding="utf-8") as f:
        json.dump(my_obj, f)
