'''
Write a function that accepts a dictionary
of term/definition pairs.
The function should ask the user to 
enter a programming term and then prints
the definition of that term
(you can limit the user to the terms in the dictionary). 
'''

# program_dict = {'smol':'chihuahua','fluffy':'porcupine','chonkers':'hippo'}

# def user_dict(rand_dict):
#     keep_going = True
#     while = keep_going:

#         user_prompt = input('What type of animal do you see? ')
        
#         if user_prompt in rand_dict:
        
#         while user_prompt == "smol":
#             print('(❍ᴥ❍ʋ)')
#             break
        
#         while user_prompt == "fluffy":
#             print('  (•ᴥ• )́`́’́`́’⻍ ')
#             break
        
#         while user_prompt == "chonkers":
#             print('ʕ ´•̥̥̥ ᴥ•̥̥̥`ʔ')
#             break
        
#         again = input("Another? Y or N? ")
#             if again == 'N' or again == 'n':
#                 keep_going = False
#                 break

#     print("That's a " + rand_dict[user_prompt] + "!")

# user_dict(program_dict)

program_dict = {
    'smol':'chihuahua',
    'fluffy':'porcupine',
    'chonkers':'hippo'}

def print_definition():
    keep_going = True
    while keep_going:
        user_prompt = input("What type of animal do you see? ")
        print(program_dict.get(user_prompt))
        while user_prompt == "smol":
            print('(❍ᴥ❍ʋ)')
            return
        while user_prompt == "fluffy":
            print('  (•ᴥ• )́`́’́`́’⻍ ')
            return
        while user_prompt == "chonkers":
            print('ʕ ´•̥̥̥ ᴥ•̥̥̥`ʔ')
            return
        again = input("More? Y or N? ")
        if again == 'N' or again == 'n':
            keep_going = False
            break
        
print_definition()
