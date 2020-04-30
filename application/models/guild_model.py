from datetime import datetime

from sqlalchemy import Column, String, Integer, Boolean, ForeignKey, DateTime, BigInteger
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship



Base = declarative_base()

class CommandOnGuildModel(Base):
    __tablename__ = "command_on_guild"
    command_id = Column(Integer, ForeignKey('command.command_id'), primary_key=True)
    guild_id = Column(BigInteger, ForeignKey('guild.guild_id'), primary_key=True)
    last_run_datetime = Column(DateTime, default=datetime.utcnow)
    channel1_id = Column(BigInteger, default=None)
    channel2_id = Column(BigInteger, default=None)
    channel3_id = Column(BigInteger, default=None)
    guild = relationship("GuildModel", back_populates="command")
    command = relationship("CommandModel", back_populates="guild")

    def __init__(self,guild_id,command_id):
        self.guild_id = guild_id
        self.command_id = command_id
    def __repr__(self):
        return '<guild_id: {}, command_id : {} last_run : {}, guild:{}, command : {}>'.format(self.guild_id,self.command_id,self.last_run_datetime,self.guild, self.command) 

class GuildModel(Base):
    __tablename__ = 'guild'
    guild_id = Column(BigInteger,primary_key = True)
    joined_on = Column(DateTime, default=datetime.utcnow)
    command = relationship("CommandOnGuildModel", back_populates="guild")

    def __init__(self,guild_id,joined_on=None):
        self.guild_id = guild_id
        self.joined_on = joined_on
    def __repr__(self):
        return '<guild_id: {}, joined_on : {}>'.format(self.guild_id,self.joined_on) 

class CommandModel(Base):
    __tablename__ = 'command'
    command_id = Column(Integer,primary_key = True,autoincrement=True)
    command_name = Column(String(50),nullable=False)
    channel_count_required = Column(Integer, nullable=True, default=0)
    guild = relationship("CommandOnGuildModel", back_populates="command")

    def __init__(self,command_id,command_name,channel_count_required=0):
        self.command_id = command_id
        self.command_name = command_name
        self.channel_count_required = channel_count_required
    def __repr__(self):
        return '<command_id: {}, command_name : {},channel_count_required : {}>'.format(self.command_id,self.command_name,self.channel_count_required) 
    
