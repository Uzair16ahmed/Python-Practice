import os

def list_file_of_dir(dirpath):
    # for file in os.listdir(dirpath):
    #     print(file)
    files = os.listdir(dirpath)

    for file in files:
        print(file)

path = './PythonbyTraversyMedia'

list_file_of_dir(path)