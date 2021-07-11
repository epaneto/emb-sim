from PlayerDeck import PlayerDeck

class Player:
    
    def __init__(self):
        self.deck = PlayerDeck()
        self.totalChests = 0
        self.recyclingChests = 0
        self.recyclingSteps = 0
        
    def addGold(self, gold):
        self.deck.SC += gold

