# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

# Create a tuple
fruits = ('Apples', 'Oranges', 'Grapes')
fruits2 = tuple(('Apples', 'Oranges', 'Grapes'))

# Get value
print(fruits[1])

# Can't change a tuple
#fruits[0] = 'Pears'

# Delete tuple
del fruits2

# get length
print(len(fruits))


# A Set is a collection which is unordered and unindexed. No duplicate members.

# Create set
fruits_set = {'Apples', 'Oranges', 'Mango'}

# Check if in set
print('Apples' in fruits_set)

# Add to Set
fruits_set.add('Grapes')
fruits_set.add('Grapes')

print(fruits_set)

# Remove from set
fruits_set.remove('Grapes')

# Clear
fruits_set.clear()

# Delete
del fruits_set

print(fruits_set)
