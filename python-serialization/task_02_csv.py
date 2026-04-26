#!/usr/bin/python3
import csv
import json

def convert_csv_to_json(csv_filename):
    """
    CSV faylını oxuyur və məlumatları 'data.json' faylına 
    JSON formatında yazır.
    
    Parametrlər:
    csv_filename (str): Oxunacaq CSV faylının adı.
    
    Geri qaytarır:
    bool: Proses uğurla tamamlanarsa True, xəta baş verərsə (məsələn, fayl tapılmazsa) False.
    """
    try:
        # CSV faylını oxumaq üçün açırıq
        with open(csv_filename, 'r', encoding='utf-8') as csv_file:
            # DictReader hər sətri lüğətə (dictionary) çevirir
            csv_reader = csv.DictReader(csv_file)
            
            # Bütün lüğətləri bir siyahıya (list) yığırıq
            data_list = list(csv_reader)
            
        # Siyahını JSON formatında 'data.json' faylına yazırıq
        with open('data.json', 'w', encoding='utf-8') as json_file:
            # indent=4 parametri JSON faylının daha oxunaqlı olmasını təmin edir
            json.dump(data_list, json_file, indent=4)
            
        return True
        
    except FileNotFoundError:
        # Fayl tapılmadıqda False qaytarırıq
        return False
    except Exception:
        # Digər gözlənilməz xətalarda da False qaytarırıq
        return False
