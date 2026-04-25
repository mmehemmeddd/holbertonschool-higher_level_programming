#!/usr/bin/python3
"""
Bu modul verilmiş mətni (string) mətn faylının sonuna əlavə etmək
və əlavə edilmiş simvolların sayını qaytarmaq üçündür.
"""


def append_write(filename="", text=""):
    """
    Mətni faylın sonuna utf-8 formatında əlavə edir.
    Fayl yoxdursa, onu sıfırdan yaradır.
    Sonda əlavə olunan simvolların sayını (int) qaytarır.
    """
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
