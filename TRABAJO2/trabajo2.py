loop = 1

while loop < 10:
    # Se le pide al usuario que ingrese cierta información
    sustantivo = input("Elige un sustantivo: ")
    sustantivo_plural = input("Elige un sustantivo en plural: ")
    sustantivo2 = input("Elige otro sustantivo: ")
    lugar = input("Nombra un lugar: ")
    adjetivo = input("Elige un adjetivo (palabra que describe): ")
    sustantivo3 = input("Elige un sustantivo: ")

    # Muestra la historia basada en la información proporcionada por el usuario
    print("------------------------------------------")
    print("Sé amable con tu", sustantivo, "de pies -")
    print("Pues un pato podría ser el", sustantivo2, "de alguien,")
    print("Sé amable con tus", sustantivo_plural, "en", lugar)
    print("Donde el clima siempre es", adjetivo, ".")
    print()
    print("Puedes pensar que esto es el", sustantivo3, ",")
    print("Bueno, lo es.")
    print("------------------------------------------")

    loop = loop + 1

