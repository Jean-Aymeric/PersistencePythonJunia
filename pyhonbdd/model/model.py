from typing import Any

from pyhonbdd.model.dbconnector import DBConnector
from pyhonbdd.shared.data.data import Data
from pyhonbdd.shared.imodel import IModel


class Model(IModel):
    def __init__(self):
        self.__dbConnector: DBConnector = DBConnector("dbconf.json")

    def getDataById(self, entityName: str, __idData: int) -> Data:
        jsonData = self.__dbConnector.getJsonDataById(entityName, __idData)
        return Model.__dataConverter(entityName, jsonData)

    def getAllData(self, entityName: str) -> [Data]:
        jsonData: [dict[str, Any]] = self.__dbConnector.getAllJsonData(entityName)
        data: [Data] = []
        for json in jsonData:
            data.append(Model.__dataConverter(entityName, json))
        return data

    @staticmethod
    def __dataConverter(entityName: str, jsonData: dict[str, Any]) -> Data:
        if entityName == "auberge":
            from pyhonbdd.shared.data.tavern import Tavern
            return Tavern.jsonToData(jsonData)
        elif entityName == "region":
            from pyhonbdd.shared.data.region import Region
            return Region.jsonToData(jsonData)
        else:
            raise Exception("Unknown entity name")
