# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
 
# Create a tuple
fruits = ('Apples', 'Oranges', 'Grapes')
#fruits2 = tuple(('Banana', 'Mango'))

# Single value needs comma
fruits2 = ('Apples',)

# Delete tuple
#del fruits2

# get length
print(len(fruits))

# A Set is a collection which is unordered and unindexed. No duplicate members.
fruit_set = {'Apples', 'Mangos', 'Oranges'}

# Check if in set
print('Apples' in fruit_set)

# add to set
fruit_set.add('Grapes')
# remove from set
fruit_set.remove('Grapes')
# clear set
fruit_set.clear()
# delete set
# del fruit_set
print(fruit_set)