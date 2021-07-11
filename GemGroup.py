class GemGroup:

    def __init__(self):
        self.uniqueGems = []

    def addGem(self, gemType):

        repeated = False
        for acquiredGem in self.uniqueGems:
            if acquiredGem == gemType:
                repeated = True

        if not repeated:
            self.uniqueGems.append(gemType)

    def isComplete(self):

        return len(self.uniqueGems) >= 4

    def resetGroup(self):
        self.uniqueGems = []
