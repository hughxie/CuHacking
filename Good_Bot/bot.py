import socket, string, time
from random import randint

#from commands import *
#from functions import *
# Set all the variables necessary to connect to Twitch IRC
HOST = "irc.twitch.tv"
NICK = "hackbot"
PORT = 6667
PASS = "oauth:1ums1vm612j3vhtb4ocxztzh77rs4h"
readbuffer = ""
MODT = True
state = "lobby"
UserWaiting = ""
server = []
game = []
gameTeam = []
playersSubmitted = []
team1 = []
team2 = []
questionsAsked = 0
answer = -1
trueCount = falseCount = 0

questions = [[0, "Richard is Cool"], [1, "Forest > Aidan"]]

# Connecting to Twitch IRC by passing credentials and joining a certain channel
s = socket.socket()
s.connect((HOST, PORT))
s.send("PASS " + PASS + "\r\n")
s.send("NICK " + NICK + "\r\n")
s.send("JOIN #cuhacking \r\n")

# Method for sending a message
def Send_message(message):
    s.send("PRIVMSG #cuhacking :" + message + "\r\n")

def Send_whisper(message, player):
    s.send("PRIVMSG #cuhacking :/w " + player + " " + message + "\r\n")
    #s.send("PRIVMSG #AngelOnFira :test\r\n")
    time.sleep(1)
    print("PRIVMSG #cuhacking :/w " + player + " " + message + "\r\n")

def askQuestion(questions):
    #Pick a random question from the list
    random = randint(0, len(questions))

    #Ask the question
    s.send("PRIVMSG #cuhacking :" + quesitons[random][1] + "\r\n")

    #Return the answer (0 for false, 1 for true)
    return quesitons[random][0]

while True:
    #s.send("PRIVMSG #cuhacking :/w angelonfira test\r\n")
    readbuffer = readbuffer + s.recv(1024)
    temp = string.split(readbuffer, "\n")
    readbuffer = temp.pop()

    for line in temp:
        print line
        # Checks whether the message is PING because its a method of Twitch to check if you're afk
        if (line[0] == "PING"):
            s.send("PONG %s\r\n" % line[1])
        else:
            # Splits the given string so we can work with it better
            parts = string.split(line, ":")

            if "QUIT" not in parts[1] and "JOIN" not in parts[1] and "PART" not in parts[1]:
                try:
                    # Sets the message variable to the actual message sent
                    message = parts[2][:len(parts[2]) - 1]
                except:
                    message = ""
                # Sets the username variable to the actual username
                usernamesplit = string.split(parts[1], "!")
                username = usernamesplit[0]

                badUserName = username.split()
                print("test username " + badUserName[0] + "|")
                if badUserName[0] <> "tmi.twitch.tv" and badUserName[0] <> "cuhacking.tmi.twitch.tv":
                    if username not in server:
                        server.append(username)
                        if message <> "!join":
                            Send_message("Welcome to my stream, " + username + " type !join to join the game.")

                    if state == "lobby":
                        if username not in game and message == "!join":
                            game.append([randint(0, 100), username])
                            Send_message(username + " has joined the game PogChamp")
                        elif message == "!join":
                            Send_message(username + " , you're already in the game DansGame ")

                        if message == "!start":
                            print game
                            gameTeam = []
                            team1 = []
                            team2 = []
                            game.sort()
                            for i in range(0, len(game)):
                                gameTeam.append(game[i][1])
                                if i < len(game) / 2:
                                    team1.append(game[i][1])
                                else:
                                    team2.append(game[i][1])
                                print("added a player")
                            state = "game"
                            print team1
                            print team2
                            #Ask a question
                            answer = askQuestion(questions)

                            for p in range(0, len(team1)):
                                Send_whisper(str(team1[p]) + ", you're on team 1 with " + str(len(team1) - 1) + " other players", str(team1[p]))

                            for p in range(0, len(team2)):
                                Send_whisper(str(team2[p]) + ", you're on team 2 with " + str(len(team2) - 1) + " other players", str(team2[p]))

                    if state == "game":
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
                            Send_message(str(rightAnswerCount) + " people got that question right, " + str(wrongAnswerCount) + " people got it wrong.")

                            #reset all of the numbers
                            rightAnswerCount = wrongAnswerCount = trueCount = falseCount = 0

                            #you need to set the playerSubmitted list back to empty

                            #make another question
                            answer = askQuestion(questions)

                            #here we need to check that we still need to ask questions rather than just returning to the lobby

                if MODT:
                    #print (username + ": " + message)

                    # You can add all your plain commands here
                    if message == "Hey":
                        Send_message("Fuck off, " + username)
                        Send_message("Are u trying to steal our idea plebs?")
                        print ("Sending Message")

                    if UserWaiting == username:
                        Send_message("Welcome to my stream, " + username)
                        print ("Sending Message")



                for l in parts:
                    if "End of /NAMES list" in l:
                        MODT = True
