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
    async def on_member_join(self, member):
        x = time.time()
        if member.guild.id == 561249245672374273:  # 1947 Server
            welcomechannel = self.bot.get_channel(569973273253904385)
            apply_eka = self.bot.get_channel(566609366770515989)
            about = self.bot.get_channel(567962887054950420)
            directory = os.getcwd()
            file = discord.File(os.path.join(directory + str('/') + "images/recruitment.jpg"),
                                filename="recruitment.jpg")
            embed = discord.Embed(title="**__WELCOME TO EKA__**", colour=discord.Colour(0x673c27),
                                  url="https://link.clashofclans.com/?action=OpenClanProfile&tag=29L9RVCL8",
                                  description=f"Hello {member.name},  \n\n:point_right:Elite Kerala Alliance. \n:point_right: CWL CLAN.\n:point_right: CWL PREMIER, CWL PHEONIX, MLCW-GWL \n\n  ",
                                  timestamp=datetime.datetime.utcfromtimestamp(x))
            embed.set_thumbnail(url=str(member.avatar_url))
            embed.set_author(name="Elite Kerala Alliance ",
                             url="https://link.clashofclans.com/?action=OpenClanProfile&tag=RJ9JYYQQ",
                             icon_url="https://cdn.discordapp.com/attachments/562537063052738569/582847093434089472/eka.jpg")
            embed.set_footer(text="Team EKA |",
                             icon_url="https://cdn.discordapp.com/attachments/562537063052738569/582847093434089472/eka.jpg")
            embed.add_field(name=f"Want to join With Us ?",
                            value=f"React with :envelope_with_arrow: in {apply_eka.mention} \n\n\n\n")
            embed.add_field(name=f"Want to get GUEST role ?",
                            value=f":sos: React with EKA logo in {about.mention} \n\n")
            # embed.set_image(url="attachment://recruitment.jpg")
            await welcomechannel.send(content=f"{member.mention}", file=file, embed=embed)
            try:
                await member.send(content=f"{member.mention}", file=file, embed=embed)
            except:
                pass
        if member.guild.id == 586915159377707027:  # Support Server
            welcomechannel = self.bot.get_channel(588632891710504960)
            embed = discord.Embed(title="**__WELCOME TO EKA BOT Support__**", colour=discord.Colour(0x673c27),
                                  description=f"Hello {member.mention} | {member.name}  You are {member.guild.member_count} th Member \n Greetings from EKA BOT Developers  ",
                                  timestamp=datetime.datetime.utcfromtimestamp(x))
            await welcomechannel.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        if member.guild.id == 561249245672374273:
            welcomechannel = self.bot.get_channel(562568072146321418)
            embed = discord.Embed(title="You Lost a member",
                                  description=f"{member} left {member.guild.name} server!",
                                  color=0x07999b
                                  )
            await welcomechannel.send(embed=embed)

        if member.guild.id == 586915159377707027:
            welcomechannel = self.bot.get_channel(588632891710504960)
            embed = discord.Embed(title="You Lost a member",
                                  description=f"{member} left {member.guild.name} server!",
                                  color=0x07999b
                                  )
            await welcomechannel.send(embed=embed)

    @commands.command(aliases=['sixpack', '6pack'])
    @commands.has_any_role("Admin", "C o м м a n d e r")
    # @commands.is_owner()
    async def six_pack(self, ctx, user: discord.User):
        """eka 6pack @mention <Optional Msg>"""
        msg = await self.bot.get_channel(id=590236928918552713).send(
            f" Congratulate {user.mention} for Six Pack Performance")
        await msg.add_reaction("🍻")
        await ctx.message.add_reaction("✅")
        try:
            await user.send(f" Dear EKA Warrior {user.name} ,Team EKA is very proud of your performance. Keep it up")
        except:
            pass

    @commands.command(aliases=['newwar'])
    @commands.has_any_role("Admin", "C o м м a n d e r")
    # @commands.is_owner()
    async def new_war(self, ctx):
        """eka new_war <Optional Clan Name>"""
        GuildObj = self.bot.get_guild(561249245672374273)
        Categories = GuildObj.by_category()
        for category in Categories:
            CategoryInfo, Channels = category
            if CategoryInfo.id == 561270179221471274:  # Enemy base channel
                for channels in Channels:
                    if channels.id == 568094450144903188:
                        continue
                    msg = await self.bot.get_channel(id=channels.id).send(
                        f"https://cdn.discordapp.com/attachments/701323612665151488/701323681619640400/new_war.jpg")
        await ctx.message.add_reaction("✅")
        try:
            await user.send(f" Dear EKA Warrior {user.name} ,Team EKA is very proud of your performance. Keep it up")
        except:
            pass

    @commands.command(aliases=['misshit', 'hitmissed'])
    @commands.has_any_role("Admin", "C o м м a n d e r")
    # @commands.is_owner()
    async def miss_hit(self, ctx, user: discord.User):
        """eka misshit @mention <Optional Msg>"""
        msg = await self.bot.get_channel(id=590236928918552713).send(
            f" {user.mention} has been warned for missing hit  in the WAR :sos: ")
        await msg.add_reaction("⚠")
        await ctx.message.add_reaction("✅")
        try:
            await user.send(
                f" Dear EKA Warrior {user.name} , You ought to use both attacks in war. Discuss with team the reason ASAP")
        except:
            pass

    @commands.command(aliases=['latehit', 'lateattack'])
    @commands.has_any_role("Admin", "C o м м a n d e r")
    # @commands.is_owner()
    async def late_hit(self, ctx, user: discord.User):
        """eka latehit @mention <Optional Msg>"""
        msg = await self.bot.get_channel(id=590236928918552713).send(
            f" {user.mention} has been warned for Late hit  in the WAR :sos: ")
        await msg.add_reaction("⚠")
        await ctx.message.add_reaction("✅")
        try:
            await user.send(
                f" Dear EKA Warrior {user.name} , You ought to plan and attack in time. Discuss with team the reason ASAP")
        except:
            pass

    @commands.command()
    @commands.has_any_role("Admin", "C o м м a n d e r")
    # @commands.is_owner()
    async def vote(self, ctx, user: discord.User, message: str = None):
        """eka vote @mention <Optional Msg>"""
        chId = self.bot.get_channel(id=588736568597151760)
        if message:
            msg = await self.bot.get_channel(id=588736568597151760).send(
                f"  Please vote for {user.name} according to war performance against {message} :thumbsup: Good :thumbsdown: Bad")
        else:
            msg = await self.bot.get_channel(id=588736568597151760).send(
                f"  Please vote for {user.name} according to war performance :thumbsup: Good :thumbsdown: Bad")

        await msg.add_reaction("\U0001f44d")
        await msg.add_reaction("\U0001f44e")
        await msg.add_reaction("⛔")
        await self.bot.get_channel(id=564838401258422283).send(
            f"@everyone Voting for evaluvating war performance of {user.name} has started. Cast your votes {chId.mention}")
        await ctx.message.add_reaction("✅")

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        if payload.channel_id == 588736568597151760:

            memberObj = self.bot.get_guild(payload.guild_id).get_member(payload.user_id)
            messageObj = await self.bot.get_channel(payload.channel_id).fetch_message(payload.message_id)
            if (discord.utils.get(memberObj.roles, name='f ι e l d  м a r ѕ н a l')):
                try:
                    u = self.bot.get_user(payload.user_id)
                    await u.send(
                        "You can't cast vote sorry.Sorry, You need to have higher roles in our server to cast vote.")
                    await messageObj.remove_reaction(payload.emoji, memberObj)
                except:
                    await self.bot.get_channel(id=569086204621094912).send(
                        f"{memberObj.mention} DM is disabled. Sorry, You need to have higher roles to cast the vote")
                    await messageObj.remove_reaction(payload.emoji, memberObj)
            else:
                likeCount = dislikeCount = 0
                try:
                    likeReactionObj = messageObj.reactions[0]
                    dislikeReactionObj = messageObj.reactions[1]
                    noentryReactionObj = messageObj.reactions[2]
                    tickReactionObj = messageObj.reactions[3]
                except:
                    pass
                try:
                    if str(noentryReactionObj.emoji) == str(payload.emoji):
                        if discord.utils.get(memberObj.roles, name='C o м м a n d e r'):
                            await messageObj.add_reaction("✅")
                        else:
                            if not memberObj.bot:
                                # print(f'RT')
                                await messageObj.remove_reaction(payload.emoji, memberObj)
                except UnboundLocalError:
                    pass

                try:
                    if str(tickReactionObj.emoji) == str(payload.emoji):
                        if discord.utils.get(memberObj.roles, name='C o м м a n d e r'):
                            FmessageObj = await self.bot.get_channel(payload.channel_id).fetch_message(
                                payload.message_id)
                            await self.bot.get_channel(id=588736568597151760).send(
                                f" {list(str(FmessageObj.content).split())[3]} Performance Evaluation  Result **Like** {likeReactionObj.count - 1} **Dislike** {dislikeReactionObj.count - 1} Poll has been ended by {memberObj.name}")
                            await messageObj.delete()
                        else:
                            if not memberObj.bot:
                                # print(f'NOT')
                                await messageObj.remove_reaction(payload.emoji, memberObj)
                except UnboundLocalError:
                    pass
                try:
                    if not memberObj.bot:
                        if (str(payload.emoji) == str(dislikeReactionObj.emoji)) or (
                                str(payload.emoji) == str(likeReactionObj.emoji)):
                            async for user in likeReactionObj.users():
                                if user.id == payload.user_id:
                                    likeCount = 1
                            async for user in dislikeReactionObj.users():
                                if user.id == payload.user_id:
                                    dislikeCount = 1
                except UnboundLocalError:
                    pass

                if likeCount + dislikeCount > 1:
                    # print(f'asd')
                    if str(likeReactionObj.emoji) == str(payload.emoji):
                        await messageObj.remove_reaction(payload.emoji, memberObj)
                    if str(dislikeReactionObj.emoji) == str(payload.emoji):
                        await messageObj.remove_reaction(payload.emoji, memberObj)

        if payload.channel_id == 633715289309052942:
            memberObj = self.bot.get_guild(payload.guild_id).get_member(payload.user_id)
            if payload.message_id == 633725319207190548:
                messageObj = await self.bot.get_channel(payload.channel_id).fetch_message(payload.message_id)
                if str(payload.emoji) == str("🔞"):
                    GuildObj = self.bot.get_guild(561249245672374273)
                    roleObj = discord.utils.get(GuildObj.roles, name="18+")
                    await memberObj.add_roles(roleObj)
                    await self.bot.get_channel(id=573789844745224192).send(
                        f"{memberObj.mention} Reacted to get `18+` Role ")

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):

        if payload.channel_id == 633715289309052942:
            memberObj = self.bot.get_guild(payload.guild_id).get_member(payload.user_id)
            if payload.message_id == 633725319207190548:
                messageObj = await self.bot.get_channel(payload.channel_id).fetch_message(payload.message_id)
                if str(payload.emoji) == str("🔞"):
                    GuildObj = self.bot.get_guild(561249245672374273)
                    roleObj = discord.utils.get(GuildObj.roles, name="18+")
                    await memberObj.remove_roles(roleObj)
                    await self.bot.get_channel(id=573789844745224192).send(
                        f"{memberObj.mention} Reacted to Remove `18+` Role ")

    @commands.Cog.listener()
    async def on_message(self, message):

        if message.author.bot:
            return
        if message.channel.id == 590236645442453544:
            if list(str(message.content).split())[0] not in ['eka', 'Eka', 'EKA']:
                # await message.delete()
                await self.bot.get_channel(id=message.channel.id).send(
                    "Invalid BOT command.  ```eka help``` If you are looking for BOT commands. Pls use loungue to chat. Thanks")


def setup(bot):
    bot.add_cog(Owner(bot))
