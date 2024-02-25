# A function is a block of code which only runs when it is called. In Python, we do not use 
# curly brackets, we use indentation with tabs or spaces

# Create function
def sayHello(name='Sam'):
    print(f'Hello {name}')

# sayHello()

# Return Values
def getSum(num1, num2):
    total = num1 + num2
    return total

num = getSum(7, 3)
# print(num)

# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression. 
# Very similar to JS arrow functions

getSub = lambda num1, num2 : num1 - num2

print(getSub(10, 3))































import os

def list_file_of_dir(dirpath):
    # for file in os.listdir(dirpath):
    #     print(file)
    files = os.listdir(dirpath)

    for file in files:
        print(file)

path = './PythonbyTraversyMedia'

# list_file_of_dir(path)