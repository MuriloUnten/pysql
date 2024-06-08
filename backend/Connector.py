import mysql.connector as mysql
import psycopg2 as postgres

from abc import ABC, abstractmethod


class Connector(ABC):
    @abstractmethod
    def conenct():
        pass

    @abstractmethod
    def getDBInfo():
        pass

    @abstractmethod
    def getTableInfo():
        pass


class MySQLConnector(Connector):
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


class PostgresConnector(Connector):
    def __init__(self):
        pass

    def connect(self, database, user, password, port=5432):
        try:
            self.connection = postgres.connect(
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
