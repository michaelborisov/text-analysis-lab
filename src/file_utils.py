import json


class FileUtils:

    def __init__(self):
        pass

    @staticmethod
    def fix_json(file_path):
        # Read in the file
        with open(file_path, 'r') as my_file:
            filedata = my_file.read()

        # Replace the target string
        filedata = filedata.replace('}', '},')
        filedata = filedata[0:len(filedata) - 2] + filedata[len(filedata) - 1:]
        filedata = '[' + filedata + ']'
        return filedata
