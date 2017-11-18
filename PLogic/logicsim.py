import sys

import pygame
from pygame import *

from PLogic import *
from PLogic.Components import GateAnd, GateOr, GateXor, GateNor, GateXnor, GateNand, GateNot, Switch, LightBulb, \
    LogicOne, ExtPin, Clock


class LogicSim():
    _drag = None
    _connection = None
    _connectionHelper = EmptyObject()

    _mouse_pos = Vector2.zero()
    _mouse_press_pos = Vector2.zero()
    _pan = False

    MODE = (800, 640)

    def init(self, assets, on_save, on_load):

        self.on_save = on_save
        self.on_load = on_load

        pygame.init()
        pygame.display.set_caption("PLS")

        self.resources = ResourceManager(assets)

        self.screen = pygame.display.set_mode(self.MODE)
        self.viewport = Viewport(Vector2(self.MODE[0], self.MODE[1]))
        self.scene = Scene()

        self.raycaster = Raycaster(self)

        self.tick_subscribers = []

    def tick_subscribe(self, func):
        self.tick_subscribers.append(func)

    def tick_unsubscribe(self, func):
        self.tick_subscribers.remove(func)

    def render(self):
        self.screen.fill(Color.Gray)

        for render_object in self.scene.scene_objects:
            render_object.render(self.viewport, self.screen)

        pygame.display.update()

    def begin_drag(self):
        hits = self.raycaster.raycast(self._mouse_pos, True)
        if hits is not None:
            for hit in hits:
                self._drag = hit

        if self._drag is None:
            self._pan = True

    def zoom(self, zoom):
        if not self.viewport.set_zoom(zoom):
            return
        sign = 1 if zoom > 0 else -1

    def get_pins(self, obj):
        pins = []
        for child in obj.children:
            if issubclass(type(child), Pin):
                pins.append(child)
        return pins

    def save_scene(self):
        serialized = []
        for obj in self.scene.scene_objects:
            if issubclass(type(obj), Serializable):
                data = obj.to_json()
                serialized.append({type(obj).__name__: data})
        return Serializable.json_dumps(serialized)

    def load_scene(self, data):
        objs = []
        objs.extend(self.scene.scene_objects)
        for obj in objs:
            if issubclass(type(obj), Serializable):
                self.remove_object(obj)

        deserialized = Serializable.json_loads(data)

        wires = []

        for gates in deserialized:
            for k in gates:
                t = None

                try:
                    t = getattr(sys.modules['PLogic.Components'], k)
                except:
                    t = getattr(sys.modules['PLogic'], k)

                data = Serializable.json_loads(gates[k])

                if t == Wire:
                    wires.append(data)
                    continue
                else:
                    ComponentFactory.create(self, t, data)

        for wire_data in wires:
            ComponentFactory.create(self, Wire, wire_data)

    def get_wires(self, pin):
        wires = []
        for obj in self.scene.scene_objects:
            if issubclass(type(obj), Wire):
                if pin is not None:
                    if obj.pin1 == pin or obj.pin2 == pin:
                        wires.append(obj)
                else:
                    wires.append(obj)
        return wires

    def remove_wires(self, *pins):
        for p in pins:
            wires = self.get_wires(p)
            for wire in wires:
                wire.on_remove()

    def remove_object(self, obj: SceneObject):
        if obj is not None:
            if issubclass(type(obj), Pin):
                self.remove_wires(obj)
                return

            obj.on_remove()

    def handle_keyboard_input(self, key):
        pos = self.viewport.screen_to_viewport_pos(self._mouse_pos)
        focused = self.raycaster.raycast(self._mouse_pos, False)
        if key == K_SPACE:
            if issubclass(type(focused), InteractiveComponent):
                focused.interact()

        if key == K_1:
            ComponentFactory.create(self, GateAnd, {'pos': pos.to_array()})
        if key == K_2:
            ComponentFactory.create(self, GateOr, {'pos': pos.to_array()})
        if key == K_3:
            ComponentFactory.create(self, GateXor, {'pos': pos.to_array()})
        if key == K_4:
            ComponentFactory.create(self, GateNor, {'pos': pos.to_array()})
        if key == K_5:
            ComponentFactory.create(self, GateXnor, {'pos': pos.to_array()})
        if key == K_6:
            ComponentFactory.create(self, GateNand, {'pos': pos.to_array()})
        if key == K_7:
            ComponentFactory.create(self, GateNot, {'pos': pos.to_array()})
        if key == K_8:
            ComponentFactory.create(self, Switch, {'pos': pos.to_array()})
        if key == K_9:
            ComponentFactory.create(self, LogicOne, {'pos': pos.to_array()})
        if key == K_0:
            ComponentFactory.create(self, LightBulb, {'pos': pos.to_array()})
        if key == K_w:
            ComponentFactory.create(self, ExtPin, {'pos': pos.to_array()})
        if key == K_q:
            ComponentFactory.create(self, Clock, {'pos': pos.to_array()})
        if key == K_x:
            self.remove_object(focused)
        if key == K_s:
            self.on_save(self)
        if key == K_l:
            self.on_load(self)

    def resolve_circuit(self):
        for func in self.tick_subscribers:
            func()

    def run(self):
        while 1:

            mpos = pygame.mouse.get_pos()
            self._mouse_pos = Vector2.from_array(mpos)

            for e in pygame.event.get():
                if e.type == QUIT:
                    raise SystemExit

                if e.type == KEYDOWN:
                    self.handle_keyboard_input(e.key)

                if e.type == pygame.MOUSEBUTTONDOWN:
                    if e.button == 4:
                        self.zoom(0.1)
                    elif e.button == 5:
                        self.zoom(-0.1)
                    elif e.button == 1:
                        self._mouse_press_pos = self._mouse_pos
                        self.begin_drag()
                elif e.type == pygame.MOUSEBUTTONUP:
                    if e.button == 1:
                        self._drag = None
                        self._pan = False
                        if self._connection is not None:
                            hits = self.raycaster.raycast(self._mouse_pos, True)
                            close_pin = None
                            if hits is not None:
                                for hit in hits:
                                    if issubclass(type(hit), Pin):
                                        close_pin = hit

                            if close_pin is not None and close_pin is not self._connection.pin1:
                                self._connection.close(close_pin)
                                # Check if wire already exists
                                count = 0
                                for wire in self.get_wires(None):
                                    if self._connection == wire:
                                        count += 1
                                if count > 1:
                                    self.scene.unregister_object(self._connection)
                            else:
                                self.scene.unregister_object(self._connection)

                            self._connection = None

            if self._drag is not None:
                vppos = self.viewport.screen_to_viewport_pos(self._mouse_pos)
                pos = vppos - self._drag.size / 2
                self._connectionHelper.position = vppos - self._connectionHelper.size / 2

                if self._drag.move_on_drag:
                    self._drag.position = pos
                else:
                    if self._connection is None:
                        self._connection = Wire(self)
                        self._connection.init(self._drag, self._connectionHelper)
                        self.scene.register_object(self._connection)
            elif self._pan:
                delta = self._mouse_press_pos - self._mouse_pos
                self._mouse_press_pos = self._mouse_pos
                self.viewport.pan(delta / self.viewport.zoom)

            self.resolve_circuit()
            self.render()
