from Card import *
import random
from player import Player


def generate_moves(hand, num_cards_to_play):
  if num_cards_to_play not in [1,2,3]:
    raise ValueError("Not a valid input - num_cards_to_play not in [1,2,3]")

  # remove twos
  cleaned = [card for card in hand if card.score != 2]

def valid_moves(hand, stack):
  # valid moves:
  # play a 2
  # if empty or 1 card last on stack: play one card >= the stack card
  # if empty or 2 cards last on stack: play two cards >= the stack cards
  # if empty or 3 cards last on stack: play three cards >= the stack cards


  # twos are always a valid play, so I'm doing them out of the loop
  valid = [card for card in hand if card.score == 2]
  

  
  if not stack:
    # all moves are valid
    pass

  else:
    # number of cards previously put down in the last turn
    last_play = len(stack[-1])
    # SCORE of cards previously put down in last turn
    last_score = stack[-1][0].score
    

if __name__ == "__main__":
  num_players = 4
  deck = [Card(rank, suit) for suit in suits for rank in ranks]
  random.shuffle(deck)
  stack = []
  hands = [[] for _ in range(num_players)]

  ## there is probably a function that does this, but I don't know of it off hand
  ## as equally as possible, distribute cards between players
  going = True
  while going:
    for i in range(num_players):
      if deck:
        hands[i].append(deck.pop())
      else:
        going = False
        break
  players = []
  for hand in hands:
    print(len(hand), hand)
    players.append(Player(len(players) , hand))
  for i in range(len(players)):
    players[i].setPrev(players[i - 1])
    players[i].setNext(players[(i + 1) % num_players])
  
  
  pl = players[0]
  prevPl = []
  winners = []
  while len(players) > 1:
    prevPl, nextpl = pl.play(prevPl)
    if not pl.hand:
      #if player has an empty hand remove from game
      next = pl.next
      prev = pl.prev
      prev.setNext(next)
      next.setPrev(prev)
      players = [player for player in players if not player == pl]
      winners.append(pl)
      print("player {} has finished".format(pl.idNum))
    pl = nextpl
  
  winners.append(players.pop())
  
  for c, v in enumerate(winners):
    print("winner number {} is player {}".format(c, v.idNum))
    
    
    
