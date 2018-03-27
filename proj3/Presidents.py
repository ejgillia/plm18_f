from Game import Game

class Presidents(Game):
  
  def endCondition(self):
    for player in self.players:
      if player.noCardsLeft() and player not in self.winner:
        print("Player is done")
        print(player)
        #removing player from game
        next = player.next
        prev = player.prev
        prev.next = next
        next.prev = prev
        
        self.winner.append(player)
    return len(self.winner) == len(self.players)
  
  def winMessage(self):
    print("The winner of presidents is: ")
    place = 0
    for player in self.winner:
      place += 1
      print("%dst %s"% ( place, player.idNum))
  
  def validPlays(self, hand, lastPlayed):
    
    print('last played')
    print(lastPlayed)
    
    #copying hand so changes do not affect actual hand
    tmpHand = sorted(hand.copy())
 
    #setting up to group cards based on their rank, to make it easer to find valid plays
    hand = []
    card = tmpHand.pop()
    currentRank = card.rank
    currentSet = [card]
    while tmpHand:
      card = tmpHand.pop()
      if card.rank == currentRank:
        currentSet.append(card)
      else:
        hand.append(currentSet)
        currentRank = card.rank
        currentSet = [card]
    hand.append(currentSet)
    
    
    #setting up the valid plays
    valid = []
    prevLen = len(lastPlayed)
    if lastPlayed:
      prevCard = lastPlayed[0]
    for cardSet in hand:
      setLen = len(cardSet)
      setCard = cardSet[0]
      if setCard.rank == '2':
        [valid.append([card]) for card in cardSet]
      elif setLen > prevLen:
        [valid.append(cardSet[0:i]) for i in range(prevLen, setLen + 1)]
      elif setLen == prevLen and setCard > prevCard:
        valid.append(cardSet)
    valid = [cardSet for cardSet in valid if cardSet]
    return valid

  
  def cantPlay(self, player):
    self.played.append([])
    return player.prev
  
  def playerPlayed(self, player, played):
    
    if played[0].rank == '2':
      self.played.append([])
      return player
    
    self.played.append(played)
    return player.next
  
  def dealHands(self):
    count = 0
    while self.deck.cardsLeft():
      self.players[count % self.totPlayers].drawCard()
      count +=1
      

      
Presidents(numPlayers = 1, numAI = 3).play()   
  
  
