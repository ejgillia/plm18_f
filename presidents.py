from Card import *
import random
import itertools

def same_score(combo):
  tbc = combo[0].score
  for item in combo:
    if item.score != tbc:
      return False
    
  return True
  


def generate_moves(hand, num_cards_to_play, last_score):
  if num_cards_to_play not in [1,2,3]:
    raise ValueError("Not a valid input - num_cards_to_play not in [1,2,3]")

  # remove twos
  cleaned = [card for card in hand if card.score != 2]
  tbr = []

  for combo in itertools.combinations(cleaned, num_cards_to_play):
    if same_score(combo) and combo[0].score >= last_score:
      tbr.append(combo)
  
  return tbr
    
    
  
  
def valid_moves(hand, stack):
  # valid moves:
  # play a 2
  # if empty or 1 card last on stack: play one card >= the stack card
  # if empty or 2 cards last on stack: play two cards >= the stack cards
  # if empty or 3 cards last on stack: play three cards >= the stack cards


  # twos are always a valid play, so I'm doing them out of the loop
  # I'm not telling you why this is a tuple to keep you on your toes xd
  valid = [(card,) for card in hand if card.score == 2]
  

  
  if not stack:
    # all moves are valid
    for i in range(1, 4):
      valid.extend(generate_moves(hand, i, 0))

  else:
    # number of cards previously put down in the last turn
    last_play = len(stack[-1])
    # SCORE of cards previously put down in last turn
    last_score = stack[-1][0].score
    valid.extend(generate_moves(hand, last_play, last_score))
    
  meaningful_variable_name = sorted(valid, key = lambda x : x[0].score)
    
  print(meaningful_variable_name)
  
  return meaningful_variable_name
    

if __name__ == "__main__":
  num_players = 5
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

  valid_moves(hands[0], [[Card("A", "H")]])
  valid_moves(hands[0], [[Card("3", "H"), Card("3", "S")]])
  valid_moves(hands[0], [[Card("3", "H"), Card("3", "S"), Card("3", "C")]])
