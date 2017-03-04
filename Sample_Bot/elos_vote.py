#may need to modify if only two are playing in TOTAL
# Takes two cases and users vote on which, then calculates the total votes
# can define number of votes to equal PIE!

K = 10 #constant

class Elo(object):
    def match(self, p1, p2):
        algo_func = self.__match_algo_strict
        return algo_func(p1, p2)

    @staticmethod
    def __match_algo_strict(winner, loser):
        # elo algorithm - simple modifications
        r1 = max(min(loser.score - winner.score, 400), -400)
        r2 = max(min(winner.score - loser.score, 400), -400)
        e1 = 1.0 / (1 + 10 ** (r1 / 400))
        e2 = 1.0 / (1 + 10 ** (r2 / 400))

        s1 = 1
        s2 = 0

        winner.score = winner.score + K * (s1 - e1)
        loser.score = loser.score + K * (s2 - e2)

        # increase wincounter
        winner.wins += 1

        # increase matchcounter
        winner.matches += 1
        loser.matches += 1

        return winner, loser

    def __match_algo_experimental(self, winner, loser):
        # elo algorithm - simple modifications
        r1 = max(min(loser.score - winner.score, 400), -400)
        r2 = max(min(winner.score - loser.score, 400), -400)
        e1 = 1.0 / (1 + 10 ** (r1 / 400))
        e2 = 1.0 / (1 + 10 ** (r2 / 400))

        winner.set_score(winner.score + K * e2)
        loser.set_score(loser.score - K * e2)

        # increase wincounter
        winner.wins += 1

        # increase matchcounter
        winner.matches += 1
        loser.matches += 1
