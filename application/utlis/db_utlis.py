import logging

from application.config.db_connection import PostgreDBConnector

from application.models.member_model import MemberModel 

class PostgreDB_Utils:

    def __init__(self,db_uri, dbname, sql_session, port=5432):
        try:
            self.client = PostgreDBConnector(db_uri).connect()
            self.database = dbname
            self.sql_session =sql_session
        except Exception as ex:
            logging.exception(" Error Initializing Mongo Client  :- {}".format(ex))

    def insert_into_db(self):
        try:
            result = self.sql_session.query(MemberModel).all()
            if result is not None:
                return result
            else:
                return None

        except Exception as Ex:
            logging.error(" Error in insertion : {}".format(Ex))