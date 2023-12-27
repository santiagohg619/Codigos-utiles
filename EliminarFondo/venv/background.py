import os
from datetime import datetime
from removebg import removebg

class BackgroundRemover:
    def __init__(self, inputFolder, outputFolder):
        self.inputFolder = inputFolder
        self.outputFolder = outputFolder