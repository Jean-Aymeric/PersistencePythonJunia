from __future__ import annotations

from typing import Any

from pyhonbdd.shared.data.data import Data


class Tavern(Data):
    def __init__(self, idData: int, label: str, elf: int, goblin: int, id_region: int):
        super().__init__(idData)
        self.__label: str = label
        self.__elf: int = elf
        self.__goblin: int = goblin
        self.__id_region: int = id_region

    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def elf(self) -> int:
        return self.__elf

    @elf.setter
    def elf(self, elf: int):
        self.__elf = elf

    @property
    def goblin(self) -> int:
        return self.__goblin

    @goblin.setter
    def goblin(self, goblin: int):
        self.__goblin = goblin

    @property
    def id_region(self) -> int:
        return self.__id_region

    @staticmethod
    def jsonToData(jsonData: dict[str, Any]) -> Tavern:
        return Tavern(jsonData["id"],
                      jsonData["denomination"],
                      jsonData["elfe"],
                      jsonData["gobelin"],
                      jsonData["id_Region"])

    def dataToJson(self) -> dict[str, Any]:
        return {"id": self.idData,
                "denomination": self.label,
                "elfe": self.elf,
                "gobelin": self.goblin,
                "id_Region": self.id_region}
