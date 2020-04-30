import discord
import asyncio
from datetime import datetime
from application.constants.guildsupport import GuildSupport
from application.constants.guild1947 import Guild1947
from application.constants.config import DiscordConfig
from application.utlis.on_loop import LoopTaks

class OnReady():
    def __init__(self,bot,db_utlis):
        self.bot= bot
        self.db_utlis = db_utlis
    async def print_msg(self):
        print(f'Successfully logged...!')
        bot_online_channel_id = GuildSupport.BOT_STATUS_CHANNEL_ID
        total_width = 0
        infos = (
            'EKA Bot',
            f'{self.bot.user.name} [{self.bot.user.id}]',
            f'Discord: {discord.__version__}',
            f'Guilds: {len(self.bot.guilds)}',
            f'Users: {len(self.bot.users)}'
        )
        for info in infos:
            width = len(str(info)) + 4
            if width > total_width:
                total_width = width

        sep = '+'.join('-' * int((total_width / 2) + 1))
        sep = f'+{sep}+'

        information = [sep]
        for info in infos:
            elem = f'|{info:^{total_width}}|'
            information.append(elem)
        information.append(sep)
        bot_online_channel = self.bot.get_channel(bot_online_channel_id)
        title = " BOT Online Status"
        description = "\n".join(information)
        embed = discord.Embed(title=title,
                              description=description,
                              color=discord.Color.green())
        await bot_online_channel.send(embed=embed)

    async def run_tasks(self):
        tasks = LoopTaks(self.bot,self.db_utlis)
        tasks.run()
        
    
