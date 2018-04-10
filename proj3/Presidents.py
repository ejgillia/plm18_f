from GameRules import GameRules
from Utilities import *

"""
defining rule for preprocessing hand
"""
def preproHand(hand):
  return groupCards(hand, lambda card: card.rank)

"""
defining the valid play rules
if a rule returns true
the play is valid
"""
def setOf4Rule(prevPlay, cardSet):
  return len(prevPlay) == 4

def rankOf2Rule(prevPlay, cardSet):
  return cardSet[0].rank == '2'

def biggerSetRule(prevPlay, cardSet):
  return len(cardSet) > len(prevPlay)

def sameSizeHigherRankRule(prevPlay, cardSet):
  return len(prevPlay) == len(cardSet) and prevPlay and cardSet[0] > prevPlay[0]    


"""
defining the valid out of turn plays rule
"""
def outOfTurnPlayRule(lastPlayed, cardSet):
  return setOf4(lastPlayed, cardSet) if lastPlayed else False

 
"""
 defining rule for when player can't play
""" 
def cantPlayRule(game, player):
  game.played.append([])
  return player.prev

"""
defining rules for what to do based on what a player played
"""
def playerPlayedA2Rule(player, played):
  return player, played[0].rank == '2'

def playerPlayedRegRule(player, played):
  return player.next, True


"""
defining rule for dealing hands
"""
def dealHandRule(deck, players):
  count = 0
  numPlayers = len(players)
  while deck.cardsLeft():
    players[count % numPlayers].drawCard()
    count+= 1
  return deck, players
    
"""
defining rule for ending the game
"""    
def endGameRule(game):
  for player in game.players:
    if player.noCardsLeft() and player not in game.winners:
      player.remove()
      game.winners.append(player)
  return len(game.winners) == len(game.players)
      
  
  
GameRules(numPlayers = 1, 
          numAI = 3,
          gameName = "presidents",
          preprocessHand = preproHand,
          validPlayRules = [setOf4Rule, rankOf2Rule, biggerSetRule, sameSizeHigherRankRule],
          outOfTurnPlayRules = [outOfTurnPlayRule],
          playerPlayedRules = [playerPlayedA2Rule, playerPlayedRegRule],
          cantPlayRule = cantPlayRule,
          endGameRule = endGameRule,
          dealHandsRule = dealHandRule).play()
  
  
