import os #sistema operativo y manejo de carpetas
from pytube import YouTube #videos de youtube
import flet as ft #UI de la app

def main(page):
    url = ft.TextField(label= 'URL', autofocus = True)
    submit = ft.ElevatedButton("Descargar")
    def click_boton(e):
        carpeta_actual = os.getcwd()
        yt = YouTube(url.value)
        video = yt.streams.get_highest_resolution()
        video.download(output_path = carpeta_actual)

    submit.on_click = click_boton
    page.add(url, submit)

ft.app(target = main)




