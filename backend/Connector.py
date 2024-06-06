import mysql.connector as mysql


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

    def getDBInfo():
        pass

    def getTableInfo(table):
        pass


