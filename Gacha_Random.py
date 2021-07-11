import random
import json
from InventoryItem import InventoryItem


class Gacha_Random:

    def __init__(self):
        self.sortedPerks = []
        self.currentPool = []
        self.allPerks = []

        # Opening JSON file
        perkJson = open('perks.json', )

        # returns JSON object as a dictionary
        data = json.load(perkJson)

        # Iterating through the json list
        for i in data['perks']:
            ii = InventoryItem(i["perkID"], i["tier"], i["type"])
            self.allPerks.append(ii)

        # Closing file
        perkJson.close()

    def open_chest(self, playerDeck):
        self.sortedPerks = []

        # will this chest give a perk?
        hasPerk = random.randint(1, 100) < 30

        if hasPerk:
            # which type of perk will be selected?
            perkType = random.randint(0, 6)

            # Generate pool
            self.generatePool(playerDeck.what_is_my_proficiency(perkType), perkType)

            # get perk
            self.get_perk()

    def generatePool(self, tier, perkType):
        self.currentPool = []

        # add perks relevant to the type selected
        for perk in self.allPerks:
            if perk.tier <= tier and perk.type == perkType:
                self.currentPool.append(perk)

    def get_perk(self):
        if len(self.currentPool) > 0:
            # randomize a perk
            chosenPerkIndex = random.randint(1, len(self.currentPool))
            chosenPerk = self.currentPool[chosenPerkIndex - 1]
            for gachaItem in self.currentPool:

                if gachaItem.perkID == chosenPerk.perkID:
                    inventoryItem = InventoryItem(gachaItem.perkID, gachaItem.tier, gachaItem.type)
                    self.sortedPerks.append(inventoryItem)

    def reset(self):
        self.sortedPerks = []
