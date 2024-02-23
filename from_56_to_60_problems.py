import time
import datetime
# import from_51_to_55_problems
import os
import collections


"""  
Problem 56: Write a function valuesort to sort values of a dictionary based on the key.

"""
# dictionary = {'x': 1, 'y': 2, 'a': 3}
def valueSort(d):
    # Sort the dictionary by keys and return a list of corresponding values
    return [value for key, value in sorted(d.items())]


# print(valueSort(dictionary))


"""  
Problem 57: Write a function invertdict to interchange keys and values in a dictionary. For simplicity,
assume that all values are unique
"""

dic = {'x': 1, 'y': 2, 'z': 3}
a = 3
def invertDict(dic):
    print(locals())  # {'dic': {'x': 1, 'y': 2, 'z': 3}} where dic is the local variable of the function
    new_dic = {}
    for key, value in dic.items():
        new_dic[value] = key
    return new_dic

# print(invertDict(dic))


"""   
  Understanding Python Execution Environment
"""
"""  
Python stores the variables we use as a dictionary. The "globals()" function returns all the globals variables in
the current environment.
"""

# print(globals())
# {'__builtins__': <module '__builtin__' (built-in)>, '__name__': '__main__', '__doc__': None}
""" Just like globals python also provides a function "locals" which gives all the local variables in a function.
 """

def f(name):
    return "Hello %(name)s!" % locals() # the locals() returns {'name': 'John'}

# print(f("John"))

"""  Further Reading:
• The article "A Plan for Spam" by "Paul Graham" describes a method of detecting spam using probability of
occurrence of a word in spam.
"""


""" Modules """

""" Modules are "reusable libraries of code" in Python. Python comes with many standard library modules.
    A module is imported using the import statement.
"""
# In this example, we’ve imported the time module and called the asctime function from that module, which returns current time as a string
# print(time.asctime()) # Fri Feb 23 11:26:02 2024
""" The pydoc command provides help on any module or a function. """
""" On Windows, the pydoc command is not available. The work-around is to use, the built-in "help" function."""
# print(help('time'))

""" In Python, it is possible to associate documentation for each module, function using docstrings. Docstrings are
strings written at the top of the module or at the beginning of a function. 

Under the hood, "python stores the documentation as a special field called __doc__".

"""
# print(os.getcwd.__doc__) # '__doc__': 'This is from problems 51 to 55\n\nno description \n' for file problems 51 to 55
# print(help('from_51_to_55_problems')) #



""" Standard Library """
#  what i am currently working can be considered as a library.

""" os module """
# The "os and os.path modules" provides functionality to work with files, directories etc.

""" Problem 58: Write a program to list all files in the given directory. """

def list_file_of_dir(dirpath):
    # for file in os.listdir(dirpath):
    #     print(file)
    files = os.listdir(dirpath)

    for file in files:
        print(file)

path = './PythonbyTraversyMedia'

# list_file_of_dir(path)

"""  Problem 59: Write a program extcount.py to count number of files for each extension in the given directory. The
program should take a directory name as argument and print count and extension for each available file extension.
"""
def extCount(dirPath):
    extension_counts = collections.defaultdict(int)
    for root, _, files in os.walk(dirPath):
        for file in files:
            if file.endswith(".py"):
                _, extension = os.path.splitext(file)
                extension_counts[extension] += 1
                # print(os.path.join(root, file))
            elif file.endswith(".csv"):
                _, extension = os.path.splitext(file)
                extension_counts[extension] += 1
                # print(root, file)
                # print(os.path.join(root, file))
            elif file.endswith(".txt"):
                _, extension = os.path.splitext(file)
                extension_counts[extension] += 1
                # print(root, file)

    #  Print the count and extension for each available file extension
    for extension, count in extension_counts.items():
        print(f"{extension}: {count}")

# def main():
#     dirPath = './'
#     extCount(dirPath)

# if __name__ == "__main__":
#     main()



""" 
Problem 60: Write a program to list all the files in the given directory along with their length and last modification
time. The output should contain one line for each file containing filename, length and modification date separated
by tabs. Hint: see help for os.stat.
"""

def list_files_with_info(directory):
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        #  check if each item is a file using os.path.isfile().
        if os.path.isfile(filepath):
            # Get file information using os.stat()
            file_stat = os.stat(filepath)

            # Extract file length and last modification time
            file_length = file_stat.st_size
            modification_time = datetime.datetime.fromtimestamp(file_stat.st_mtime)

            output = f"{filename}\t{file_length}\t{modification_time}"

            print(output)


path = './'
list_files_with_info(path)