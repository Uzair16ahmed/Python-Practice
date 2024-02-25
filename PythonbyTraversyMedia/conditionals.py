# if/ Else conditions are used to decide to do something based on something being true or false.

x = 10
y = 50

# Comparison Operators (==, !=, >, <, >=, <=) - Used to compare values

# simple if
    # if x > y:
    #     print(f"{x} is greater than {y}")

# if/else

    # if x > y:
    #     print(f"{x} is greater than {y}")
    # else:
    #     print(f"{x} is not greater than {y}")

# elif 
    # if x > y:
    #     print(f"{x} is greater than {y}")
    # elif x == y:
    #     print(f"{x} is equal to {y}")
    # else:
    #     print(f"{x} is less than {y}")

# Nested if

    # if x > 2:
    #     if x <= 10:
    #         print(f"{x} is between greater than 2 and less than or equal to 10")


# Logical Operators (and, or, not) - Used to combine conditions.

# and
    # if x > 2 and x <= 10:
    #     print(f"{x} is between greater than 2 and less than or equal to 10")

#  or
    # if x < 2 or x == 10:
    #     print(f"{x} is less than 2 or equal to 10")

# not 
    # if not(x == y):
    #     print(f"{x} is not equal to {y}")


# Membership Operators (not, not in) - Membership operators are used to test if a sequence is present in an object.

a = 3
numbers = [1, 2, 3, 4, 5]

# in
    # if a in numbers:
    #     print(a in numbers)
    #     print(f"{a} is in {numbers}")


#  not in
    # if x not in numbers:
    #     print(x not in numbers)
    #     print(f"{x} is not in {numbers}")


# Identity Operators (is, is not) - Compare the objects, not if they are equal,
#  but if they are actually the same object, with the same memory location.


#  is 
b , c , d = 12 , 12 , 10
if b is c:
    print(b is c)

#  is not
if b is not d:
    print(b is not d)