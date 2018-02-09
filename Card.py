suits = "C S D H".split(" ")
ranks = [str(i) for i in range(2, 11)] + "J Q K A".split(" ")


class Card(object):

    scores = {rank: value for rank, value in zip(ranks, range(2, 15))}

    def __init__(self, rank, suit):
        self.rank = str(rank)
        self.suit = str(suit)
        self.score = Card.scores[rank]

    def __repr__(self):
        return "{} of {}".format(self.rank, self.suit)

    def __lt__(self, other):
        return self.score < other.score

    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit
