#Write a function that takes an integer (x)
# and then returns the sum of all integers up to and including x.
#ex. my_function(6) would do 
# 1 + 2 + 3 + 4 + 5 + 6 and then return that answer

user = int(input("Insert a number: "))

def sum_func(user):
    #take user data turn into range
    range_of_numbers = [x for x in range(user + 1)]
    #then take sum of all integers
    total = sum(range_of_numbers)
    # sum(range(user))
    print(total)


sum_func(user)

