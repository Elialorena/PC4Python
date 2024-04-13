def contar_lineas_codigo(archivo):
    try:
        if archivo.endswith(".py"):
            with open(archivo, "r") as file:
                lineas = file.readlines()
                lineas_codigo = 0
                for linea in lineas:
                    linea = linea.strip()  # Eliminar espacios en blanco al principio y al final
                    if linea and not linea.startswith("#"):
                        lineas_codigo += 1
                return lineas_codigo
        else:
            print("El archivo no es un archivo .py.")
    except FileNotFoundError:
        print("No se pudo encontrar el archivo.")

def main():
    ruta_archivo = input("Ingrese la ruta del archivo .py: ")
    lineas_codigo = contar_lineas_codigo(ruta_archivo)
    if lineas_codigo is not None:
        print(f"El archivo '{ruta_archivo}' tiene {lineas_codigo} líneas de código.")

if __name__ == "__main__":
    main()
