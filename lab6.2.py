#Write a python function that takes a list of first names and returns a list of only the first letter of every name.


name = input("LE", "Chelsea", "Harlan", "Dixie")
name = name.split(' ')
print('. '.join([n[0] if i != len(name) - 1 else n for i, n in enumerate(name)]))

#
# Create an empty list that holds first names
first_list = ['L.E.','Clarissa']

def name_first(list_sample1):

    name_list=[list_sample1]
    final_list=[]

    letter_list=[]

    sample_length=len(list_sample1)

    for name in name_list:
        # Return a list of only the first letter of name

        letter_1 = name[0][0]

        final_list.append(letter_1)

    print(final_list)

    return(sample_length)

name_first(first_list)