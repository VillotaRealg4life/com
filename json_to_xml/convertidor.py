### 📁 `json_to_xml/convertidor.py`

import json
import xml.etree.ElementTree as ET

def json_a_xml(obj, raiz):
    for clave, valor in obj.items():
        if isinstance(valor, dict):
            sub_elemento = ET.SubElement(raiz, clave)
            json_a_xml(valor, sub_elemento)
        elif isinstance(valor, list):
            for item in valor:
                sub_elemento = ET.SubElement(raiz, clave)
                json_a_xml(item, sub_elemento)
        else:
            sub_elemento = ET.SubElement(raiz, clave)
            sub_elemento.text = str(valor)

def convertir(archivo_entrada, archivo_salida):
    with open(archivo_entrada, 'r', encoding='utf-8') as f:
        datos = json.load(f)

    raiz = ET.Element('root')
    json_a_xml(datos, raiz)
    tree = ET.ElementTree(raiz)
    tree.write(archivo_salida, encoding='utf-8', xml_declaration=True)

# Ejecución
if __name__ == '__main__':
    convertir('ejemplo.json', 'salida.xml')
