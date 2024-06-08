from abc import ABC, abstractmethod


class Table:
    def __init__(self, name, rows, cols):
        self.name = name
        self.rows = rows
        self.cols = cols
        self.pk = self.getPrimaryKey()

    def getPrimaryKey(self):
        for col in self.cols:
            if col.key == "PRI":
                return col.name

        return "No Primary Key"
