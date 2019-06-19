
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
#userFunctions
from cogs.utils import context
import os

description='A Discord Bot for Elite Kerala Alliance'
OWNER = 286367865462980608


def get_prefix(bot, message):
    """A callable Prefix for our bot. This could be edited to allow per server prefixes."""

    prefixes = ['eka ', 'EKA ','Eka ']
    if not message.guild:
        return 'eka'
    if message.author.id == OWNER:
        prefixes.append('')

    return commands.when_mentioned_or(*prefixes)(bot, message)

initial_extensions = (
    'cogs.owner',
    'cogs.debug',
    'cogs.user',
    'cogs.helper',
    
)



class EkaBot(commands.AutoShardedBot):

    def __init__(self):
        super().__init__(command_prefix=get_prefix, description=description)
        
        self.owner_id = 286367865462980608
        self.channel_id= [586915160015503390,590236645442453544,562537063052738569,588736568597151760,590626344459698177]
        #bot_command, eka_bot,bot_test,votting_recruitment, longue
        self._task = self.loop.create_task(self.initialize())
        # self.spam_control = commands.CooldownMapping.from_cooldown(10, 12, commands.BucketType.user)
        self.activity = discord.Activity(type=discord.ActivityType.listening,name='Pc')
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
        if message.channel.id not in self.channel_id:
            #await message.channel.send("Bot commands don't work in this channel")
            return
        '''
        if message.author.id :
            if message.author.id in self.owner_id:
                await self.invoke(ctx)
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
        bot_online_channel_id = 586993318035062785
        total_width = 0
        infos = (
            'EKA Bot',
            f'{self.user.name} [{self.user.id}]',
            f'Discord: {discord.__version__}',
            f'Guilds: {len(self.guilds)}',
            f'Users: {len(self.users)}',
            f'Shards: {self.shard_count}'
        )
        for info in infos:
            width = len(str(info)) + 4
            if width > total_width:
                total_width = width

        sep = '+'.join('-' * int((total_width/2)+1))
        sep = f'+{sep}+'

        information = [sep]
        for info in infos:
            elem = f'|{info:^{total_width}}|'
            information.append(elem)
        information.append(sep)
        bot_online_channel = super().get_channel(bot_online_channel_id)
        title = " BOT Online Status"
        description= "\n".join(information)
        embed = discord.Embed(title=title,
                              description=description,
                              color=discord.Color.green())
        await bot_online_channel.send(embed=embed)

        
        # print(f'\n\nLogged in as: {self.user.name} - {self.user.id}\nVersion: {discord.__version__}\n\n'
        #       f'Guilds: {len(self.guilds)}\nUsers: {len(self.users)}\n'
        #       f'Shards: {self.shard_count}\n\n')

        print(f'Successfully logged in and booted...!')


    async def on_resumed(self):
        print('resumed...')


    async def close(self):
        bot_online_channel_id = 586993318035062785
        bot_online_channel = super().get_channel(bot_online_channel_id)
        title = " BOT Online Status"
        description= "\n BOT is offline"
        embed = discord.Embed(title=title,
                              description=description,
                              color=discord.Color.red())
        await bot_online_channel.send(embed=embed)
        print(f'BOT is offline')
        await super().close()
        await self.session.close()
        self._task.cancel()
    

    def run(self):
        try:
            super().run(os.environ.get('TOKEN'), bot=True, reconnect=True)
        except Exception as e:
            print(f'Troubles running the bot!\nError: {e}')
            # traceback.print_exc()

def main():
    bot = EkaBot()
    bot.run()


if __name__ == '__main__':
    main()
