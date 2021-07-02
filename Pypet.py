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
for individual_pet in pets:
   print('Hello ' + individual_pet['name'])
   print(individual_pet['photo'])

def feed(pets):
    if pets['hungry'] == True:
        pets['hungry'] = False
        pets['weight'] = pets['weight'] + 2
        print('omnomom!!')
    else:
        print("Stop feeding me! I'm chonky!")

for individual_pet in pets:
    feed(individual_pet)
    print (individual_pet)
    