# python_bot

This bot is written in python3, use it according to the license. 

## JSON

The bot now uses a JSON-file for storing all of the functions. 
As of writing this there is only 3 functions that are unique, one 
of them returns a anonymous function, this is used to search for a keyword on wikipedia. 

```JSON
{
    "id": 2,
    "name": "!wikipedia",
    "type": 0,
    "return": "lambda a: wikipedia.summary(a, sentences=2)"
}
```

If you want to create more functions like this add make the return into a lambda function. The lambda is ran like this:
```Python
lambda parameters: function(paramenters)
```

## connection.py

```Python
PASS = "" #https://www.twitchapps.com/tmi/
NICK = "" #Bot name.
CHAN = "#" #Channel name, the # is in front of the channel name. 
HOST = "irc.chat.twitch.tv" #Twitch irc server
PORT =  6667 #irc server port
RATE = 20 #Message rate, check https://dev.twitch.tv/docs/irc/guide/#command--message-limits
```

Create the following file and fill in the blanks
