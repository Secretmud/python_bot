import socket
import re
import io
import random
import connection
import csv
import datetime
from time import sleep
def memePicker(numb):
    if numb == 1:
        return "✿*∗˵╰༼✪ᗜ✪༽╯˵∗*✿"
    elif numb == 2:
        return "┏(-_-)┓┏(-_-)┛┗(-_-﻿ )┓"
    elif numb == 3:
        return "(ノ◉◞౪◟◉‵)ノ⌒[̲̅$̲̅(̲̅ ͡° ͜ʖ ͡°̲̅)̲̅$̲̅]"
    elif numb == 4:
        return "─=≡Σ((( つ◕ل͜◕)つ"

def olives(numb):
    if numb ==1:
        return " :I'm a cat mjau mjau mjau CoolCat CoolCat CoolCat CoolCat and Stefler12 is a qt π Kappa \n"
    if numb ==2:
        return " :Stefler12 tend to say some strange things... \n"
    if numb ==3:
        return " :What do you want? I don't even know you... \n"

def quote(numb):
    if numb ==1:
        return "We are all born ignorant, but one must work hard to remain stupid KappaRoss"
    elif numb ==2:
        return "Life is tough, but it's tougher since you're stupid Kappa"
    elif numb ==3:
        return ", what's that? It's not in my vodkabulary, but let me check in whiskypedia BCWarrior "
    elif numb ==4:
        return "Stupid is when you spend 18 hours trying to drown a fish KappaClaus"
    elif numb ==5:
        return "I couldn’t repair your brakes, so I made your horn louder Kappa"
    elif numb ==6:
        return "Have you ever wondered why you can't taste your tongue?"
    elif numb ==7:
        return "I never apologise. I'm sorry, that's just the way I am"
    elif numb ==8:
        return "Alcohol makes other people less tedious, food less bland, can help provide what the Greeks called entheos, or the slight buzz of inspiration when reading or writing. - Christopher Hitchens"
    elif numb ==9:
        return "87% young people have back pain. The other 13% have no computer."
    elif numb ==10:
        return "I poured some shampoo over my speakers today and  they blew up.... So much for extra volume Kappa"
    elif numb ==11:
        return "I don't hate you, but I wish your dad used a condom KappaRoss"
    elif numb ==12:
        return "I meant to behave but there were to many other options"
    elif numb ==13:
        return "The police are looking for a suspect described as sexy, funny & great in bed. Your ugly ass is safe, but where should i hide?"
    elif numb ==14:
        return "When people call me weird I laugh cause they haven't met the people that I hang out with lol"
    elif numb ==15:
        return "Our doubts are traitors,and make us lose the good we oft might win,by fearing to attempt. - Sir William Shakespeare"
    elif numb ==16:
        return "If you're red, you're dead - xToFxREAPER"
    elif numb ==17:
        return "I'm as fine as sand. Cuz I'm rough around the edges - BeardMagic253"
    elif numb ==18:
        return "You can't really chill while eating chili... - Die4frags"


CHAT_MSG = re.compile(r"^:\w+!\w+@\w+\.tmi\.twitch\.tv PRIVMSG #\w+ :")

#Network functions
#Uses socket to connect you to host +port, the rest will connect you to the channel +using oauth key +nick
s = socket.socket()
s.connect((connection.HOST, connection.PORT))
s.send("PASS {}\r\n".format(connection.PASS).encode("utf-8"))
s.send("NICK {}\r\n".format(connection.NICK).encode("utf-8"))
s.send("JOIN {}\r\n".format(connection.CHAN).encode("utf-8"))



hype = ["HYPE", "Hype", "hype"]    
greetings = ["Hello", "hello",
             "Hi", "hi", 
             "Yo", "yo", 
             "Evening", "evening"]
names = ["tmi", "botmud"]
hype_names = []
time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
while True:
    response = s.recv(1024).decode("utf-8") #Get text from twitch +decodes it for py3 to play with
    if response == "PING :tmi.twitch.tv\r\n": #Twich will send you a ping every 5 minutes to check if you're still there
        print("test2")
        s.send("PONG :tmi.twitch.tv\r\n".encode("utf-8")) # You have to pong back to stay up
    else:
        username = re.search(r"\w+", response).group(0) # return the username
        message = CHAT_MSG.sub(" ", response) #return the message
        print(username + ": " + message)
        sleep(1/connection.RATE)
        x = [time, username, message]
        print(names)
        log_name = str(time) +'log.csv'
        with open(log_name, 'a') as csvfile:
            fieldnames = ['1', '2', '3']
            writer = csv.writer(csvfile, lineterminator='\n')
            
            writer.writerow(x)
        

        for x in greetings:
            for n in names:
                if username not in names and x in message:
                    nothisisnotlive = ("PRIVMSG " + connection.CHAN + " :Hello :) "
                        + username + " how's life?\n ").encode("utf-8")
                    s.send(nothisisnotlive)
                    names.append(username)
                    
        if "!wisdom" in message:
            r = random.randint(4-3,21-3)
            fun = quote(r)
            this = ("PRIVMSG " + connection.CHAN + " :@"+ username + " " + fun + " \n").encode("utf-8")
            s.send(this)
        
        elif "!oliveoil" in message:
            get = ("PRIVMSG " + connection.CHAN + " :That's some pretty nice olive oil! Wouldn't mind passing some over to me " + username + "? k thx bye <3 \n").encode("utf-8")
            s.send(get)
        
        elif "!cowbell" in message:
            r= random.randint(1,4)
            fun = memePicker(r)
            get = ("PRIVMSG " + connection.CHAN + " :Where's the cowbells at? Do you have some for me @" + username + " " + fun + " \n").encode("utf-8")
            s.send(get)

        elif "!help" in message:
            msg = ("PRIVMSG " + connection.CHAN + " :These are my commands - " +
                    "!wisdom, !oliveoil, !cowbell \n").encode("utf-8")
            s.send(msg)
