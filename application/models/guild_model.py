from datetime import datetime

from sqlalchemy import Column, String, Integer, Boolean, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class GuildModel(Base):
    __tablename__ = 'guild'
    guild_id = Column(Integer,primary_key = True)
    joined_on = Column(DateTime,datetime.utcnow())