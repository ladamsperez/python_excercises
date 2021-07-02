# # break Statements
# If the execution reaches a break statement, 
# it immediately exits the while loop’s clause.
# In code, a break statement simply contains the break keyword.

while True:
    print('Please type your name.')
    name = input()
    if name == 'your name':
        break
print("Thank you!")

