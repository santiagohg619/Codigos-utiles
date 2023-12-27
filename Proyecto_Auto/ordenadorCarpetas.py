# Manejo de carpetas y archivos en sistema operativo: Crear, eliminar, mover,
# copiar, renombrar, etc.
import os
import shutil

extensionesDic = {
    '.txt':'DOCUMENTOS',
    '.docx':'DOCUMENTOS',
    '.pdf':'DOCUMENTOS',
    '.xlsx':'DOCUMENTOS',
    '.pptx':'DOCUMENTOS',
    '.jpg':'IMAGENES',
    '.png':'IMAGENES',
    '.jpeg':'IMAGENES',
}
#Carpeta predeterminada
prederterminada = 'OTROS'
#carpeta a ordenar
carpeta_ordenar = 'C:/Users/Santiago HG/Downloads'

archivos = os.listdir(carpeta_ordenar)
for archivo in archivos:
    archivo_origen_ruta = os.path.join(carpeta_ordenar,archivo)
    if os.path.isfile(archivo_origen_ruta):

        _, extension = os.path.splitext(archivo)

        nombre_carpeta = extensionesDic.get(extension.lower(), prederterminada)

        archivo_destino_ruta = os.path.join(carpeta_ordenar, nombre_carpeta)

        if not os.path.exists(archivo_destino_ruta):
            os.mkdir(archivo_destino_ruta)

        shutil.move(archivo_origen_ruta, archivo_destino_ruta)
