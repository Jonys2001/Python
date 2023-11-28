def calcular_propina(factura_total, personas, dividir_desigual=False):
    propina_18 = factura_total * 0.18
    propina_20 = factura_total * 0.20
    propina_25 = factura_total * 0.25

    total_con_18 = factura_total + propina_18
    total_con_20 = factura_total + propina_20
    total_con_25 = factura_total + propina_25

    propina_por_persona = {
        '18%': propina_18 / personas,
        '20%': propina_20 / personas,
        '25%': propina_25 / personas
    }

    total_por_persona = {
        '18%': total_con_18 / personas,
        '20%': total_con_20 / personas,
        '25%': total_con_25 / personas
    }

    if dividir_desigual:
        total_por_persona_desigual = {
            '18%': total_con_18 * 0.7 / personas + propina_18 * 0.7 / personas,
            '20%': total_con_20 * 0.7 / personas + propina_20 * 0.7 / personas,
            '25%': total_con_25 * 0.7 / personas + propina_25 * 0.7 / personas
        }
        return total_por_persona_desigual
    else:
        return total_por_persona

# Obtener la factura total y la cantidad de personas involucradas
factura = float(input("¿Cuál es el total de la factura hoy, por favor? $"))
numero_personas = int(input("¿Cuántas personas están involucradas? "))

# Calcular y mostrar la propina y el total por persona para diferentes porcentajes de propina
propina_total_por_persona = calcular_propina(factura, numero_personas)
for porcentaje, total in propina_total_por_persona.items():
    print(f"{porcentaje} de propina es ${total:.2f}, lo que lleva el total a ${factura + total:.2f} por persona.")

# Permitir la opción de dividir de manera desigual (70% - 30%)
dividir_desigual = input("¿Quieres dividir de manera desigual? (sí/no) ").lower()
if dividir_desigual == 'sí' or dividir_desigual == 'si':
    propina_total_por_persona_desigual = calcular_propina(factura, numero_personas, True)
    for porcentaje, total in propina_total_por_persona_desigual.items():
        print(f"División desigual (70% - 30%): {porcentaje} de propina es ${total:.2f}, lo que lleva el total a ${factura + total:.2f} por persona.")
