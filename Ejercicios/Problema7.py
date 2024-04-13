import requests
import sqlite3

# Función para obtener los datos del tipo de cambio del dólar del API de SUNAT
def obtener_tipo_cambio():
    url = "https://api.apis.net.pe/v1/tipo-cambio"
    params = {
        "anio": 2023,
        "mes": None,
        "dia": None,
        "currencies": "USD",
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()["result"]
    else:
        print("Error al obtener los datos del tipo de cambio:", response.text)
        return []

# Función para crear la tabla 'sunat_info' en la base de datos 'base.db'
def crear_tabla():
    try:
        conn = sqlite3.connect("base.db")
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS sunat_info (
                fecha TEXT PRIMARY KEY,
                compra REAL,
                venta REAL
            )
        """)
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print("Error al crear la tabla:", e)

# Función para insertar los datos del tipo de cambio en la tabla 'sunat_info'
def insertar_datos(datos):
    try:
        conn = sqlite3.connect("base.db")
        cursor = conn.cursor()
        for fecha, valores in datos.items():
            compra = valores["compra"]
            venta = valores["venta"]
            cursor.execute("""
                INSERT OR IGNORE INTO sunat_info (fecha, compra, venta)
                VALUES (?, ?, ?)
            """, (fecha, compra, venta))
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print("Error al insertar datos en la tabla:", e)

# Función para mostrar el contenido de la tabla 'sunat_info'
def mostrar_tabla():
    try:
        conn = sqlite3.connect("base.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM sunat_info")
        rows = cursor.fetchall()
        print("Contenido de la tabla 'sunat_info':")
        for row in rows:
            print(row)
        conn.close()
    except sqlite3.Error as e:
        print("Error al mostrar el contenido de la tabla:", e)

def main():
    # Obtener los datos del tipo de cambio del API de SUNAT
    datos_tipo_cambio = obtener_tipo_cambio()

    # Crear la tabla 'sunat_info' si no existe
    crear_tabla()

    # Insertar los datos del tipo de cambio en la tabla 'sunat_info'
    insertar_datos(datos_tipo_cambio)

    # Mostrar el contenido de la tabla 'sunat_info'
    mostrar_tabla()

if __name__ == "__main__":
    main()
