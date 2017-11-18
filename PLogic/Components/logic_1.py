from PLogic import SpriteRenderer, Pin, Vector2, LogicGate, Serializable


class LogicOne(SpriteRenderer, LogicGate, Serializable):
    def __init__(self, simulator):
        LogicGate.__init__(self)
        image = simulator.resources.load_image("logic1.png")
        SpriteRenderer.__init__(self, image)
        self.pin = Pin.create_pin(simulator, self, Vector2(40, 110))
        self.pin.source = True
        simulator.tick_subscribe(self.tick)
        self.simulator = simulator

    def tick(self):
        self.pin.set_signal(self, 1)

    def to_json(self):
        return Serializable.json_dumps(
            {
                'pos': self.position.to_array(),
                'uid': self.uid,
                'pin': self.pin.uid
            }
        )

    def on_remove(self):
        super(LogicOne, self).on_remove()
        self.simulator.remove_wires(self.pin)
        self.pin.on_remove()
        self.simulator.scene.unregister_object(self)