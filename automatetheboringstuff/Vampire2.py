# The order of the elif statements does matter, however. 
# Let’s rearrange them to introduce a bug. 
# Remember that the rest of the elif clauses are 
# automatically skipped once a True condition has been found,
# so if you swap around some of the clauses in vampire.py,
# you run into a problem.


# name = 'Carol'
# age = 3000

# if name == 'Alice':
#     print('Hi, Alice.')
# elif age < 12:
#     print('You are not Alice, kiddo.')
# elif age > 100:
#     print('You are not Alice, grannie.')
# elif age > 2000:
#     print('Unlike you, Alice is not an undead, immortal vampire.')

# Optionally, you can have an else statement after the last elif statement. 
# In that case, it is guaranteed that at least one (and only one) of the clauses will be executed. 
# If the conditions in every if and elif statement are False,
# then the else clause is executed. 
# For example, let’s re-create the Alice program to use if, elif, 
# and else clauses.
name = 'Carol'
age = 3000

if name == 'Alice':
    print('Hi, Alice.')
elif age < 12:
    print('You are not Alice, kiddo.')
else:
    print('You are neither Alice nor a little kid.')
    
