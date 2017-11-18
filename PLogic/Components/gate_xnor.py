from PLogic import SpriteRenderer, Pin, Vector2, LogicGate, Serializable


class GateXnor(SpriteRenderer, LogicGate, Serializable):
    def __init__(self, simulator):
        LogicGate.__init__(self)
        image = simulator.resources.load_image("xnor.png")
        SpriteRenderer.__init__(self, image)

        self.i1 = Pin.create_pin(simulator, self, Vector2(-27, 14))
        self.i2 = Pin.create_pin(simulator, self, Vector2(-27, 70))
        self.q = Pin.create_pin(simulator, self, Vector2(250, 42))
        self.i1.on_value_changed = self.resolve
        self.i2.on_value_changed = self.resolve
        self.simulator = simulator

    def resolve(self):
        self.q.set_signal(self, 1 if (self.i1.signal == self.i2.signal) else 0)

    def to_json(self):
        return Serializable.json_dumps(
            {
                'pos': self.position.to_array(),
                'uid': self.uid,
                'p_i1': self.i1.uid,
                'p_i2': self.i2.uid,
                'p_q': self.q.uid
            }
        )

    def on_remove(self):
        super(GateXnor, self).on_remove()
        self.simulator.remove_wires(self.i1, self.i2, self.q)
        self.i1.on_remove()
        self.i2.on_remove()
        self.q.on_remove()
        self.simulator.scene.unregister_object(self)