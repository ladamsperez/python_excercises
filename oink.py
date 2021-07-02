
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


# "Choose Heads or Tails:"
# User input ___
# "Coin flip! Player ___ goes first!"

# ***AI will ALWAYS hold until it gets to a sum 20 points in a turn-
    #how and where to handle this???
# after every turn, print players score

from icecream import ic
import random



def greeting():
    print("Oink! Oink! Let's Pig Out!")

class Player:
    def __init__(self, type):
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
        score = die.roll()
        self.score += score
        ic(score)
        

    def AI_move(self, die):
        '''This move defines AI's action in turn. Will hold until sum of 20 points within turn.'''
        score = die.roll()
        self.score += score
        ic(score)
    
    
class Die:
    def __init__(self, n = 6):
        self.sides = n

    def roll(self):
        # Random number that is 1-6 
        return random.randint(1, self.sides)

# die = Die()
# "Print Roll: __"
# print(die.roll())

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
    # No: continue

            # "print: play again? Yes or No?
            # user input_ yes or no
            #   yes: play again
            #   no: "Print: Game Over. Goodbye!"


#is it 1?
    # yes: "print: No points! Next player's turn."
            #display players' points

    # no: "Print total turn sum:__. Would you like to hold or keep rollin'?"
        #user input: hold
            #Update score: add total turn points to score +=
            # "Print total turn sum:__."
            #display players' points
            # next player's turn 
        #user input: Roll, roll, r, keep rolling, Keep Rolling, Keep Rollin, keep rollin
            #go back to "Player rolls"





def main():
    greeting()
    new_game = Game()
    new_game.play()
    

main()

