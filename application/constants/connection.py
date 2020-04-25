from application.constants.guild1947 import Guild1947
from application.constants.guildsupport import GuildSupport

class DiscordConnection():
    def __init__(self):
        pass

    TOKEN = ""
    PREFIX = ['eka ', 'EKA ', 'Eka ']
    BOT_OWNER_ID =286367865462980608
    ALLOWED_CHANNELS= [Guild1947.BOT_TESTING_CHANNEL_ID,Guild1947.EKA_BOT_CHANNEL_ID,Guild1947.VOTING_FOR_RECRUIT_CHANNEL_ID,GuildSupport.COMMANDS_CHANNEL_ID,GuildSupport.BOT_COMMANDS_CHANNEL_ID ]
