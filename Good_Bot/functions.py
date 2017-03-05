from random import randint

questions = [[0, "Richard is Cool"], [1, "Forest > Aidan"]]

def askQuestion(s):
    random = randint(0, len(questions)
    s.send(quesitons[random][1])
    return quesitons[random][0]
