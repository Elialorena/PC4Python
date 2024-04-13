from pyfiglet import Figlet
import random

def imprimir_texto_con_fuente():
    # Obtener la lista de fuentes disponibles
    figlet = Figlet()
    fuentes_disponibles = figlet.getFonts()

    # Solicitar al usuario el nombre de una fuente o seleccionar una aleatoria
    fuente_seleccionada = input("Ingrese el nombre de una fuente (o presione Enter para seleccionar una aleatoria): ")
    if fuente_seleccionada == "":
        fuente_seleccionada = random.choice(fuentes_disponibles)
        print("Fuente seleccionada aleatoriamente:", fuente_seleccionada)
    elif fuente_seleccionada not in fuentes_disponibles:
        print("La fuente ingresada no es válida. Seleccione una de las siguientes fuentes:")
        print(", ".join(fuentes_disponibles))
        return

    # Solicitar al usuario un texto
    texto_imprimir = input("Ingrese el texto que desea imprimir: ")

    # Configurar la fuente seleccionada
    figlet.setFont(font=fuente_seleccionada)

    # Imprimir el texto utilizando la fuente seleccionada
    print(figlet.renderText(texto_imprimir))

if __name__ == "__main__":
    imprimir_texto_con_fuente()
