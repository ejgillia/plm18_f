def group(cards, strat):
        if not cards:
          return cards
        cards = cards.copy()
        #print (cards)
        tmpCards = sorted(cards, key = strat)
        cards = [[tmpCards.pop()]]
        while tmpCards:
                card = tmpCards.pop()
                if strat(card) == strat(cards[-1][0]):
                        tmp = cards[-1]
                        tmp = tmp.copy()
                        tmp.append(card)
                        cards.append(tmp)
                else:
                        cards.append([card])
        return cards

