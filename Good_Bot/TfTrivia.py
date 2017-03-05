class TfTrivia:
	rightAnswerCount = 0
	wrongAnswerCount = 0
	trueCount = 0
	falseCount = 0
	gameTeam, playerSubmitted
	answer = -1

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
                trueCount++
			#add the player to the list of players who have voted
			playerSubmitted.append(username)
			
		elif (message == "false"):
			falseCount++
			playerSubmitted.append(username)

		if len(playerSubmitted) and len(gameTeam):
       		#find out how many people choose the right answer
            if (answer = 0):
                rightAnswerCount = falseCount
                wrongAnswerCount = trueCount
            elif (answer = 1):
                rightAnswerCount = trueCount
                wrongAnswerCount = falseCount

            totalQuestions--
			if totalQuestions <= 0:

	def nextQuestion(s):
		answer = askQuestion(questions, s)

	def endGame(self,correctAnswer):


#Check if the user is part of this current game, and if they have not answered yet
                        if username in gameTeam and username not in playerSubmitted:
                            #if they answered true
                            if (message == "true"):
                                #add 1 to the tally of people who have chosen
                                trueCount++
                                #add the player to the list of players who have voted
                                playerSubmitted.append(username)
                                
                            elif (message == "false"):
                                falseCount++
                                playerSubmitted.append(username)

                        #if the list of players who have voted is equal to the list of players playing
                        if len(playerSubmitted) and len(gameTeam):
                            #find out how many people choose the right answer
                            if (answer = 0):
                                rightAnswerCount = falseCount
                                wrongAnswerCount = trueCount
                            elif (answer = 1):
                                rightAnswerCount = trueCount
                                wrongAnswerCount = falseCount

                            #display how many people got it right and wrong    
                            Send_message(s, str(rightAnswerCount) + " people got that question right, " + str(wrongAnswerCount) + " people got it wrong.")

                            #reset all of the numbers
                            rightAnswerCount = wrongAnswerCount = trueCount = falseCount = 0

                            #you need to set the playerSubmitted list back to empty

                            #make another question
                            answer = askQuestion(questions)

                            #here we need to check that we still need to ask questions rather than just returning to the lobby
