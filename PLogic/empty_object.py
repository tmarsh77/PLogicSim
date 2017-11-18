from PLogic import Vector2, Transform


class EmptyObject(Transform):
    def __init__(self):
        Transform.__init__(self)

    def transform_refresh(self, pos: Vector2, size: Vector2):
        pass
