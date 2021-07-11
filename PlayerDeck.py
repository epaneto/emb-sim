import json


class PlayerDeck:

    def __init__(self):
        # character inventory, made of InventoryItem type objects

        self.sniperLevelHistory = []
        self.shotgunLevelHistory = []
        self.pistolLevelHistory = []
        self.assaultLevelHistory = []
        self.lightArmourLevelHistory = []
        self.mediumArmourLevelHistory = []
        self.heavyArmourLevelHistory = []

        self.sniperLevel = 0
        self.shotgunLevel = 0
        self.pistolLevel = 0
        self.assaultLevel = 0
        self.lightArmourLevel = 0
        self.mediumArmourLevel = 0
        self.heavyArmourLevel = 0

        self.unlockedPerks = []
        self.unlockedPerksHistory = []

        self.totalPerks = 0
        self.battleGearXP = 50
        self.battlesGearRequirements = [5, 15, 35, 75, 100]

        self.totalBattles = 0
        self.weaponBattles = 0
        self.armourBattles = 0

        self.recycledPerks = 0

        # Load characters and fill deck with level 0
        perkJSON = open('perks.json', )

        # returns JSON object as a dictionary
        data = json.load(perkJSON)

        # Iterating through the json list
        for i in data['perks']:
            self.totalPerks = self.totalPerks + 1

    def unlockPerk(self, perkChosen):
        for perk in perkChosen:


            found = False
            for unlocked in self.unlockedPerks:
                if unlocked.perkID == perk.perkID:
                    found = True
                    self.recycledPerks += 1

            if not found:
                self.unlockedPerks.append(perk)

    def upgradeGear(self):
        self.totalBattles += 1
        self.weaponBattles += 1
        self.armourBattles += 1

        # upgrade weapon
        if self.sniperLevel < 5 and self.battlesGearRequirements[self.sniperLevel] <= self.weaponBattles:
            self.sniperLevel += 1
            if self.sniperLevel == 5:
                self.weaponBattles = 0
        elif self.sniperLevel == 5 and self.shotgunLevel < 5 and self.battlesGearRequirements[self.shotgunLevel] <= self.weaponBattles:
            self.shotgunLevel += 1
            if self.shotgunLevel == 5:
                self.weaponBattles = 0
        elif self.sniperLevel == 5 and self.pistolLevel < 5 and self.battlesGearRequirements[self.pistolLevel] <= self.weaponBattles:
            self.pistolLevel += 1
            if self.pistolLevel == 5:
                self.weaponBattles = 0
        elif self.pistolLevel == 5 and self.assaultLevel < 5 and self.battlesGearRequirements[self.assaultLevel] <= self.weaponBattles:
            self.assaultLevel += 1
            if self.assaultLevel == 5:
                self.weaponBattles = 0

        # upgrade armour
        if self.lightArmourLevel < 5 and self.battlesGearRequirements[self.lightArmourLevel] <= self.armourBattles:
            self.lightArmourLevel += 1
            if self.lightArmourLevel == 5:
                self.armourBattles = 0
        elif self.lightArmourLevel == 5 and self.mediumArmourLevel < 5 and self.battlesGearRequirements[self.mediumArmourLevel] <= self.armourBattles:
            self.mediumArmourLevel += 1
            if self.mediumArmourLevel == 5:
                self.armourBattles = 0
        elif self.mediumArmourLevel == 5 and self.heavyArmourLevel < 5 and self.battlesGearRequirements[self.heavyArmourLevel] <= self.armourBattles:
            self.heavyArmourLevel += 1
            if self.heavyArmourLevel == 5:
                self.armourBattles = 0

        self.sniperLevelHistory.append(self.sniperLevel)
        self.shotgunLevelHistory.append(self.shotgunLevel)
        self.pistolLevelHistory.append(self.pistolLevel)
        self.assaultLevelHistory.append(self.assaultLevel)
        self.lightArmourLevelHistory.append(self.lightArmourLevel)
        self.mediumArmourLevelHistory.append(self.mediumArmourLevel)
        self.heavyArmourLevelHistory.append(self.heavyArmourLevel)
        self.unlockedPerksHistory.append(len(self.unlockedPerks))


    def what_is_my_proficiency(self, gearType):
        if gearType == 0:
            return self.sniperLevel
        elif gearType == 1:
            return self.shotgunLevel
        elif gearType == 2:
            return self.pistolLevel
        elif gearType == 3:
            return self.assaultLevel
        elif gearType == 4:
            return self.lightArmourLevel
        elif gearType == 5:
            return self.mediumArmourLevel
        elif gearType == 6:
            return self.heavyArmourLevel

    def isMaxedOut(self):

        ended = True

        if len(self.unlockedPerks) < self.totalPerks:
            ended = False

        return ended
