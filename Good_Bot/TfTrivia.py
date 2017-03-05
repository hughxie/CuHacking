from functions import *

class TfTrivia:
    rightAnswerCount = 0
    wrongAnswerCount = 0
    rightCount = 0
    wrongCount = 0
    gameTeam = []
    playerSubmitted = []
    answer = -1
    finalScores = 0

    playerSubmitted = []
    totalQuestions = 8

    def __init__ (self, gameTeamIn, s):
        self.userIn = userInput
        self.name = userName
        gameTeam = gameTeamIn

        for p in range(0, len(team1)):
            Send_whisper(s, str(team1[p]) + ", you're on team 1 with " + str(len(team1) - 1) + " other players", str(team1[p]))

        for p in range(0, len(team2)):
            Send_whisper(s, str(team2[p]) + ", you're on team 2 with " + str(len(team2) - 1) + " other players", str(team2[p]))

        nextQuestion(s)

    def processMessage(message, username, s):
        if (message == "true"):
            #add 1 to the tally of people who have chosen
            rightCount += 1
            #add the player to the list of players who have voted
            playerSubmitted.append(username)
            
        elif (message == "false"):
            falseCount += 1
            playerSubmitted.append(username)

        if len(playerSubmitted) and len(gameTeam):
            #find out how many people choose the right answer
            if (answer == 0):
                rightAnswerCount = falseCount
                wrongAnswerCount = trueCount
            elif (answer == 1):
                rightAnswerCount = trueCount
                wrongAnswerCount = falseCount

            if trueCount > falseCount:
                Send_message(s, "More people got that right")
                finalScores += 1
            elif trueCount < falseCount:
                Send_message(s, "More people got that wrong")
                finalScores -= 1
            else:
                Send_message(s, "That was a tie!")

            totalQuestions -= 1
            if totalQuestions <= 0:
                endGame(s)
                return 1
            else:
                nextQuestion(s)
                return 0

    def nextQuestion(s):
        answer = askQuestion(questions, s)

    def endGame(s):
        if finalScores > 0:
            Send_message(s, "Game is over. Right got " + finalScores + " more points than wrong")
        elif finalScores < 0:
            Send_message(s, "Game is over. Wrong got " + finalScores + " more points than right")
        else:
            Send_message(s, "Right got just as many points as wrong!")
            
