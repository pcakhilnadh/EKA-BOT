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
        
        await self.bot.get_channel(id=590236645442453544).send(embed=embed)
        await ctx.message.add_reaction("✅")

    @commands.command(aliases=['Dm','dm','DM'])
    async def dm_user(self, ctx, user:discord.User,msg:str):
        """--> `eka dm @mentionUser message`"""
        if user.bot:
            return
        embed = discord.Embed(title = f"You have a message from : {ctx.message.author}",
            description = msg,
            color = 0x98FB98
            )
        embed.set_thumbnail(url=str(ctx.message.author.avatar_url))
        
        try:
            await ctx.message.author.send(embed=embed)
        except:
            await self.bot.get_channel(id=590236645442453544).send("The user has disabled DM.")
        await ctx.message.add_reaction("✅")

        

def setup(bot):
    bot.add_cog(User(bot))

