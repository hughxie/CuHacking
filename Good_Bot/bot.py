import socket, string, time
from random import randint

from commands import *
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
server = []
game = []
team1 = []
team2 = []
answer = -1

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
                            print 
                            team1 = []
                            team2 = []
                            game.sort()
                            for i in range(0, len(game)):
                                if i < len(game) / 2:
                                    team1.append(game[i][1])
                                else:
                                    team2.append(game[i][1])
                                print("added a player")
                            state = "game"
                            print team1
                            print team2
                            #askQuestion(

                            for p in range(0, len(team1)):
                                Send_whisper(str(team1[p]) + ", you're on team 1 with " + str(len(team1) - 1) + " other players", str(team1[p]))

                            for p in range(0, len(team2)):
                                Send_whisper(str(team2[p]) + ", you're on team 2 with " + str(len(team2) - 1) + " other players", str(team2[p]))

                    if state == "game":
                        print "ingame"

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
