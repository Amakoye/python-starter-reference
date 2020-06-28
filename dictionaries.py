# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# Create a dict
person = {
    'firstName': 'John',
    'lastName': 'Doe',
    'Age': 31
}

# Get  value
print(person['firstName'])
print(person.get('lastName'))

# Add key/value
person['phone'] = '0700200500'
# print(person, type(person))

# Get dict  keys
print(person.keys())

# Get dict items
print(person.items())

# Copy dict
person2 = person.copy()
person2['City'] = 'Nairobi'
print(person2)

# Remove item
del(person['Age'])
person.pop('phone')

# Clear
#person.clear()

# Get length
print(len(person))

# List of Dict
people = [
    {'name':'Martha', 'age':30},
    {'name':'Kevin', 'age':25}
]
print(people)