from PLogic import Vector2


class Viewport():
    size = None
    pos = Vector2.zero()
    zoom = 1

    def __init__(self, size: Vector2):
        self.size = size

    def set_zoom(self, delta):
        zoom_prev = self.zoom
        zoom = self.zoom + delta
        zoom = 0.1 if zoom < 0.1 else zoom
        zoom = 1 if zoom > 1 else zoom
        if zoom != zoom_prev:
            self.zoom = zoom
            return True
        return False

    def pan(self, delta: Vector2):
        self.pos = self.pos + delta

    def screen_to_viewport_pos(self, pos: Vector2):
        return (pos / self.zoom + self.pos) - (self.size / 2 / self.zoom)

    def viewport_to_screen_pos(self, pos: Vector2):
        return (pos - self.pos) * self.zoom + self.size / 2
