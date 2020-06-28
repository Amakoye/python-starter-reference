# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods
name = 'Charles'
age = 22

# Concatenate
# print('My name is' +name +' and I am '+str(age))

# String Formatting

# 1.Arguments by position
#print('My name is{name} and I am {age}'.format(name=name, age=age))

# 2. F-Strings
#print(f'Hello {name}, age {age}')

# String Methods
s = 'hello world'

# Capitalize string
print(s.capitalize())

# Make all uppercase
print(s.upper())

# Make all lower
print(s.lower())

# Swap case
print(s.swapcase())

# Get len
print(len(s))

# Replace
print(s.replace('world', 'everyone'))

# Count
sub = 'h'
print(s.count(sub))

# Starts with
print(s.startswith('hello'))

# Ends with
print(s.endswith('d'))

# Split into a list
print(s.split())

# Find position
print(s.find('r'))

# is all  alphanumeric
print(s.isalnum())

# is all alphabetic
print(s.isalpha())

# is all numeric
print(s.isnumeric())