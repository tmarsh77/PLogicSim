from pygame import transform

from PLogic import Transform, RenderObject, Vector2, Interactable


class SpriteRenderer(Transform, RenderObject, Interactable):
    def __init__(self, image):
        Transform.__init__(self)
        # super(SpriteRenderer, self).__init__()
        self.image_original = image
        rect = self.image_original.get_rect()
        self.size = Vector2(rect.width, rect.height)
        self.image_rect = rect

    def transform_refresh(self, pos: Vector2, size: Vector2):
        self.image_rect.x = pos.x
        self.image_rect.y = pos.y

    @property
    def rect(self):
        return self.image_rect

    def render(self, viewport, renderer):
        # move to base RENDERABLE class
        size = self.size * viewport.zoom
        pos = viewport.viewport_to_screen_pos(self.position)

        image = transform.scale(self.image_original, (int(size.x), int(size.y)))
        renderer.blit(image, (pos.x, pos.y))

    def on_remove(self):
        pass