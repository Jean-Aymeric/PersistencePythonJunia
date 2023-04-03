from __future__ import annotations
from typing import Any
from pyhonbdd.shared.data.data import Data


class Region(Data):
    def __init__(self, idData: int, name: str):
        super().__init__(idData)
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @staticmethod
    def jsonToData(jsonData: dict[str, Any]) -> Region:
        return Region(jsonData["id"],
                      jsonData["nom"])

    def dataToJson(self) -> dict[str, Any]:
        return {"id": self.idData,
                "nom": self.name}
