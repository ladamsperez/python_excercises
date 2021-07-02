import random

class Rank:
	def __init__(self, value, points):
		self.value = value
		self.points = points


class Suit:
	def __init__(self, symbol, name):
		self.symbol = symbol
		self.name = name


class Card:
	def __init__(self, suit, rank):
		self.suit = suit
		self.rank = rank


class Deck:
	'''takes a list of suits and a list of ranks and generates one card of each combination'''
	def __init__(self, suits, ranks):
		self.cards = []
	for suit in suits:
		for rank in ranks:
			self.cards.append(Card(suit, rank))

	def shuffle(self):
		return random.shuffle(self.cards)

	def deal(self, player, dealer):
# '''distributes two cards to each player's hand from the deck'''
		players = (player, dealer)
		for player in players:
		
				self.cards.pop()


    
class Player:
  def __init__(self, number, is_dealer=False):
    self.number = number
    self.hand = []
    self.is_dealer = is_dealer

  # def deal(self, deck):
  #   '''distributes two cards to this player's hand from the deck'''
  #   pass

# class Dealer():
  
class Table:
  pass



class Game:
  pass


rank_point_relationships = [
  ('A', (1, 11)), 
  (2, 2), 
  (3, 3),
  (4, 4),
  (5, 5),
  (6, 6), 
  (7, 7),
  (8, 8),
  (9, 9), 
  (10, 10),
  ('J', 10),
  ('Q', 10),
  ('K', 10),
  ]

my_ranks = []
for rank in rank_point_relationships:
  my_ranks.append(Rank(rank[0], rank[1]))

# for rank in ranks:
#   print(f'{rank.value} is worth {rank.points} points.')

suit_options = [('hearts', '♥'), ('diamonds', '♦'),('spades', '♠'), ('clubs', '♣')]

my_suits = []

for suit in suit_options:
  my_suits.append(Suit(suit[1], suit[0]))

# for suit in suits:
#   print(suit.symbol, suit.name)

deck = Deck(my_suits, my_ranks)
deck.shuffle()

# for card in deck.cards:
#   print(f'{card.rank.value} of {card.suit.symbol}')


player1 = Player(1)
print(player1.is_dealer)

dealer = Player(2, is_dealer=True)
print(dealer.is_dealer)