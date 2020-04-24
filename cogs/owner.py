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
                                  description=f"Hello {member.name},  \n\n:point_right:Elite Kerala Alliance. \n:point_right: CWL \n:point_right: MLCW \n:point_right: NDL \n\n  ",
                                  timestamp=datetime.datetime.utcfromtimestamp(x))
            embed.set_thumbnail(url=str(member.avatar_url))
            embed.set_author(name="Elite Kerala Alliance ",
                             url="https://link.clashofclans.com/?action=OpenClanProfile&tag=RJ9JYYQQ",
                             icon_url="https://cdn.discordapp.com/attachments/702407723190452324/702782913137213450/JPEG_20200421_200632.jpg")
            embed.set_footer(text="Team EKA |",
                             icon_url="https://cdn.discordapp.com/attachments/702407723190452324/702782913137213450/JPEG_20200421_200632.jpg")
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

    # RECRUITMENT

    async def recruitment_log_maker(self, channel):
        # channel = self.bot.get_channel(703262862612758652)  #703104758814212197 703262862612758652
        ch = self.bot.get_channel(574920208590831657)  # interview_log_channel 574920208590831657
        messages = await channel.history().flatten()
        messages.reverse()
        # msg = await channel.fetch_message(703309098367844434)

        try:
            count = 1
            l = len(messages)
            for msg in messages:
                files = list()
                for attachment in msg.attachments:
                    files.append(await attachment.to_file())

                if len(msg.embeds) > 0:
                    one_time_embed = True
                    for e in msg.embeds:

                        e.set_author(name=msg.author.name, icon_url=msg.author.avatar_url)
                        e.set_footer(text=f"Message {count}  of {l} in channel {channel.name} ")
                        if one_time_embed:
                            one_time_embed = False
                            one_time_file_embed = True
                            if len(files) > 0:
                                for file in files:
                                    if one_time_file_embed:
                                        one_time_file_embed = False
                                        if e.description:
                                            e.add_field(name=f"{e.author.name}", value=f"{e.description}")
                                        e.description = msg.clean_content
                                        e.set_image(url=f"attachment://{file.filename}")
                                        await ch.send(embed=e, file=file)
                                    else:
                                        e.set_image(url=f"attachment://{file.filename}")
                                        await ch.send(embed=e, file=file)
                            else:
                                if one_time_file_embed:  # One Embed NO File
                                    one_time_file_embed = False
                                    if e.description:
                                        e.add_field(name=f"{e.author.name}", value=f"{e.description}")
                                    e.description = msg.clean_content
                                    await ch.send(embed=e)

                        else:
                            if len(files) > 0:
                                for file in files:
                                    e.set_image(url=f"attachment://{file.filename}")
                                    await ch.send(embed=e, file=file)
                            else:
                                await ch.send(content="No file content 2", embed=e)
                else:

                    if msg.embeds:
                        msg.embeds.description = msg.clean_content
                        msg.embeds.set_author(name=msg.author.name, icon_url=msg.author.avatar_url)
                        msg.embeds.set_footer(text=f"Message {count}  of {l} in channel {channel.name} ")

                        await ch.send(content="No file content 3", embed=msg.embeds)
                    else:
                        e = discord.Embed()

                        e.set_author(name=msg.author.name, icon_url=msg.author.avatar_url)
                        e.set_footer(text=f"Message {count}  of {l} in channel {channel.name} ")
                        if len(files) > 0:
                            one_time_file_embed = True
                            for file in files:
                                e.set_image(url=f"attachment://{file.filename}")
                                if one_time_file_embed:  # NO EMBED ONE FILE
                                    one_time_file_embed = False
                                    e.description = msg.clean_content
                                    await ch.send(embed=e, file=file)
                                else:  # NO EMBED MULTIPLE FILES
                                    await ch.send(embed=e, file=file)


                        else:  # NO EMBED NO FILE
                            e.description = msg.clean_content
                            await ch.send(embed=e)
                count += 1

        except Exception as Ex:
            await ch.send(f"ERROR -----> {msg.clean_content}, {msg.id},{msg.channel}")
            print(Ex)

    async def get_applicant_id(self, channel):
        messages = await channel.history().flatten()
        messages.reverse()
        return int(messages[0].content.split(":")[2].strip())

    async def recruitment_channel_creation(self, memberObj):
        GuildObj = self.bot.get_guild(561249245672374273)
        x = time.time()
        Categories = GuildObj.by_category()
        for category in Categories:
            CategoryInfo, Channels = category
            if CategoryInfo.id == 579704405666824222:  # Recruitment Category 562541400542019584
                permission = CategoryInfo.overwrites
                permission[memberObj] = discord.PermissionOverwrite(read_messages=True, manage_channels=False,
                                                                    add_reactions=False, read_message_history=True,
                                                                    create_instant_invite=False)
                recruitmentchannel = await CategoryInfo.create_text_channel(f'Applicant-{memberObj.name}',
                                                                            overwrites=permission)
                await recruitmentchannel.send(f"RECRUITMENT : {memberObj.name} : {memberObj.id}")
                embed = discord.Embed(colour=discord.Colour(0x673c27),
                                      description=f"Hello {memberObj.name}, Please Post the following information in this channel  \n\n:point_right:ss of your base and Profile. \n:point_right: Tell the Strategies You use.\n:point_right: Previous Clans.\n:point_right: Reason to Join EKA\n:point_right: Actual Name and Age\n:point_right: Place and Timezone\n:point_right: Other COC accounts\n:point_right: Opinion about our server and EKA \n\n Tag a Recruiter afterwards. ",
                                      timestamp=datetime.datetime.utcfromtimestamp(x))

                embed.set_author(name="Elite Kerala Alliance - RECRUITMENT ",
                                 url="https://link.clashofclans.com/?action=OpenClanProfile&tag=RJ9JYYQQ",
                                 icon_url="https://cdn.discordapp.com/attachments/702407723190452324/702782913137213450/JPEG_20200421_200632.jpg")
                embed.set_footer(text="Recruitment Team EKA |",
                                 icon_url="https://cdn.discordapp.com/attachments/702407723190452324/702782913137213450/JPEG_20200421_200632.jpg")
                message = await recruitmentchannel.send(content=f"{memberObj.mention}", embed=embed)
                await message.add_reaction("⛔")
                roleObj = discord.utils.get(GuildObj.roles, name="Applicant")
                await memberObj.add_roles(roleObj)

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
        if payload.channel_id == 702923115432378459:
            memberObj = self.bot.get_guild(payload.guild_id).get_member(payload.user_id)
            messageObj = await self.bot.get_channel(payload.channel_id).fetch_message(payload.message_id)
            if payload.message_id == 702924182823895171:
                await messageObj.remove_reaction(payload.emoji, memberObj)
                applicant_set = False
                for role in memberObj.roles:
                    if role.name == 'Applicant':
                        applicant_set = True
                if applicant_set:
                    embed = discord.Embed(title=f"{memberObj.mention}You have already opened one Application",
                                          description=" Swipe from left and check channels, We have already opened an application for you",
                                          color=0x98FB98)
                    embed.set_thumbnail(
                        url="https://cdn.discordapp.com/attachments/702407723190452324/702782913137213450/JPEG_20200421_200632.jpg")
                    try:
                        await applicantObj.send(embed=embed)
                    except:
                        await self.bot.get_channel(565202300163850240).send(embed=embed)
                else:
                    await self.recruitment_channel_creation(memberObj)

        if self.bot.get_channel(payload.channel_id).category_id == 579704405666824222:
            memberObj = self.bot.get_guild(payload.guild_id).get_member(payload.user_id)
            messageObj = await self.bot.get_channel(payload.channel_id).fetch_message(payload.message_id)
            if str(payload.emoji) == str("⛔"):
                if (discord.utils.get(memberObj.roles, name='R e c r U ι т e r')):
                    await messageObj.add_reaction("✅")
                    await messageObj.add_reaction("❎")
                    await messageObj.remove_reaction(payload.emoji, memberObj)
                else:
                    if memberObj.bot == False:
                        await self.bot.get_channel(payload.channel_id).send(
                            f"{memberObj.mention} Sorry, only a EKA recruiter is authorized to close application.")
                        await messageObj.remove_reaction(payload.emoji, memberObj)

            elif str(payload.emoji) == str("✅"):
                if (discord.utils.get(memberObj.roles, name='R e c r U ι т e r')):
                    permission = self.bot.get_channel(payload.channel_id).overwrites
                    for k, v in permission.items():
                        if k == self.bot.get_guild(payload.guild_id).default_role:
                            continue
                        permission[k] = discord.PermissionOverwrite(read_messages=True, manage_channels=False,
                                                                    add_reactions=False, read_message_history=True,
                                                                    create_instant_invite=False, send_messages=False)

                    await self.bot.get_channel(payload.channel_id).edit(overwrites=permission)
                    await messageObj.clear_reactions()
                    embed = discord.Embed(colour=discord.Colour(0x673c27),
                                          description=f"Hello {memberObj.name}, Please update the interview status   \n\n:one: Accepted for Tryout. \n:two: Rejected.\n\n ")
                    embed.set_author(name="EKA - RECRUITMENT STATUS",
                                     icon_url="https://cdn.discordapp.com/attachments/702407723190452324/702782913137213450/JPEG_20200421_200632.jpg")
                    message = await self.bot.get_channel(payload.channel_id).send(
                        content=f"{memberObj.mention} has closed this application", embed=embed)
                    await message.add_reaction("1\N{variation selector-16}\N{combining enclosing keycap}")
                    await message.add_reaction("2\N{variation selector-16}\N{combining enclosing keycap}")

                    # roleObj = discord.utils.get(GuildObj.roles, name = "Applicant")
                    # await memberObj.add_roles(roleObj)

                else:
                    if memberObj.bot == False:
                        await self.bot.get_channel(payload.channel_id).send(
                            f"{memberObj.mention} Sorry, only a EKA recruiter is authorized to close application.")
                        await messageObj.remove_reaction(payload.emoji, memberObj)

            elif str(payload.emoji) == str("❎"):
                if (discord.utils.get(memberObj.roles, name='R e c r U ι т e r')):
                    await messageObj.clear_reaction("❎")
                    await messageObj.clear_reaction("✅")
                else:
                    if memberObj.bot == False:
                        await self.bot.get_channel(payload.channel_id).send(
                            f"{memberObj.mention} Sorry, only a EKA recruiter is authorized to close application.")
                        await messageObj.remove_reaction(payload.emoji, memberObj)

            elif str(payload.emoji) == str("1\N{variation selector-16}\N{combining enclosing keycap}"):
                if (discord.utils.get(memberObj.roles, name='R e c r U ι т e r')):
                    await messageObj.clear_reaction("1\N{variation selector-16}\N{combining enclosing keycap}")
                    await messageObj.clear_reaction("2\N{variation selector-16}\N{combining enclosing keycap}")
                    applicant_id = await self.get_applicant_id(self.bot.get_channel(payload.channel_id))
                    applicantObj = self.bot.get_guild(payload.guild_id).get_member(applicant_id)
                    GuildObj = self.bot.get_guild(561249245672374273)
                    applicantRoleObj = discord.utils.get(GuildObj.roles, name="Applicant")
                    ekajoinRoleObj = discord.utils.get(GuildObj.roles, name="eka_join")
                    guestRoleObj = discord.utils.get(GuildObj.roles, name="g u e ѕ т")
                    fieldMarshalRoleObj = discord.utils.get(GuildObj.roles, name="f ι e l d  м a r ѕ н a l")
                    try:
                        await applicantObj.remove_roles(applicantRoleObj)
                        await applicantObj.remove_roles(ekajoinRoleObj)
                        await applicantObj.remove_roles(guestRoleObj)
                    except:
                        pass
                    await applicantObj.add_roles(fieldMarshalRoleObj)
                    await self.recruitment_log_maker(self.bot.get_channel(payload.channel_id))
                    await self.bot.get_channel(payload.channel_id).delete()
                    await self.bot.get_channel(569086204621094912).send(
                        f"@everyone A new Recruit has been joined EKA, Please wish {applicantObj.mention} Goodluck !")
                    embed = discord.Embed(title=f"Congrats ! You are recruited",
                                          description=" You are selected for Tryouts in EKA. Goodluck", color=0x98FB98)
                    embed.set_thumbnail(
                        url="https://cdn.discordapp.com/attachments/702407723190452324/702782913137213450/JPEG_20200421_200632.jpg")

                    try:
                        await applicantObj.send(embed=embed)
                    except:
                        pass

                else:
                    if memberObj.bot == False:
                        await messageObj.remove_reaction(payload.emoji, memberObj)

            elif str(payload.emoji) == str("2\N{variation selector-16}\N{combining enclosing keycap}"):
                if (discord.utils.get(memberObj.roles, name='R e c r U ι т e r')):
                    await messageObj.clear_reaction("1\N{variation selector-16}\N{combining enclosing keycap}")
                    await messageObj.clear_reaction("2\N{variation selector-16}\N{combining enclosing keycap}")
                    applicant_id = await self.get_applicant_id(self.bot.get_channel(payload.channel_id))
                    applicantObj = self.bot.get_guild(payload.guild_id).get_member(applicant_id)
                    GuildObj = self.bot.get_guild(561249245672374273)
                    applicantRoleObj = discord.utils.get(GuildObj.roles, name="Applicant")

                    try:
                        await applicantObj.remove_roles(applicantRoleObj)
                    except:
                        pass
                    await self.recruitment_log_maker(self.bot.get_channel(payload.channel_id))
                    await self.bot.get_channel(payload.channel_id).delete()

                    embed = discord.Embed(title=f"Sorry ! Your Application to join EKA has been rejected",
                                          description=" Stay in touch with us in the global chat, You can try again after a while ",
                                          color=0x98FB98)
                    embed.set_thumbnail(
                        url="https://cdn.discordapp.com/attachments/702407723190452324/702782913137213450/JPEG_20200421_200632.jpg")

                    try:
                        await applicantObj.send(embed=embed)
                    except Exception as Ex:
                        await self.bot.get_channel(586932176403169281).send(f"{Ex}")

                else:
                    if memberObj.bot == False:
                        await messageObj.remove_reaction(payload.emoji, memberObj)

            else:
                if memberObj.bot == False:
                    await messageObj.remove_reaction(payload.emoji, memberObj)

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
