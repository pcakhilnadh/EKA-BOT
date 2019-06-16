from discord.ext import commands
import discord
import asyncio
import asyncio
import traceback
import inspect
import textwrap
from contextlib import redirect_stdout
import io
import os
import psycopg2
from typing import Union
import datetime
import time
class User(commands.Cog):
    """ EKA members will have all these fun """
    def __init__(self, bot):
        self.bot = bot
        self.sessions = set()
    
    @commands.command(aliases=['Av','av','avatar','Avatar'])
    async def user_avatar(self, ctx, user:discord.User):
        """--> `eka av @mentionUser `"""
        if user.bot:
            return
        embed = discord.Embed(title = f"Avatar Requested of EKA Warrior : {user.name}",
            color = 0x98FB98
            )
        embed.set_image(url = user.avatar_url) 
        
        await self.bot.get_channel(id=569086204621094912).send(embed=embed)
        
        

def setup(bot):
    bot.add_cog(User(bot))

