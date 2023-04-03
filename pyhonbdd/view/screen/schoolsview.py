from pyhonbdd.shared.data.school import School
from pyhonbdd.view.screen.idataview import IDataView


class SchoolsView(IDataView):
    __IdWidth: int = 4
    __LabelWidth: int = 50
    __TotalWidth: int = 0

    def __init__(self, schools: [School]):
        self.__schools: [School] = schools
        SchoolsView.__TotalWidth = 8 + SchoolsView.__IdWidth + SchoolsView.__LabelWidth

    def display(self):
        self.__displayHeader()
        for school in self.__schools:
            self.__displaySchool(school)
        self.__displayFooter()

    @staticmethod
    def __displayHeader():
        print("=" * SchoolsView.__TotalWidth)
        print("Ecoles".center(SchoolsView.__TotalWidth, ' '))
        print("=" * SchoolsView.__TotalWidth)

    @staticmethod
    def __displaySchool(school: School):
        print(str(school.idData) + "\t"
              + school.name.ljust(SchoolsView.__LabelWidth))

    @staticmethod
    def __displayFooter():
        print("=" * SchoolsView.__TotalWidth)
