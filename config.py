import logging
import os

# This is a minimal configuration to get you started with the Text mode.
# If you want to connect Errbot to chat services, checkout
# the options in the more complete config-template.py from here:
# https://raw.githubusercontent.com/errbotio/errbot/master/errbot/config-template.py

BACKEND = 'Slack'  # Errbot will start in text mode (console only mode) and will answer commands from there.

BOT_IDENTITY = {
    'token': os.getenv('SLACK_API_KEY'),
}

BOT_DATA_DIR = r'/err/data'
BOT_EXTRA_PLUGIN_DIR = r'/err/plugins'

BOT_LOG_FILE = r'/err/errbot.log'
BOT_LOG_LEVEL = logging.DEBUG

BOT_ALT_PREFIXES = ('@jarvis',)
BOT_ADMINS = ('@a.upperwal', )  # !! Don't leave that to "@CHANGE_ME" if you connect your errbot to a chat system !!