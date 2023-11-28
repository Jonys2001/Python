def obtener_tipo_dominio(correo):
    dominios_populares = ["gmail.com", "yahoo.com", "hotmail.com", "outlook.com"]
    dominio = correo.split('@')[-1]

    if dominio.lower() in dominios_populares:
        return "popular"
    else:
        return "personalizado"

def analizar_correo():
    email = input("Por favor, ingresa tu dirección de correo electrónico: ")

    nombre_usuario, dominio = email.split('@')

    tipo_dominio = obtener_tipo_dominio(email)

    if tipo_dominio == "popular":
        print(f"Hey {nombre_usuario.capitalize()}, veo que tu correo está registrado con un proveedor popular como {dominio.capitalize()}. ¡Eso es genial!")
    else:
        print(f"Hey {nombre_usuario.capitalize()}, parece que tienes tu propia configuración personalizada en {dominio.capitalize()}. ¡Impresionante!")

    # Si deseas enviar un mensaje al anfitrión con esta información, aquí podrías implementar el código para enviar el mensaje.

# Ejecutar la función para analizar el correo electrónico
analizar_correo()
