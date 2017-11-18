from PLogic import SpriteRenderer, Pin, Vector2, LogicGate, Serializable


class GateNot(SpriteRenderer, LogicGate, Serializable):
    def __init__(self, simulator):
        LogicGate.__init__(self)
        image = simulator.resources.load_image("not.png")
        SpriteRenderer.__init__(self, image)

        self.i1 = Pin.create_pin(simulator, self, Vector2(-25, 35))
        self.q = Pin.create_pin(simulator, self, Vector2(175, 35))
        self.i1.on_value_changed = self.resolve
        self.simulator =simulator

    def resolve(self):
        self.q.set_signal(self, 1 if self.i1.signal == 0 else 0)

    def to_json(self):
        return Serializable.json_dumps(
            {
                'pos': self.position.to_array(),
                'uid': self.uid,
                'p_i1': self.i1.uid,
                'p_q': self.q.uid
            }
        )

    def on_remove(self):
        super(GateNot, self).on_remove()
        self.simulator.remove_wires(self.i1)
        self.i1.on_remove()
        self.q.on_remove()
        self.simulator.scene.unregister_object(self)