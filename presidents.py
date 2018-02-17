from Card import *
import random


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

  for hand in hands:
    print(len(hand), hand)

  valid_moves(hands[0], stack)
