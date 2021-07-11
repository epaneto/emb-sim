from GemGroup import GemGroup
import random


class GemPlayer:

    def __init__(self):
        self.color1Group = GemGroup()
        self.color2Group = GemGroup()
        self.color3Group = GemGroup()
        self.color4Group = GemGroup()
        self.color5Group = GemGroup()
        self.color6Group = GemGroup()

        self.firstSkillTime = 0

        self.gemTypes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]

        self.totalWeaponSKills = 30
        self.acquiredSkills = 0

        self.numSessions = 0
        self.gemCountHistory = []
        self.sessionHistory = []
        self.startGemHunt()



    def startGemHunt(self):
        while self.acquiredSkills < self.totalWeaponSKills:
            self.numSessions += 1

            sortedGem = random.randint(0, len(self.gemTypes))

            if sortedGem == 1 or sortedGem == 2 or sortedGem == 3 or sortedGem == 4:
                self.color1Group.addGem(sortedGem)
            elif sortedGem == 5 or sortedGem == 6 or sortedGem == 7 or sortedGem == 8:
                self.color2Group.addGem(sortedGem)
            elif sortedGem == 9 or sortedGem == 10 or sortedGem == 11 or sortedGem == 12:
                self.color3Group.addGem(sortedGem)
            elif sortedGem == 13 or sortedGem == 14 or sortedGem == 15 or sortedGem == 16:
                self.color4Group.addGem(sortedGem)
            elif sortedGem == 17 or sortedGem == 18 or sortedGem == 19 or sortedGem == 20:
                self.color5Group.addGem(sortedGem)
            elif sortedGem == 21 or sortedGem == 22 or sortedGem == 23 or sortedGem == 24:
                self.color6Group.addGem(sortedGem)

            self.gemCountHistory.append(self.acquiredSkills)
            self.sessionHistory.append(self.numSessions)
            self.checkCompletion()
        print("player completed", self.numSessions)

    def checkCompletion(self):
        if self.color1Group.isComplete() or self.color2Group.isComplete() or self.color3Group.isComplete() or self.color4Group.isComplete() or self.color5Group.isComplete():
            self.color1Group.resetGroup()
            self.color2Group.resetGroup()
            self.color3Group.resetGroup()
            self.color4Group.resetGroup()
            self.color5Group.resetGroup()
            self.color6Group.resetGroup()

            self.acquiredSkills += 1


            if(self.acquiredSkills == 1):
                self.firstSkillTime = self.numSessions


