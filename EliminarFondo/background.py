import os
from datetime import datetime
from removebg import RemoveBg

class BackgroundRemover:
    def __init__(self, inputFolder, outputFolder):
        self.inputFolder = inputFolder
        self.outputFolder = outputFolder

    def process_images(self):
        timestamp = datetime.now().strftime("%Y-%m-%d %H.%M.%S")
        process_folder = os.path.join(self.outputFolder, timestamp)
        # Verificar si la carpeta de salida existe, si no, crearla
        os.makedirs(process_folder, exist_ok=True)

        # Verificar si la carpeta de entrada existe
        for filename in os.listdir(self.inputFolder):
            if filename.endswith((".jpg", ".png", ".jpeg")):
                input_path = os.path.join(self.inputFolder, filename)
                output_path = os.path.join(process_folder, filename)
                self._remove_background(input_path, output_path)
                self._move_original(input_path, process_folder)

    def _remove_background(self, input_p, output_p):
        with open(input_p, "rb") as inp, open(output_p, 'wb') as outp:
            background_output = RemoveBg(inp.read())
            outp.write(background_output)

    def _move_original(self, input_p, process_folder):
        originals_folder = os.path.join(process_folder, "originals")
        os.makedirs(originals_folder, exist_ok=True)

        filename = os.path.basename(input_p)
        new_path = os.path.join(originals_folder, filename)
        os.rename(input_p, new_path)

if __name__ == "__main__":
    input_folder = "input"
    output_folder = "output"
    
    remover = BackgroundRemover(input_folder, output_folder)
    remover.process_images()
