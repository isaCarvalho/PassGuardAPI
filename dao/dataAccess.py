import psycopg2
from dao.config import config

class DataAccess:

    @staticmethod
    def queryStatement(fields, table, condition = True):
        conn = None
        data = None
    
        try:
            params = config()
            conn = psycopg2.connect(**params)

            cur = conn.cursor()

            statement = "SELECT {} FROM {} WHERE {}".format(fields, table, condition)

            cur.execute(statement)

            data = cur.fetchall()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()

            return data
        
    @staticmethod
    def executeStatement(statement):
        conn = None
        data = None

        try:
            params = config()
            conn = psycopg2.connect(**params)

            cur = conn.cursor()
            cur.execute(statement)
            cur.statusmessage

            conn.commit()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

        finally:
            if conn is not None:
                conn.close()