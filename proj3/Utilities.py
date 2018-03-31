def group(cards, strat):
        if not cards:
          return cards
        cards = cards.copy()
        tmpCards = sorted(cards, key = strat)
        cards = [[tmpCards.pop()]]
        while tmpCards:
                card = tmpCards.pop()
                if strat(card) == strat(cards[-1][0]):
                        cards[-1].append(card)
                else:
                        cards.append([card])
        return cards
