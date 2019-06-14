import discord
from discord.ext import commands

import asyncio
import traceback
from .utils.chat_formatting import pagify


DEBUG_SERVER_ID = 586915159377707027
ERROR_LOGS_ID   = 586932176403169281
COMMANDS_DEBUG  = 586932197752176651
BOT_JOIN_ID      = 586986233289244692

VC_CHANNELS = [
    586915160015503392,     # Total Servers
    586932359253983252      # Last Joined/Left Server
]


class Debug(commands.Cog):
    """Cog for various events and debugging"""

    def __init__(self, bot):
        self.bot = bot
        self.error_logs = None
        self.commands_debug = None
        self.vc_channels = []
        self.task = self.bot.loop.create_task(self.initialize())

    def cog_unload(self):
        self.task.cancel()


    async def initialize(self):
        await self.bot.wait_until_ready()
        self.error_logs = self.bot.get_channel(ERROR_LOGS_ID)
        self.commands_debug = self.bot.get_channel(COMMANDS_DEBUG)
        for channel in VC_CHANNELS:
            self.vc_channels.append(self.bot.get_channel(channel))


    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        """Debugs when a guild is joined by the bot!"""
        joinchannel= self.bot.get_channel(BOT_JOIN_ID)
        title = "Joined a new server"
        description = f"""{guild.name} [{guild.id}]
Members: {len(guild.members)}
Owner: {guild.owner} [{guild.owner.id}]"""
        embed = discord.Embed(title=title,
                              description=description,
                              color=discord.Color.green())
        embed.set_thumbnail(url=guild.icon_url)
        await joinchannel.send(embed=embed)

        total_servers = len(self.bot.guilds)
        total_vc = self.vc_channels[0]
        last_joined_vc = self.vc_channels[1]
        await total_vc.edit(name=f"On {total_servers} Servers")
        await last_joined_vc.edit(name=f"Last joined: {guild.name}")
        



    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        """Debugs when a guild is left by the bot!"""
        joinchannel= self.bot.get_channel(BOT_JOIN_ID)
        title = "Left a server"
        description = f"{guild.name} [{guild.id}]"
        embed = discord.Embed(title=title, description=description, color=discord.Color.red())
    #    embed.set_thumbnail(url=guild.icon.url)
        await joinchannel.send(embed=embed)
        total_servers = len(self.bot.guilds)
        total_vc = self.vc_channels[0]
        last_left_vc = self.vc_channels[1]
        await total_vc.edit(name="On {} Servers".format(str(total_servers)))
        await last_left_vc.edit(name=f"Last left: {guild.name}")
        

    @commands.Cog.listener()
    async def on_command(self, ctx):
        title = "Command invoked!"
        guild = f"{ctx.guild.name}[{ctx.guild.id}]" if ctx.guild else "DMs"
        description = f"""Command - `{ctx.message.content}`
Server = {guild}
"""
        avatar = ctx.author.avatar_url if ctx.author.avatar else ctx.author.default_avatar_url
        embed = discord.Embed(title=title, description=description, color=discord.Color.orange())
        embed.set_author(name=f"{ctx.author}", icon_url=avatar)
        embed.set_thumbnail(url=avatar)
        embed.set_footer(text=str(ctx.author.id))
        await self.commands_debug.send(embed=embed)



    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.errors.CommandNotFound):
            await ctx.send("That command doesn't exist.")
        elif isinstance(error, commands.NoPrivateMessage):
            await ctx.send('This command cannot be used in private messages.')
        elif isinstance(error, commands.errors.TooManyArguments):
            await ctx.send(error)
        elif isinstance(error, commands.DisabledCommand):
            await ctx.send('Sorry. This command is disabled and cannot be used.')
        elif isinstance(error, commands.errors.MissingRequiredArgument):
            await ctx.send(f"Not enough arguments supplied.")
            await ctx.send_help(ctx.command)
        elif isinstance(error, commands.errors.BadArgument):
            await ctx.send(f"Bad arguments supplied.")
            await ctx.send_help(ctx.command)
        elif isinstance(error, commands.errors.NotOwner):
            await ctx.send("This command is only for my master, Pc!!!!")
        elif isinstance(error, discord.errors.Forbidden):
            await ctx.send("I don't have enough permsissions to do that!")
        elif isinstance(error, commands.errors.MissingPermissions):
            await ctx.send("You don't have enough permissions to use this command!")
        elif isinstance(error, commands.errors.CommandOnCooldown):
            pass
       
        else:
            try:
                invite = await ctx.channel.create_invite(max_uses=1)
                invite = invite.url
            except:
                invite = "Couldn't create an invite"

            log = "".join(traceback.format_exception(type(error), error, error.__traceback__))

            #description = f"```py\n{log}\n```"
            embed = discord.Embed(title="An error occured",
                                  #description=description,
                                  color=discord.Color.orange())
            field = f"""Command: `{ctx.message.content}`
Author: {ctx.author}[{ctx.author.id}]
Server: {ctx.guild.name}[{ctx.guild.id}]
Server Invite: {invite}
"""

            for page in pagify(log, page_length=1024):
                embed.add_field(name='\u200b',
                                value=f'```py\n{page}\n```')
            embed.add_field(name="Information", value=field)
            await self.error_logs.send(embed=embed)
            raise error


def setup(bot):
    n = Debug(bot)
    bot.add_cog(n)