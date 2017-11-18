from PLogic import SceneObject


class Scene():
    def __init__(self):
        self.scene_objects = []

    def register_object(self, object: SceneObject):
        # self.scene_objects.insert(0, object)
        self.scene_objects.append(object)

    def unregister_object(self, object: SceneObject):
        if object in self.scene_objects:
            self.scene_objects.remove(object)

    def find_by_uid(self, uid):
        for obj in self.scene_objects:
            if issubclass(type(obj), SceneObject) and obj.uid == uid:
                return obj
        print("Object with uid {%s} not found" % uid)
        return None
