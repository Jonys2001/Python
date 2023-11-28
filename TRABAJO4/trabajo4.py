# Función para validar el nombre
def validar_nombre(nombre):
    return nombre.replace(" ", "").isalpha() and len(nombre) > 0

# Función para validar la fecha de nacimiento
def validar_fecha(fecha):
    return True  # Por simplicidad, esta función devuelve True siempre

# Función para imprimir el resumen de la información ingresada
def imprimir_resumen(info):
    print("\nResumen de la información ingresada:")
    print("- Name:", info['nombre'])
    print("- Date of birth:", info['fecha_nacimiento'])
    print("- Address:", info['direccion'])
    print("- Personal goals:", info['metas_personales'])

# Solicitar información personal al usuario
informacion = {}
print("Por favor, ingresa tu información personal.")

# Solicitar y validar el nombre del usuario
nombre = input("¿Cómo te llamas? ")
while not validar_nombre(nombre):
    print("Por favor, ingresa un nombre válido.")
    nombre = input("¿Cómo te llamas? ")
informacion['nombre'] = nombre

# Solicitar y validar la fecha de nacimiento del usuario
fecha_nacimiento = input("¿Cuál es tu fecha de nacimiento? (Ejemplo: Jan 1, 2000) ")
while not validar_fecha(fecha_nacimiento):
    print("Por favor, ingresa una fecha de nacimiento válida.")
    fecha_nacimiento = input("¿Cuál es tu fecha de nacimiento? (Ejemplo: Jan 1, 2000) ")
informacion['fecha_nacimiento'] = fecha_nacimiento

# Solicitar la dirección del usuario (sin validación específica en este ejemplo)
direccion = input("¿Cuál es tu dirección? ")
informacion['direccion'] = direccion

# Solicitar las metas personales del usuario
metas_personales = input("¿Cuáles son tus metas personales? ")
informacion['metas_personales'] = metas_personales

# Imprimir el resumen de la información ingresada por el usuario
imprimir_resumen(informacion)
