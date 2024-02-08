""" The For statement """
# Python provides for statement to iterate over a list. A for statement executes the specified block of code for
# every element in a list.

# for x in [1,2,3,4]:print(x)


# for i in range(10):print(i,i*i,i*i*i)
"""The built-in function zip takes two lists and returns list of pairs"""
# x = [1,2,3,4]
# y = [4,5,6,7]

# print(list(zip(x,y)))
# print(list(zip(["a", "b", "c"], [1, 2, 3])))

"""It is handy when we want to iterate over two lists together"""

# name = ["mark","pilgrim","south"]
# values = [1,2,3]

# for name, value in zip(name,values):
#     print(name, value)
"""Problem 21: Python has a built-in function sum to find sum of all elements of a list. Provide an implementation
for sum."""
# values = [1,2,3]
# print(sum(values))
"""Problem 22: What happens when the above sum function is called with a list of strings? Can you make your sum
function work for a list of strings as well."""
# name = ['mark','pilgrim','south']
# print(sum(name))
# cause a type error as sum only works on int and floats
# we can use join() to concatenate the strings
"""Problem 23: Implement a function product, to compute product of a list of numbers."""
# def product(x):
#     num = 1
#     for i in x:
#         num*=i
#     return print(num)

# values = [1,2,3]
# product(values)  

"""Problem 24: Write a function factorial to compute factorial of a number. Can you use the product function
defined in the previous example to compute factorial?"""

# def factorial(x):
#     num = 1
#     for i in range(1,(x+1)):
#         print('ad',i)
#         num*=i
#     print(f'factorial of {x} is: ',num)

# factorial(0)

"""
^
|
When the value of x is 0, the loop for i in range(1, (x + 1)): becomes for i in range(1, 1):, which means the loop will not execute at all.

This is because range(1, 1) creates an empty range. In Python, range(start, stop) generates numbers starting from start up to, but not including, stop. Since the start value is greater than or equal to the stop value, the resulting range is empty.

So, when you pass 0 as the value of x, the loop doesn't iterate at all, and the factorial remains 1. This is consistent with the mathematical definition of the factorial, where the factorial of 0 is defined to be 1
"""


# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1) # recursively calling the function in itself 

# print(factorial(5))

# print(list(range(1,1)))

"""Problem 25: Write a function reverse to reverse a list. Can you do this without using list slicing?"""

# def reverse(x):
#     length = len(x)
#     for i in range(length // 2):
#         x[i], x[length -i -1] = x[length -i -1], x[i]
#         print('swapping values', x)
#     print(x)

# values = [1,2,3,4,5]

# reverse(values)

"""Problem 26: Python has built-in functions min and max to compute minimum and maximum of a given list.
Provide an implementation for these functions. What happens when you call your min and max functions with a
list of strings?"""
# name = ['mark','before','banana']
# name = ['before','banana']
# values = [1,2,3,4,5]
# empty = []
def custom_min(lst):
    if not lst:
        raise ValueError("List is Empty")
    min_value = lst[0]
    for item in lst:
        if item < min_value:
            min_value= item
    return print(min_value)

# custom_min(name)

def custom_max(lst):
    if not lst:
        raise ValueError("List is Empty")
    max_value = lst[0]
    for item in lst:
        if item > max_value:
            max_value= item
    return print(max_value)

# custom_max(values)
# custom_max(name)
# custom_max(empty)


"""Problem 27: Cumulative sum of a list [a, b, c, ...] is defined as [a, a+b, a+b+c, ...]. Write a
function cumulative_sum to compute cumulative sum of a list. Does your implementation work for a list of
strings?"""
# values = [1,2,3,4,5]
# test = [4, 3, 2, 1]
def cumulative_sum(lst):
    """
        when list is [] it gives IndexError: list index out of range
        # for item in lst:
        #     sum.append(sum[-1] + item) 
        # return print(sum)
        
        # for i in range(len(lst)):
        #     sum.append(sum[i] + lst[i])
        # return print(sum)
        """
    if not lst:
        raise ValueError("List is Empty")
    sum = []
    total = 0
    for item in lst:
        total += item
        sum.append(total)
    return print(sum)


# cumulative_sum(values)
# cumulative_sum(test)

"""Problem 28: Write a function cumulative_product to compute cumulative product of a list of numbers.
"""

# values = [1,2,3,4,5]
# test = [4, 3, 2, 1]

def cumulative_product(lst):
    if not lst:
        raise ValueError("List is Empty")
    product = []
    num = 1
    for item in lst:
        num *= item
        product.append(num)
    return print(product)

# cumulative_product(values)
# cumulative_product(test)

"""Problem 29: Write a function unique to find all the unique elements of a list.
"""

# values = [1, 2, 1, 3, 2, 5, 5, 6]

def unique(lst):
    if not lst:
        raise ValueError("List is Empty")
    unique_lst = []
    for item in lst:
        if item not in unique_lst:
            unique_lst.append(item)
    return print(unique_lst)

# unique(values)

"""Problem 30: Write a function dups to find all duplicates in the list."""
# values = [1, 2, 1, 3, 2, 5, 5, 6]

def duplicate(lst):
    if not lst:
        raise ValueError("List is Empty")
    duplicate_list = []
    seen = []
    for item in lst:
        if item in seen and item not in duplicate_list:
            duplicate_list.append(item)
        else:
            seen.append(item)
    return print(duplicate_list)
# duplicate(values)

"""Problem 31: Write a function group(list, size) that take a list and splits into smaller lists of given size.
"""
# values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def group(lst, size):
    if not lst:
        raise ValueError("List is Empty")
    group_list = []
    for i in range(0, len(lst), size):
        group_list.append(lst[i:i+size])
    return print(group_list)

# group(values, 4)

""" Sorting Lists """
"""The "sort method" sorts a list in place"""
# a = [2, 10, 4, 3, 7]

# a.sort()
# print(a)

"""The "built-in function" sorted returns a new sorted list without modifying the source list.
"""

# b = [2, 10, 4, 3, 7]
# c = sorted(b)
# print(c)
# print(b)

"""The sort method works even when the list has different types of objects and even lists.
"""

"""The ""key parameter"" in the sort() method is used to specify a function that will be called on each element of the list before sorting."""
# a = [[2, 3], [1, 6]]
# a = ["hello", 1, "world", 45, 2]
# a = [str(x) for x in a]
# a.sort()
# print(a)
"""We can optionally specify a function as sort key."""
# a = [[2, 3], [4, 6], [6, 1]]
"""lambda x:: This defines an anonymous function that takes one argument x.
x[1]: This accesses the second element of the argument x."""

# a.sort(key=lambda x: x[1])
# print(a)
"""This sorts all the elements of the list based on the value of second element of each entry."""


"""Problem 32: Write a function lensort to sort a list of strings based on length.
"""
# values = ['python', 'perl', 'java', 'c', 'haskell', 'ruby']
def lensort(lst):
    if not lst:
        raise ValueError("List is Empty")
    lst.sort(key=lambda x: len(x))
    """# key used here tells how to sort the 
    # list which here is by length

    lstsorted = sorted(lst, key=len) 
    return print(lstsorted)
    """
    return print(lst)

# lensort(values)

"""Problem 33: Improve the unique function written in previous problems to take an optional key function as argument and use the return value of the key function to check for uniqueness.
"""
# values = ["python", "java", "Python", "Java"]

def key_unique(lst, key=None):
    if not lst:
        raise ValueError("List is Empty")
    unique_lst = []
    for item in lst:
        key_value = item if key is None else key(item)
        if key_value not in unique_lst:
            unique_lst.append(key_value)
    return print(unique_lst)

# key_unique(values, key=lambda x: x.lower())
# key_unique(values)


""" Tuples """

# parentheses ()

"""Tuple is a sequence type just like list, but it is immutable. A tuple consists of a number of values separated by
commas.
Tuples are immutable, which means once they are created, their contents cannot be changed. You cannot add, remove, or modify elements of a tuple after it has been created."""

a = (1,2,3)
# print(a[0])
# The built-in function len and slicing works on tuples too

# print(len(a))
# print(a[1:])

# The enclosing braces are optional.
# a = 1,2,3
# print(a[0])

# Since parenthesis are also used for grouping, tuples with a single value are represented with an additional comma.

# b = (1,)
# print(b)
# print(b[0])


""" Sets """

"""Sets are unordered collection of unique elements

Syntax: Sets are defined using curly braces {}
 or the set() constructor. 

Sets are commonly used in situations where you need to perform operations like testing for membership, eliminating duplicates,
and performing set operations such as union, intersection, and difference.
The fact that they contain only unique elements makes sets useful for tasks like counting distinct items in a collection or filtering out duplicates.
"""
# Two ways of initializing the sets

# x = set([1, 2, 3])
# y = {1, 2, 3}

# x.insert(0,4)
# for i in x:
    # print(i)

"""
"add(element)": Adds a single element to the set. If the element is already present, it does nothing.

"update(iterable)": Adds elements from an iterable (such as another set, list, or tuple) to the set.

"remove(element)": Removes a specified element from the set. Raises a KeyError if the element is not present.

"discard(element)": Removes a specified element from the set if it is present. If the element is not present, it does nothing.

"pop()": Removes and returns an arbitrary element from the set. If the set is empty, it raises a KeyError.

"clear()": Removes all elements from the set, making it empty.

"copy()": Returns a shallow copy of the set.

"len()": Returns the number of elements in the set.

in: Allows you to check if an element is present in the set using the in operator.

Set Operations: Sets support various operations such as union (|), intersection (&), difference (-), symmetric difference (^), and subset/superset checks (<=, >=).
"""


# Just like lists, the existance of an element can be checked
#  using the "in" operator. However, this operation is faster
# in sets compared to lists.

x = set([1, 2, 3])

# user_input = input("Enter an Integer to check if its in the Set")
# if int(user_input) in x:
#     print("yes")
# else:
#     print("no")


"""Problem 34: Reimplement the unique function implemented in the earlier examples using sets.
"""
# values = [1, 2, 1, 3, 2, 5, 5, 6]
def unique_using_set(lst):
    if not lst:
        raise ValueError("List is Empty")
    unique_set = set()
    for item in lst:
        if item not in unique_set:
            unique_set.add(item)
    return print(unique_set)

# unique_using_set(values)

""" Strings """

"""Strings also behave like lists in many ways.
 Length of a string can be found using built-in function len.
"""
# print(len("abrakadabra"))

"""
Indexing and slicing on strings
behave similar to that of lists.
"""
# a = "helloworld"

# print(a[0]) h
# print(a[1:6]) ellow
# print(a[2:]) lloworld
# print(a[:5]) hello
# print(a[-2]) l
# print(a[-2:]) ld
# print(a[:-2]) hellowor
# print(a[::-1] ) dlrowolleh

# if 'well' in a:
#     print("Yes")
# else:
#     print("No")

"""There are many useful methods on strings."""

"""The "split method" splits a string using a delimiter. If no delimiter is specified, it uses any whitespace char as
delimiter"""
# a = "Hello World Badass world"
# print(a.split()) ['Hello', 'World', 'Badass', 'world']
# print("a,b,c".split(",")) ['a', 'b', 'c']

"""The "join method" joins a list of strings."""

# print(" ".join(['Hello', 'world'])) Hello world
# print(",".join(['a', 'b', 'c'])) a,b,c

"""
The "strip method" returns a copy of the given string with leading and trailing whitespace removed. Optionally a
string can be passed as argument to remove characters from that string instead of whitespace.
"""
# a = ' hello world\n'
# print(a.strip()) hello world

# a = 'abrakadabra'
# print(a.strip('adabra')) # k
# print(a.strip('a')) brakadabr
# print(a.strip('abra')) kad
# print(a.strip('adbr')) k
# print(a.strip('ad')) brakadabr
# print(a.strip('abr')) kad
# print(a.strip('adab'))rakadabr
# print(a.strip('adabr')) k
# print(a.strip('adbr')) k

"""
Python supports formatting values into strings.
Although this can include very complicated expressions,
the most basic usage is to insert values into a string
with the %s placeholder.
"""
# a = 'hello'
# b = 'python'

# print("%s %s" % (a,b))
# print("Chapter %d: %s" % (2,'Data Structure'))

"""
Problem 35: Write a function extsort to sort a list of files based on extension.
"""

def extsort(lst):
    if not lst:
        raise ValueError("List is Empty")
    #custom key function specified using a lambda function. 
    # when a string is split its form change into []  
    lst.sort(key=lambda x: x.split('.')[-1])
    # [-1] takes the last element of list 
    # sorts based on that
    return print(lst)

# extsort(['a.c', 'a.py', 'b.py', 'bar.txt', 'foo.txt', 'x.c'])


""" working with files """

"""
Python provides a built-in function "open" to open a file,
 which returns a file object.
"""
"""
f = open('foo.txt', 'r') # open a file in read mode
f = open('foo.txt', 'w') # open a file in write mode
f = open('foo.txt', 'a') # open a file in append mode

The second argument to open is optional, 
which defaults to 'r' when not specified.
Unix does not distinguish binary files from text files but windows does.
On windows 'rb', 'wb', 'ab' should
be used to open a binary file in read, write and append mode 
respectively.
"""
file_path = 'foo.txt'
"""
The write method is used to write data to a file
opened in "write" or "append" mode.

"""
with open(file_path, 'w') as file:
    file.write('Hello New File\n')
    file.writelines(['Earth\n','Mars\n','jupiter\n'])
    file.close()

f = open(file_path, 'a')
f.write("Virtual world")
f.close()

"""
Contents of a file can be read line-wise using
"readline" and "readlines" methods.
The readline method returns empty string
when there is nothing more to read in a file.
"""
with open(file_path, 'r') as file:
    # print(file.read())
    # print(file.readline(), end='')
    # print(file.readline(), end='')
    # print(file.readlines(), end='')
    file.close()

"""Number of characters in a file is same as the length of its contents.
"""

def charcount(filename):
    return len(open(filename).read())

# print(charcount(file_path)) # 47

def wordcount(filename):
    return len(open(filename).read().split())

# print(wordcount(file_path)) # 8

def linecount(filename):
    return len(open(filename).readlines())

# print(linecount(file_path)) # 5

"""
    Problem 36: Write a program reverse.py to print lines of a file in reverse order.
"""

"""
import sys

def main(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        file.close()

    for line in reversed(lines):
        print(line.strip())


if __name__ == "__main__":
    filename = sys.argv[1]
    main(filename)

"""

"""
Problem 37: Write a program to print each line of a file in reverse order.

"""

"""
import sys

def main(filename):
    with open(filename, 'r') as file:

        for line in file:
            print(line.strip()[::-1])


if __name__ == "__main__":
    filename = sys.argv[1]
    main(filename)

"""

"""
Problem 38: Implement unix commands head and tail. The head and tail commands take a file as argument and prints its first and last 10 lines of the file respectively.
"""

"""
import sys

def head(filename):
    with open(filename, 'r') as file:
        for i, line in enumerate(file):
            if i >= 10:
                break
            print(line.strip())

def tail(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    for line in lines[-10:]:
        print(line.strip())

if __name__ == "__main__":
    filename = sys.argv[1]
    head(filename)
    print("space")
    tail(filename)

"""

"""
Problem 39: Implement unix command grep. The grep command takes a string and a file as arguments and
prints all lines in the file which contain the specified string
"""

"""
import sys

def grep(filename, string):
    with open(filename, 'r') as file:
        lines = file.readlines()
    for line in lines:
        if string in line:
            print(line.strip())

if __name__ == "__main__":
    filename = sys.argv[1]
    string = sys.argv[2]
    grep(filename, string)

"""

"""
Problem 40: Write a program wrap.py that takes filename and width as aruguments and wraps the lines longer
than width.
"""

"""
import sys

def wrap(filename, width):
    with open(filename, 'r') as file:
        lines = file.readlines()
    wrapped_lines = []

    for line in lines:
        while len(line) > width:
            wrapped_lines.append(line[:width])
            line = line[width:]
        wrapped_lines.append(line)

    for wrapped_line in wrapped_lines:
        print(wrapped_line.strip())

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python wrap.py <filename> <width>")
        sys.exit()
    
    filename = sys.argv[1]
    width = int(sys.argv[2])

    wrap(filename, width)

"""



