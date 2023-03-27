from pyhonbdd.shared.data.tavern import Tavern
from pyhonbdd.view.screen.idataview import IDataView


class TavernsView(IDataView):
    __IdWidth: int = 4
    __LabelWidth: int = 50
    __ElfWidth: int = 5
    __GoblinWidth: int = 5
    __IdRegionWidth: int = 4
    __TotalWidth: int = 0

    def __init__(self, taverns: [Tavern]):
        self.__taverns: [Tavern] = taverns
        TavernsView.__TotalWidth = 8 + TavernsView.__IdWidth + TavernsView.__LabelWidth + TavernsView.__ElfWidth + \
            TavernsView.__GoblinWidth + TavernsView.__IdRegionWidth

    def display(self):
        self.__displayHeader()
        for tavern in self.__taverns:
            self.__displayTavern(tavern)
        self.__displayFooter()

    @staticmethod
    def __displayHeader():
        print("=" * TavernsView.__TotalWidth)
        print("Auberges".center(TavernsView.__TotalWidth, ' '))
        print("=" * TavernsView.__TotalWidth)

    @staticmethod
    def __displayTavern(tavern: Tavern):
        print(str(tavern.idData) + "\t"
              + tavern.label.ljust(TavernsView.__LabelWidth) + "\t"
              + ("*" * tavern.elf).ljust(TavernsView.__ElfWidth) + "\t"
              + ("*" * tavern.goblin).ljust(TavernsView.__GoblinWidth) + "\t"
              + str(tavern.id_region).ljust(TavernsView.__IdRegionWidth))

    @staticmethod
    def __displayFooter():
        print("=" * TavernsView.__TotalWidth)
