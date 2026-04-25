#!/usr/bin/python3
"""Bu modul obyekti JSON formatına çevirir."""
import json


def to_json_string(my_obj):
    """Obyektin JSON string versiyasını qaytarır."""
    return json.dumps(my_obj)
