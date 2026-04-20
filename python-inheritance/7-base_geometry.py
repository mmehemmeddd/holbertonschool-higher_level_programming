#!/usr/bin/python3
"""
Bu modul BaseGeometry sinfini ehtiva edir.
"""


class BaseGeometry:
    """
    Həndəsi fiqurlar üçün baza sinfi.
    """

    def area(self):
        """
        Sahəni hesablayır.
        Həmişə Exception qaldırır, çünki hələ tətbiq edilməyib.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Verilmiş dəyərin düzgün (integer və > 0) olmasını yoxlayır.

        Args:
            name (str): Dəyərin adı (həmişə string olacağı fərz edilir).
            value (int): Yoxlanılacaq dəyər.

        Raises:
            TypeError: value tam ədəd (int) deyilsə.
            ValueError: value 0-a bərabər və ya kiçikdirsə.
        """
        # Strict (qəti) tip yoxlaması
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        
        # Dəyər yoxlaması
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
