# A List is a collection which is ordered and changeable. Allows duplicate members.

# Create a list
numbers = [1,2,3,4,5]
fruits = ['Apples', 'Oranges', 'Grapes', 'Peas']
# use a constructor
#numbers2 = list((5,6,7,8,9,10))

print(numbers)

# Get a value
print(fruits[2])

# Change a value
fruits[0] = 'Blueberries'
print(fruits)
# Get length
print(len(fruits))

# Append to list
fruits.append('Mangos')
print(fruits)

# Remove from list
fruits.remove('Grapes')
print(fruits)

# Insert into position
fruits.insert(2, 'Strawberry')
print(fruits)

# Remove with pop
fruits.pop(2)
print(fruits)

# Reverse list
fruits.reverse()
print(fruits)

# sort list
fruits.sort()
print(fruits)

# Reverse sort
fruits.sort(reverse=True)
print(fruits)