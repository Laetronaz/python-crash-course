# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

peoples = ['John', 'Paul', 'Sarah', 'Lily']

# simple for loop
# for person in peoples:
#    print(f'Current Person:{person}')

# Break
for person in peoples:
    if person == 'Sarah':
        break
    print(f'Current Person:{person}')

# Continue
for person in peoples:
    if person == 'Sarah':
        continue
    print(f'Current Person:{person}')

# Range
for i in range(len(peoples)):
    print(peoples[i])

for i in range(0, 11):
    print(f'Number: {i}')

# While loops execute a set of statements as long as a condition is true.

count = 0
while count <= 10:
    print(f'Count: {count}')
    count += 1
