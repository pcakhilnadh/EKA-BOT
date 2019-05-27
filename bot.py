import discord
import os 
from discord.ext import commands

client = commands.Bot(command_prefix='.')

@client.event
async def on_ready():
    print("BOt is ready")
@client.event
async def on_member_join(member):
    channel = member.guild.system_channel
    await channel.send('Elite Kerala Alliance you got a new member {0.mention}.'.format(member))
@client.event
async def on_member_remove(member):
    channel = member.guild.system_channel
    await channel.send('Elite Kerala Alliance you lost the member  {0}.'.format(member))

client.run(os.environ.get('TOKEN')) #Token is env config var in Heroku Settings
