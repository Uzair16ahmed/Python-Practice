# Python has functions for creating, reading, updating and deleting files.

# Open a file
myfile = open('myfile.txt', 'w')

# Get some info
print('Name :', myfile.name)
print('is closed :', myfile.closed)
print('Opening mode :', myfile.mode)


# Write to file
myfile.write('i am starting to love programming')
myfile.write(' and i will be consistent.')
myfile.close()

# Append to file
myfile = open('myfile.txt', 'a')
myfile.write(' and i also like data structure')
myfile.close()

# Read from file

myfile = open('myfile.txt', 'r+')
text = myfile.read(100) # read one hundred characters
print(text)
myfile.close()


