import os
import datetime
import discord
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
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="itz__pc"))
    print("BOt is ready")
    
@client.event
async def on_member_join(member):
    if member.guild.id == 561249245672374273:
        welcomechannel = client.get_channel(569973273253904385)
        apply_eka = client.get_channel(566609366770515989)
        about =client.get_channel(567962887054950420)
        directory=os.getcwd()
        file = discord.File(os.path.join(directory+str('/')+"images/recruitment.jpg"),filename="recruitment.jpg")
        embed = discord.Embed(title="**__WELCOME TO EKA__**", colour=discord.Colour(0x673c27), url="https://link.clashofclans.com/?action=OpenClanProfile&tag=RJ9JYYQQ", description=f"Hello {member.mention} \n\n:point_right:Elite Kerala Alliance. \n:point_right: MLCW - GWL & EWL -ELITE clan.\n :point_right: WCL Semi Finalists, EWL Quarter Finalists.\n\n  ", timestamp=datetime.datetime.utcfromtimestamp(1559028785))
        embed.set_thumbnail(url=str(member.avatar_url))
        embed.set_author(name="Elite Kerala Alliance ", url="https://link.clashofclans.com/?action=OpenClanProfile&tag=RJ9JYYQQ", icon_url="https://cdn.discordapp.com/attachments/562537063052738569/582847093434089472/eka.jpg")
        embed.set_footer(text="Team EKA |", icon_url="https://cdn.discordapp.com/attachments/562537063052738569/582847093434089472/eka.jpg")
        embed.add_field(name=f"Want to join With Us ?", value=f"React with :envelope_with_arrow: in {apply_eka.mention} \n\n")
        embed.add_field(name=f"Want to join get GUEST role ?", value=f":sos: React with EKA logo in {about.mention} ")
        embed.set_image(url="attachment://recruitment.jpg")
        await welcomechannel.send(file=file,embed = embed)
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
