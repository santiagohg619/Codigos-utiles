import socket

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)

print("Ordenador: ", hostname)
print("Direccion IP: ", ip)