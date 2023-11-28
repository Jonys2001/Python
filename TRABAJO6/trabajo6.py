def obtener_ganador(jugador1, jugador2):
    if jugador1 == jugador2:
        return "¡Es un empate!"
    elif (jugador1 == "piedra" and jugador2 == "tijeras") or (jugador1 == "papel" and jugador2 == "piedra") or (jugador1 == "tijeras" and jugador2 == "papel"):
        return "¡Jugador 1 gana!"
    else:
        return "¡Jugador 2 gana!"

def jugar_piedra_papel_tijeras():
    print("Bienvenido a Piedra, Papel o Tijeras!")
    print("Jugador 1, elige: piedra, papel o tijeras")
    jugador1 = input("Jugador 1: ").lower()
    while jugador1 not in ['piedra', 'papel', 'tijeras']:
        jugador1 = input("Por favor, elige piedra, papel o tijeras: ").lower()

    print("\nExcelente. Ahora es el turno del Jugador 2.")
    jugador2 = input("Jugador 2: ").lower()
    while jugador2 not in ['piedra', 'papel', 'tijeras']:
        jugador2 = input("Por favor, elige piedra, papel o tijeras: ").lower()

    resultado = obtener_ganador(jugador1, jugador2)
    print("\n" + resultado)

# Llamar a la función para iniciar el juego
jugar_piedra_papel_tijeras()
