import psycopg2
import logging
import sys


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#from application.utlis.db_utlis import PostgreDB_Utils
from application.constants.config import PostgreeDB_Config
from application.utlis.db_utlis import PostgreDB_Utils
from app_driver import EkaBot

class EkaBOTApp():
    def __init__(self):
        self.sql_session = None

    def create_session(self):
        try:
            if self.sql_session is None:
                engine = create_engine(PostgreeDB_Config.URI, echo=False)
                Session = sessionmaker(bind=engine)
                self.sql_session = Session()
        except Exception as dbEx:
            logging.error("Error creating database connection :-  {} ".format(dbEx))
            sys.exit(-1)

    def close_session(self):
        if self.sql_session is not None:
            self.sql_session.close()

    def execute(self):
        try:
            self.create_session()
            db_utlis = PostgreDB_Utils(PostgreeDB_Config.URI,PostgreeDB_Config.DB,self.sql_session)
            #print(db_utlis.insert_into_db())
            eka_bot_driver = EkaBot(db_utlis)
            eka_bot_driver.run()

        except Exception as Ex:
            logging.error("Exception : {}".format(Ex))
        
        finally:
            self.close_session()


if __name__ == "__main__":
    
    #db_utlis = PostgreDB_Utils(PostgreeDB_Config.HOST,PostgreeDB_Config.USER,PostgreeDB_Config.PASSWORD,PostgreeDB_Config.DB)

    Eka_Bot = EkaBOTApp()
    Eka_Bot.execute()