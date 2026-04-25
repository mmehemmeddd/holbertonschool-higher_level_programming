#!/usr/bin/python3
"""
Bu modul verilmiş mətn faylını oxumaq və 
onun məzmununu ekrana yazdırmaq üçün nəzərdə tutulub.
"""


def read_file(filename=""):
    """
    Bu funksiya faylın adını qəbul edir, onu utf-8 formatında açır
    və məzmununu olduğu kimi ekrana (stdout) çap edir.
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
