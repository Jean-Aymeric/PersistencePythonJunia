from pyhonbdd.shared.data.region import Region
from pyhonbdd.shared.data.tavern import Tavern
from pyhonbdd.shared.iview import IView
from pyhonbdd.shared.imodel import IModel
from pyhonbdd.view.screen.regionview import RegionsView
from pyhonbdd.view.screen.tavernsview import TavernsView



class View(IView):
    def __init__(self):
        self.__model: IModel | None = None
        self.__controller = None

    @property
    def controller(self):
        return self.__controller

    @property
    def model(self) -> IModel:
        return self.__model

    @controller.setter
    def controller(self, controller):
        self.__controller = controller
        if controller.view != self:
            controller.view = self
        self.model = controller.model

    @model.setter
    def model(self, model: IModel):
        self.__model = model

    def displayTaverns(self, tavern: [Tavern]):
        TavernsView(tavern).display()

    def displayRegions(self, region: [Region]):
        RegionsView(region).display()
