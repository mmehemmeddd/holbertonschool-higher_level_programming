#!/usr/bin/python3
import pickle

class CustomObject:
    """
    Xüsusi Python obyektlərinin yaradılması, serializasiyası 
    və deserializasiyası üçün sinif.
    """
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Obyektin atributlarını tələb olunan formatda ekrana çap edir."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Cari obyekti pickle vasitəsilə binar formatda fayla yazır.
        Xəta baş verərsə None qaytarır.
        """
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Binar fayldan obyekti oxuyub bərpa edir.
        Fayl tapılmazsa və ya zədələnmişsə None qaytarır.
        """
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except Exception:
            return None
