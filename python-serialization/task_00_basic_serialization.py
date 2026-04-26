#!/usr/bin/python3
import json

def serialize_and_save_to_file(data, filename):
    """
    Python lüğətini (dictionary) JSON formatında fayla yadda saxlayır.
    Əgər fayl artıq mövcuddursa, üzərinə yazılır.
    
    Parametrlər:
    data (dict): Serializasiya ediləcək Python lüğəti.
    filename (str): Çıxış (output) JSON faylının adı.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file)

def load_and_deserialize(filename):
    """
    JSON faylındakı məlumatı oxuyur və Python lüğəti kimi qaytarır.
    
    Parametrlər:
    filename (str): Oxunacaq JSON faylının adı.
    
    Geri qaytarır:
    dict: Deserializasiya olunmuş Python lüğəti.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
