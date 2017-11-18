import uuid
from abc import ABCMeta, abstractmethod

class SceneObject():
    def __init__(self):
        self.children = []
        self.uid = uuid.uuid4().hex

    def add_child(self, child):
        self.children.append(child)

    def remove_child(self, child):
        self.children.remove(child)

    @abstractmethod
    def on_remove(self):
        pass