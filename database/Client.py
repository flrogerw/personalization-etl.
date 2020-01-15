import psycopg2
from Config import Config


class Client:

    def __init__(self, profile):
        params = Config.getPostgres(profile)
        self.conn = psycopg2.connect(**params)
        self.cur = self.conn.cursor()

    def query(self, query):
        self.cur.execute(query)

    def close(self):
        self.cur.close()
