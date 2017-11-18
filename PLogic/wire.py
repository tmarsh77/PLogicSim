from pygame import draw

from PLogic import RenderObject, Math, Vector2, Color, Pin, Serializable


class Wire(RenderObject, Serializable):
    pin1: Pin = None
    pin2: Pin = None
    closed = False

    def __init__(self, simulator):
        super().__init__()
        self.simulator = simulator

    def init(self, pin1: Pin, pin2: Pin):
        self.pin1 = pin1
        self.pin2 = pin2

    def close(self, pin):
        self.pin2 = pin

        self.pin1.connect(self.pin2)
        self.pin2.connect(self.pin1)

        self.closed = True

    def on_remove(self):
        self.pin1.disconnect(self.pin2)
        self.pin2.disconnect(self.pin1)
        self.simulator.scene.unregister_object(self)

    @property
    def rect(self):
        return None

    def to_json(self):
        return Serializable.json_dumps({'pin1': self.pin1.uid, 'pin2': self.pin2.uid})

    def __eq__(self, other):
        if isinstance(self, other.__class__):
            if (other.pin1 == self.pin1 and other.pin2 == self.pin2) or \
                        (other.pin2 == self.pin1 and other.pin1 == self.pin2):
                return True
        return False

    def render(self, viewport, renderer):
        vpos0 = self.pin1.position + self.pin1.size * 0.5
        vpos1 = self.pin2.position + self.pin2.size * 0.5

        # h1 = (vpos1 - vpos0).normalized()
        # h2 = (vpos0 - vpos1).normalized()

        t = 0

        points = []

        if False and Vector2.distance(vpos0, vpos1) > 200:
            # curve
            for t in range(0, 21):
                p = Math.get_cubic_bezier_point(vpos0, vpos0, vpos1, vpos1, t / 20)
                points.append(p)
        else:
            # straight line
            points.append(vpos0)
            points.append(vpos1)

        c = len(points)
        for i in range(0, c):
            if i + 1 >= c:
                break
            p1 = points[i]
            p2 = points[i + 1]
            color = Color.White
            if self.closed:
                color = Color.Green if self.pin1.signal == 1 or self.pin2.signal == 1 else Color.White
            draw.line(renderer, color, viewport.viewport_to_screen_pos(p1).to_array(),
                      viewport.viewport_to_screen_pos(p2).to_array(), 3)
