
def encontrar_numero(rango_inicial, rango_final):
    while rango_inicial <= rango_final:
        numero_medio = (rango_inicial + rango_final) // 2
        respuesta = input("¿Es {} el número que elegiste? (s/n): ".format(numero_medio))
        
        if respuesta.lower() == "s":
            print("¡Encontré el número!")
            return numero_medio
        elif respuesta.lower() == "n":
            respuesta = input("¿Es mayor que {}? (s/n): ".format(numero_medio))
            if respuesta.lower() == "s":
                rango_inicial = numero_medio + 1
            elif respuesta.lower() == "n":
                rango_final = numero_medio - 1
            else:
                print("Respuesta inválida. Por favor, responde 's' o 'n'.")
        else:
            print("Respuesta inválida. Por favor, responde 's' o 'n'.")
    
    print("No pude encontrar el número en el rango especificado.")
    return None

# Ejemplo de uso:
rango_inicial = 1
rango_final = 100

numero_elegido = encontrar_numero(rango_inicial, rango_final)
if numero_elegido is not None:
    print("El número elegido es:", numero_elegido)
