from __future__ import annotations
from typing import Any
from pyhonbdd.shared.data.data import Data


class Map(Data):
    def __init__(self, idData: int, name: str):
        super().__init__(idData)
        self.__name = name

    @property
    def name(self):
        return self.__name

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @staticmethod
    def jsonToData(jsonData: dict[str, Any]) -> Region:
        return Region(jsonData["id"],
                      jsonData["nom"])

    def dataToJson(self) -> dict[str, Any]:
        return {"id": self.idData,
                "nom": self.name}
