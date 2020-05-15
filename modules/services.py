import os

# temp file
TMP_FILE = ".logs/"
class Service:

    @staticmethod
    def copy_file(filename):
        """
        copy selected file into a copie file
        """
        from shutil import copyfile
        copyfile(filename, TMP_FILE)
    
    @staticmethod
    def remove_tmp_file():
        """
        remove temp file created by copy_file() func
        """
        os.remove(TMP_FILE)