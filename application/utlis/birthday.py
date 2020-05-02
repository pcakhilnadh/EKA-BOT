import discord
import asyncio
from datetime import datetime
from application.constants.guild1947 import Guild1947
from application.constants.guildsupport import GuildSupport
from application.constants.emoji import Emoji

class Birthday():
    def __init__(self,bot,db_utlis,userObj):
        self.bot=bot
        self.db_utlis=db_utlis
        self.userObj = userObj
    async def update_lasttime_run_in_db(self):
        time = datetime.now()
        time = time.replace(hour=0, minute=0, second=0,microsecond=0)
        await self.db_utlis.update_last_run_into_command_on_guild(Guild1947.SERVER_ID,time)

    async def wish_birthday(self):
        await self.update_lasttime_run_in_db()
        birthday_wishes = f"@everyone Wish {self.userObj.mention}, Happy Birthday !"
        embed = discord.Embed(title = f"Happy Birthday : {self.userObj.name}",color = 0x98FB98)
        embed.set_image(url = self.userObj.avatar_url)
        msg = await self.bot.get_channel(Guild1947.ANNOUNCEMENT_CHANNEL_ID).send(content=birthday_wishes,embed=embed)
        await msg.add_reaction(Emoji.BIRTHDAY)