from Game import Game
from Game import group

class Presidents(Game):
  
  def endCondition(self):
    for player in self.players:
      if player.noCardsLeft() and player not in self.winner:
        player.remove()  
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
    if lastPlayed and (lastPlayed[0].rank == '2' or len(lastPlayed) == 4):
      lastPlayed = []
    hand = group(hand, lambda card: card.rank)
    
    #setting up the valid plays
    valid = []
    prevLen = len(lastPlayed)
    prevCard = lastPlayed[0] if lastPlayed else None
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

  def outOfTurnPlay(self, lastPlayer, lastPlayed):
    if not lastPlayed:
      return lastPlayer
      
    for player in self.players:
      if player.noCardsLeft():
        continue
      cardSets = group(player.hand, lambda card: card.rank)
      for play in cardSets:
        if play[0].rank == lastPlayed[0].rank and (len(play) + len(lastPlayed)) == 4:
          lastPlayed += play
          return player
      
    return lastPlayer
  
  def cantPlay(self, player):
    self.played.append([])
    return player.prev
  
  def playerPlayed(self, player, played): 
    if played[0].rank == '2':
      return player
    
    self.played.append(played)
    return player.next
  
  def dealHands(self):
    count = 0
    while self.deck.cardsLeft():
      self.players[count % self.totPlayers].drawCard()
      count +=1
      

      
Presidents(numPlayers = 1, numAI = 3).play()   
  
  
