from abc import ABCMeta, abstractmethod

from PLogic import SceneObject


class RenderObject(SceneObject, metaclass=ABCMeta):

    def __init__(self):
        super().__init__()

    @property
    @abstractmethod
    def rect(self):
        pass

    @abstractmethod
    def render(self, viewport, renderer):
        pass

    @abstractmethod
    def on_remove(self):
        pass