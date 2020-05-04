import asyncio
import logging
from datetime import datetime,date

import discord
from discord.ext import tasks
from discord.ext import commands

from application.utlis.birthday import Birthday
from application.constants.guild1947 import Guild1947
from application.constants.guildsupport import GuildSupport
from application.constants.config import DiscordConfig
from application.constants.emoji import Emoji
class LoopTaks(commands.Cog):
    def __init__(self, bot,db_utlis):
        self.bot = bot
        self.db_utlis = db_utlis
        self.check=0

    async def run(self):
        try:
            self.periodic_check.start()
        except RuntimeError as Ex:
            self.periodic_check.cancel()
            self.periodic_check.start()
            await self.bot.get_channel(GuildSupport.BOT_STATUS_CHANNEL_ID).send(f"Error : {Ex}")

    def stop(self):
        self.periodic_check.cancel()

    def cog_unload(self):
        self.periodic_check.cancel()
    
    async def birthday_checker(self):
        today = date.today()
        user_id = self.db_utlis.users_has_bday_on_date(today)
        if user_id:
            for uid in user_id:
                userObj=self.bot.get_user(uid)
                if userObj:
                    await Birthday(self.bot,self.db_utlis,userObj).wish_birthday()
    
    @tasks.loop(hours=1)
    async def periodic_check(self):
        try:
            last_run = await self.db_utlis.fetch_last_run_from_command_on_guild(Guild1947.SERVER_ID)
            now_time = datetime.utcnow()
            time_diiference = now_time - last_run
            await self.bot.get_channel(GuildSupport.BOT_STATUS_CHANNEL_ID).send(f"time {now_time} last time {last_run}")
            if time_diiference.days >0  :
                await self.birthday_checker()
        except Exception as Ex:
            print(Ex)
            logging.error("ERROR in on_loop.py : periodic_check () : {}".format(Ex))

    
        

    
    
    