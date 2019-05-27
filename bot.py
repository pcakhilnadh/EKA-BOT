import discord
import os 
from discord.ext import commands

client = commands.Bot(command_prefix='.')

@client.event
async def on_ready():
    print("BOt is ready")
@client.event
async def on_member_join(member):
    if member.guild.id == 561249245672374273:
        welcomechannel = client.get_channel(582661044296744961)
        embed = discord.Embed(
            title = "Welcome!",
            description = f"Hey {member.mention} welcome to {guild.name}!",
            color = 0x07999b
        )
        await channel.send(embed = embed)
@client.event
async def on_member_remove(member):
    channel = member.guild.system_channel
    await channel.send('Elite Kerala Alliance you lost the member  {0}.'.format(member))

client.run(os.environ.get('TOKEN')) #Token is env config var in Heroku Settings
