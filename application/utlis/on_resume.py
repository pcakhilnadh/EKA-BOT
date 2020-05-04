import discord
import asyncio
from datetime import datetime
from application.constants.guildsupport import GuildSupport
from application.constants.guild1947 import Guild1947
from application.constants.config import DiscordConfig
from application.utlis.on_loop import LoopTaks

class OnResume():
    def __init__(self,bot,db_utlis):
        self.bot= bot
        self.db_utlis = db_utlis
    async def print_msg(self):
        now_time = datetime.utcnow()
        message = f"Resumed : {now_time}"
        await bot_online_channel.send(content=message)

    async def run_tasks(self):
        tasks = LoopTaks(self.bot,self.db_utlis)
        tasks.run()
        
    
