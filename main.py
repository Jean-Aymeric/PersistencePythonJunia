from pyhonbdd.controller.controller import Controller
from pyhonbdd.model.model import Model
from pyhonbdd.view.view import View

controller = Controller(View(), Model())
controller.start()
