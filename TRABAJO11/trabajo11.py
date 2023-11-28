# Base de datos ficticia de canciones
canciones = {
    'Justin Bieber': ['Baby', 'Sorry', 'Yummy'],
    'Drake': ['Hotline Bling', 'Gods Plan', 'One Dance'],
    'Beyonce': ['Flawless', 'Single Ladies', 'Halo'],
    'Eminem': ['Lose Yourself', 'Stan', 'Not Afraid']
}

def mostrar_canciones_por_artista(artista):
    if artista in canciones:
        print(f"\nEstas son las canciones de {artista}:")
        for idx, cancion in enumerate(canciones[artista], start=1):
            print(f"{idx}. {cancion}")
        return True
    else:
        print("Lo siento, no se encontraron canciones para ese artista.")
        return False

def mostrar_letra(cancion_seleccionada):
    letras = {
        'Flawless by Beyonce': """
        ------- Flawless by Beyonce ------------
        I'm out that H, town coming coming down
        I'm coming down, drippin' candy on the ground
        H, Town, Town, I'm coming down, coming down
        Drippin' candy on the ground...
        """,
        'Hotline Bling by Drake': """
        ------- Hotline Bling by Drake ------------
        You used to call me on my cell phone
        Late-night when you need my love
        Call me on my cell phone
        Late-night when you need my love...
        """,
        # ... Otras letras de canciones aquí
    }

    if cancion_seleccionada in letras:
        print(letras[cancion_seleccionada])
    else:
        print("Lo siento, no se encontró la letra de esa canción.")

# Menú principal
print("¡Bienvenido! Por favor, selecciona un artista de esta lista:")
for idx, artista in enumerate(canciones.keys(), start=1):
    print(f"{idx}. {artista}")

while True:
    opcion_artista = int(input("Selecciona un número de artista: "))
    if 1 <= opcion_artista <= len(canciones):
        artistas = list(canciones.keys())
        artista_seleccionado = artistas[opcion_artista - 1]
        break
    else:
        print("Por favor, selecciona un número válido de artista.")

# Mostrar canciones del artista seleccionado
mostrar_canciones_por_artista(artista_seleccionado)

# Selección de una canción específica
while True:
    opcion_cancion = int(input("Selecciona un número de canción: "))
    if 1 <= opcion_cancion <= len(canciones[artista_seleccionado]):
        cancion_seleccionada = canciones[artista_seleccionado][opcion_cancion - 1]
        break
    else:
        print("Por favor, selecciona un número válido de canción.")

# Mostrar letra de la canción seleccionada
print(f"\nHas elegido {cancion_seleccionada} by {artista_seleccionado}. Aquí tienes la letra:")
mostrar_letra(f"{cancion_seleccionada} by {artista_seleccionado}")
