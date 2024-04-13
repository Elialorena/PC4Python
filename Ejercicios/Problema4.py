import json

def guardar_datos_json(datos, nombre_archivo):
    with open(nombre_archivo, 'w') as archivo_json:
        json.dump(datos, archivo_json, indent=4)

# Ejemplo de uso:
datos_bitcoin = {
    '2024-04-13': 60000,
    '2024-04-14': 62000,
    # Agregar más datos aquí si es necesario
}
guardar_datos_json(datos_bitcoin, 'datos_bitcoin.json')
