# A For loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

people = ['John', 'Paul','Sara','Susan']

#  Simple for loop

    # for person in people:
    #     print(f'current peron: {person}')

#  Break
    # for person in people:
    #     if person == 'Sara':
    #         break
    #     print(f'current peron: {person}')

#  Continue
    # for person in people:
    #     if person == 'Sara':
    #         continue
    #     print(f'current peron: {person}')

#  Range
    # for i in range(len(people)):
    #     print(people[i])

    # for i in range(0, 11):
    #     print(f'number: {i}')




# While loops execute a set of statements as long as a condition is true.

count = 0

while count <= 10:
    print(count)
    count += 1