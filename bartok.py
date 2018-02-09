from Card import *
import random

def valid_move(card, stack):
	
	return not stack or card.suit == stack[-1].suit or card.rank == stack[-1].rank


def handle_turn(hand, stack, deck, player = False):
	acceptable = [card for card in hand if valid_move(card, stack)]
	print(acceptable)

	if len(acceptable) > 0:
		if player:
			pass
			# TODO - logic to handle a player making a decision 
		else:

			tbr = acceptable[-1]
			hand = [card for card in hand if card != tbr]
			random.shuffle(hand)
			stack.append(tbr)
			print("You played {}".format(tbr))
		
	else:
		print("Time to draw")
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
			hands[index], stack, deck = handle_turn(hands[index], stack, deck)
			if not hands[index]:
				print("We have a winner! {}".format(index))
				going = False
				break

	print("End of program!")
	
