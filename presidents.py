from Card import *
import random
import itertools
import typing

def same_score(combo: list) -> bool:
  tbc = combo[0].score
  for item in combo:
    if item.score != tbc:
      return False
    
  return True
  


def generate_moves(hand: list, num_cards_to_play: int, last_score: int) -> list:
  if num_cards_to_play not in [1,2,3,4]:
    raise ValueError("Not a valid input - num_cards_to_play not in [1,2,3]")

  cleaned = [card for card in hand if card.score != 2]
  tbr = []

  for combo in itertools.combinations(cleaned, num_cards_to_play):
    if same_score(combo) and combo[0].score >= last_score:
      tbr.append(combo)
  
  return tbr
    

def valid_moves(stack: list, hand: list) -> list:

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
  
  return meaningful_variable_name

def handle_turn(stack: list, hand: list, player = False):
  allowed = valid_moves(stack, hand)
  if len(allowed) == 0:
    print("no moves")
    return [], hand, True

  if player:
    pass #handle all that delicious input
  else:
    random.shuffle(allowed)
  tbp = allowed.pop()
  print("This was played", tbp, "on", stack)
  stack += (tbp,)
  if tbp[0].rank == "2": stack = []
  hand = [card for card in hand if card not in tbp]


  return stack, hand, False
    
  

def four_of_a_kind(stack: list, hand: list):
  # god forgive me
  # just believe me: this works
  # fenceposting
  if not stack: return False
  
  in_play = len(stack[-1])
  # easiest case first
  if in_play == 3:
    # do you have the fourth
    missing = [card for card in hand if stack[-1][0].score == card.score]
    if missing:
      return missing, True
  if in_play == 2:
    missing = [card for card in hand if stack[-1][0].score == card.score]
    if len(missing) == 2:
      return missing, True
  if in_play == 1:
    # lord have mercy
    stk = [card[0] for card in stack if card[0].score == stack[-1][0].score]
    stlol = [card for card in hand if card.score == stack[-1][0].score]
    if len(stk) + len(stlol) == 4:
      print("yabba dabba ding dong")
      return stk, True
  
  return False
    


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
  
  # ldoifygp9e8tdfg 
  # enjoy debugging THIs
  i = 0
  while True:
    print("current player {}".format(i))
    xd = False
    puppies = -1
    lejfg = []

    for a in range(num_players):
      b = four_of_a_kind(stack, hands[a])
      if b:
        xd = True
        puppies = a
        lejfg = b[0]
        break
    
    if xd:
      i = puppies
      hands[puppies] = [card for card in hands[i] if card not in lejfg]
      print("OOOOO BOY", puppies)
      stack = []
      continue

    stack, hands[i], flag = handle_turn(stack, hands[i], player = False)
    if not hands[i]:
      print("We has a winner!")
      print("Player {}!".format(i))
      break

    if flag:
      i = (i - 1) % num_players
    else:
      i = (i + 1) % num_players
        
    

  







