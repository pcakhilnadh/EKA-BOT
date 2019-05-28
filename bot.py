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
    if member.guild.id == 422681969210556416:
        welcomechannel = client.get_channel(569025914604617729)
        
        embed = discord.Embed(
            title = "Welcome!",
            description = f"Hey {member.mention} welcome to {member.guild.name}!",
            color = 0x07999b
        )
        await welcomechannel.send(embed = embed)
@client.event
async def on_member_remove(member):
    channel = member.guild.system_channel
    await channel.send('Elite Kerala Alliance you lost the member  {0}.'.format(member))

client.run(os.environ.get('TOKEN')) #Token is env config var in Heroku Settings
