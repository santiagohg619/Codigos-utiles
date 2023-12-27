def binary(decimal):
    # Convierte un número decimal a su representación binaria.
    
    # Inicializa una cadena vacía para almacenar la representación binaria
    binary = ""

    # Realiza la conversión a binario utilizando divisiones sucesivas por 2
    while decimal // 2 != 0:
        binary = str(decimal % 2) + binary
        decimal = decimal // 2

    # Añade el último residuo y retorna la representación binaria completa
    return str(decimal) + binary

# Solicita al usuario ingresar un número decimal
number = int(input("Insert a number: "))

# Imprime la representación binaria del número ingresado
print("Binary representation of the number is: ", binary(number))
