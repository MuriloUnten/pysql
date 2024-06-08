import mysql.connector as mysql
import psycopg2 as postgres

from abc import ABC, abstractmethod

import Column as Col
import Table


class Connector(ABC):
    @abstractmethod
    def conenct(self, database, user, password, port):
        pass

    @abstractmethod
    def getDBInfo(self):
        pass

    @abstractmethod
    def getTableInfo(self, table):
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
        self.cursor.execute("SHOW COLUMNS FROM ?", tableName)

        cols = []
        for col in self.cursor:
            column = Col.MySQLColumn()
            column.populate(col)
            cols.append(column)

        table = Table.Table(tableName, [], cols)
        return table

    def getTables(self):
        self.cursor.execute("SHOW TABLES")

        tables = []
        for table in self.cursor:
            tables.append(table)

        return table


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
        self.cursor.execute('''SELECT
                            column_name, data_type,
                            character_maximum_lenght,
                            is_nullable, column_default
                            FROM information_schema.columns
                            WHERE table_name = %s''', tableName)

        results = self.cursor.fecthAll()
        cols = []
        for col in results:
            column = Col.MySQLColumn()
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
