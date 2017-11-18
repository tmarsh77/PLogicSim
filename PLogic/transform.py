from abc import ABCMeta, abstractmethod

from PLogic import Vector2, SceneObject


class Transform(SceneObject, metaclass=ABCMeta):
    zorder = 0

    __pos = Vector2.zero()
    __size = Vector2.zero()
    parent = None

    def __init__(self):
        SceneObject.__init__(self)
        # super(Transform, self).__init__()

    @property
    def position(self) -> Vector2:
        parent = self.parent
        offset = Vector2.zero()
        if parent is not None:
            offset = parent.position
        return self.__pos + offset

    @position.setter
    def position(self, pos: Vector2):
        self.__pos = pos

    @property
    def size(self) -> Vector2:
        return self.__size

    @size.setter
    def size(self, size: Vector2):
        self.__size = size

    @abstractmethod
    def transform_refresh(self, pos: Vector2, size: Vector2):
        pass

    def set_parent(self, parent: 'Transform'):
        if parent is not None:
            parent.add_child(self)
            self.parent = parent
            return
        parent.remove_child(self)
        self.parent = None
