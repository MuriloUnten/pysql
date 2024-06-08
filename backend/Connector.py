import mysql.connector as mysql
import psycopg2 as postgres


class MySQLConnector:
    def __init__(self):
        pass

    def connect(self, database, user, password, port=3306):
        try:
            self.connection = mysql.connect(
                database=database,
                user=user,
                password=password,
                port=port,
            )
            self.cursor = self.connection.cursor()
        except:
            print(f"error connecting to database {database}. Please try again.")

    def getDBInfo(self):
        pass

    def getTableInfo(self, table):
        pass


class PostgresConnector:
    def __init__(self):
        pass

    def connect(self, database, user, password, port=5432):
        self.connection = postgres.connect(
            database=database,
            user=user,
            password=password,
            port=port,
        )
        self.cursor = self.connection.cursor()

    def getDBInfo(self):
        pass

    def getTableInfo(self, table):
        pass
