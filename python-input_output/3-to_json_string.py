#!/usr/bin/python3
"""
Bu modul Python obyektini JSON formatında olan bir sətirə (string)
çevirmək üçün nəzərdə tutulub.
"""
import json


def to_json_string(my_obj):
    """
    Verilmiş obyekti (my_obj) qəbul edir və onun 
    JSON formatında olan string (mətn) versiyasını qaytarır.
    """
    return json.dumps(my_obj)
