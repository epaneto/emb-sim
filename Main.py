from Player import Player
from Gacha_Random import Gacha_Random
import math


class Main:

    def __init__(self, players, chestLimit):
        self.totalChests = 0
        self.totalBattles = 0
        self.recycledChests = 0
        self.chestLimit = chestLimit
        self.players = []
        self.battlesForChest = 2
        self.battleHistory = []


        while len(self.players) < players:
            self.play_game()
            self.recycledChests += self.players[len(self.players)-1].deck.recycledPerks
            print("player ", len(self.players))



        print("END SIMULATION")
        print(self.totalChests/players, " chests", self.totalBattles/players, " battles", self.recycledChests/players,  "recycled")
        print((self.totalBattles/players) / 6, " days")

    def play_game(self):
        # create player instance
        instancePlayer = Player()
        self.players.append(instancePlayer)
        self.battleHistory = []
        self.playerBattles = 0

        numBattles = 0

        gacha = Gacha_Random()

        if self.chestLimit == 0:
            while not instancePlayer.deck.isMaxedOut():
                # earn battle gear xp
                instancePlayer.deck.upgradeGear()
                numBattles += 1
                self.totalBattles += 1

                # open chest
                if numBattles == 2:
                    gacha.open_chest(instancePlayer.deck)
                    instancePlayer.deck.unlockPerk(gacha.sortedPerks)
                    numBattles = 0
                    self.totalChests += 1

                self.battleHistory.append(self.totalBattles)
        else:
            chestIndex = 0
            while chestIndex < self.chestLimit:
                chestIndex += 1
                # earn battle gear xp
                instancePlayer.deck.upgradeGear()
                numBattles += 1
                self.totalBattles += 1

                # open chest
                if numBattles == 2:
                    gacha.open_chest(instancePlayer.deck)
                    instancePlayer.deck.unlockPerk(gacha.sortedPerks)
                    numBattles = 0
                    self.totalChests += 1

                self.playerBattles += 1
                self.battleHistory.append(self.playerBattles)

if __name__ == '__main__':
    game = Main(1, 0)
