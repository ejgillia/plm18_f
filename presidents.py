from Card import *
import random
import itertools
import typing

# global variables are a valid strategy
total_turns = 0
num_players = 5

def same_score(combo: list) -> bool:
  tbc = combo[0].score
  for item in combo:
    if item.score != tbc:
      return False
    
  return True
  



    

def valid_moves(stack: list, hand: list) -> list:
  #copying hand so changes do not affect actual hand
  tmpHand = sorted(hand.copy())
  #setting up sets of similar cards so that plays can be easily found
  hand = [[tmpHand.pop()]]
  while tmpHand:
    card = tmpHand.pop()
    if hand[-1][0].rank == card.rank:
      hand[-1].append(card)
    else:
      hand.append([card])
  
  prevPlay = [] if not stack else stack[-1]
  valid = []
  for st in hand:
    #looping over the sets of similar cards
    if st[0].rank == '2':
      [valid.append([card]) for card in st]
    elif len(st) > len(prevPlay):
      if not prevPlay or st[0] > prevPlay[0]:
        [valid.append(st[0:i]) for i in range(len(prevPlay), len(st))]
      valid.append(st)
    elif len(st) == len(prevPlay) and st[0] > prevPlay[0]:
      valid.append(st)
  
  #removing empty set if any where added
  valid = [i for i in valid if i]
  return valid
  
  
  
  
  

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
    return [], hand, 0
  # The play that will be made.
  tbp = None
  if player:
    print("Current stack is {}".format(stack))
    print("Your current hand is {}".format(hand))
    for index, card in enumerate(allowed):
      print("{} {}".format(index, card))
    selected = 0
    while tbp is None:
      try:
        selected = int(input("Enter the index of the move you make (or -1 to pass): "))
        tbp = allowed[selected] if selected >= 0 else []
      except (ValueError, IndexError):
        print("Invalid selection")
        tbp = None
  else:
    random.shuffle(allowed)
    # AI -- always choose the best move (lowest score) except on first round
    if total_turns / num_players >= 1:
      tbp = min(allowed)
    else:
      pos = [x for x in allowed if x[0].score != 2]
      if pos:
        tbp = min([x for x in allowed if x[0].score != 2])
      else:
        tbp = allowed[0]
  print("This was played", tbp, "on", stack)
  stack += (tbp,)
  # Clear the stack if a 2 was played.
  hand = [card for card in hand if card not in tbp]
  if tbp and tbp[0].rank == "2":
    stack = []
    return stack, hand, 2
  
  if not tbp:
    stack = []
    return stack, hand, 0



  return stack, hand, 1
    
  

def four_of_a_kind(stack: list, hand: list):
 
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
      #print("yabba dabba ding dong")
      return stk, True
  
  return False
    


if __name__ == "__main__":
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
  
  
  #number of the current player
  i = 0
  #main game loop
  while True:
    
    
    #set for finding out if can play four of a kind
    set4 = -1
    play = []

    #finding out if there are 4 of a kind
    for a in range(num_players):
      b = four_of_a_kind(stack, hands[a])
      if b:
        set4 = a
        play = b[0]
        break
    
    if set4 != -1:
      i = set4
      hands[set4] = [card for card in hands[i] if card not in play]
      print("-----------------------------------")
      print("Player %d, played 4 of a kind" % (set4) )
      print(play)
      stack = []
      continue

    print("-----------------------------------")
    print("current player {}".format(i))
    stack, hands[i], flag = handle_turn(stack, hands[i], player = (i == 0))
    if not hands[i]:
      print("We have a winner!")
      print("Player {}!".format(i))
      break

    if flag == 0:
      i = (i - 1) % num_players
    elif flag == 1:
      i = (i + 1) % num_players

    total_turns += 1
        
    

  







