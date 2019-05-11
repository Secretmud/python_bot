import urllib.request
import json
import pprint
import re
class function_fun:
    def __init__(self, numb):
        self.numb = numb

    def viewCount(self):
        url = urllib.request.urlopen("http://tmi.twitch.tv/group/user/secretmud/chatters")
        data = json.load(url)
        return str(data['chatter_count'] - 1)

    def addCommand(self, new_id, name, use_type, command_return):
        """
            Adding a new command setting the name, type(who can use it) and what the command should return
            {
                "id": new_id,
			    "name": name,
			    "type": type,
			    "return": command_return
            }
        """
        regex = re.compile(r'[\r\n]')
        command_return = regex.sub("", command_return)
        pprint.pprint(str(new_id) + str(name) + str(use_type) + str(command_return))
        json_format = {"id": new_id, "name": name, "type": use_type, "return": command_return}
        with open("commands.json") as fp:
            data = json.load(fp)
        #pprint.pprint(data)    
        with open("commands.json", "w") as commands:    
            data['commands'].append(json_format)
            json.dump(data, commands, sort_keys=True, indent=4)
        commands.close()
        fp.close()