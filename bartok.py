from Card import *
import random

def valid_move(card, stack):
  
  return not stack or card.suit == stack[-1].suit or card.rank == stack[-1].rank


def handle_turn(hand, stack, deck, player = False):
  acceptable = [card for card in hand if valid_move(card, stack)]
  if len(stack) > 0:
    print("Top Card {}".format(stack[-1]))
  
  # printing cards for user to select
  if (len(acceptable) > 0):
    tbr = None
    #print("test: " + str(not tbr))
    while ( not tbr):
      if player:
        print("Your current hand is {}".format(hand))
        print("Enter the index of the card you wish to play")
        for index, card in enumerate(acceptable):
          print("{} {}".format(index, card))
        selected = 0
        try:
          selected = int(input("Input number of card to play: "))
          tbr = acceptable[selected]
          #print("tbr in acceptable: " + str(tbr in acceptable))
          if tbr not in acceptable:
            raise ValueError("Invalid Play")
        except (ValueError, IndexError):
            print("Invalid selection")
            tbr = None
      else:
        tbr = acceptable[-1]
    hand = [card for card in hand if card != tbr]
    random.shuffle(hand)
    stack.append(tbr)
    print("A {} was played".format(tbr))
    
  else:
    print("No moves available: Time to draw")
    if not deck:
      deck, stack = stack, deck
      random.shuffle(deck)
    hand.append(deck.pop())  
  
  return hand, stack, deck
      


if __name__ == "__main__":
  num_players = 5
  deck = [Card(rank, suit) for suit in suits for rank in ranks]
  random.shuffle(deck)
  stack = []

  if num_players * 7 >= len(deck):
    raise ValueError("Too many players!")

  hands = [[] for _ in range(num_players)]
  
  for i in range(num_players):
    for _ in range(7): hands[i].append(deck.pop())

  stack.append(deck.pop())

  going = True
  while going:
    for index, hand in enumerate(hands):
      print("---")
      print("I am player {}".format(index))
      hands[index], stack, deck = handle_turn(hands[index], stack, deck, index == 0)
      if not hands[index]:
        print("We have a winner! Player {}".format(index))
        if index == 0:
          print("Human won")
        else:
          print("AI won")
        
        going = False
        break

  print("End of program!")
  
