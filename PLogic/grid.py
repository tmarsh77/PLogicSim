from pygame import draw
from PLogic import Color, Vector2

from PLogic import RenderObject


class Grid(RenderObject):

    def __init__(self):
        super().__init__()

    @property
    def rect(self):
        return None

    def render(self, viewport, renderer):
        grid_side = 250

        for x in range(-grid_side, grid_side + 1, 50):
            vpos0 = viewport.viewport_to_screen_pos(Vector2.from_array([x, -grid_side]))
            vpos1 = viewport.viewport_to_screen_pos(Vector2.from_array([x, grid_side]))
            draw.line(renderer, Color.Orange, vpos0.to_array(), vpos1.to_array(), 1)

            hpos0 = viewport.viewport_to_screen_pos(Vector2.from_array([-grid_side, x]))
            hpos1 = viewport.viewport_to_screen_pos(Vector2.from_array([grid_side, x]))
            draw.line(renderer, Color.Orange, hpos0.to_array(), hpos1.to_array(), 1)

    def on_remove(self):
        pass