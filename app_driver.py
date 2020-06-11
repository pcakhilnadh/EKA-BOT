__version__ = '0.0.1'
__author__ = 'Pc'
__description__ = 'A Discord Bot for Elite Kerala Alliance !'

import discord
import sys, traceback
import aiohttp
import asyncio
from discord.ext import commands
from datetime import datetime
import logging
# userFunctions
from application.utlis.on_ready import OnReady
from application.utlis.on_resume import OnResume
from application.cogs.utils import context
from application.constants.config import DiscordConfig
from application.constants.config import GuildSupport
import os
#from application.utlis.on_loop import LoopTaks
description = 'A Discord Bot for Elite Kerala Alliance'
OWNER = DiscordConfig.BOT_OWNER_ID


def get_prefix(bot, message):
    """A callable Prefix for our bot. This could be edited to allow per server prefixes."""

    prefixes = DiscordConfig.PREFIX
    if not message.guild:
        return 'eka'
    if message.author.id == OWNER:
        prefixes.append('')

    return commands.when_mentioned_or(*prefixes)(bot, message)


initial_extensions = (
    'application.cogs.owner',
    'application.cogs.debug',
    'application.cogs.user',
    'application.cogs.helper',
    # 'cogs.music',

)


class EkaBot(commands.AutoShardedBot):

    def __init__(self):
        super().__init__(command_prefix=get_prefix, description=description)

        self.owner_id = DiscordConfig.BOT_OWNER_ID
        self.channel_id = DiscordConfig.ALLOWED_CHANNELS
        self.guild_id = DiscordConfig.ALLOWED_GUILDS
        self._task = self.loop.create_task(self.initialize())
        #self.db_utlis = db_utlis
        self.tester = " Im a tester"
        # self.spam_control = commands.CooldownMapping.from_cooldown(10, 12, commands.BucketType.user)
        self.activity = discord.Activity(type=discord.ActivityType.listening, name='EKA')
        for extension in initial_extensions:
            try:
                self.load_extension(extension)
            except:
                print(f'Failed to load extension {extension}.', file=sys.stderr)
                traceback.print_exc()

    async def initialize(self):
        self.session = aiohttp.ClientSession(loop=self.loop)
        await self.wait_until_ready()
        self.owner = self.get_user(OWNER)

    async def process_commands(self, message):
        ctx = await self.get_context(message, cls=context.Context)
        if ctx.command is None:
            return
        if message.guild.id not in self.guild_id:
            return
        if message.channel.id not in self.channel_id:
            # await message.channel.send("Bot commands don't work in this channel")
            return
        '''
        if message.author.id :
            if message.author.id in self.owner_id:
                await self.bote(ctx)
                return
            if message.author.bot:
                return
            flag=0
            for r in message.author.roles:
                if r.name =='C o м м a n d e r':
                    flag=1
            if flag==1:
                await self.invoke(ctx)
            else:
                await message.channel.send(f"Only C o м м a n d e r can use EKA BOT")
            return
        '''
        await self.invoke(ctx)

    async def on_message(self, message):
        if message.author.bot:
            return
        await self.process_commands(message)

    async def on_ready(self):
        #on_ready_obj = OnReady(super())
        #await on_ready_obj.print_msg()
        #await on_ready_obj.run_tasks()
        print(f'Ready...!')
    async def on_resumed(self):
        #on_resume_obj = OnResume(super())
        #await on_resume_obj.print_msg()
        #await on_resume_obj.run_tasks()
        print('resumed...')

    async def close(self):
        #bot_online_channel_id = 586993318035062785
        #bot_online_channel = super().get_channel(bot_online_channel_id)
        title = " BOT Online Status"
        description = "\n BOT is offline"
        embed = discord.Embed(title=title,
                              description=description,
                              color=discord.Color.red())
        #await bot_online_channel.send(embed=embed)
        print(f'BOT is offline')
        await super().close()
        await self.session.close()
        self._task.cancel()
        #LoopTaks(super()).stop()


    

    def run(self):
        try:
            #super().run(os.environ.get('TOKEN'), bot=True, reconnect=True)
            super().run(DiscordConfig.TOKEN,bot=True, reconnect=True)
            #print(self.testmodule)
        except Exception as e:
            print(f'Troubles running the bot!\nError: {e}')
            # traceback.print_exc()

