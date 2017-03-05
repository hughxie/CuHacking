from functions import *

class TfTrivia:
    #Variables for use inside of the class

    #setup a new game
    def __init__ (self):
        self.rightAnswerCount = 0
        self.wrongAnswerCount = 0
        self.rightCount = 0
        self.wrongCount = 0
        self.gameTeam = []
        self.playerSubmitted = []
        self.answer = -1
        self.finalScores = 0
        self.totalQuestions = 2

    def setupTfTrivia(self, gameTeamIn, s):
        self.gameTeam = gameTeamIn
        print "testTeam"
        print gameTeamIn

        #send a whisper to all the players on team 1 (not working yet)
        #for p in range(0, len(team1)):
        #    Send_whisper(s, str(team1[p]) + ", you're on team 1 with " + str(len(team1) - 1) + " other players", str(team1[p]))

        #for p in range(0, len(team2)):
        #    Send_whisper(s, str(team2[p]) + ", you're on team 2 with " + str(len(team2) - 1) + " other players", str(team2[p]))

        self.answer = askQuestion(s)

    #main game check for a trivia game
    def processMessage(self, message, username, s):
        if (message == "true"):
            #add 1 to the tally of people who have chosen
            self.rightCount += 1#rightCount + 1
            #add the player to the list of players who have voted
            self.playerSubmitted.append(username)
            
        elif (message == "false"):
            self.wrongCount += 1
            self.playerSubmitted.append(username)

        if len(self.gameTeam) == len(self.playerSubmitted):
            #find out how many people choose the right answer
            if (self.answer == 0):
                self.rightAnswerCount = self.wrongCount
                self.wrongAnswerCount = self.rightCount
            elif (self.answer == 1):
                self.rightAnswerCount = self.rightCount
                self.wrongAnswerCount = self.wrongCount

            #display a message for the players
            if self.rightCount > self.wrongCount:
                Send_message(s, "More people got that right")
                self.finalScores += 1
            elif self.rightCount < self.wrongCount:
                Send_message(s, "More people got that wrong")
                self.finalScores -= 1
            else:
                Send_message(s, "That was a tie!")

            #see if we can ask another question
            self.totalQuestions -= 1
            if self.totalQuestions <= 0:
                #end the game
                if self.finalScores > 0:
                    Send_message(s, "Game is over. Right got " + str(self.finalScores) + " more points than wrong")
                    sendHTTP(0)
                elif self.finalScores < 0:
                    Send_message(s, "Game is over. Wrong got " + str(abs(self.finalScores)) + " more points than right")
                    sendHTTP(1)
                else:
                    Send_message(s, "Right got just as many points as wrong!")
                return 1
            else:
                #ask a new question. game is not over yet
                self.answer = askQuestion(s)

                self.rightAnswerCount = 0
                self.wrongAnswerCount = 0
                self.rightCount = 0
                self.wrongCount = 0
                self.playerSubmitted = []
                self.finalScores = 0
                return 0
            
