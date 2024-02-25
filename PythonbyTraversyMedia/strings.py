# Strings in python are surrounded by either single or double quotation marks.abs

name = 'Brad'
age = 37

# Concatenate
print('Hello, my name is ' + name +' and i am '+ str(age))



# String Formatting

# Arguments by position
print('My name is {name} and i am {age}'.format(name=name, age=age))

# F-Strings (3.6+)
print(f'Hello, my name is {name} and i am {age}')

# String Methods

s = 'heLlo woRld'

# Capitalize the string
print('Capitalize the string:', s.capitalize())

# Make all uppercase
print('Make all uppercase:',s.upper())

# Make all lowercase
print('Make all lower:', s.lower())

# swap case
print('swap case:', s.swapcase())

# Get length
print('length of String:', len(s))

# Replace 
print('replace word:', s.replace('woRld', 'Everyone'))

# Count the specific char in string
sub = 'e'
print(f'count of char {sub} in string:', s.count(sub))

# Start with
print('if string starts with word return true:', s.startswith('heLlo'))

# Ends with
print('if string ends with word return true:', s.endswith('woRld'))
print('if string ends with word (s) return true:', s.endswith('s'))

# Split into a list
print('splits the string into a list:', s.split())

# find the position of the char
print('position of the char (w) in string:', s.find('w'))

# is all alphanumeric
print('is all alphanumeric ?:',s.isalnum())

# is all alphabetic
print('is all alphabetic ?:', s.isalpha())

# is all numeric
print('is all numeric ?:', s.isnumeric())






