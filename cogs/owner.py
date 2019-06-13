from discord.ext import commands
import discord
import asyncio
from copy import deepcopy
import asyncio
import traceback
import inspect
import textwrap
from contextlib import redirect_stdout
import io
import os
import copy
from typing import Union
# to expose to the eval command
import datetime
import time
from collections import Counter

class Owner(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.sessions = set()

    @commands.command()
    @commands.is_owner()
    async def sudo(self, ctx, user: Union[discord.Member, discord.User], *, command: str):
        """Run a command as another user."""
        msg = copy.copy(ctx.message)
        msg.author = user
        msg.content = ctx.prefix + command
        new_ctx = await self.bot.get_context(msg)
        await self.bot.invoke(new_ctx)
    @commands.Cog.listener()
    async def on_member_join(self,member):
        x=time.time()
        if member.guild.id == 561249245672374273: #1947 Server
            welcomechannel = self.bot.get_channel(569973273253904385)
            apply_eka = self.bot.get_channel(566609366770515989)
            about =self.bot.get_channel(567962887054950420)
            directory=os.getcwd()
            file = discord.File(os.path.join(directory+str('/')+"images/recruitment.jpg"),filename="recruitment.jpg")
            embed = discord.Embed(title="**__WELCOME TO EKA__**", colour=discord.Colour(0x673c27), url="https://link.clashofclans.com/?action=OpenClanProfile&tag=RJ9JYYQQ", description=f"Hello {member.mention} | {member.name}  \n\n:point_right:Elite Kerala Alliance. \n:point_right: MLCW - GWL  clan.\n:point_right: WCL, EWL, NDL WELTER\n\n  ", timestamp=datetime.datetime.utcfromtimestamp(x))
            embed.set_thumbnail(url=str(member.avatar_url))
            embed.set_author(name="Elite Kerala Alliance ", url="https://link.clashofclans.com/?action=OpenClanProfile&tag=RJ9JYYQQ", icon_url="https://cdn.discordapp.com/attachments/562537063052738569/582847093434089472/eka.jpg")
            embed.set_footer(text="Team EKA |", icon_url="https://cdn.discordapp.com/attachments/562537063052738569/582847093434089472/eka.jpg")
            embed.add_field(name=f"Want to join With Us ?", value=f"React with :envelope_with_arrow: in {apply_eka.mention} \n\n\n\n")
            embed.add_field(name=f"Want to get GUEST role ?", value=f":sos: React with EKA logo in {about.mention} \n\n")
            #embed.set_image(url="attachment://recruitment.jpg")
            await welcomechannel.send(file=file,embed = embed)
        if member.guild.id == 586915159377707027: #Support Server
            welcomechannel = self.bot.get_channel(588632891710504960)
            embed = discord.Embed(title="**__WELCOME TO EKA BOT Support__**", colour=discord.Colour(0x673c27), description=f"Hello {member.mention} | {member.name}  You are {member.guild.member_count} th Member \n Greetings from EKA BOT Developers  ", timestamp=datetime.datetime.utcfromtimestamp(x))
            await welcomechannel.send(embed = embed)
    @commands.Cog.listener()
    async def on_member_remove(self,member):
        if member.guild.id == 561249245672374273:
            welcomechannel = self.bot.get_channel(562568072146321418)
            embed = discord.Embed(title = "You Lost a member",
            description = f"{member} left {member.guild.name} server!",
            color = 0x07999b
            )
            await welcomechannel.send(embed = embed)

        if member.guild.id == 586915159377707027:
            welcomechannel = self.bot.get_channel(588632891710504960)
            embed = discord.Embed(title = "You Lost a member",
            description = f"{member} left {member.guild.name} server!",
            color = 0x07999b
            )
            await welcomechannel.send(embed = embed)

    @commands.command()
    #@commands.is_owner()
    async def vote(self, ctx, user:discord.User):
        """eka vote @mention"""
        chId=self.bot.get_channel(id=588736568597151760)
        msg= await self.bot.get_channel(id=588736568597151760).send(f"Please vote for {user.mention} according to war performance. :thumbsup: Good :thumbsdown: Bad")
        await msg.add_reaction("\U0001f44d")
        await msg.add_reaction("\U0001f44e")
        await self.bot.get_channel(id=569086204621094912).send(f"@here Voting for evaluvating war performance of {user.name} has started. Cast your votes {chId.mention}")
                    


def setup(bot):
    bot.add_cog(Owner(bot))
