import socket, string, time
from random import randint

from TfTrivia import *
from functions import *
# Set all the variables necessary to connect to Twitch IRC
HOST = "irc.twitch.tv"
NICK = "hackbot"
PORT = 6667
PASS = "oauth:1ums1vm612j3vhtb4ocxztzh77rs4h"
readbuffer = ""
MODT = True
state = "lobby"
UserWaiting = ""
modes = ["trivia"]
mode = ""
server = []
game = []
gameTeam = []
team1 = []
team2 = []
gameClass = 0

# Connecting to Twitch IRC by passing credentials and joining a certain channel
s = socket.socket()
s.connect((HOST, PORT))
s.send("PASS " + PASS + "\r\n")
s.send("NICK " + NICK + "\r\n")
s.send("JOIN #cuhacking \r\n")

# Method for sending a message

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
                            Send_message(s, "Welcome to my stream, " + username + " type !join to join the game.")

                    if state == "lobby":
                        if username not in game and message == "!join":
                            game.append([randint(0, 100), username])
                            Send_message(s, username + " has joined the game PogChamp")
                        elif message == "!join":
                            Send_message(s, username + " , you're already in the game DansGame ")

                        if message[:5] == "!mode":
                            if message[6:] in modes:
                                mode = message[6:]
                                Send_message(s, username + " , the mode has been set")
                            else:
                                Send_message(s, username + " , that is not a valid mode")

                        if message == "!start" and mode <> "":
                            print game

                            #if teamNum == 1:
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
                        elif mode == "":
                            Send_message(s, username + " , the mode has not been set yet! Enter !mode *mode name* to set it.")

                            if (mode == "trivia"):
                                gameClass = TfTrivia(gameTeam, s)

                    if state == "game":
                        if gameClass.processMessage(message, username, s):
                            state = "lobby"
                            mode = ""
