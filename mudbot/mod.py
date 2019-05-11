import urllib.request
import json
import socket
import re
import io
import random
import wikipedia
from connection import *
import csv
import datetime
from time import sleep
from src.help import *
print("""Thanks for using the nice chill bot. \nI will make you proud!""")
f = function_fun(1)
CHAT_MSG = re.compile(r"^:\w+!\w+@\w+\.tmi\.twitch\.tv PRIVMSG #\w+ :")

#Network functions
#Uses socket to connect you to host +port, the rest will connect you to the channel +using oauth key +nick
s = socket.socket()
s.connect((HOST, PORT))
s.send("PASS {}\r\n".format(PASS).encode("utf-8"))
s.send("NICK {}\r\n".format(NICK).encode("utf-8"))
s.send("JOIN {}\r\n".format(CHAN).encode("utf-8"))



hype = ["HYPE", "Hype", "hype"]    
greetings = ["Hello", "hello",
             "Hi", "hi", 
             "Yo", "yo", 
             "Evening", "evening"]
names = ["tmi", "botmud"]
hype_names = []
time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
command = []
with open("commands.json") as commands:
    data = json.load(commands)
    for x in range(0, len(data['commands']) - 1):
        command.append(data['commands'][x]['name'])
        print(command[x])
        
print(len(data['commands']) - 1)
while True:
    response = s.recv(1024).decode("utf-8") #Get text from twitch +decodes it for py3 to play with
    if response == "PING :tmi.twitch.tv\r\n": #Twich will send you a ping every 5 minutes to check if you're still there
        s.send("PONG :tmi.twitch.tv\r\n".encode("utf-8")) # You have to pong back to stay up
    else:
        username = re.search(r"\w+", response).group(0) # return the username
        message = CHAT_MSG.sub(" ", response) #return the message
        sleep(1/RATE)
        x = [time, username, message]
        log_name = str(time) +'log.csv'
        with open(log_name, 'a') as csvfile:
            fieldnames = ['1', '2', '3']
            writer = csv.writer(csvfile, lineterminator='\n')
            
            writer.writerow(x)
        
        for x in greetings:
            for n in names:
                if username not in names and x in message:
                    response = ("PRIVMSG " + CHAN + " :Hello :) "
                        + username + " how's life?\n ").encode("utf-8")
                    s.send(response)
                    print(response)

                    names.append(username)
                    
        #http://tmi.twitch.tv/group/user/{USERNAME}/chatters

        for x in command:
            if x in message:
                index = command.index(x)
                if data['commands'][index]['name'] == "!wikipedia":
                    x = eval(data['commands'][index]['return'])
                    message.split()
                    response = ("PRIVMSG " + CHAN + " :" + 
                            x(message[1:]) + "\n").encode('utf-8')
                else:
                    response = ("PRIVMSG " + CHAN + " :" + 
                            data['commands'][index]['return'] + 
                            "\n").encode('utf-8')
                s.send(response)
            
        if "!help" in message:
            msg = ("PRIVMSG " + CHAN + " :These are my commands - " +
                    "!wisdom, !oliveoil, !cowbell \n").encode("utf-8")
            s.send(msg)
