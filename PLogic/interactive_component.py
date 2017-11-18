from abc import ABCMeta, abstractmethod


class InteractiveComponent(metaclass=ABCMeta):
    @abstractmethod
    def interact(self):
        pass
