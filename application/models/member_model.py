from datetime import datetime

from sqlalchemy import Column, String, Integer, Boolean, ForeignKey, DateTime, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class MemberModel(Base):
    __tablename__ = 'member'
    member_id = Column(Integer, primary_key=True)
    joined_on = Column(DateTime, default=datetime.utcnow)
    dob = Column(Date, nullable=True)
    def __repr__(self):
        return '<member ID: {}, dob: {}, joined on : {}>'.format(self.member_id,self.dob,self.joined_on) 