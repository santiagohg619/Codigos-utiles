import hashlib

find = 0

# Solicita al usuario ingresar el hash de la contraseña
input_hash = input("Hashed password: ")

# Solicita al usuario ingresar el nombre del archivo de diccionario
pass_doc = input("Insert dictionary: ")

try:
    # Intenta abrir el archivo de diccionario en modo lectura
    pass_file = open(pass_doc, 'r')
except:
    # Imprime un mensaje de error si no se encuentra el archivo
    print("ERROR: " + pass_doc + " has not been found")

# Itera a través de cada palabra en el archivo de diccionario
for word in pass_file:
    encrypted_word = word.encode('utf-8')

    # Calcula el hash MD5 de la palabra
    hashed_word = hashlib.md5(encrypted_word.strip())
    digest = hashed_word.hexdigest()

    # Compara el hash calculado con el hash ingresado por el usuario
    if digest == input_hash:
        # Imprime el mensaje si encuentra la contraseña
        print("Password found!!!! \n The password is: " + word)
        find = 1
        break

# Imprime un mensaje si la contraseña no se encuentra en el archivo de diccionario
if not find:
    print("The password was not found. " + pass_doc)
