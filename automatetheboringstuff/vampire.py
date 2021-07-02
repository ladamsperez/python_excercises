''' The elif clause executes if age < 12 is True and name == 'Alice' is False.
However, if both of the conditions are False, 
then both of the clauses are skipped. 
It is not guaranteed that at least one of the clauses will be executed. 
When there is a chain of elif statements, 
only one or none of the clauses will be executed.
Once one of the statements’ conditions is found to be True, 
the rest of the elif clauses are automatically skipped.'''

name = 'Carol'
age = 3000

if name == 'Alice':
    print('Hi, Alice.')
elif age <12:
    print("You are not Alice, Kiddo.")
elif age > 2000:
    print("Unlike you, Alice is not an undead, immortal vampire.")
elif age > 100:
    print('You are not Alice, grannie.')