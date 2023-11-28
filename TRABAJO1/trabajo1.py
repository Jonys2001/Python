# Dar la bienvenida al usuario
print("Bienvenido")
print("Por favor, ingresa un número entre 1 y 1000.")

while True:
    try:
        # Pedir al usuario que ingrese un número
        numero = int(input("¿Qué número estás pensando? "))

        # Verifica si el número es par o impar y mostrar un mensaje correspondiente
        if numero % 2 == 0:
            print("¡Ese es un número par!")
        else:
            print("¡Ese es un número impar! ¿Tienes otro número en mente?")
        break
    except ValueError:
        print("Por favor, ingresa un número válido.")

