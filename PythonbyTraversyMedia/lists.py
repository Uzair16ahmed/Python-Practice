# A List is a collection which is ordered and changeable. Allows duplicate members.

# Create List 
numbers = [1, 2, 3, 4, 5]
fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']



# Use a constructor
numbers2 = list((1, 2, 3, 4, 5)) # like 'new Array' in Javascript
print(numbers ,numbers2)


# Get a Value
print(fruits[2])


# Get length
print(len(fruits)) # arrays are zero based meaning they start with 0 index


# Append to list (put element to the end of list)
fruits.append('Pineapples')
print('Append Pineapples to list:',fruits)


# Remove from list
fruits.remove('Grapes')
print('Remove Grapes from list:',fruits)


# Insert into position(index)
fruits.insert(2, 'Strawberries')
print('Insert Strawberries into position(2)',fruits)


# Change Value
fruits[0] = 'Blueberries'
print('Change Value:',fruits)


# Remove with pop (using the index or position)
fruits.pop(2)
print('Remove with pop (using the index 2):',fruits)


# Reverse the list
fruits.reverse()
print('Reverse the list',fruits)


# sort the list(alphabetically)
fruits.sort()
print('sort the list',fruits)


# Reverse sort
fruits.sort(reverse=True)
print('Reverse sort',fruits)



