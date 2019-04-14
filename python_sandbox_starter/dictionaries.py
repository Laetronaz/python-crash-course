# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

# Create dict
person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30
}

# Use constructor
person2 = dict(first_name='Sarah', last_name='Williams')

# get Value
print(person['first_name'])
print(person2.get('first_name'))

# add key/value
person['phone'] = '555-555-5555'

# Get dict keys
print(person.keys())

# Get dict items
print(person.items())

# Copy dict
person3 = person.copy()
person3['city'] = 'Montreal'

print(person3)

# Remove Item
del(person['age'])
person.pop('phone')

# Clear
person2.clear()

# Get length
print(len(person3))

# list of dict

people = [
    {'name': 'Martha', 'age': 30},
    {'name': 'Kevin', 'age': 25}
]
print(people)
print(people[1]['name'])


print(person, type(person))
print(person2, type(person2))
