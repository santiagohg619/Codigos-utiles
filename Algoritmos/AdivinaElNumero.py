import random

def adivina_el_numero(x):
    print("=========================")
    print(" ¡Bienvenido(a) al Juego!")
    print("=========================")
    print("Tienes que adivinar el numerado generado por la computadora")
    print("")

    numero_aleatorio = random.randint(1,x) #Numeros aleatorios entre 1 y x

    prediccion = 0
    while prediccion != numero_aleatorio:
        #Ingreso del usuario:
        prediccion = int(input(f"Adivina un número entre 1 y {x}: "))
        if prediccion < numero_aleatorio:
            print("Intenta otra vez. Este número es muy pequeño.")
        elif prediccion > numero_aleatorio:
            print("Intenta otra vez. Este número es muy grande.")
    print("")        
    print("=========================")
    print("¡FELICIDADES!")
    print("=========================")
    print(f"Adivinaste el número {numero_aleatorio} correctamente.")

x =int(input("Ingresa un número positivo: "))
while x < 0:
    print ("El valor ingresado no es válido. Por favor intente nuevamente")
    x = int(input("Ingrese un número positivo"))

adivina_el_numero(x)
