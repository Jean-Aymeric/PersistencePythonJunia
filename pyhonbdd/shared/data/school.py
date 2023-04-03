from __future__ import annotations
from typing import Any
from pyhonbdd.shared.data.data import Data


class School(Data):
    def __init__(self, idData: int, label: str):
        super().__init__(idData)
        self.__label = label

    @property
    def label(self):
        return self.__label

    @label.setter
    def name(self, label: str):
        self.__label = label

    @staticmethod
    def jsonToData(jsonData: dict[str, Any]) -> School:
        return School(jsonData["id"],
                      jsonData["denomination"])

    def dataToJson(self) -> dict[str, Any]:
        return {"id": self.idData,
                "denomination": self.label}
