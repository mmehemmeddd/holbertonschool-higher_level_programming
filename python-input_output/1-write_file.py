#!/usr/bin/python3
"""
Bu modul verilmiş mətni (string) mətn faylına yazmaq
və yazılmış simvolların sayını qaytarmaq üçündür.
"""


def write_file(filename="", text=""):
    """
    Mətni fayla utf-8 formatında yazır və yazılan simvolların sayını qaytarır.
    Fayl yoxdursa yaradır, varsa məzmununu silib yenidən yazır.
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
