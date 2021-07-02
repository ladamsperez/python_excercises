# Write a python function that takes a list of names and returns a new list
# with all the names that start with "Z" removed.
# test your function on this list:
# test_list = ['Zans', 'Dan', 'Grace', 'Zelda', 'L.E.', 'Zeke', 'Mara'] 

test_list = ['Zans', 'Dan', 'Grace', 'Zelda', 'L.E.', 'Zeke', 'Mara'] 


def noznames(namelist):
    newlist = []
    for name in namelist:
        if not name.startswith("Z"):
            newlist.append(name)
    print(newlist)

noznames(test_list)
# nosynames(name)



# namelist = ['Zans', 'Dan', 'Grace', 'Zelda', 'L.E.', 'Zeke', 'Mara'] 

# namelist.strip(name.startswith("Z"))

# print(namelist)