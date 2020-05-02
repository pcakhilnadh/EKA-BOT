import discord
import asyncio
import requests
from io import BytesIO
import os
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
from application.constants.guild1947 import *
from application.constants.guildsupport import GuildSupport
from application.constants.emoji import Emoji


class Birthday():
    def __init__(self,bot,db_utlis,userObj):
        self.bot=bot
        self.db_utlis=db_utlis
        self.userObj = userObj
        self.directory= os.getcwd()
    async def update_lasttime_run_in_db(self):
        time = datetime.now()
        time = time.replace(hour=0, minute=0, second=0,microsecond=0)
        await self.db_utlis.update_last_run_into_command_on_guild(Guild1947.SERVER_ID,time)

    async def wish_birthday(self):
        birthday_wishes = f"@everyone Wish {self.userObj.mention}, Happy Birthday !"
        await self.update_lasttime_run_in_db()
        try:
            await self.image_maker()
            file = discord.File(os.path.join(self.directory)+Guild1947Image.TEMP_IMAGE)
            msg = await self.bot.get_channel(Guild1947.ANNOUNCEMENT_CHANNEL_ID).send(content=birthday_wishes,file=file)
        except:
            msg = await self.bot.get_channel(Guild1947.ANNOUNCEMENT_CHANNEL_ID).send(content=birthday_wishes)
        await msg.add_reaction(Emoji.BIRTHDAY)

    async def image_maker(self):
        temp_image_loc = os.path.join(self.directory)+Guild1947Image.TEMP_IMAGE_LOC
        poster= os.path.join(self.directory)+Guild1947Image.POSTER_IMAGE_LOC
        response = requests.get(self.userObj.avatar_url)
        modak_font = os.path.join(self.directory)+Guild1947Font.MODAK_FONT
        poster_image = Image.open(poster)
        user_avatar = Image.open(BytesIO(response.content))

        draw = ImageDraw.Draw(poster_image)
        font = ImageFont.truetype(modak_font,size =25)
        (x, y) = (150, 20)
        message = f"{self.userObj.display_name}"
        message=message[:20]
        color = 'rgb(255,255,0)' # yellow color
        draw.text((x, y), message, fill=color, font=font)
        back_im = poster_image.copy()
        newsize = (150, 150)
        user_avatar = user_avatar.resize(newsize)
        back_im.paste(user_avatar, (175, 75))
        back_im.save(temp_image_loc+"temp.png", quality=95)
        #poster_image.save(temp_image_loc+"temp.png")