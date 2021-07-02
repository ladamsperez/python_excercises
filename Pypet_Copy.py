print('Welcome to PyPet!')



name = 'Harlan'
age = 7 
weight = 10.5
hungry = True
photo = '♡(ᐢ ᴥ ᐢし)'

pupper = {
    'name': 'Harlan',
    'hungry': True,
    'weight': 10.5,
    'age': 7,
    'photo': '♡(ᐢ ᴥ ᐢし)',
}

chickie = {
    'name': 'Lenny',
    'age': 1,
    'weight': 2,
    'hungry': False,
    'photo': '~:>'
}

pets = [pupper, chickie]

print ('Hello ' + pets['name'])
print (pets['photo'])


def feed(pets):
    if pets['hungry'] == True:
        pets['hungry'] = False
        pets['weight'] = pets['weight'] + 2
    else:
        print('The Pypet is not hungry!')


print (pets)
feed(pets)
print (pets)
feed(pets)

