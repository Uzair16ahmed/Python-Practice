# A variable is a container for a value, which can be of various types.abs

"""  
VARIABLES RULES:
  - Variable names are case sensitive (name and NAME are different variables).
  - Must start with a letter or an underscore.
  - Can have numbers but can not start with one.
"""

# x = 1          # int 
# y = 2.5        # float
# name = 'john'  # str
# is_cool = True # bool


# Multiple Assignment

x, y, name, is_cool = (1, 2.5, 'john', True)

# Basic math
a = x + y

# Check type
type(x)

# Casting
x = str(x)
y = int(y) # value will be set to 2
z = float(y) # value will be set to 2.0 but not 2.5 because it has been changed.

print(type(z), z) # <class 'float'> 2.0



