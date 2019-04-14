# Python has functions for creating, reading, updating, and deleting files.

# Open a file
myFile = open('myfile.txt', 'w')

# Get some info
print('Name: ', myFile.name)
print('isClosed: ', myFile.closed)
print('Opening Mode: ', myFile.mode)

# Write to file
myFile.write('I love python!')
myFile.write(' and Java.')
myFile.close()

# Append
myFile = open('myfile.txt', 'a')
myFile.write(' I also hate php!')

# Read from a file
myFile = open('myfile.txt', 'r+')
text = myFile.read(100)
print(text)