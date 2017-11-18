from PLogic import SpriteRenderer, LogicNode


class Pin(SpriteRenderer, LogicNode):
    def __init__(self, simulator):
        LogicNode.__init__(self)
        image = simulator.resources.load_image("pin.png")
        SpriteRenderer.__init__(self, image)
        self.simulator = simulator

    @staticmethod
    def create_pin(simulator, parent, pos):
        pin = Pin(simulator)
        if parent is not None:
            pin.set_parent(parent)
        pin.position = pos
        pin.move_on_drag = False
        simulator.scene.register_object(pin)
        return pin

    def on_remove(self):
        super(Pin, self).on_remove()
        self.simulator.scene.unregister_object(self)