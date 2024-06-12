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
        query = (
            "SELECT"
            "column_name, data_type,"
            "character_maximum_lenght,"
            "is_nullable, column_default"
            "FROM information_schema.columns"
            "WHERE table_name = %s"
        )
        self.cursor.execute(query, (tableName, ))

        results = self.cursor.fecthAll()
        cols = []
        for col in results:
            column = MySQLColumn()
            column.populate(col)
            cols.append(column)

        table = Table.Table(tableName, [], cols)
        return table

    def getTables(self):
        self.cursor.execute("SHOW TABLES")

        rows = self.cursor.fecthAll()

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
            result = self.cursor.fetchAll()
            return result
