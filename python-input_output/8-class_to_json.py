#!/usr/bin/python3
"""Bu modul sinif obyektini lüğətə çevirmək üçün funksiyanı ehtiva edir."""


def class_to_json(obj):
    """Obyektin JSON-a çevrilə bilən atributlar lüğətini qaytarır."""
    return obj.__dict__
