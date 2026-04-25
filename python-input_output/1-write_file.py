#!/usr/bin/python3
"""
Bu modul verilmiş mətn faylını oxumaq və
onun məzmununu ekrana yazdırmaq üçün nəzərdə tutulub.
"""
def write_file(filename="", text=""):
    """
    Bu funksiya faylın adını qəbul edir, onu utf-8 formatında açır
    və məzmununu olduğu kimi ekrana (stdout) çap edir.
    """
    with open(filename, encoding="utf-8") as f:
        return f.write(text)
