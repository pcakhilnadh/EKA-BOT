import logging
import asyncio
from sqlalchemy import and_,desc,extract

from application.config.db_connection import PostgreDBConnector
from application.models.member_model import MemberModel 
from application.models.guild_model import CommandOnGuildModel


class PostgreDB_Utils:

    def __init__(self,db_uri, dbname, sql_session, port=5432):
        try:
            self.client = PostgreDBConnector(db_uri).connect()
            self.database = dbname
            self.sql_session =sql_session
        except Exception as ex:
            logging.exception(" Error Initializing Mongo Client  :- {}".format(ex))

    def fetch_all_from_table(self,Table):
        try:
            result = self.sql_session.query(Table).all()
            if result is not None:
                return result
            else:
                return None
        except Exception as Ex:
            logging.error(" Error in fetch_all_from_table : {}".format(Ex))
    
    def insert_into_member_table(self,id,join_date):
        try:
            r = self.sql_session.query(MemberModel).filter(MemberModel.member_id==id).first()
            if r is None :
                ins = MemberModel(member_id=id,joined_on=join_date)
                self.sql_session.add(ins)
                self.sql_session.commit()
            return True
        except Exception as Ex:
            logging.error(" Error in insert_into_table : {}".format(Ex))
            return False
    
    def delete_from_member_table(self,id):
            try:
                id=int(id)
                ins = self.sql_session.query(MemberModel).filter(MemberModel.member_id==id).delete()
                self.sql_session.commit()
                return True
            except Exception as Ex:
                logging.error(" Error in insert_into_table : {}".format(Ex))
                return False
    

    def update_member_table(self,id,join_date,dob,update_dob=False):
        try:
            fetch = self.sql_session.query(MemberModel).filter(MemberModel.member_id == id).first()
            if fetch is None:
                self.insert_into_member_table(id,join_date)
                fetch = self.sql_session.query(MemberModel).filter(MemberModel.member_id == id).first()
            if fetch.dob is None:
                fetch.dob = dob
                self.sql_session.commit()
                return True
            else:
                if update_dob:
                    fetch.dob = dob
                    self.sql_session.commit()
                    return True
                else:
                    return fetch.dob
            
        except Exception as Ex:
            logging.error(" Error in update_member_table : {}".format(Ex))
            return False

    async def update_last_run_into_command_on_guild(self,guild_id,now_time,command_id=1):
        try:
            fetch =self.sql_session.query(CommandOnGuildModel).filter(and_(CommandOnGuildModel.command_id==int(command_id),CommandOnGuildModel.guild_id==int(guild_id))).first()
            if fetch:
                fetch.last_run_datetime =now_time
                self.sql_session.commit()
        except Exception as Ex:
            logging.error("ERROR : db_utlis.py : update_last_run_into_command_on_guild : {}".format(Ex))

    async def fetch_last_run_from_command_on_guild(self,guild_id,command_id=1):
        try:
            fetch =self.sql_session.query(CommandOnGuildModel).filter(and_(CommandOnGuildModel.command_id==int(command_id),CommandOnGuildModel.guild_id==int(guild_id))).first()
            if fetch:
                return fetch.last_run_datetime
            else:
                return False
        except Exception as Ex:
            logging.error(" Error in fetch_last_run_from_command_on_guild : {}".format(Ex))
            return False

    def users_has_bday_on_date(self,date):
        try:
            user_id = list()
            result =self.sql_session.query(MemberModel).filter(MemberModel.dob.isnot(None)).all()
            for row in result: 
                if ((row.dob.month == date.month) and (row.dob.day == date.day)):
                    user_id.append(row.member_id)
            return user_id
        except Exception as Ex:
            logging.error(" Error in users_has_bday_on_date : {}".format(Ex))
            return None
    def fetch_bday(self):
        try:
            result =self.sql_session.query(MemberModel).filter(MemberModel.dob.isnot(None)).order_by(desc(MemberModel.dob)).all()
            if result:
                return result
            else:
                return False
                    
        except Exception as Ex:
            logging.error(" db_utlis.py : fetch_bday : {}".format(Ex))
            return None
