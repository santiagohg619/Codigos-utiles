def binary(decimal):
    binary = ""
    while decimal // 2 != 0:
        binary = str(decimal % 2) + binary
        decimal = decimal // 2
    return str(decimal) + binary

number = int(input("Insert a number: "))
print("Binary representation of the number is: ", binary(number))