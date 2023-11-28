def es_palindromo(palabra):
    palabra = palabra.lower()
    return palabra == palabra[::-1]

def verificar_palindromos():
    palabras = []
    print("Por favor, ingresa cinco palabras:")

    for i in range(5):
        palabra = input(f"Palabra {i + 1}: ")
        palabras.append(palabra)

    palindromos = [palabra for palabra in palabras if es_palindromo(palabra)]

    if palindromos:
        print("\n¡Al menos una de las palabras ingresadas es un palíndromo!")
        print("Palíndromos encontrados:")
        for palindromo in palindromos:
            print("-", palindromo)
    else:
        print("\nNinguna de las palabras ingresadas es un palíndromo.")

# Verificar palíndromos entre las palabras ingresadas por el usuario
verificar_palindromos()
