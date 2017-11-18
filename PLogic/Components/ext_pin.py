from PLogic import SpriteRenderer, Pin, Vector2, LogicGate, Serializable


class ExtPin(SpriteRenderer, LogicGate, Serializable):
    def __init__(self, simulator):
        LogicGate.__init__(self)
        image = simulator.resources.load_image("ext_pin.png")
        SpriteRenderer.__init__(self, image)
        self.pin = Pin.create_pin(simulator, self, Vector2(20, 50))
        self.simulator = simulator

    def to_json(self):
        return Serializable.json_dumps(
            {
                'pos': self.position.to_array(),
                'uid': self.uid,
                'pin': self.pin.uid
            }
        )

    def on_remove(self):
        super(ExtPin, self).on_remove()
        self.simulator.remove_wires(self.pin)
        self.pin.on_remove()
        self.simulator.scene.unregister_object(self)