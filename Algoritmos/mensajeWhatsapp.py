
import pyautogui, webbrowser
from time import sleep
numero_telefono = input("Ingrese su numero de telefono: ")
webbrowser.open("https://web.whatsapp.com/send?phone=+57"+numero_telefono)

sleep(10)

for i in range(1):
    pyautogui.typewrite("tú no mete cabra sarambanbiche")
    pyautogui.press("enter")



