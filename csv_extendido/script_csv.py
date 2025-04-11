import csv

def leer_csv(ruta):
    datos = []
    with open(ruta, newline='', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            datos.append(fila)
    return datos

def limpiar_datos(datos):
    return [fila for fila in datos if all(fila.values())]

def analizar_datos(datos):
    print(f"Total de filas válidas: {len(datos)}")
    for clave in datos[0]:
        print(f"- {clave}: {set(fila[clave] for fila in datos)}")

def exportar_datos(datos, ruta_salida):
    with open(ruta_salida, 'w', newline='', encoding='utf-8') as archivo:
        campos = datos[0].keys()
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(datos)

# Ejecución
if __name__ == '__main__':
    archivo = 'datos.csv'
    datos = leer_csv(archivo)
    datos_limpios = limpiar_datos(datos)
    analizar_datos(datos_limpios)
    exportar_datos(datos_limpios, 'salida.csv')
