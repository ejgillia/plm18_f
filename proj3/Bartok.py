from GameRules import GameRules
from Utilities import *

"""
defining rule for preprocessing hand
"""
def preproHand(hand):
  return hand

"""
defining the valid play rules
if a rule returns true
the play is valid
"""
def sameRankRule(prevPlay, card):
  return prevPlay.rank == card.rank if prevPlay else True

def sameSuitRule(prevPlay, card):
  return prevPlay.suit == card.suit if prevPlay else True


 
"""
 defining rule for when player can't play
""" 
def cantPlayRule(game, player):
  player.drawCard()
  return player

"""
defining rules for what to do based on what a player played
"""
def playerPlayedRegRule(player, played):
  return player.next, True


"""
defining rule for dealing hands
"""
def dealHandRule(deck, players):
  for player in players:
    [player.drawCard() for i in range(7)]
  return deck, players
    
"""
defining rule for ending the game
"""    
def endGameRule(game):
  for player in game.players:
    if player.noCardsLeft() and player not in game.winners:
      player.remove()
      game.winners.append(player)
  return len(game.winners)
      
  
  
GameRules(numPlayers = 1, 
          numAI = 3,
          gameName = "bartok",
          preprocessHand = preproHand,
          validPlayRules = [sameRankRule, sameSuitRule],
          outOfTurnPlayRules = [],
          playerPlayedRules = [playerPlayedRegRule],
          cantPlayRule = cantPlayRule,
          endGameRule = endGameRule,
          dealHandsRule = dealHandRule).play()
  
  
