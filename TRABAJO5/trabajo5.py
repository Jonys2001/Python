# Función para generar el acrónimo
def generar_acronimo(significado):
    # Dividir las palabras en el significado completo y generar el acrónimo
    palabras = significado.split()
    acronimo = ''.join(word[0].upper() for word in palabras)
    return acronimo

# Pedir al usuario el significado completo para obtener el acrónimo
significado = input("Ingrese el significado completo: ")

# Generar y mostrar el acrónimo correspondiente
acr = generar_acronimo(significado)
print("El acrónimo es:", acr)
