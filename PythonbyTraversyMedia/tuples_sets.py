# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

# Create tuple

fruits = ('Apples', 'Orange', 'Pineapples')
# fruits2 = tuple(('Banana', 'Mango', 'Strawberry'))

fruits2 = ('Apples',)
    # print(fruits2, type(fruits2)) # ('Apples',) <class 'tuple'>

# Get Value
    # print(fruits[1])

# Can't change value
    # fruits[0] = 'Pears'

# Delete tuple

    # print(fruits2)
    # del fruits2
    # print(fruits2)

# Get length 

    # print(len(fruits))




# A Set is a collection which is unordered and unIndexed. No duplicate members.
""" 
"update(iterable)": Adds elements from an iterable (such as another set, list, or tuple) to the set.

"discard(element)": Removes a specified element from the set if it is present. If the element is not present, it does nothing.

"pop()": Removes and returns an arbitrary element from the set. If the set is empty, it raises a KeyError.

"copy()": Returns a shallow copy of the set.

"len()": Returns the number of elements in the set. """
# Create set

fruits_set = {'Apples', 'Oranges', 'Mango'}

# Check if in set
# print('Apples' in fruits_set)

# Add to set
fruits_set.add('Grapes')

# Remove from set
fruits_set.remove('Grapes')

# Clear set
fruits_set.clear()

# Delete
del fruits_set

print(fruits_set)