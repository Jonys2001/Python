# Pregunta al usuario qué tiene en mente y cuenta las palabras en la oración
def contar_palabras_oracion():
    oracion = input("¿En qué estás pensando hoy? ")
    palabras = oracion.split()
    cantidad_palabras = len(palabras)
    print(f"¡Oh, genial! ¡Acabas de decirme lo que pasa por tu mente en {cantidad_palabras} palabras!")

# Función para contar las palabras en un archivo
def contar_palabras_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            contenido = archivo.read()
            palabras = contenido.split()
            cantidad_palabras = len(palabras)
            print(f"El archivo '{nombre_archivo}' contiene {cantidad_palabras} palabras.")
    except FileNotFoundError:
        print("El archivo no se encontró.")

# Llamada a la función para contar palabras en una oración ingresada por el usuario
contar_palabras_oracion()

# Pedir al usuario que ingrese el nombre del archivo para contar las palabras
nombre_archivo = input("Por favor, ingresa el nombre del archivo para contar las palabras: ")
contar_palabras_archivo(nombre_archivo)
