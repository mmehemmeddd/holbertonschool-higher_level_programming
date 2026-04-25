#!/usr/bin/python3
"""Bu modul JSON mətnini Python obyektinə çevirir."""
import json


def from_json_string(my_str):
    """JSON string qəbul edib onu Python obyektinə çevirir."""
    return json.loads(my_str)
