from errbot import BotPlugin, botcmd

import search 
import random
import re

class ISCFBot(BotPlugin):
    """
    This is a very basic plugin to try out your new installation and get you started.
    Feel free to tweak me to experiment with Errbot.
    You can find me in your init directory in the subdirectory plugins.
    """

    @botcmd  # flags a command
    def find(self, msg, args):  # a command callable with !tryme
        """
        Execute to check if Errbot responds to command.
        Feel free to tweak me to experiment with Errbot.
        You can find me in your init directory in the subdirectory plugins.
        """
        #print('pp')
        """ print(args)"""
        return search.se(args) 

    @botcmd
    def hi(self, msg, args):
        return self.send_random_greet()
    
    def callback_mention(self, message, mentioned_people):
        if self.bot_identifier in mentioned_people:
            if bool(re.match(r'/(hi)|(hello)|(hey)/gi', s.lower())):
                return self.send_random_greet()
    
    def send_random_greet(self):
        response = [
            "Hello",
            "Hello there.",
            "Hi",
            "Hi there.",
            "Hey",
            "Good day",
            "Pleased to meet you",
            "How are things?",
            "Hiya",
            "Sup?",
            "What's up?",
            "Whasssup?",
            "How's it going?",
            "Howdy",
            "Well hello!",
            "Yo",
            "Greetings!",
            "Look who it is!"
        ]
        return random.choice(response)
