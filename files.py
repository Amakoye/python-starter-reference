# Python has functions for creating, reading, updating, and deleting files.

# Open a file
myFile = open('myFile.txt', 'w')

# Get some info
print('Name: ', myFile.name)
print('Is closed: ', myFile.closed)
print('Opening mode: ', myFile.mode)

# Write to file
myFile.write('In love with python ')
myFile.write('and Javascript')
myFile.close()

# Append to file
myFile =  open('myFile.txt', 'a')
myFile.write(' this is appended text')
myFile.close()

# Read from a file
myFile =  open('myFile.txt', 'r+')
text = myFile.read(100)
print(text)
