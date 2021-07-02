# Some functions can be called with multiple arguments 
# separated by a comma, and range() is one of them. 
# This lets you change the integer passed to range() to follow any sequence of integers,
#  including starting at a number other than zero.
# for i in range(12, 16):
#     print(i)

# The range() function can also be called with three arguments. 
# The first two arguments will be the start and stop values, 
# and the third will be the step argument. 
# The step is the amount that the variable is increased by after each iteration.
# for i in range(0, 10, 2):
#     print(i)

# The range() function is flexible in the sequence of numbers it produces for for loops.
# For example (I never apologize for my puns), 
# you can even use a negative number for the step argument to make the for loop count down instead of up.

for i in range(5, -1, -1):
    print(i)
