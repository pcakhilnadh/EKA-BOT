import discord
import os 
from discord.ext import commands

client = commands.Bot(command_prefix='.')
'''
def read_token():
    with open("token.txt","r") as f:
        lines=f.readlines()
        return lines[0].strip() 
'''
@client.event
async def on_ready():
    print("BOt is ready")
    
@client.event
async def on_member_join(member):
    if member.guild.id == 561249245672374273:
        welcomechannel = client.get_channel(582661044296744961)
        embed = discord.Embed(
            title = "Welcome",
            description = f"Hey {member.mention} welcome to {member.guild.name} Server!",
            color = 0x07999b
        )
        await welcomechannel.send(embed = embed)
@client.event
async def on_member_remove(member):
    
    if member.guild.id == 561249245672374273:
        welcomechannel = client.get_channel(582661044296744961)
        embed = discord.Embed(
            title = "Bye Bye",
            description = f"{member} left {member.guild.name} server!",
            color = 0x07999b
        )
        await welcomechannel.send(embed = embed)

client.run(os.environ.get('TOKEN')) #Token is env config var in Heroku Settings
#client.run(read_token())
