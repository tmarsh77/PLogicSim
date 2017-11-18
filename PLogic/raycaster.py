from PLogic import Vector2, Transform, Interactable


class Raycaster():
    def __init__(self, simulator):
        self.simulator = simulator

    def raycast(self, point: Vector2, all: bool):
        hits = []
        for render_object in self.simulator.scene.scene_objects:
            if not issubclass(type(render_object), Interactable):
                continue

            if self.__overlaps_point(render_object, point):
                hits.append(render_object)

        if len(hits) > 0:
            if all:
                # return all hits
                return hits
            else:
                # return only closest to camera
                closest = -1000
                result = None
                for hit in hits:
                    if hit.zorder > closest:
                        result = hit
                        closest = hit.zorder
                return result
        return None

    def __overlaps_point(self, transform: Transform, point: Vector2):

        viewport = self.simulator.viewport

        trsize = transform.size * viewport.zoom
        trpos = viewport.viewport_to_screen_pos(transform.position)

        point = point

        return (point.x > trpos.x and point.x < trpos.x + trsize.x) and \
               (point.y > trpos.y and point.y < trpos.y + trsize.y)
