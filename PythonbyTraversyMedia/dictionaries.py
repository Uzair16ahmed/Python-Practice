# A Dictionary is a collection of unordered, changeable and indexed. no duplicate members. 

# Create Dictionary

person = {
    'first_name': 'john',
    'last_name': 'doe',
    'age': 25,
    'city': 'New York'
}
# print(person, type(person))


# Use constructor

# person2 = dict(first_name= 'sara', last_name='johnson', age='35', city='Ankik')
# print(person2, type(person2))


# Get a Value
# print(person['first_name'])
# print(person.get('last_name'))

# Add key/value
person['phone'] = '5555-5555'
# print(person)


# Get dict keys
# print(person.keys())


# Get dict values
# print(person.values())


# Get dict items
# print(person.items())


# Copy dict # spread method in javascript
person2 = person.copy()
person2['email'] = 'john@email.com'
print(person2)

# Remove Item
del(person['city'])
person.pop('phone')


# Clear 
person.clear()


# Get length
# print(len(person2))

# list of dict # in javascript a array of object

people = [
    {'name': 'martha', 'age': 30},
    {'name': 'john', 'age': 25},
    {'name': 'jane', 'age': 20}
]
print(people[1]['name']) # john
