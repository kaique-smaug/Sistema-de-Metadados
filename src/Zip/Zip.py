from zipfile import ZipFile, ZIP_DEFLATED
from os.path import join, relpath
from os import walk

class Zip:
    def ziping(self, path: str, output_zip_name: str) -> None:
        """
        Compresses all .wav files in a directory into a zip archive.

        :param path: The directory path containing files to be zipped.
        :param output_zip_name: The name of the output zip file.
        """
        with ZipFile(output_zip_name, 'w', ZIP_DEFLATED) as zipf:
            # Iterate over all files and subdirectories within the specified path
            for root, dirs, files in walk(path):
                self._waw(zipf, root, files, path)

        return 0
    
    def _waw(self, zipf: ZipFile, root: str, files: list, path: str) -> None:
        """
        Adds .wav files to the zip file with relative paths.

        :param zipf: The ZipFile object for adding files.
        :param root: The current directory being iterated over.
        :param files: List of files in the current directory.
        :param path: The base directory to use for relative paths.
        """
        for file in files:
            if file.lower().endswith('.wav'):  # Checks for both .wav and .WAV extensions
                file_path = join(root, file)  # Gets the full file path
                # Adds the file to the zip archive with a relative path
                zipf.write(file_path, relpath(file_path, path))