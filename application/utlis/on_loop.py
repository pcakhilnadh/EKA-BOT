import asyncio
import logging
from datetime import datetime,date

import discord
from discord.ext import tasks
from discord.ext import commands

from application.constants.guild1947 import Guild1947
from application.constants.config import DiscordConfig
from application.constants.emoji import Emoji
class LoopTaks(commands.Cog):
    def __init__(self, bot,db_utlis):
        self.bot = bot
        self.db_utlis = db_utlis
        self.check=0

    def run(self):
        self.periodic_check.start()

    def cog_unload(self):
        self.periodic_check.cancel()
    
    async def birthday_checker(self):
        await self.db_utlis.update_last_run_into_command_on_guild(Guild1947.SERVER_ID,datetime.now())
        today = date.today()
        user_id = self.db_utlis.users_has_bday_on_date(today)
        if user_id:
            for uid in user_id:
                await self.wish_birthday(self.bot.get_user(uid))
        
    async def wish_birthday(self,user_obj):
        birthday_wishes = f" Wish {user_obj.mention}, Happy Birthday !"
        msg = await self.bot.get_channel(Guild1947.ANNOUNCEMENT_CHANNEL_ID).send(content=birthday_wishes)
        await msg.add_reaction(Emoji.BIRTHDAY)

    @tasks.loop(hours=8.0)
    async def periodic_check(self):
        try:
            last_run = await self.db_utlis.fetch_last_run_from_command_on_guild(Guild1947.SERVER_ID)
            now_time = datetime.utcnow()
            time_diiference_in_sec = now_time - last_run
            if time_diiference_in_sec.days >0  :
                await self.birthday_checker()
        except Exception as Ex:
            logging.error("ERROR in on_loop.py : periodic_check () : {}".format(Ex))

    
        

    
    
    