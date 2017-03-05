from random import randint

questions = [[0, "Richard is Cool"], [1, "Forest > Aidan"],\
             [1,"As far as has ever been reported, no-one has ever seen an ostrich bury its head in the sand."],\
             [1, "Approximately one quarter of human bones are in the feet."],[1, "Popeye's nephews are called Peepeye, Poopeye, Pipeye and Pupeye"], \
             [0,"In ancient Rome, a special room called a vomitorium was available for diners to purge food in during meals."],[0,"The average person will shed 10 pounds of skin during their lifetime."],\
             [1,"Sneezes regularly exceed 100 mph."],[1,"A slug has green blood."],\
             [0,"The Great Wall of China is visible from the moon."],[1,"Virtually all Las Vegas gambling casinos ensure that they have no clocks"],
             [1,"The total surface area of two human lungs have a surface area of approximately 70 square metres."],[1,"You cannot cry in space"],\
             [1,"The inventor of the light bulb, Thomas Edison, was afraid of the dark."],[0,"The letter T is the most common in the English Language"],\
             [1,"The strongest muscle in proportion to its size in the human body is the tongue"],\
             [1,"A duck's quack doesn't echo."], [1,"A pregnant goldfish is called a twit"],[0,"Women can read smaller print than men, men have better hearing"],\
             [1, "Ben Franklin's formal education ended at 10 years old."],[1,"Everyday more money is printed for monopoly than the US Treasury"]
             ]

def askQuestion(s):
    random = randint(0, len(questions)
    s.send(quesitons[random][1])
    return quesitons[random][0]

def Send_message(s, message):
    s.send("PRIVMSG #cuhacking :" + message + "\r\n")

def Send_whisper(s, message, player):
    s.send("PRIVMSG #cuhacking :/w " + player + " " + message + "\r\n")
    #s.send("PRIVMSG #AngelOnFira :test\r\n")
    time.sleep(1)
    print("PRIVMSG #cuhacking :/w " + player + " " + message + "\r\n")

def askQuestion(questions, s):
    #Pick a random question from the list
    random = randint(0, len(questions)-1)

    #Ask the question
    Send_message(s, str(questions[random][1]) + " answer true or false.\r\n")

    #Return the answer (0 for false, 1 for true)
    return questions[random][0]