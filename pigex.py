#********************************************
#Pig.py
# 
#Plays the interactive dice game Pig
#
#Written by Cannon
#********************************************

import random

score = 0

# The main function for the applicaiton
def main():
    greeting()
    playgame()
    goodbye()


def playgame():
    '''This function plays the game Pig'''
    p1score=0
    p2score=0
    #establish a while loop for the game
    while (p1score <100 and p2score <100):
        print ('your score total is now: {} \n \n'.format(p1score))
        p1score=p1score + playerMove()
        print ('your score total is now: {} \n \n'.format(p1score))
        if(p1score<100):
            p2score=p2score + computerMove()
            print ('the computer score total is now:{}\n \n'.format(p2score))
    if (p1score>p2score):
        print ('you win!')
    else:
        print ('you lose!')

def playerMove():
    '''manages the human players move in Pig. Returns their score'''
    roundScore=0
    again='y'
    #establish a while loop for the player's turn
    while again=='y':
        roll=rollDice()
        if roll==1:
            print ('you rolled a 1')
            roundScore=0
            again='n'
        else:
            print( 'you rolled a {}'.format(roll))
            roundScore=roundScore+roll
            print( 'your round score is {}'.format(roundScore))
            again=input('roll again? (y/n)')
    print ('your turn is over')
    return roundScore


def computerMove():
    '''plays the computer players turn in Pig returns their turn score'''
    roundScore=0
    again='y'
    #establish a while loop for the computer's turn
    while again=='y':
        roll=rollDice()
        if roll==1:
            print ('computer rolled a 1')
            roundScore=0
            again='n'
        else:
            print( 'computer rolled a {}'.format(roll))
            roundScore=roundScore+roll
            if roundScore < 20:
                print( 'computer will roll again')
            else:
                again='n'
                
    print( 'computer turn is over')
    print( 'computer round score is {}'.format(roundScore))
    return roundScore

def rollDice():
    '''Rolls a 6 sided die and returns an int 1-6'''
    face=int(random.random()*6+1)
    return face

def greeting():
    '''Displays a greeting for the game Pig'''
    print( 'welcome to Pig Death Match!')
    
def goodbye():
    '''Displays a goodbye message for the game Pig'''
    print()
    print()
    print('Toodles!')
    