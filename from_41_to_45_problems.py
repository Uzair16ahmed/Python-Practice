"""
Problem 41: The above wrap program is not so nice because it is breaking the line at middle of any word. Can
you write a new program wordwrap.py that works like wrap.py, but breaks the line only at the word boundaries?
"""
"""
import sys

def wordwrap(text, width):
    words = text.split()
    lines = []
    current_line = words[0]

    for word in words[1:]:
        if len(current_line) + len(word) + 1 <= width:
            current_line += " " + word
        else:
            lines.append(current_line)
            current_line = word
    
    lines.append(current_line)
    return "\n".join(lines)

def main():
    if len(sys.argv) != 3:
        print("Usage: python wrap.py <filename> <width>")
        sys.exit()

    filename = sys.argv[1]
    width = int(sys.argv[2])

    with open(filename, 'r') as file:
        text = file.read()

    print(wordwrap(text, width))

if __name__ == "__main__":
    main()

"""

"""
Problem 42: Write a program center_align.py to center align all lines in the given file.

"""

"""
import sys

def center_align(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            max_length = max(len(line.strip()) for line in lines)

            print("Center Aligned Text:")
            for line in lines:
                centered_line = line.strip().center(max_length)
                print(centered_line)

    except FileNotFoundError:
        print("File not Found")


def main():
    if len(sys.argv) != 2:
        print("Usage: python center_align.py <filename>")
        sys.exit()
    
    filename = sys.argv[1]

    center_align(filename)


if __name__ == "__main__":
    main()

"""

""" 
    "List Comprehensions"

List Comprehensions provide a concise way of creating lists. Many times a complex task can be modelled in a
single line
"""

# a = list(range(10))
# print(a)
# print([x for x in a])
# print([x*x for x in a])
# print([x+1 for x in a])
""" It is also possible to filter a list using if inside a list comprehension """
# print([x for x in a if x % 2 == 0 ]) [0, 2, 4, 6, 8]
# print([x*x for x in a if x % 2 == 0 ])  [0, 4, 16, 36, 64]

# x is the outer loop and y is the inner loop
# print([( x, y) for x in range(5) for y in range(5) if (x+y) % 2 == 0])
# print([( x, y) for x in range(5) for y in range(5) if (x+y) % 2 == 0 and x != y])
# print([(x, y) for x in range(5) for y in range(x) if (x+y)%2 == 0])

# The following example finds all Pythagorean triplets using numbers below 25. (x, y, z) is a called
# pythagorean triplet if x*x + y*y == z*z.

n = 25
# print([(x, y, z) for x in range(1, n) for y in range(x, n) for z in range(y, n) if x*x + y*y == z*z])

"""
Problem 43: Provide an implementation for zip function using list comprehensions.

"""

# not working (understanding required)
# def custom_zip(*iterables): 
#     # Get the iterators for all input iterables
#     iterators = [iter(iterable) for iterable in iterables]

#     # Iterate over the shortest iterator
#     while True:
#         try:
#             # Yield a tuple containing the next element from each iterator
#             yield tuple(next(iterator) for iterator in iterators)
#         except StopIteration:
#             # If any iterator is exhausted, stop iteration
#             return

def custom_zip(*iterables):
    min_length = min(len(iterable) for iterable in iterables)

    return [tuple(iterable[i] for iterable in iterables) for i in range(min_length)]


# print(list(custom_zip([1, 2, 3], ['a', 'b', 'c'])))
# print( list(zip([1, 2, 3], ["a", "b", "c"])))


"""

Problem 44: Python provides a built-in function map that applies a function to each element of a list. Provide an
implementation for map using list comprehensions
"""
def square(x): return x*x

def custom_map(function, iterable):
    return [function(element) for element in iterable]


# print(custom_map(square, range(5)))


"""
Problem 45: Python provides a built-in function filter(f, a) that returns items of the list a for which
f(item) returns true. Provide an implementation for filter using list comprehensions.
"""
# without list comprehension
def custom_filter(func, iterable):
    filtered_list = []
    for x in iterable:
        if func(x):
            filtered_list.append(x)
    return filtered_list
def even(x): return x % 2 == 0
# using list comprehension
def custom_filter(function, iterables):
    return [iterable for iterable in iterables if function(iterable)]
    # return list(filter(function, iterables)) using built-in filter
    # return [iterable for iterable in iterables for element in iterable if function(element)]  using this input => print(custom_filter(even, [(1, 2, 3, 4), (5, 6, 7, 8)]))
print(custom_filter(even, [1, 2, 3, 4, 5, 6, 7, 8]))
"""

"""


