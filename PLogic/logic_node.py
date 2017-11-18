class LogicNode():
    def __init__(self):
        self._connected = []
        self._signal = 0
        self.on_value_changed = None
        self.source = False

    def connect(self, node: 'LogicNode'):
        self._connected.append(node)

    def disconnect(self, node: 'LogicNode'):
        if node in self._connected:
            self._connected.remove(node)

    @property
    def signal(self):
        return self._signal

    def set_signal(self, sender, value, recursive = True):
        self._signal = value
        if recursive:
            try:
                for c in self._connected:
                    if c != sender and c.signal != value:
                        c.set_signal(self, value)
            except RuntimeError:
                pass
        if self.on_value_changed is not None:
            self.on_value_changed()
