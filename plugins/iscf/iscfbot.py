from errbot import BotPlugin, botcmd

import search 

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
        return 'Hey!'
