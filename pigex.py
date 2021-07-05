import random
 


    
def greeting():
    '''Displays a greeting for the game Pig'''
    print("Oink! Oink! Let's Pig Out!")
    

class Game:
    
    def __init__(self,p1_human=True,p2_human=False):
        self.die=Die()
        self.p1 = Player('Player 1',p1_human)
        self.p2 = Player('Player 2',p2_human)
        
    def play(self):
        while (self.p1.score<100 and self.p2.score<100):
            self.p1.move()
            if self.p1.score<100:
                self.p2.move()
        if (self.p1.score>self.p2.score):
            print ('Player 1 wins!')
        else:
            print ('Player 2 wins!')

class Player:
    
    def __init__(self,title,human_player=False):
        self.name=title
        self.is_human=human_player
        self.score=0
        self.die=Die(6)
        
    def move(self):
        if self.is_human:
            self.human_move()
        else:
            self.AI_move()
            
    def human_move(self):
        round_score=0
        again='y'
        #establish a while loop for the player's turn
        while again=='y':
            self.die.roll()
            roll=self.die.face
            if roll==1:
                print ('{} rolled a 1'.format(self.name))
                round_score=0
                again='n'
            else:
                print( '{} rolled a {}'.format(self.name,roll))
                round_score=round_score+roll
                print( "{}'s round score is {}".format(self.name,round_score))
                again=input('roll again? (y/n)')
        self.score+=round_score
        print ("{}'s turn is over".format(self.name))
        print( "{}'s total score is {}\n\n".format(self.name,self.score))
        
    def AI_move(self):
        round_score=0
        again='y'
        #establish a while loop for the computer's turn
        while again=='y':
            self.die.roll()
            roll=self.die.face
            if roll==1:
                print ('{} rolled a 1'.format(self.name))
                roundScore=0
                again='n'
            else:
                print( '{} rolled a {}'.format(self.name,roll))
                round_score=round_score+roll
                if round_score < 20:
                    print( '{} will roll again'.format(self.name))
                else:
                    again='n'     
        self.score+=round_score
        print( 'Turn is over')
        print( "{}'s round score is {}".format(self.name,round_score))
        print( "{}'s total score is {}\n\n".format(self.name,self.score))

class Die:
    
    def __init__(self,n=6):
        self.sides=n
        self.roll()
        
    def roll(self):
        self.face=int(random.random()*self.sides+1)

def goodbye():
    '''Displays a goodbye message for the game Pig'''
    print()
    print()
    print('GAME OVER!')

def main():
    greeting()
    game=Game()
    game.play()
    goodbye()


main()
