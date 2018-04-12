from Game import Game
class GameRules(Game):
  
  def __init__(self, numPlayers = 1, numAI = 3, gameName = "", preprocessHand = None, validPlayRules = [], outOfTurnPlayRules = [], playerPlayedRules = [], cantPlayRule = None, endGameRule = None, dealHandsRule = None):
    super().__init__(numPlayers, numAI)
    self.validPlayRules = validPlayRules
    self.outOfTurnPlayRules = outOfTurnPlayRules
    self.playerPlayedRules = playerPlayedRules
    self.cantPlayRule = cantPlayRule
    self.endGameRule = endGameRule
    self.gameName = gameName
    self.preprocessHand = preprocessHand
    self.dealHandsRule = dealHandsRule
    
  def endCondition(self):
    return self.endGameRule(self)
  
  def winMessage(self):
    print("The winner of " + self.gameName + " is: ")
    place = 0
    for player in self.winners:
      place += 1
      print("%dst %s"% ( place, player.idNum))
  
  def validPlays(self, hand, lastPlayed):
    hand = hand if not self.preprocessHand else self.preprocessHand(hand)
    #setting up the valid plays
    valid = []
    for cardSet in hand:
      for rule in self.validPlayRules:
        if rule(lastPlayed, cardSet):
          valid.append(cardSet)
          break
    return valid

  def outOfTurnPlay(self, lastPlayer, lastPlayed):
    for player in self.players:
      hand = player.hand
      hand = hand if not self.preprocessHand else self.preprocessHand(hand)
      for play in hand:
        for rule in self.outOfTurnPlayRules:
          if rule(lastPlayed, play):
            return player
    return lastPlayer
  
  def cantPlay(self, player):
    return self.cantPlayRule(self, player)
  
  def playerPlayed(self, player, played): 
    for rule in self.playerPlayedRules:
      nextPlayer, condition = rule(player, played)
      if condition:
        return nextPlayer
    print("ERROR: reacing this point means no valid play condition was met")
    
  
  def dealHands(self):
    self.deck, self.players = self.dealHandsRule(self.deck, self.players)

