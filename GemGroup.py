class GemGroup:

    def __init__(self):
        self.uniqueGems = []
        self.uselessGems = 0
    def addGem(self, gemType):

        repeated = False
        for acquiredGem in self.uniqueGems:
            if acquiredGem == gemType:
                repeated = True
                self.uselessGems += 1

        if not repeated:
            self.uniqueGems.append(gemType)

    def isComplete(self):

        return len(self.uniqueGems) >= 4

    def resetGroup(self):
        self.uniqueGems = []
