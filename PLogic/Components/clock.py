import time

from PLogic import SpriteRenderer, Pin, Vector2, LogicGate, InteractiveComponent, Serializable


class Clock(SpriteRenderer, LogicGate, InteractiveComponent, Serializable):
    def __init__(self, simulator):
        LogicGate.__init__(self)
        self.images = []
        self.images.append(simulator.resources.load_image("clock_0.png"))
        self.images.append(simulator.resources.load_image("clock_1.png"))
        self.images.append(simulator.resources.load_image("clock_2.png"))
        image = self.images[0]
        SpriteRenderer.__init__(self, image)
        self.pin = Pin.create_pin(simulator, self, Vector2(40, 110))
        self.timeStamp = 0
        self.freq_table = [50, 200, 500]
        self.mode = 0
        self.state = False
        simulator.tick_subscribe(self.tick)
        self.simulator = simulator

    def tick(self):
        ms = int(round(time.time() * 1000))
        delay = self.freq_table[self.mode]
        if (ms - self.timeStamp >= delay):
            self.timeStamp = ms
            self.state = not self.state
        self.pin.set_signal(self, 1 if self.state else 0)

    def interact(self):
        mode = self.mode + 1
        if mode > 2:
            mode = 0
        self.mode = mode
        self.image_original = self.images[mode]

    def to_json(self):
        return Serializable.json_dumps(
            {
                'pos': self.position.to_array(),
                'uid': self.uid,
                'pin': self.pin.uid,
                'mode': self.mode
            }
        )

    def on_remove(self):
        super(Clock, self).on_remove()
        self.simulator.tick_unsubscribe(self.tick)
        self.simulator.remove_wires(self.pin)
        self.pin.on_remove()
        self.simulator.scene.unregister_object(self)
