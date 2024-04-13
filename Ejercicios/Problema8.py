import requests
import sqlite3
from datetime import datetime

def obtener_tipo_cambio():
    try:
        url = "https://api.apis.net.pe/v1/tipo-cambio"
        params = {
            "fecha": datetime.now().strftime("%Y-%m-%d"),
            "currencies": "PEN",
        }
        response = requests.get(url, params=params)
        if response.status_code == 200:
            return response.json()["result"]["values"]["PEN"]
        else:
            print("Error al obtener el tipo de cambio:", response.text)
            return None
    except Exception as e:
        print("Error al obtener el tipo de cambio:", e)
        return None

def obtener_precio_bitcoin():
    try:
        url = "https://api.coindesk.com/v1/bpi/currentprice.json"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()["bpi"]
        else:
            print("Error al obtener el precio del Bitcoin:", response.text)
            return None
    except Exception as e:
        print("Error al obtener el precio del Bitcoin:", e)
        return None

def crear_tabla_bitcoin():
    try:
        conn = sqlite3.connect("base.db")
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS bitcoin (
                fecha TEXT PRIMARY KEY,
                precio_usd REAL,
                precio_gbp REAL,
                precio_eur REAL,
                precio_pen REAL
            )
        """)
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print("Error al crear la tabla 'bitcoin':", e)

def insertar_datos_bitcoin():
    try:
        precios_bitcoin = obtener_precio_bitcoin()
        if precios_bitcoin:
            precio_pen = obtener_tipo_cambio() * precios_bitcoin["USD"]["rate_float"]
            fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            conn = sqlite3.connect("base.db")
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO bitcoin (fecha, precio_usd, precio_gbp, precio_eur, precio_pen)
                VALUES (?, ?, ?, ?, ?)
            """, (fecha, precios_bitcoin["USD"]["rate_float"], precios_bitcoin["GBP"]["rate_float"], precios_bitcoin["EUR"]["rate_float"], precio_pen))
            conn.commit()
            conn.close()
            print("Datos del Bitcoin insertados correctamente.")
        else:
            print("No se pudo obtener el precio del Bitcoin.")
    except sqlite3.Error as e:
        print("Error al insertar datos del Bitcoin:", e)

def calcular_precio_compra_10_bitcoins():
    try:
        conn = sqlite3.connect("base.db")
        cursor = conn.cursor()
        cursor.execute("SELECT precio_pen, precio_eur FROM bitcoin ORDER BY fecha DESC LIMIT 1")
        row = cursor.fetchone()
        if row:
            precio_compra_pen = row[0] * 10
            precio_compra_eur = row[1] * 10
            print(f"Precio de compra de 10 bitcoins en PEN: {precio_compra_pen}")
            print(f"Precio de compra de 10 bitcoins en EUR: {precio_compra_eur}")
        else:
            print("No hay datos disponibles en la tabla 'bitcoin'.")
        conn.close()
    except sqlite3.Error as e:
        print("Error al calcular el precio de compra de 10 bitcoins:", e)

def main():
    # Crear la tabla 'bitcoin' si no existe
    crear_tabla_bitcoin()

    # Insertar los datos del Bitcoin en la tabla 'bitcoin'
    insertar_datos_bitcoin()

    # Calcular el precio de compra de 10 bitcoins en PEN y EUR
    calcular_precio_compra_10_bitcoins()

if __name__ == "__main__":
    main()
