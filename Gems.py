from GemPlayer import GemPlayer

class Gems:

    def __init__(self, numPlayers):
        self.players = []
        self.sessionHistory = []

        while len(self.players) < numPlayers:
            self.play_game()

        total = 0
        firsttime = 0
        for player in self.players:
            total += player.numSessions
            firsttime += player.firstSkillTime

        print("average sessions : ", total/len(self.players))
        print("average days : ", (total / len(self.players)/3))
        print("average time to complete one set : ", firsttime/len(self.players))


    def play_game(self):
        instancePlayer = GemPlayer()
        self.players.append(instancePlayer)



if __name__ == '__main__':
    game = Gems(1000)