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
import logging
from typing import Union
# to expose to the eval command
import datetime
import time
from collections import Counter
from application.constants.guildsupport import *
from application.constants.guild1947 import *
from application.constants.emoji import *
from application.constants.config import *
from application.models.member_model import MemberModel 
from application.utlis.discordGuild import Guild
from application.constants.config import DiscordConfig
from application.cogs.utils.paginator import TextPages
from application.utlis.birthday import Birthday
from application.utlis.on_loop import LoopTaks

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
    @commands.command()
    @commands.is_owner()
    async def delete_member(self, ctx, id: int):
        """Delete a member by ID"""
        if self.bot.db_utlis.delete_from_member_table(int(id)):
            await ctx.message.add_reaction(Emoji.GREEN_TICK)
        else:
            await ctx.message.add_reaction(Emoji.GREEN_CROSS)
    @commands.Cog.listener()
    async def on_member_join(self,member):
        x=time.time()
        if member.guild.id == Guild1947.SERVER_ID: #1947 Server
            welcomechannel = self.bot.get_channel(Guild1947.WELCOME_CHANNEL_ID)
            apply_eka = self.bot.get_channel(Guild1947.APPLY_EKA_CHANNEL_ID)
            about =self.bot.get_channel(Guild1947.ABOUT_CHANNEL_ID)
            directory=os.getcwd()
            file = discord.File(os.path.join(directory+Guild1947Image.RECRUITMENT_IMAGE_LOC),filename=Guild1947Image.RECRUITMENT_IMAGE_NAME)
            embed = discord.Embed(title="**__WELCOME TO EKA__**", colour=discord.Colour(0x673c27), url=Guild1947Clan.CLAN_URL_1947, description=f"Hello {member.name},  \n\n:point_right:Elite Kerala Alliance. \n:point_right: CWL \n:point_right: MLCW \n:point_right: NDL \n\n  ", timestamp=datetime.datetime.utcfromtimestamp(x))
            embed.set_thumbnail(url=str(member.avatar_url))
            embed.set_author(name="Elite Kerala Alliance ", url=Guild1947Clan.CLAN_URL_1947, icon_url=Guild1947Image.EKA_ICON_URL)
            embed.set_footer(text="Team EKA |", icon_url=Guild1947Clan.CLAN_URL_1947)
            embed.add_field(name=f"Want to join With Us ?", value=f"React with :envelope_with_arrow: in {apply_eka.mention} \n\n\n\n")
            embed.add_field(name=f"Want to get GUEST role ?", value=f":sos: React with EKA logo in {about.mention} \n\n")
            #embed.set_image(url="attachment://recruitment.jpg")
            await welcomechannel.send(content=f"{member.mention}",file=file,embed = embed)
            if not self.bot.db_utlis.insert_into_member_table(member.id,member.joined_at):
                logging,error("Cannot Insert Member on join")
            try:
                await member.send(content=f"{member.mention}",file=file, embed =embed)
            except:
                pass
        if member.guild.id == GuildSupport.SERVER_ID: #Support Server
            welcomechannel = self.bot.get_channel(GuildSupport.WELCOME_CHANNEL_ID)
            embed = discord.Embed(title="**__WELCOME TO EKA BOT Support__**", colour=discord.Colour(0x673c27), description=f"Hello {member.mention} | {member.name}  You are {member.guild.member_count} th Member \n Greetings from EKA BOT Developers  ", timestamp=datetime.datetime.utcfromtimestamp(x))
            await welcomechannel.send(embed = embed)
    @commands.Cog.listener()
    async def on_member_remove(self,member):
        if member.guild.id == Guild1947.SERVER_ID:
            welcomechannel = self.bot.get_channel(Guild1947.DISCORD_ACTIVITY_LOG_CHANNEL_ID)
            embed = discord.Embed(title = "You Lost a member",
            description = f"{member} left {member.guild.name} server!",
            color = 0x07999b
            )
            await welcomechannel.send(embed = embed)
            # if not self.bot.db_utlis.delete_from_member_table(member.id):
            #     logging,error("Cannot Delete Member on join")

        if member.guild.id == GuildSupport.SERVER_ID:
            welcomechannel = self.bot.get_channel(GuildSupport.WELCOME_CHANNEL_ID)
            embed = discord.Embed(title = "You Lost a member",
            description = f"{member} left {member.guild.name} server!",
            color = 0x07999b
            )
            await welcomechannel.send(embed = embed)
    
    @commands.command(aliases=['sixpack','6pack'])
    @commands.has_any_role(RolesGuildSupport.ADMIN_ROLE_NAME, RolesGuild1947.ADMIN_ROLE_NAME) 
    #@commands.is_owner()
    async def six_pack(self, ctx, user:discord.User):
        """eka 6pack @mention <Optional Msg>"""
        msg= await self.bot.get_channel(id=Guild1947.WARRIOR_UPDATE_CHANNEL_ID).send(f" Congratulate {user.mention} for Six Pack Performance")
        await msg.add_reaction(Emoji.CELEBRATION_BEER)
        await ctx.message.add_reaction(Emoji.GREEN_TICK)
        try:
            await user.send(f" Dear EKA Warrior {user.name} ,Team EKA is very proud of your performance. Keep it up")
        except:
            pass

    @commands.command(aliases=['newwar'])
    @commands.has_any_role(RolesGuildSupport.ADMIN_ROLE_NAME, RolesGuild1947.ADMIN_ROLE_NAME)
    # @commands.is_owner()
    async def new_war(self, ctx ):
        """eka new_war <Optional Clan Name>"""
        GuildObj = self.bot.get_guild(Guild1947.SERVER_ID)
        Categories = GuildObj.by_category()
        for category in Categories:
            CategoryInfo, Channels = category
            if CategoryInfo.id == Guild1947.ENEMY_BASE_CATEGORY_ID: # Enemy base category
                for channels in Channels:
                    if channels.id == Guild1947.HOW_TO_PLAN_ATTACK_CHANNEL_ID:
                        continue
                    msg = await self.bot.get_channel(id=channels.id).send(Guild1947Image.NEW_WAR_IMAGE_URL)
        await ctx.message.add_reaction(Emoji.GREEN_TICK)

    # RECRUITMENT
    
    async def recruitment_log_maker(self,channel,emoji):
        ch = self.bot.get_channel(Guild1947.INTERVIEW_LOG_CHANNEL) 
        messages = await channel.history().flatten()
        messages.reverse()
        #msg = await channel.fetch_message()
        
        try:
            count =1
            l = len(messages)
            for msg in messages:
                files = list()
                for attachment in msg.attachments:
                    files.append(await attachment.to_file())
                
                if len(msg.embeds)>0:
                    one_time_embed = True
                    for e in msg.embeds:
                        
                        e.set_author(name=msg.author.name,icon_url=msg.author.avatar_url)
                        e.set_footer(text=f"Message {count}  of {l} in channel {channel.name} ")
                        if one_time_embed:
                            one_time_embed = False
                            one_time_file_embed = True
                            if len(files)>0:
                                for file in files:
                                    if one_time_file_embed:
                                        one_time_file_embed = False
                                        if e.description:
                                            e.add_field(name=f"{e.author.name}", value=f"{e.description}")
                                        e.description=msg.clean_content
                                        e.set_image(url=f"attachment://{file.filename}")
                                        last_message = await ch.send(embed=e,file=file )
                                    else:
                                        e.set_image(url=f"attachment://{file.filename}")
                                        last_message = await ch.send(embed=e,file=file)
                            else:
                                if one_time_file_embed:  # One Embed NO File
                                    one_time_file_embed = False
                                    if e.description:
                                        e.add_field(name=f"{e.author.name}", value=f"{e.description}")
                                    e.description=msg.clean_content
                                    last_message = await ch.send(embed=e)
                                
                        else:
                            if len(files)>0:
                                for file in files:
                                    e.set_image(url=f"attachment://{file.filename}")
                                    last_message = await ch.send(embed=e,file=file)
                            else:
                                last_message = await ch.send(content="No file content 2",embed=e)
                else:
                    
                    if msg.embeds:
                        msg.embeds.description=msg.clean_content
                        msg.embeds.set_author(name=msg.author.name,icon_url=msg.author.avatar_url)
                        msg.embeds.set_footer(text=f"Message {count}  of {l} in channel {channel.name} ")

                        last_message = await ch.send(content="No file content 3",embed=msg.embeds)
                    else:  
                        e = discord.Embed()
                        
                        e.set_author(name=msg.author.name,icon_url=msg.author.avatar_url)
                        e.set_footer(text=f"Message {count}  of {l} in channel {channel.name} ")
                        if len(files)>0:
                            one_time_file_embed = True
                            for file in files:
                                e.set_image(url=f"attachment://{file.filename}")
                                if one_time_file_embed: # NO EMBED ONE FILE
                                    one_time_file_embed = False
                                    e.description=msg.clean_content
                                    last_message = await ch.send(embed=e, file=file)
                                else:    # NO EMBED MULTIPLE FILES
                                    last_message = await ch.send(embed=e,file=file)   


                        else: # NO EMBED NO FILE
                            e.description=msg.clean_content
                            last_message = await ch.send(embed=e)
                count +=1
            await last_message.add_reaction(emoji)                
        except Exception as Ex:
            await ch.send(f"ERROR -----> {msg.clean_content}, {msg.id},{msg.channel}")
            print(Ex)

    async def get_applicant_id(self,channel):
        messages = await channel.history().flatten()
        messages.reverse()
        return int(messages[0].content.split(":")[2].strip())

    async def recruitment_channel_creation(self,memberObj):
        GuildObj = self.bot.get_guild(Guild1947.SERVER_ID)
        x=time.time()
        Categories = GuildObj.by_category()
        for category in Categories:
            CategoryInfo, Channels = category
            if CategoryInfo.id == Guild1947.RECRUITMENT_CATEGORY_ID: #Recruitment Category 
                permission=CategoryInfo.overwrites
                permission[memberObj]=discord.PermissionOverwrite(read_messages=True,manage_channels=False,add_reactions=False,read_message_history=True,create_instant_invite=False)
                recruitmentchannel = await CategoryInfo.create_text_channel(f'Applicant-{memberObj.name}', overwrites=permission)
                await recruitmentchannel.send(f"RECRUITMENT : {memberObj.name} : {memberObj.id}")
                embed = discord.Embed(colour=discord.Colour(0x673c27),description=f"Hello {memberObj.name}, Please Post the following information in this channel  \n\n{Emoji.NUMBER_ONE} ss of your base and Profile. \n{Emoji.NUMBER_TWO}  Tell the Strategies You use.\n{Emoji.NUMBER_THREE}  Previous Clans.\n{Emoji.NUMBER_FOUR} Reason to Join EKA\n{Emoji.NUMBER_FIVE} Actual Name and Age\n{Emoji.NUMBER_SIX} Place and Timezone\n{Emoji.NUMBER_SEVEN} COC Player Tag of All of your accounts \n{Emoji.NUMBER_EIGHT} Leage Experience (Specify Leagues and represented Clan Name you had participated) \n\n {Emoji.SOS} Tag a Recruiter afterwards. ", timestamp=datetime.datetime.utcfromtimestamp(x))
                
                embed.set_author(name="Elite Kerala Alliance - RECRUITMENT ", url=Guild1947Clan.CLAN_URL_1947, icon_url=Guild1947Image.EKA_ICON_URL)
                embed.set_footer(text="Recruitment Team EKA |", icon_url=Guild1947Image.EKA_ICON_URL)
                message = await recruitmentchannel.send(content=f"{memberObj.mention}",embed = embed)
                await message.add_reaction(Emoji.NO_ENTRY)
                roleObj = discord.utils.get(GuildObj.roles, name = RolesGuild1947.APPLICANT_ROLE_NAME)
                await memberObj.add_roles(roleObj)
        
    @commands.command(aliases=['misshit','hitmissed'])
    @commands.has_any_role(RolesGuildSupport.ADMIN_ROLE_NAME, RolesGuild1947.ADMIN_ROLE_NAME) 
    #@commands.is_owner()
    async def miss_hit(self, ctx, user:discord.User):
        """eka misshit @mention <Optional Msg>"""
        msg= await self.bot.get_channel(id=Guild1947.WARRIOR_UPDATE_CHANNEL_ID).send(f" {user.mention} has been warned for missing hit  in the WAR :sos: ")
        await msg.add_reaction(Emoji.WARNING)
        await ctx.message.add_reaction(Emoji.GREEN_TICK)
        try:
            await user.send(f" Dear EKA Warrior {user.name} , You ought to use both attacks in war. Discuss with team the reason ASAP")
        except:
            pass
    @commands.command(aliases=['test','t'])
    @commands.is_owner()
    async def test_command(self, ctx):
        """Test"""
        try:
            tasks = LoopTaks(self.bot,self.bot.db_utlis)
            tasks.run()
            await ctx.message.add_reaction(Emoji.GREEN_TICK)
            time = datetime.utcnow()
            await self.bot.get_channel(id=Guild1947.EKA_BOT_CHANNEL_ID).send(f"Time :{time}")
        except:
            await ctx.message.add_reaction(Emoji.GREEN_CROSS)
        #await self.bot.get_channel(GuildSupport.BOT_COMMANDS_CHANNEL_ID).send(f"---->{r} {type(r)}")
    
    @commands.command(aliases=['latehit','lateattack'])
    @commands.has_any_role(RolesGuildSupport.ADMIN_ROLE_NAME, RolesGuild1947.ADMIN_ROLE_NAME) 
    #@commands.is_owner()
    async def late_hit(self, ctx, user:discord.User):
        """eka latehit @mention <Optional Msg>"""
        msg= await self.bot.get_channel(id=Guild1947.WARRIOR_UPDATE_CHANNEL_ID).send(f" {user.mention} has been warned for Late hit  in the WAR :sos: ")
        await msg.add_reaction(Emoji.WARNING)
        await ctx.message.add_reaction(Emoji.GREEN_TICK)
        try:
            await user.send(f" Dear EKA Warrior {user.name} , You ought to plan and attack in time. Discuss with team the reason ASAP")
        except:
            pass
    
    @commands.command()
    @commands.has_any_role(RolesGuildSupport.ADMIN_ROLE_NAME, RolesGuild1947.ADMIN_ROLE_NAME) 
    #@commands.is_owner()
    async def vote(self, ctx, user:discord.User , message:str = None ):
        """eka vote @mention <Optional Msg>"""
        chId= self.bot.get_channel(id=Guild1947.VOTING_FOR_RECRUIT_CHANNEL_ID)
        if message:
            msg= await self.bot.get_channel(id=Guild1947.VOTING_FOR_RECRUIT_CHANNEL_ID).send(f"  Please vote for {user.name} according to war performance against {message} :thumbsup: Good :thumbsdown: Bad")
        else:
            msg= await self.bot.get_channel(id=Guild1947.VOTING_FOR_RECRUIT_CHANNEL_ID).send(f"  Please vote for {user.name} according to war performance :thumbsup: Good :thumbsdown: Bad")
            
        await msg.add_reaction(Emoji.THUMPS_UP)
        await msg.add_reaction(Emoji.THUMPS_DOWN)
        await msg.add_reaction(Emoji.NO_ENTRY)
        await self.bot.get_channel(id=Guild1947.ADMIN_TALK_CHANNEL_ID).send(f"@everyone Voting for evaluvating war performance of {user.name} has started. Cast your votes {chId.mention}")
        await ctx.message.add_reaction(Emoji.GREEN_TICK)

    @commands.Cog.listener()
    async def on_raw_reaction_add(self,payload):
        if payload.channel_id == Guild1947.VOTING_FOR_RECRUIT_CHANNEL_ID:
            
            memberObj=self.bot.get_guild(payload.guild_id).get_member(payload.user_id)
            messageObj=await self.bot.get_channel(payload.channel_id).fetch_message(payload.message_id)
            if (discord.utils.get(memberObj.roles, name=RolesGuild1947.TRYOUTS_ROLE_NAME)):
                try:
                    u=self.bot.get_user(payload.user_id)
                    await u.send("You can't cast vote sorry.Sorry, You need to have higher roles in our server to cast vote.")
                    await messageObj.remove_reaction(payload.emoji,memberObj)
                except:
                    await self.bot.get_channel(id=Guild1947.LONGUE_CHANNEL_ID).send(f"{memberObj.mention} DM is disabled. Sorry, You need to have higher roles to cast the vote")
                    await messageObj.remove_reaction(payload.emoji,memberObj)
            else:
                likeCount=dislikeCount=0
                try:
                    likeReactionObj=messageObj.reactions[0]
                    dislikeReactionObj=messageObj.reactions[1]
                    noentryReactionObj=messageObj.reactions[2]
                    tickReactionObj=messageObj.reactions[3]
                except:
                    pass
                try:
                    if str(noentryReactionObj.emoji)== str(payload.emoji):
                        if discord.utils.get(memberObj.roles, name=RolesGuild1947.ADMIN_ROLE_NAME):
                            await messageObj.add_reaction(Emoji.GREEN_TICK)
                        else:
                            if not memberObj.bot:
                                await messageObj.remove_reaction(payload.emoji,memberObj)
                except UnboundLocalError:
                    pass

                try:
                    if str(tickReactionObj.emoji)== str(payload.emoji):
                        if discord.utils.get(memberObj.roles, name=RolesGuild1947.ADMIN_ROLE_NAME):
                            FmessageObj=await self.bot.get_channel(payload.channel_id).fetch_message(payload.message_id)
                            await self.bot.get_channel(id=Guild1947.VOTING_FOR_RECRUIT_CHANNEL_ID).send(f" {list(str(FmessageObj.content).split())[3]} Performance Evaluation  Result **Like** {likeReactionObj.count-1} **Dislike** {dislikeReactionObj.count-1} Poll has been ended by {memberObj.name}")
                            await messageObj.delete()
                        else:
                            if not memberObj.bot:
                                await messageObj.remove_reaction(payload.emoji,memberObj)
                except UnboundLocalError:
                    pass   
                try:
                    if not memberObj.bot:
                        if (str(payload.emoji)==str(dislikeReactionObj.emoji)) or (str(payload.emoji)==str(likeReactionObj.emoji)):
                            async for user in likeReactionObj.users():
                                if user.id == payload.user_id:
                                    likeCount=1
                            async for user in dislikeReactionObj.users():
                                if user.id == payload.user_id:
                                    dislikeCount=1
                except UnboundLocalError:
                    pass
                
                if likeCount+dislikeCount>1:
                    if str(likeReactionObj.emoji) == str(payload.emoji):
                        await messageObj.remove_reaction(payload.emoji,memberObj)
                    if str(dislikeReactionObj.emoji) == str(payload.emoji):
                        await messageObj.remove_reaction(payload.emoji,memberObj)
            
        if payload.channel_id == Guild1947.SERVER_UPDATES_CHANNEL_ID:    
            memberObj=self.bot.get_guild(payload.guild_id).get_member(payload.user_id)
            if payload.message_id == Guild1947.ADULT_PAGE_REACTION_MESSAGE_ID:
                messageObj=await self.bot.get_channel(payload.channel_id).fetch_message(payload.message_id)
                if str(payload.emoji) == str(Emoji.UNDER_AGE):
                    GuildObj = self.bot.get_guild(Guild1947.SERVER_ID)
                    roleObj = discord.utils.get(GuildObj.roles, name = RolesGuild1947.ADULT_ROLE_NAME)
                    await memberObj.add_roles(roleObj)
                    await self.bot.get_channel(id=Guild1947.ADULT_CONTENT_CHANNEL_ID).send(f"{memberObj.mention} Reacted to get `18+` Role ")
        if payload.channel_id == Guild1947.APPLY_EKA_CHANNEL_ID:
            
            memberObj=self.bot.get_guild(payload.guild_id).get_member(payload.user_id)
            messageObj=await self.bot.get_channel(payload.channel_id).fetch_message(payload.message_id)
            if payload.message_id == Guild1947.APPLY_EKA_MESSAGE_ID:
                await messageObj.remove_reaction(payload.emoji,memberObj)
                applicant_set = False
                for role in memberObj.roles:
                    if role.name == RolesGuild1947.APPLICANT_ROLE_NAME:
                        applicant_set = True 
                if applicant_set:
                    embed = discord.Embed(title = f"{memberObj.name}, You have already opened one Application",description = " Swipe from left and check channels, We have already opened an application for you",color = 0x98FB98)
                    embed.set_thumbnail(url=Guild1947Image.EKA_ICON_URL)
                    try:
                        await memberObj.send(embed=embed)
                    except:
                        await self.bot.get_channel(Guild1947.GLOBAL_CHAT_CHANNEL_ID).send(content=f"{memberObj.mention}",embed=embed)
                else:
                    await self.recruitment_channel_creation(memberObj)

        if self.bot.get_channel(payload.channel_id).category_id ==Guild1947.EKA_RECRUITMENT_CATEGORY_ID:
            memberObj=self.bot.get_guild(payload.guild_id).get_member(payload.user_id)
            messageObj=await self.bot.get_channel(payload.channel_id).fetch_message(payload.message_id)
            if str(payload.emoji) == str(Emoji.NO_ENTRY):
                if (discord.utils.get(memberObj.roles, name=RolesGuild1947.RECRUITER_ROLE_NAME)):
                    await messageObj.add_reaction(Emoji.GREEN_TICK)
                    await messageObj.add_reaction(Emoji.GREEN_CROSS)
                    await messageObj.remove_reaction(payload.emoji,memberObj)
                else:
                    if memberObj.bot == False:
                        await self.bot.get_channel(payload.channel_id).send(f"{memberObj.mention} Sorry, only a EKA recruiter is authorized to close application.")
                        await messageObj.remove_reaction(payload.emoji,memberObj)

            elif str(payload.emoji) == str(Emoji.GREEN_TICK):
                if (discord.utils.get(memberObj.roles, name=RolesGuild1947.RECRUITER_ROLE_NAME)):
                    permission = self.bot.get_channel(payload.channel_id).overwrites
                    for k,v in permission.items():
                        if k == self.bot.get_guild(payload.guild_id).default_role:
                            continue
                        permission[k]=discord.PermissionOverwrite(read_messages=True,manage_channels=False,add_reactions=False,read_message_history=True,create_instant_invite=False,send_messages=False)
                    
                    await self.bot.get_channel(payload.channel_id).edit(overwrites=permission)
                    await messageObj.clear_reactions()
                    embed = discord.Embed(colour=discord.Colour(0x673c27),description=f"Hello {memberObj.name}, Please update the interview status   \n\n:one: Accepted for Tryout. \n:two: Rejected.\n\n ")
                    embed.set_author(name="EKA - RECRUITMENT STATUS",icon_url=Guild1947Image.EKA_ICON_URL)
                    message= await self.bot.get_channel(payload.channel_id).send(content=f"{memberObj.mention} has closed this application",embed=embed)
                    await message.add_reaction(Emoji.NUMBER_ONE)
                    await message.add_reaction(Emoji.NUMBER_TWO)

                else:
                    if memberObj.bot == False:
                        await self.bot.get_channel(payload.channel_id).send(f"{memberObj.mention} Sorry, only a EKA recruiter is authorized to close application.")
                        await messageObj.remove_reaction(payload.emoji,memberObj)

            elif str(payload.emoji) == str(Emoji.GREEN_CROSS):
                if (discord.utils.get(memberObj.roles, name=RolesGuild1947.RECRUITER_ROLE_NAME)):
                    await messageObj.clear_reaction(Emoji.GREEN_CROSS)
                    await messageObj.clear_reaction(Emoji.GREEN_TICK)
                else:
                    if memberObj.bot==False:
                        await self.bot.get_channel(payload.channel_id).send(f"{memberObj.mention} Sorry, only a EKA recruiter is authorized to close application.")
                        await messageObj.remove_reaction(payload.emoji,memberObj)

            elif str(payload.emoji) == str(Emoji.NUMBER_ONE):
                if (discord.utils.get(memberObj.roles, name=RolesGuild1947.RECRUITER_ROLE_NAME)):
                    await messageObj.clear_reaction(Emoji.NUMBER_ONE)
                    await messageObj.clear_reaction(Emoji.NUMBER_TWO)
                    applicant_id= await self.get_applicant_id(self.bot.get_channel(payload.channel_id))
                    applicantObj = self.bot.get_guild(payload.guild_id).get_member(applicant_id)
                    GuildObj = self.bot.get_guild(Guild1947.SERVER_ID)
                    applicantRoleObj = discord.utils.get(GuildObj.roles, name = RolesGuild1947.APPLICANT_ROLE_NAME)
                    ekajoinRoleObj = discord.utils.get(GuildObj.roles, name = RolesGuild1947.NEW_SERVER_JOIN_ROLE_NAME)
                    guestRoleObj = discord.utils.get(GuildObj.roles, name = RolesGuild1947.GUEST_ROLE_NAME)
                    fieldMarshalRoleObj = discord.utils.get(GuildObj.roles, name = RolesGuild1947.TRYOUTS_ROLE_NAME)
                    try:
                        await applicantObj.remove_roles(applicantRoleObj)
                        await applicantObj.remove_roles(ekajoinRoleObj)
                        await applicantObj.remove_roles(guestRoleObj)
                    except:
                        pass
                    await applicantObj.add_roles(fieldMarshalRoleObj) 
                    await self.recruitment_log_maker(self.bot.get_channel(payload.channel_id),Emoji.NUMBER_ONE)
                    await self.bot.get_channel(payload.channel_id).delete()    
                    await self.bot.get_channel(Guild1947.ANNOUNCEMENT_CHANNEL_ID).send(f"@here, A new Recruit has been joined EKA, Please wish {applicantObj.mention} Goodluck !")
                    await self.bot.get_channel(Guild1947.POST_TO_TWITTER_CHANNEL_ID).send(f"Everyone, A new Recruit has been joined EKA, Please wish {applicantObj.display_name} Goodluck !")
                    embed = discord.Embed(title = f"Congrats ! You are recruited",description = " You are selected for Tryouts in EKA. Goodluck",color = 0x98FB98)
                    embed.set_thumbnail(url=Guild1947Image.EKA_ICON_URL)
        
                    try:
                        await applicantObj.send(embed=embed)
                    except:
                        pass
                
                else:
                    if memberObj.bot==False:
                        await messageObj.remove_reaction(payload.emoji,memberObj)

            elif str(payload.emoji) == str(Emoji.NUMBER_TWO):
                if (discord.utils.get(memberObj.roles, name=RolesGuild1947.RECRUITER_ROLE_NAME)):
                    await messageObj.clear_reaction(Emoji.NUMBER_ONE)
                    await messageObj.clear_reaction(Emoji.NUMBER_TWO)
                    applicant_id= await self.get_applicant_id(self.bot.get_channel(payload.channel_id))
                    applicantObj = self.bot.get_guild(payload.guild_id).get_member(applicant_id)
                    GuildObj = self.bot.get_guild(Guild1947.SERVER_ID)
                    applicantRoleObj = discord.utils.get(GuildObj.roles, name = RolesGuild1947.APPLICANT_ROLE_NAME)
                    
                    try:
                        await applicantObj.remove_roles(applicantRoleObj)
                    except:
                        pass
                    await self.recruitment_log_maker(self.bot.get_channel(payload.channel_id),Emoji.NUMBER_TWO)
                    await self.bot.get_channel(payload.channel_id).delete()    
                    
                    embed = discord.Embed(title = f"Sorry ! Your Application to join EKA has been rejected",description = " Stay in touch with us in the global chat, You can try again after a while ",color = 0x98FB98)
                    embed.set_thumbnail(url=Guild1947Image.EKA_ICON_URL)
        
                    try:
                        await applicantObj.send(embed=embed)
                    except Exception as Ex:
                        await self.bot.get_channel(Guild1947.BOT_TESTING_CHANNEL_ID).send(f"{Ex}")
                
                else:
                    if memberObj.bot==False:
                        await messageObj.remove_reaction(payload.emoji,memberObj)

            else:
                if memberObj.bot==False:
                    await messageObj.remove_reaction(payload.emoji,memberObj)
        if payload.channel_id == Guild1947.OPT_INT_OUT_CHANNEL_ID:
            
            memberObj=self.bot.get_guild(payload.guild_id).get_member(payload.user_id)
            messageObj=await self.bot.get_channel(payload.channel_id).fetch_message(payload.message_id)
            permission_error_msg = f"{memberObj.mention}Sorry, Only `{RolesGuild1947.ROSTER_COLONAL_ROLE_NAME}` can close the roster opt-in-out"
            if str(payload.emoji) not in [str(Emoji.TH11),str(Emoji.TH12),str(Emoji.TH13),str(Emoji.NO_ENTRY),str(Emoji.GREEN_TICK),str(Emoji.GREEN_CROSS),str(Emoji.X)]:
                await messageObj.remove_reaction(payload.emoji,memberObj)
            else:
                if str(payload.emoji) == str(Emoji.NO_ENTRY):
                    if (discord.utils.get(memberObj.roles, name=RolesGuild1947.ROSTER_COLONAL_ROLE_NAME)):
                        await messageObj.add_reaction(Emoji.GREEN_TICK)
                        await messageObj.add_reaction(Emoji.GREEN_CROSS)
                        await messageObj.remove_reaction(payload.emoji,memberObj)
                    else:
                        if memberObj.bot == False:
                            try:
                                await memberObj.send(permission_error_msg)
                                await messageObj.remove_reaction(payload.emoji,memberObj)
                            except:
                                await self.bot.get_channel(Guild1947.LONGUE_CHANNEL_ID).send(permission_error_msg)
                                await messageObj.remove_reaction(payload.emoji,memberObj)
                elif str(payload.emoji) == str(Emoji.GREEN_CROSS):
                    if (discord.utils.get(memberObj.roles, name=RolesGuild1947.ROSTER_COLONAL_ROLE_NAME)):
                        await messageObj.clear_reaction(Emoji.GREEN_CROSS)
                        await messageObj.clear_reaction(Emoji.GREEN_TICK)
                    else:
                        if memberObj.bot == False:
                            await self.bot.get_channel(Guild1947.LONGUE_CHANNEL_ID).send(permission_error_msg)
                            await messageObj.remove_reaction(payload.emoji,memberObj)
                elif str(payload.emoji) == str(Emoji.GREEN_TICK):
                    if (discord.utils.get(memberObj.roles, name=RolesGuild1947.ROSTER_COLONAL_ROLE_NAME)):
                        if memberObj.bot == False:
                            await messageObj.clear_reaction(payload.emoji)
                            await messageObj.clear_reaction(Emoji.NO_ENTRY)
                            await messageObj.clear_reaction(Emoji.GREEN_CROSS)
                            try:
                                nl ="\n"
                                msg_content= messageObj.content.replace("@everyone","")
                                text = f"{msg_content}{nl} -Closed by {memberObj.name}{nl}**__ROSTER__** {nl}"
                                for reaction in messageObj.reactions:
                                    users = await reaction.users().flatten()
                                    if len(users) >1:
                                        text +=f"{reaction.emoji} {nl}```"
                                        count =1
                                        for user in users:
                                            if user.bot == False :
                                                text+= f"{count}  {user.display_name} {nl}"
                                                count+=1
                                        text += '```'
                                if len(text)>1900:
                                    texts = [(text[i:i+1900]) for i in range(0, len(text), 1900)]
                                    for text in texts: 
                                        await self.bot.get_channel(Guild1947.ROSTER_CHANNEL_ID).send(content = text)
                                else:
                                    await self.bot.get_channel(Guild1947.ROSTER_CHANNEL_ID).send(content = text)
                                await messageObj.delete()
                            except Exception as Ex:
                                await self.bot.get_channel(Guild1947.BOT_TESTING_CHANNEL_ID).send(content =f"{Ex}")

                    else:
                        if memberObj.bot == False:
                            await self.bot.get_channel(Guild1947.LONGUE_CHANNEL_ID).send(permission_error_msg)
                            await messageObj.remove_reaction(payload.emoji,memberObj)
                else:
                    pass

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self,payload):
        
        if payload.channel_id == Guild1947.SERVER_UPDATES_CHANNEL_ID:    
            memberObj=self.bot.get_guild(payload.guild_id).get_member(payload.user_id)
            if payload.message_id == Guild1947.ADULT_PAGE_REACTION_MESSAGE_ID:
                messageObj=await self.bot.get_channel(payload.channel_id).fetch_message(payload.message_id)
                if str(payload.emoji) == str(Emoji.UNDER_AGE):
                    GuildObj = self.bot.get_guild(Guild1947.SERVER_ID)
                    roleObj = discord.utils.get(GuildObj.roles, name = RolesGuild1947.ADULT_ROLE_NAME)
                    await memberObj.remove_roles(roleObj)
                    await self.bot.get_channel(id=Guild1947.ADULT_CONTENT_CHANNEL_ID).send(f"{memberObj.mention} Reacted to Remove `18+` Role ")
    @commands.Cog.listener()
    async def on_message(self,message):
        
        if message.author.bot:
            return
        if message.channel.id == Guild1947.EKA_BOT_CHANNEL_ID:
            prefix = list(str(message.content).split())[0]
            prefix+=" "
            if prefix not in DiscordConfig.PREFIX:
                await message.delete()
                await self.bot.get_channel(id=message.channel.id).send(content="Invalid BOT command.  ```eka help``` If you are looking for BOT commands. Pls use loungue to chat. Thanks",delete_after=90)
        if message.channel.id == Guild1947.OPT_INT_OUT_CHANNEL_ID:
            await message.add_reaction(Emoji.NO_ENTRY)
            await message.add_reaction(Emoji.X)
            await message.add_reaction(Emoji.TH11)
            await message.add_reaction(Emoji.TH12)
            await message.add_reaction(Emoji.TH13)
            
        

        
                    


def setup(bot):
    bot.add_cog(Owner(bot))
