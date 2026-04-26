#!/usr/bin/python i
mport xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    """
    Python lüğətini XML formatına çevirir və fayla yadda saxlayır.
    
    Parametrlər:
    dictionary (dict): XML-ə çevriləcək Python lüğəti.
    filename (str): Yadda saxlanılacaq XML faylının adı.
    """
    try:
        # Əsas (root) elementi yaradırıq, adı <data> olacaq
        root = ET.Element('data')
        
        # Lüğətin hər bir açar-dəyər cütünü (key-value) dövrə salırıq
        for key, value in dictionary.items():
            # Hər bir açar üçün əsas elementin (root) daxilində yeni alt element yaradırıq
            child = ET.SubElement(root, key)
            # Alt elementin mətnini (dəyərini) təyin edirik
            # XML yalnız mətn formatını dəstəklədiyi üçün dəyəri str() ilə sətrə çeviririk
            child.text = str(value)
            
        # XML ağacını (tree) yaradırıq
        tree = ET.ElementTree(root)
        
        # Ağacı göstərilən fayla yazırıq
        tree.write(filename, encoding='utf-8')
        
    except Exception as e:
        print(f"Xəta baş verdi (Serializasiya): {e}")

def deserialize_from_xml(filename):
    """
    XML faylını oxuyur və məlumatları Python lüğəti kimi qaytarır.
    
    Parametrlər:
    filename (str): Oxunacaq XML faylının adı.
    
    Geri qaytarır:
    dict: Bərpa edilmiş Python lüğəti.
    """
    try:
        # Boş bir lüğət yaradırıq
        result_dict = {}
        
        # XML faylını parse edirik (oxuyuruq və strukturu qururuq)
        tree = ET.parse(filename)
        
        # Əsas (root) elementi əldə edirik (yəni, <data> teqini)
        root = tree.getroot()
        
        # Əsas elementin daxilindəki bütün alt elementləri dövrə salırıq
        for child in root:
            # Teqin adını (tag) açar kimi, mətnini (text) isə dəyər kimi lüğətə əlavə edirik
            result_dict[child.tag] = child.text
            
        return result_dict
        
    except FileNotFoundError:
        print(f"Xəta: {filename} faylı tapılmadı.")
        return None
    except Exception as e:
        print(f"Xəta baş verdi (Deserializasiya): {e}")
        return None
