from pyhonbdd.shared.data.region import Region
from pyhonbdd.view.screen.idataview import IDataView


class RegionsView(IDataView):
    __IdWidth: int = 4
    __NameWidth: int = 50
    __TotalWidth: int = 0

    def __init__(self, regions: [Region]):
        self.__regions: [Region] = regions
        RegionsView.__TotalWidth = 8 + RegionsView.__IdWidth + RegionsView.__NameWidth

    def display(self):
        self.__displayHeader()
        for region in self.__regions:
            self.__displayRegion(region)
        self.__displayFooter()

    @staticmethod
    def __displayHeader():
        print("=" * RegionsView.__TotalWidth)
        print("Régions".center(RegionsView.__TotalWidth, ' '))
        print("=" * RegionsView.__TotalWidth)

    @staticmethod
    def __displayRegion(region: Region):
        print(str(region.idData) + "\t"
              + region.name.ljust(RegionsView.__NameWidth))

    @staticmethod
    def __displayFooter():
        print("=" * RegionsView.__TotalWidth)
