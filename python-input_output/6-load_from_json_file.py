#!/usr/bin/python3
"""Bu modul JSON faylından oxuyaraq Python obyekti yaradır."""
import json


def load_from_json_file(filename):
    """JSON faylını oxuyub onu Python obyektinə çevirir."""
    with open(filename, mode="r", encoding="utf-8") as f:
        return json.load(f)
