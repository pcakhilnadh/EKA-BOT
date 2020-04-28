import os
from application.constants.guild1947 import Guild1947
from application.constants.guildsupport import GuildSupport

class DiscordConfig():
    def __init__(self):
        pass

    #TOKEN = ""   local
    TOKEN = os.environ.get('TOKEN')
    PREFIX = ['eka ', 'EKA ', 'Eka ']
    BOT_OWNER_ID =286367865462980608
    ALLOWED_CHANNELS= [Guild1947.BOT_TESTING_CHANNEL_ID,Guild1947.EKA_BOT_CHANNEL_ID,Guild1947.VOTING_FOR_RECRUIT_CHANNEL_ID,GuildSupport.COMMANDS_CHANNEL_ID,GuildSupport.BOT_COMMANDS_CHANNEL_ID ]
    ALLOWED_GUILDS = [ GuildSupport.SERVER_ID] 

class PostgreeDB_Config():
    HOST = "localhost"
    DB = "eka_bot_db"
    USER = "postgres"
    PASSWORD = "password"
    #URI = 'postgresql://postgres:password@localhost/eka_bot_db' #local
    URI = os.environ.get('DATABASE_URL')
