from PyPDF2 import PdfMerger
from tkinter import Tk, filedialog

def seleccionar_archivos():
    # Función para seleccionar archivos PDF mediante una interfaz gráfica
    
    # Crea una ventana emergente de Tkinter sin mostrarla
    root = Tk()
    root.withdraw()
    
    # Abre el cuadro de diálogo para seleccionar archivos PDF
    archivos = filedialog.askopenfilenames(title="Seleccionar archivos PDF", filetypes=[("Archivos PDF", "*.pdf")])
    
    # Cierra la ventana después de la selección
    root.destroy()
    
    return archivos

def unir_pdfs(archivos, nombre_salida="resultado.pdf"):
    # Función para unir archivos PDF en uno solo
    
    # Inicializa un objeto PdfMerger
    merger = PdfMerger()

    # Agrega cada archivo de la lista al objeto PdfMerger
    for archivo in archivos:
        merger.append(archivo)

    # Escribe el archivo de salida fusionado
    with open(nombre_salida, "wb") as salida:
        merger.write(salida)

if __name__ == "__main__":
    # Ejecuta el código solo si este script es el principal

    # Obtiene la lista de archivos PDF seleccionados por el usuario
    archivos_seleccionados = seleccionar_archivos()

    if archivos_seleccionados:
        # Solicita al usuario el nombre de salida para el archivo unido
        nombre_salida = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("Archivos PDF", "*.pdf")])

        if nombre_salida:
            # Une los archivos PDF seleccionados y guarda el resultado
            unir_pdfs(archivos_seleccionados, nombre_salida)
            print("Archivos PDF unidos exitosamente.")
        else:
            print("Operación cancelada.")
    else:
        print("No se seleccionaron archivos.")
