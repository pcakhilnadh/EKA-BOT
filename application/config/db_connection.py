import psycopg2

class PostgreDBConnector:
    """
        Connects to the PostgreSQL server and creates a client instance.
    """
    def __init__(self,connection_uri, port=5432):
        self.connection_uri = connection_uri
        self.port = port
        self.connection = None

    def connect(self):
        self.connection = psycopg2.connect(self.connection_uri)
        return self.connection.cursor()

    def close(self):
        if self.connection is not None:
            self.connection.cursor.close()
            self.connection = None
