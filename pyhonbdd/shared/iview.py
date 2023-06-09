from abc import ABCMeta, abstractmethod

from pyhonbdd.shared.data.region import Region
from pyhonbdd.shared.data.school import School
from pyhonbdd.shared.data.tavern import Tavern
from pyhonbdd.shared.imodel import IModel


class IView(metaclass=ABCMeta):
    @property
    @abstractmethod
    def controller(self):
        pass

    @controller.setter
    @abstractmethod
    def controller(self, view):
        pass

    @property
    @abstractmethod
    def model(self) -> IModel:
        pass

    @model.setter
    @abstractmethod
    def model(self, model: IModel):
        pass

    @abstractmethod
    def displayTaverns(self, tavern: [Tavern]):
        pass

    @abstractmethod
    def displayRegions(self, region: [Region]):
        pass

    def displaySchools(self, school: [School]):
        pass
