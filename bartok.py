from Card import *
import random

interactive = False

def valid_move(card, stack):
	
	if not stack or card.suit == stack[-1].suit or card.rank == stack[-1].rank:
		return True

	return False


def handle_turn(hand, stack, deck, player = False):
	acceptable = [card for card in hand if valid_move(card, stack)]

	if len(acceptable) > 0:
		if player:
			pass
			# TODO - logic to handle a player making a decision 
		else:
			print("You can play from one of these! I'ma just take the last one!")
			tbr = acceptable[-1]
			hand = [card for card in hand if card != tbr]
			random.shuffle(hand)
			stack.append(tbr)
		
	else:
		print("Time to draw")
		if not deck:
			deck, stack = stack, deck
			random.shuffle(deck)
		hand.append(deck.pop())

	print(len(hand))	
	
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
			hands[index], stack, deck = handle_turn(hands[index], stack, deck)
			if not hands[i]:
				print("We have a winner!")
				going = False
				break

	print("End of program!")
	
