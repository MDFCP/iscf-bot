
import re
import random
from errbot import BotPlugin, botcmd
import shlex

import search 
import webinar

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
            if bool(re.search(r'(^|\W)+(hi|hello|hey)\W+', message.body.lower())):
                self.send(message.frm, self.send_random_greet())
    
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
    
    @botcmd
    def wb(self, msg, args):
        args = shlex.split(args)

        if args[0].lower() == 'submit':
            return webinar.submit(self, args[1:])
        elif args[0].lower() == 'get':
            return webinar.get(self, args[1:])
        return 'Web'
    
    def callback(self):
        webinar.notify(self)
    
    def activate(self):
        super().activate()
        self.start_poller(60, self.callback)
