from PyPDF2 import PdfMerger
from tkinter import Tk, filedialog

def seleccionar_archivos():
    root = Tk()
    root.withdraw()
    archivos = filedialog.askopenfilenames(title="Seleccionar archivos PDF", filetypes=[("Archivos PDF", "*.pdf")])
    root.destroy()
    return archivos

def unir_pdfs(archivos, nombre_salida="resultado.pdf"):
    merger = PdfMerger()

    for archivo in archivos:
        merger.append(archivo)

    with open(nombre_salida, "wb") as salida:
        merger.write(salida)

if __name__ == "__main__":
    archivos_seleccionados = seleccionar_archivos()

    if archivos_seleccionados:
        nombre_salida = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("Archivos PDF", "*.pdf")])
        if nombre_salida:
            unir_pdfs(archivos_seleccionados, nombre_salida)
            print("Archivos PDF unidos exitosamente.")
        else:
            print("Operación cancelada.")
    else:
        print("No se seleccionaron archivos.")
