import time
import sys
# print("abc")


# x = 2 + 3
# print(x)


"""# Problem 2: Create a python script to print hello, world! four times
"""
# solution:

# for _ in range(4):

#     print("Hello, world")



"""# Problem 3: Create a python script with the following text and see the output.
"""
# solution:

# print(1 + 2) 

# print() used to show the value of 1 + 2


# swapping values of 2 variables

# x, y = 1, 2
# print(x, y)

# x, y = y, x
# print(x, y)


# When executing assignments, python evaluates the right hand side first and then assigns those values to the variables specified in the left hand side

# x = 4

# y = x + 1

# x = 2
# print(x, y) 


"""# Problem 5: What will be the output of the following program
"""
# x, y = 2, 6

# x, y = y, x + 2

# print(x, y)


"""# Problem 6: What will be the output of the following program.
"""
# a, b = 2, 3

# c, b = a, c + 1
# print( a, b , c)

# NameError: name 'c' is not defined


# print(4.2 + 4.2)


"""

Multi-line strings can be written using three single quotes or three double quotes

"""

# a piece of logic can also be associated with a name by defining a

# function.

def square(x):

    return x * x


# print(square(square(2)))



# Existing functions can be used in creating new functions


def sum_of_squares(x, y):

    return print(square(x) + square(y))


# sum_of_squares(2, 3)


# Functions are just like other values, they can assigned, passed as arguments to other functions etc.


# f = square


# print(f(2))


def fxy(f, x , y):

    return print(f(x) + f(y))


# fxy(square, 2, 3)


# It is important to understand, the scope of the variables used in functions.


# x = 0

# y = 0


def increment(x):

    y = x + 1
    return y

# Variables assigned in a function, including the arguments are called the local variables to the function. The

# variables defined in the top-level are called global variables.

# Changing the values of x and y inside the function incr won’t effect the values of global x and y.

# y = increment(5)
# print (x, y)

numerals = 0

def square1(x):
    global numerals
    numerals = numerals + 1

    return x * x

# # print(square1(2
# print(numerals)
# Problem 7: How many multiplications are performed when each of the following lines of code is executed?
# print(square1(5))
# print(square1(2*5))


"""# Problem 8: What will be the output of the following program?
"""
# x = 1
def f():
    return x
# In Python, when a variable is referenced inside a function, Python looks for that variable in the local scope first, then in enclosing functions' scopes, and finally in the global scope. If it's not found in any of these, Python raises a NameError.
# print(x)
# print(f())

"""# Problem 9: What will be the output of the following program?
"""
# x = 1
def f():
    x = 2
    return x
# print (x)
# print (f())
# print (x)

"""# Problem 10: What will be the output of the following program?
"""
# x = 1
def f():
    y = x # 1 
    x = 2 # 2
    return x + y 

    # which confuses Python. It doesn't know if x is a local variable or if it should be fetched from the global scope.
# print (x)
# print (f())
# print (x)

"""# Problem 11: What will be the output of the following program?
"""# x = 2 
def f(a):
    x = a * a
    return x

# y = f(3)
# print(x, y)

# functions can be called with keyword arguments
def difference(x, y):
    return x - y

# print(difference(5, 2))
# print(difference(x=5, y=2))
# print(difference(5, y=2))
# print(difference(y=2, x=5))

"""There is another way of creating functions, using the lambda operator"""

cube = lambda x: x ** 3
""" lambda doesn’t need a return. The body of the lambda is a single
expression."""
# fxy(cube, 2, 3)

""" Built-In functions """
# print(min(2,3))
# print(max(5,6))
# The built-in function len computes length of a string
# print (len("hello world"))
# The built-in function int converts string to ingeter and built-in function str converts integers and other type of
# objects to strings.
# print(int("50"))
# print(str(123))

"""# Problem 12: Write a function count_digits to find number of digits in the given number.
"""
def count_digits(x):
    return print(len(str(x)))

# count_digits(12345.446)

""" Methods """
""" Methods are special kind of functions that work on an object. """

# upper is a method available on string objects.
x = "hello"
# print(x.upper())

"""methods are also functions. They can be assigned to other variables and can be called separately."""

f = x.upper
# print(f())

"""# Problem 13: Write a function istrcmp to compare two strings, ignoring the case.
"""
def istrcmp(x, y):
    # return print(x.upper() == y.upper())
    return print(x.lower() == y.lower())

# istrcmp('python', 'PYTHON')


"""Conditional Expressions"""
""" Python provides various operators for comparing values. The result of a comparison is a boolean value, either True or False."""

# == equal to
# != not equal to
# < less than
# > greater than
# <= less than or equal to
# >= greater than or equal to

"""The conditional operators work even on strings - the ordering being the lexical order"""

"""There are few logical operators to combine boolean values"""
# a and b is True only if both a and b are True.
# a or b is True if either a or b is True
# not a is True only if a is False


"""# Problem 14: What will be output of the following program?
"""
# print (2 < 3 and 3 > 1) # True
# print (2 < 3 or 3 > 1) #  True 
# print (2 < 3 or not 3 > 1) # True
# print (2 < 3 and not 3 > 1) # False

"""# Problem 15: What will be output of the following program?
"""
# x = 4
# y = 5
# p = x < y or x < z
# print(p) 

"""# Problem 16: What will be output of the following program?
"""
# True , False = False , True
# print(True, False)
"""you cannot directly assign values to the built-in constants True and False. Attempting to do so would result in a syntax error."""

# print(2 < 3)

"""The If statement """
# x = 42
# if x % 2 == 0: print('even')
"""The code associated with if can be written as a separate indented block of code, which is often the case when
there is more than one statement to be executed."""

# x = 3
# if x % 2 == 0:
#     print('even')
# else:
#     print('odd')

"""The if statement can have optional elif clauses when there are more conditions to be checked."""

# x = 42 
# if x < 10:
#     print('one digit number')
# elif x < 100:
#     print('two digit number')
# else:
#     print('big number')


"""# Problem 17: What happens when the following code is executed? Will it give any error? Explain the reasons.
"""
# x = 2
# if x == 2:
    # print(x)
# else:
    # print(y)

# will produce NameError when x is not equal to 2

"""Problem 18: What happens the following code is executed? Will it give any error? Explain the reasons
"""
# x = 3

# if x == 2:
    # print(x)
# else:
    # x +

    # SyntaxError: invalid syntax

""" Lists """    

"""Lists are one of the great datastructures in Python."""
# built-in function also works for list 

x = [1, 2, 3]
# print(len(x))
# The [] operator is used to access individual elements of a list.
# print(x[2])
x[2] = 4
# print(x) 

"""Modules"""

# Modules are libraries in Python. Python ships with many standard library modules.
# A module can be imported using the import statement.
# for example
"""# time module"""
# print(time.asctime())
# The asctime function from the time module returns the current time of the system as a string.
"""sys module"""
# import sys
# print(sys.argv[1])
# python hello.py hello planet
# output: ['hello.py', 'hello', 'planet']
# As a convention, the first element of that list is the name of the program.

"""Problem 19: Write a program add.py that takes 2 numbers as command line arguments and prints its sum.
"""
# import sys

# def main():
    # x = int(sys.argv[1])
    # y = int(sys.argv[2])
    # return print(x + y)

# if __name__ == "__main__":
    # main()

""" Working with Data LISTs"""
# x = [1,2,3]
# b = [x,4,5]
# print(b[0])

""" using a built in function Range """
# The built-in function range can be used to create a list of integers
"""#  The range() function takes three arguments: start, stop, and step"""
"""#  print(list(range(4)))
print(len(list(range(4))))
# for num in range(4):
#     print(num)"""

# The + and * operators work even on lists
# x = [1,2,3]
# y = [4, 5]
# print(x + y)
# print(y *2)
# List can be indexed to get individual entries. Value of index can go from 0 to (length of list - 1).
# print(x[-1]) # prints last element of list
"""print(x[4])
when wrong index is used it python gives an error 
   print(x[4])
          ~^^^
IndexError: list index out of range
"""

"""Negative indices can be used to index the list from right."""

"""list slicing is used to get a part of the list """
# x = [1, 2, 3, 4, 5]
# print(x[1:4]) # [2, 3, 4]

# Even negative indices can be used in slicing. For example, the following examples strips the last element from the list.

# print(x[0:-1])  # [1, 2, 3, 4]

"""Slice indices have useful defaults; an omitted first index defaults to zero, an omitted second index defaults to the
size of the list being sliced."""
# print(x[:4]) # takes 0 as default [1, 2, 3, 4]
# print(x[1:]) # [2, 3, 4, 5] takes the size of the list being sliced

"""An optional third index can be used to specify the increment, which defaults to 1."""

# x = list(range(10))
# x = range(10) # range(0, 9, 2)
# print(x[:])
# print(x[0::2]) # [0, 2, 4, 6, 8]
# print(x[0:-1:2]) # [0, 2, 4, 6, 8]
# print(x[::-1]) # reverse the list [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

"""List members can be modified by assignment.
"""
# >>> x = [1, 2, 3, 4]
# >>> x[1] = 5
# >>> x
# [1, 5, 3, 4]

"""Presence of a key in a list can be tested using (in) operator.
"""
# x = [1, 2, 3, 4]
# print(2 in x)

"""Values can be appended to a list by calling append method on list.
A method is just like a function, but it is
associated with an object and 
can access that object when it is called.
We will learn more about methods when we study classes."""

# x = [1, 2, 3, 4]
# x.append(5)
# print(x) #[1, 2, 3, 4, 5]

"""Problem 20: What will be the output of the following program?"""
x = [0, 1, [2]]
x[2][0] = 3
print(x) # [0,1,[3]]
x[2].append(4)
print(x) # [0,1,[3,4]]
x[2] = 2
print(x) # [0,1,2]
