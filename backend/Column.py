from abc import ABC, abstractmethod


class Column(ABC):
    @abstractmethod
    def populate(fieldTuple):
        pass


class MySQLColumn(Column):
    def __init__(self):
        pass

    def populate(self, fieldTuple):
        self.name = fieldTuple[0]
        self.type = fieldTuple[1]
        self.null = fieldTuple[2]
        self.key = fieldTuple[3]
        self.default = fieldTuple[4]


class PostgresColumn(Column):
    def __init__(self):
        pass

    def populate(self, fieldTuple):
        self.name = fieldTuple[0]
        self.type = fieldTuple[1]
        typeLength = str(fieldTuple[2])
        print(typeLength)
        if typeLength != "None":
            self.type += f"({typeLength})"
        self.null = fieldTuple[3]
        self.key = fieldTuple[4]
        self.default = fieldTuple[5]
