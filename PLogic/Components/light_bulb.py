from PLogic import SpriteRenderer, Pin, Vector2, LogicGate, Serializable


class LightBulb(SpriteRenderer, LogicGate, Serializable):
    def __init__(self, simulator):
        LogicGate.__init__(self)
        self.image_off = simulator.resources.load_image("light_off.png")
        self.image_on = simulator.resources.load_image("light_on.png")
        SpriteRenderer.__init__(self, self.image_off)
        self.pin = Pin.create_pin(simulator, self, Vector2(30, 170))
        self.pin.on_value_changed = self.resolve
        self.simulator = simulator

    def resolve(self):
        self.image_original = self.image_on if self.pin.signal == 1 else self.image_off

    def to_json(self):
        return Serializable.json_dumps(
            {
                'pos': self.position.to_array(),
                'uid': self.uid,
                'pin': self.pin.uid
            }
        )

    def on_remove(self):
        super(LightBulb, self).on_remove()
        self.simulator.remove_wires(self.pin)
        self.pin.on_remove()
        self.simulator.scene.unregister_object(self)