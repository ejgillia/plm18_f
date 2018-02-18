class Player(object):
  """
  object for containing data relating a to player and state machine for order of play
  """
  
  def __init__(self, idNum,  hand):
    self.idNum = idNum
    self.setHand(hand)
  
  
  def setHand(self,  hand):
    
    #sorts cards in hand for esier matching
    hand = sorted(hand)
    #initates self.hand
    self.hand = [[hand.pop()]]
    #loop over hand until all cards have been added to self.hand
    while hand:
      card = hand.pop()
      if self.hand[-1][0].rank == card.rank:
        #if the current card has the same rank as previous than it belongs to current set
        self.hand[-1].append(card)
      else:
        #else make a new set
        self.hand.append([card])
  
  def setPrev(self, prev):
    """
    this is used to set the previous player
    when player cannot play
    previous player gets to play
    """
    self.prev = prev
  
  def setNext(self, next):
    """
    this used to set the next player
    when player successfully plays
    the next player plays
    """
    self.next = next
  
  def play(self, prevPlay):
    print("--------------------------------------------")
    print("player {} turn".format(self.idNum))
    valid = self.getValid(prevPlay)
    if valid:
      print("Valid plays: ")
      for (c, v) in enumerate(valid):
        print("{}\t {}".format(c, v))
      while True:
        try:
          sel = int(input("Input number of valid play to play: "))
          if valid[sel][0].rank == '2':
            #if 2 was played stack is cleared and player plays again
            played = valid[sel]
            next = self
          else:
            #else next player respons
            played = valid[sel]
            next = self.next
          
          self.hand = [card for card in self.hand if not card == played]
          if played[0].rank == '2':
            played = []
          return played, next  
        except KeyboardInterrupt as e:
          print("exiting from keyboard interrupt")
          raise e
        except Exception as e:
          print("invalid selection")
          print(e)
    else:
      #if player cannot play, the previous player plays again
      return [], self.prev


  def getValid(self, prevPlay):
    valid = []
    for st in self.hand:
      if len(st) > len(prevPlay):
        valid.append(st)
      elif len(st) == len(prevPlay) and st[0] > prevPlay[0]:
        valid.append(st)
      elif st[0].rank == '2':
        valid.append(st)
    return valid
               
          
          
        
  
    
