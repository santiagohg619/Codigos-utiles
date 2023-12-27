import sys
import socket

target = socket.gethostbyname(input("Enter the ip address: "))

print("Scan target: " + target)
try:
    for port in range(1, 150):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target,port))
        if result == 0:
            print("The port {} is open".format(port))
        s.close()
except:
    print ("\nClosing...")
    sys.exit(0)