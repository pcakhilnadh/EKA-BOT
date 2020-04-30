from datetime import datetime

from sqlalchemy import Column, String, Integer, Boolean, ForeignKey, DateTime, Date, BigInteger
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class MemberModel(Base):
    __tablename__ = 'member'
    member_id = Column(BigInteger, primary_key=True)
    joined_on = Column(DateTime, default=datetime.utcnow)
    dob = Column(Date, nullable=True)
    def __repr__(self):
        return '<member ID: {}, dob: {}, joined on : {}>'.format(self.member_id,self.dob,self.joined_on) 

    def __init__(self,member_id,joined_on=None):
        self.member_id = member_id
        self.joined_on = joined_on