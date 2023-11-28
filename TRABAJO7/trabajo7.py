import random

def adivina_el_numero():
    numero_secreto = random.randint(1, 50)
    intentos = 0

    print("¡Bienvenido al juego de adivinar el número entre 1 y 50!")

    while True:
        intento = int(input("Intenta adivinar el número: "))

        if intento < 1 or intento > 50:
            print("Por favor, elige un número dentro del rango de 1 a 50.")
            continue

        intentos += 1

        if intento < numero_secreto:
            print("El número es mayor. Intenta de nuevo.")
        elif intento > numero_secreto:
            print("El número es menor. Intenta de nuevo.")
        else:
            print(f"¡Felicitaciones! ¡Has adivinado el número {numero_secreto} en {intentos} intentos!")
            break

        continuar = input("¿Quieres seguir intentando? (sí/no): ")
        if continuar.lower() != "sí" and continuar.lower() != "si":
            print(f"El número correcto era {numero_secreto}. ¡Gracias por jugar!")
            break

# Iniciar el juego
adivina_el_numero()
