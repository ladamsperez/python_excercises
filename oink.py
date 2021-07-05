
# Read the specs for your project and re-state them to yourself to make sure you understand them and ask for clarification where needed.
# Decide the order of priority for meeting the requirements.
# Sketch/map out your game.
# Set up a file in VS Code for your project.
# From the sketch process, determine what classes you will need. You might find this list helpful.
# Build each class one at a time.
# Build the action of the game one step at a time, adding methods to classes as you deem necesary.

# Number-Based Option: Pig Dice Game
# You are going to implement a version of the game of Pig in Python. Here's how the game works.

# Two players are trying to reach 100 points first.
# On a player's turn, they roll a die over and over until they roll a 1 (a "pig") or they choose to hold.
# If they hold, they add the sum of their rolls to their score. If they roll a 1, they get no points.
# After a 1 is rolled or the player holds, the other player takes their turn.
# The first player is chosen randomly. (For example, you could flip a coin or both roll a die and pick the higher roll.)
# In your implementation, there will be one human player and one computer player. The computer player will always hold until they roll a total of 20 points.
from icecream import ic
import random



def greeting():
    print("Oink! Oink! Let's Pig Out!")

class Player:
    def __init__(self):
        self.type = type
        self.score = 0
        
# Player Rolls
    def move(self, die):
        if self.type == "human_player":
            self.human_move(die)
        else:
            self.AI_move(die)
        
    def human_move(self, die):
        '''This move defines human's action in turn. Will ask human to hold or keep rolling.'''
        round_score=0
        again='y'
        #establish a while loop for the player's turn
        while again=='y':
            self.die.roll()
            roll=self.die.face
            if roll==1:
                print ('{} rolled a 1'.format(self.human_move))
                round_score=0
                again='n'
            else:
                print( '{} rolled a {}'.format(self.human_move,roll))
                round_score=round_score+roll
                print( "{}'s round score is {}".format(self.human_move,round_score))
                again=input('roll again? (y/n)')
        self.score+=round_score
        print ("{}'s turn is over".format(self.human_move))
        print( "{}'s total score is {}\n\n".format(self.human_move,self.score))
        

    def AI_move(self, die):
        '''This move defines AI's action in turn. Will hold until sum of 20 points within turn.'''
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
        print( "{}'s round score is {}".format(self.AI_move,round_score))
        print( "{}'s total score is {}\n\n".format(self.AI_move,self.score))
    
    
class Die:
    def __init__(self, n = 6):
        self.sides = n
        self.roll()
        
    def roll(self):
        self.face=int(random.random()*self.sides+1)


class Game:
    def __init__(self):
        self.winner = None
        self.rules = []
        self.die = Die()
        self.die.roll()
        self.player_1, self.player_2 = self.create_players()

    def create_players(self):
        player_types = ["human_player", "AI_player"]
        #the first player is chosen randomly
        player_1 = Player(random.choice(player_types))
        if player_1.type == "human_player":
            player_2 = Player("AI_player")
        else: 
            player_2 = Player("human_player")       

        print (f"Player 1 is {player_1.type}. Player 2 is {player_2.type}.")
        return player_1, player_2

    def play(self):
        # is the total sum of either player 100?
        while (self.player_1.score <= 100 and self.player_2.score <= 100):
            ic(self.player_1.score, self.player_2.score)
            # yes: which player?
            self.player_1.move(self.die)
            if self.player_1.score <= 100:
                self.player_2.move(self.die)
       # player ___ wins!
        if (self.player_1.score>self.player_2.score):
            print("Player 1 wins!")
        else:
            print("Player 2 wins!")
            return

def main():
    greeting()
    new_game = Game()
    new_game.play()
    

main()

