from PLogic import SpriteRenderer, Pin, Vector2, LogicGate, Serializable
from PLogic.interactive_component import InteractiveComponent


class Switch(SpriteRenderer, InteractiveComponent, LogicGate, Serializable):
    image_off = None
    image_on = None

    def __init__(self, simulator):
        LogicGate.__init__(self)
        self.image_off = simulator.resources.load_image("switch_off.png")
        self.image_on = simulator.resources.load_image("switch_on.png")
        SpriteRenderer.__init__(self, self.image_off)
        self.pin = Pin.create_pin(simulator, self, Vector2(60, 140))
        self.state = False
        simulator.tick_subscribe(self.tick)
        self.simulator = simulator

    def tick(self):
        self.pin.set_signal(self, 1 if self.state else 0)

    def refresh_state(self, state):
        self.state = state
        self.pin.source = state
        self.image_original = self.image_on if self.state else self.image_off

    def interact(self):
        self.refresh_state(not self.state)

    def to_json(self):
        return Serializable.json_dumps(
            {
                'pos': self.position.to_array(),
                'uid': self.uid,
                'pin': self.pin.uid,
                'state': 1 if self.state else 0
            }
        )

    def on_remove(self):
        super(Switch, self).on_remove()
        self.simulator.tick_unsubscribe(self.tick)
        self.simulator.remove_wires(self.pin)
        self.pin.on_remove()
        self.simulator.scene.unregister_object(self)