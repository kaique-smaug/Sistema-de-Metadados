__version__ = '1.1.4'
"""
    Import all libraries bibliotecas what i am using at the script
"""
from os import makedirs, listdir, rename, remove,  O_WRONLY, O_CREAT, fdopen, open
from os.path import join, exists, splitext, isfile, isdir, basename
from shutil import copy, rmtree, move
from codecs import open as open_dcs
import time

class Files:
    def __init__(self):
        pass

    '''
        Copy any file
    '''
    def copy(self, path: str = None, file: str = None, destiny: str = None) -> None:
        self._pathFileComplet = join(path, file)
        copy(self._pathFileComplet, destiny)

    '''
        create a new folder from  of specifications what past and copy at the a place for other
    '''
    def craeteForlderAndCopy(self, name_folder: str = None, path : str = None, file: str = None, destiny: str = None) -> None:
        self._nameFolder = name_folder

        if not exists(name_folder):
            makedirs(self._nameFolder, exist_ok=True)
            self.copy(path, file, destiny)

        else:
            self.copy(path, file, destiny)

    '''
        Create folder from especigications 
    '''
    def create(self, name_folder: str = None):
        if not exists(name_folder):
            makedirs(name_folder, exist_ok=True)

    '''
        Rename alls files whet have at folfer
        Enough to spend the path and name at the files together the extension
        Must be spend a the format at list  
    '''
    def renameFiles(self, path: str = None, files: str = None, extension: str = None) -> None:

        itens = listdir(path)

        for i in range(len(itens)):
            self._folder = join(path, itens[i])
            self._renameFile = join(path, files[i])

            self._name, self._extension = splitext(itens[i]) 

            if self._extension != extension:
                rename(self._folder, f'{self._renameFile.replace(f"{self._extension}", "")}.{extension}')

    '''
        Check if files is at folder if not have wait teh download or something like that
    '''
    def check_file_with_extension(self, directory, extension) -> None:
        self._check = True
        while self._check:
            time.sleep(2)
            try:
                for file_name in listdir(directory):
                    if file_name.endswith(extension):
                        self._check = False
            except:
                self._check = True
        
    def delete(self, path) -> None:
        if exists(path):
            if isfile(path):
                remove(path)  # Remove the file
            elif isdir(path):
                rmtree(path)  # Remove the directory and its contents
    
    def move_file(self, nameFile, destinyFile) -> None:
            self._destination_path = join(destinyFile, basename(nameFile))
            move(nameFile, self._destination_path)
                
    def create_text(self, nameFile) -> None:
        self._nameFile = nameFile

        with fdopen(open(self._nameFile, O_WRONLY | O_CREAT), 'wb') as file:
            pass
            
    def convert_file(self, nameFile, newNameFile) -> None:
        self._filetxt = nameFile
        self._fileBat = newNameFile

        rename(self._filetxt, self._fileBat)
    
    # Method to adjust the content of a file
    def adjust_bar(self, path: str = None, path_destiny: str = None):
        self._list = []
        # Opens the specified file for reading and preparing to write
        with open_dcs(path, 'r+', encoding='utf-8') as f:
            # Reads the content of the file
            self._content = f.read()
            # Replaces triple backslashes with double backslashes in the content
            self._content = self._list.append(self._content.replace('\\\\\\', '\\\\'))

        # Opens the destination file for appending
        with open_dcs(path_destiny, 'a', encoding='utf-8') as f:
            # Writes each line from the list to the destination file
            for line in self._list:
                
                f.write(line)
