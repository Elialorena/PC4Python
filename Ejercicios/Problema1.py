import requests

def obtener_precio_bitcoin():
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response.raise_for_status()  # Lanza una excepción si la solicitud no fue exitosa (código de estado diferente de 200)
        data = response.json()
        return data["bpi"]["USD"]["rate_float"]  # Retorna el precio actual de Bitcoin en USD como un número decimal
    except requests.RequestException as e:
        print("Error al realizar la solicitud a la API:", e)
        return None

def main():
    # Solicitar al usuario la cantidad de bitcoins
    while True:
        try:
            cantidad_bitcoins = float(input("Ingrese la cantidad de bitcoins que posee: "))
            break
        except ValueError:
            print("Ingrese un número válido.")

    # Obtener el precio actual de Bitcoin en USD
    precio_bitcoin = obtener_precio_bitcoin()

    if precio_bitcoin is not None:
        # Calcular el costo total de los bitcoins del usuario
        costo_total_usd = cantidad_bitcoins * precio_bitcoin

        # Mostrar el costo total en USD con cuatro decimales
        print(f"El costo actual de {cantidad_bitcoins} Bitcoins es: ${costo_total_usd:,.4f}")
    else:
        print("No se pudo obtener el precio actual de Bitcoin.")

if __name__ == "__main__":
    main()
