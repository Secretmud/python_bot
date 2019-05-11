from random import randint
class function_fun:
    def __init__(self, numb):
        self.numb = numb


    def memePicker(self, numb):
        if  self.numb == 1:
            return "✿*∗˵╰༼✪ᗜ✪༽╯˵∗*✿"
        elif  self.numb == 2:
            return "┏(-_-)┓┏(-_-)┛┗(-_-﻿ )┓"
        elif self.numb == 3:
            return "(ノ◉◞౪◟◉‵)ノ⌒[̲̅$̲̅(̲̅ ͡° ͜ʖ ͡°̲̅)̲̅$̲̅]"
        elif self.numb == 4:
            return "─=≡Σ((( つ◕ل͜◕)つ"

    def olives(self, numb):
        responses = ["I'm a cat mjau mjau mjau CoolCat CoolCat CoolCat CoolCat"]
        r = randint(0, len(responses) - 1)
        print(r)
        return responses[r]

    def quote(self):
        responses = ["People who think they know everything are a great annoyance to those of us who do. -Isacc Asimov",
                  "The saddest aspect of life right now is that science gathers knowledge faster than society gathers wisdom. -Isacc Asimov",
                  "1",
                  "2",
                  "3"
                 ]
        r = randint(0, len(responses) - 1)
        print(r)
        return responses[r]