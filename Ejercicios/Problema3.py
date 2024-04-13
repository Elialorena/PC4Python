import requests
import zipfile
from io import BytesIO
import os

# URL de la imagen a descargar
url = "https://images.unsplash.com/photo-1546527868-ccb7ee7dfa6a?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"

def descargar_imagen(url):
    try:
        # Realizar la solicitud GET para descargar la imagen
        response = requests.get(url)
        response.raise_for_status()  # Lanzar una excepción si la solicitud no fue exitosa
        
        # Crear un objeto BytesIO para almacenar los datos de la imagen en memoria
        imagen_bytes = BytesIO(response.content)
        return imagen_bytes
    except requests.RequestException as e:
        print("Error al descargar la imagen:", e)
        return None

def comprimir_imagen(imagen_bytes, nombre_archivo_zip):
    try:
        # Crear un archivo zip
        with zipfile.ZipFile(nombre_archivo_zip, "w") as zip_file:
            # Agregar la imagen al archivo zip
            zip_file.writestr("imagen.jpg", imagen_bytes.read())
        print("Imagen comprimida correctamente en", nombre_archivo_zip)
    except Exception as e:
        print("Error al comprimir la imagen:", e)

def descomprimir_zip(nombre_archivo_zip):
    try:
        # Crear un directorio para la descompresión
        directorio_destino = nombre_archivo_zip.replace(".zip", "")
        os.makedirs(directorio_destino, exist_ok=True)

        # Descomprimir el archivo zip
        with zipfile.ZipFile(nombre_archivo_zip, "r") as zip_file:
            zip_file.extractall(directorio_destino)
        print("Archivo zip descomprimido correctamente en", directorio_destino)
    except Exception as e:
        print("Error al descomprimir el archivo zip:", e)

if __name__ == "__main__":
    # Descargar la imagen
    imagen_bytes = descargar_imagen(url)
    if imagen_bytes:
        # Comprimir la imagen en un archivo zip
        comprimir_imagen(imagen_bytes, "imagen_comprimida.zip")

        # Descomprimir el archivo zip
        descomprimir_zip("imagen_comprimida.zip")
