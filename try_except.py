# Example 1
def divide42(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error you tried to divide by zero')

print(divide42(2))
print(divide42(12))
print(divide42(0))
print(divide42(1))

# Example 2 
print('How many cats do you have?')
numCats = input()

try:   
    if int(numCats) > 4:
        print('Thats alot of cats')
    else:
        print('Thats not many cats')
except ValueError:
    print('You did not enter a number')
