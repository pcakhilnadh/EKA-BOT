import discord
import asyncio


class Guild():
    def __init__(self,guild_object):
        self.guildObj=guild_object

    def fetch_all_member(self):
        "return a list of discord.Member "
        return self.guildObj.members
    
    