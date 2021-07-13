from GemPlayer import GemPlayer

class Gems:

    def __init__(self, numPlayers):
        self.players = []
        self.sessionHistory = []

        while len(self.players) < numPlayers:
            self.play_game()

        total = 0
        firsttime = 0
        uselessGems = 0
        for player in self.players:
            total += player.numSessions
            firsttime += player.firstSkillTime
            uselessGems += player.getUselessGems()

        print("average sessions : ", total/len(self.players))
        print("average days : ", (total / len(self.players)/3))
        print("average time to complete one set : ", firsttime/len(self.players))
        print("useless gems: ", uselessGems/len(self.players))


    def play_game(self):
        instancePlayer = GemPlayer()
        self.players.append(instancePlayer)



if __name__ == '__main__':
    game = Gems(1000)