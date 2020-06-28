# If/ Else conditions are used to decide to do something based on something being true or false
x = 15
y = 16


# Comparison Operators (==, !=, >, <, >=, <=) - Used to compare values
# Simple if
#if x>y:
#    print(f'{x} is greater than {y}')
# if/else
#if x>y:
#    print(f'{x} is greater than {y}')
#else:
#    print(f'{y} is greater than {x}')
#if x>y:
#   print(f'{x} is greater than {y}')
#elif x==y:
#    print(f'{x} is equal to {y}')
#else:
#    print(f'{y} is greater than {x}')
# Logical operators (and, or, not) - Used to combine conditional statements
#if x>2 and x<=10:
#    print(f'{x} is greater than 2 and equal  to or less than 10')
# not
#if not(x==y):
 #   print(f'{x} is not equal to {y}')


# Membership Operators (in, not in) - Membership operators are used to test if a sequence is presented in an object
# in
numbers = [1,2,3,4,5]
if x in numbers:
    print(x in numbers)

# not in
numbers = [1,2,3,4,5]
if x not in numbers:
    print(x not in numbers)


# Identity Operators (is, is not) - Compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:
# is
if x is y:
    print(x is y)

# is
if x is not y:
    print(x is not y)