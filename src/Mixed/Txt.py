from os import fdopen, open, rename, makedirs, O_WRONLY, O_CREAT
from os.path import join, getsize, basename, exists
from datetime import datetime
from shutil import move

# Class responsible for file conversion and manipulation operations
class convertFile:
    def __int__(self):  # Constructor method of the class
        self._date = None  # Initializes the date variable as None

    # Method to create a text file
    def _createText(self, nameFile):
        self._nameFile = nameFile
        self._date = datetime.date(datetime.now())  # Gets the current date

        print('Start')
        try:
            print('Trying')
            # Tries to create the file with the specified name
            with fdopen(open(self._nameFile, O_WRONLY | O_CREAT), 'wb') as file:
                pass  # The file is created and immediately closed

        except Exception as e:
            pass  # In case of error, it is ignored (potentially risky)
    
    # Method to rename a file
    def _convertFile(self, nameFile, newNameFile):
        self._filetxt = nameFile
        self._fileBat = newNameFile

        rename(self._filetxt, self._fileBat)  # Renames the file

    # Method to create a directory
    def _crateForlder(self, name_folder):
        self._nameFolder = name_folder
    
        if not exists(self._nameFolder):
            makedirs(self._nameFolder, exist_ok=True)  # Creates the directory if it doesn't exist

    # Method to move a file to a new directory
    def _moveFile(self, nameFile, destinyFile):
        # Defines the destination path with the base name of the file
        self._destination_path = join(destinyFile, basename(nameFile))
        
        move(nameFile, self._destination_path)  # Moves the file to the destination

    # Method to rename and modify the content of a text file
    def _renameDataTxt(self, nameFile: str = None, selection: str = None, columnSelect: str = None, destiny_folder: str = None):
        self._date = datetime.date(datetime.now())  # Gets the current date
        self._filetxt = nameFile
        self._data = selection
        
        # Creates the text file if it doesn't exist
        if not exists(self._filetxt):
            with fdopen(open(self._filetxt, O_WRONLY | O_CREAT), 'wb') as file:
                pass
        
        try:
            if exists(self._filetxt):
                # Checks if the selected column is "LOCAL DE ESTOCAGEM"
                if columnSelect == "LocalDeEstocagem":
                    with fdopen(open(self._filetxt, O_WRONLY | O_CREAT), 'ab') as file:
                        if getsize(self._filetxt) > 1:
                            # Adds a copy command line to the file
                            file.write(f'copy "\\\{self._data}" "{destiny_folder}"\n'.encode('utf-8'))
                        else:
                            file.write(f'copy "\\\{self._data}" "{destiny_folder}"\n'.encode('utf-8'))
                else:
                    
                    # Adds a line to the text file for other columns
                    with fdopen(open(self._filetxt, O_WRONLY | O_CREAT), 'ab') as file:
                        if getsize(self._filetxt) > 1:
                            file.write(f'{self._data}\n'.encode('utf-8'))

                        else:
                            file.write(f'{self._data} \n'.encode('utf-8'))

        except Exception as e:
            # In case of error, logs the exception to a log file
            with fdopen(open(f'V:\Kaique\Robos\SAI\LOG_{self._date}.txt', O_WRONLY | O_CREAT),
                           'ab') as file:
                if getsize(f'V:\Kaique\Robos\SAI\LOG_{self._date}.txt') > 1:
                    file.write(f'Error: {e} {self._date} \n'.encode('utf-8'))
                else:
                    file.write(f'Error: {e} {self._date} \n'.encode('utf-8'))
        pass
