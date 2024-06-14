import mysql.connector as mysql
import psycopg2 as postgres

from abc import ABC, abstractmethod

from backend.Table import *
from backend.Column import *


class Connector(ABC):
    @abstractmethod
    def connect(self, database, user, password, port):
        pass

    @abstractmethod
    def getDBInfo(self):
        pass

    @abstractmethod
    def getTableInfo(self, tableName):
        pass

    @abstractmethod
    def getTables(self):
        pass


class MySQLConnector(Connector):
    def __init__(self):
        pass

    def connect(self, database, user, password, port=3306):
        try:
            self.database = database

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

    def getTableInfo(self, tableName):
        query = "SHOW COLUMNS FROM " + tableName
        self.cursor.execute(query)

        cols = []
        for col in self.cursor:
            column = MySQLColumn()
            column.populate(col)
            cols.append(column)

        table = Table(tableName, [], cols)
        return table

    def getTables(self):
        self.cursor.execute("SHOW TABLES")

        tables = []
        for table in self.cursor:
            tables.append(table[0])

        return tables

    def execute(self, query, *params):
        try:
            self.cursor.execute(query, params)
        except:
            print("Error executing query")
            return ("")
        finally:
            result = self.cursor.fetchall()
            column_names = [i[0] for i in self.cursor.description]
            return result, column_names


class PostgresConnector(Connector):
    def __init__(self):
        pass

    def connect(self, database, user, password, port=5432):
        try:
            self.database = database

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

    def getTableInfo(self, tableName):
        query = ("SELECT column_name, data_type, "
                 "character_maximum_length, "
                 "is_nullable, column_default "
                 "FROM information_schema.columns "
                 f"WHERE table_name = '{tableName}'")
        self.cursor.execute(query)
        results = self.cursor.fetchall()

        # This query returns the name of the column that is the PRIMARY KEY
        query = ("SELECT a.attname "
                 "FROM   pg_index i "
                 "JOIN   pg_attribute a ON a.attrelid = i.indrelid "
                 "AND a.attnum = ANY(i.indkey) "
                 f"WHERE  i.indrelid = '{tableName}'::regclass "
                 "AND    i.indisprimary; ")
        self.cursor.execute(query)
        pksTuple = self.cursor.fetchall()
        pks = []
        for key in pksTuple:
            pks.append(key[0])

        cols = []
        for col in results:
            tmp = col
            col = (tmp[0], tmp[1], tmp[2], tmp[3], "PRI" if tmp[0] in pks else "NO", tmp[4])
            column = PostgresColumn()
            column.populate(col)
            cols.append(column)

        table = Table(tableName, [], cols)
        return table

    def getTables(self):
        self.cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'")

        rows = self.cursor.fetchall()

        tables = []
        for row in rows:
            tables.append(row[0])
        return tables

    def execute(self, query, *params):
        try:
            self.cursor.execute(query, params)
        except:
            print("Error executing query")
            return ("")
        finally:
            result = self.cursor.fetchall()
            column_names = [i[0] for i in self.cursor.description]
            return result, column_names
