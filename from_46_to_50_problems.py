""" 
Write a function triplets that takes a number n as argument and returns a list of triplets such
that sum of first two elements of the triplet equals the third element using numbers below n. Please note that (a,
b, c) and (b, a, c) represent same triplet.

"""

def triplets(n):
    # return [(x, y, x + y) for x in range(1,n) for y in range(x, n) if x + y < n]
    return [(x, y, x + y) for x in range(1, n) for y in range(x, n) if x + y < n]

# print(triplets(5))



""" Problem 47: Write a function enumerate that takes a list and returns a list of tuples containing
(index,item) for each item in the list

"""

# def enumerate(lst):
#     return [(i, lst[i]) for i in range(len(lst))]

# print(enumerate(["a", "b", "c"]))

# lst = ["a", "b", "c"]

# for index, item in enumerate(lst):
#     print(index, item)


""" 
Problem 48: Write a function array to create an 2-dimensional array. The function should take both dimensions
as arguments. Value of each element can be initialized to None:
"""

def array(rows, cols):
    """
    Create a 2-dimensional array with specified dimensions.
    
    Args:
    - rows: int, number of rows in the array
    - cols: int, number of columns in the array
    
    Returns:
    - list of lists, a 2-dimensional array with dimensions rows x cols
    """

    return [[None for _ in range(cols)] for _ in range(rows)]

    """
    created without list comprehension
    array_2d = [] 
    # Iterate over each row
    for _ in range(rows):
        # Create a new row with 'cols' number of 'None' elements
        new_row = [None for _ in range(cols)]
        # Append the new row to the 2D array
        array_2d.append(new_row)
    
    # Return the 2D array
    return array_2d 
    """

a = array(2, 3)
# print(a)

a[0][0] = 1
a[0][2] = 3

a[1][0] = 5
a[1][2] = 7

# print(a)

""" 

Problem 49: Write a python function parse_csv to parse csv (comma separated values) files.

"""
# print(open('test.csv').read()) # Displays all the csv file data.

def parse_csv(filename):
    """
    Parse a CSV file and return its contents as a list of dictionaries.

    Args:
    - file_path: str, path to the CSV file

    Returns:
    - list of dictionaries, where each dictionary represents a row in the CSV file
    """

    # csv_data = []

    # with open(filename, 'r') as file:

    #     headers = file.readline().strip().split(',')

    #     for line in file:

    #         values = line.strip().split(',')

    #         row_dic = {}
    #         for i in range(len(headers)):
    #             row_dic[headers[i]] = values[i]

    #         csv_data.append(row_dic)

    # return csv_data

    """
    Parse CSV file and return its contents as a list of lists.

    Args:
    - file_path: str, path to the CSV file

    Returns:
    - list of lists, where each inner list represents a row in the CSV file
    """

    """
    using normal way
    """
    # with open(filename, 'r') as file:
    # csv_data = []  # Initialize an empty list to store parsed data
    # lines = file.strip().split('\n')  # Split the content into lines
    # for line in lines:  # Iterate over each line
    #     row = line.strip().split(',')  # Split the line into values
    #     csv_data.append(row)  # Append the row to the list
    # return csv_data  # Return the list of lists


    with open(filename , 'r') as file:
        return [line.strip().split(',') for line in file]

# print(parse_csv('test.csv'))


""" 
Problem 50: Generalize the above implementation of csv parser to support any delimiter and comments.

"""

def parse_csv_extend(filename, delimiter=',', comments='#'):
    """
    Parse a CSV file and return its contents as a list of dictionaries.
    """
    csv_data = []
    with open(filename, 'r') as file:
        for line in file:
            if line.startswith(comments): # skips the lines which start with # 
                continue
            print(line)
            values = line.strip().split(delimiter) # split them into pieces and put these pieces in a list
            print(values)
            csv_data.append(values) # putting these  values (lists) in our csv_data list

        return csv_data # returning the csv_data list


print(parse_csv_extend('test.csv'))




