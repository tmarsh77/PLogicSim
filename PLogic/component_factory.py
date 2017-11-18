from PLogic.Components import GateAnd, LightBulb, Switch, ExtPin, GateOr, GateNand, GateXor, GateNor, LogicOne, Clock
from PLogic.Components.gate_not import GateNot
from PLogic.Components.gate_xnor import GateXnor

from PLogic import Vector2, Wire


class ComponentFactory:
    @staticmethod
    def create(simulator, type, data):

        # data[gate-specific data]

        if type == Wire:
            wire = Wire(simulator)
            pin1 = simulator.scene.find_by_uid(data['pin1'])
            pin2 = simulator.scene.find_by_uid(data['pin2'])
            if pin1 is not None and pin2 is not None:
                wire.init(pin1, pin2)
                wire.close(pin2)
                simulator.scene.register_object(wire)

        if type == GateAnd:
            pos = Vector2.from_array(data['pos'])
            gate_and = GateAnd(simulator)

            if 'uid' in data:
                gate_and.uid = data['uid']

            if 'p_i1' in data:
                gate_and.i1.uid = data['p_i1']
            if 'p_i2' in data:
                gate_and.i2.uid = data['p_i2']
            if 'p_q' in data:
                gate_and.q.uid = data['p_q']

            gate_and.position = pos
            simulator.scene.register_object(gate_and)
            return gate_and

        if type == ExtPin:
            pos = Vector2.from_array(data['pos'])
            ext_pin = ExtPin(simulator)

            if 'uid' in data:
                ext_pin.uid = data['uid']

            if 'pin' in data:
                ext_pin.pin.uid = data['pin']

            ext_pin.position = pos
            simulator.scene.register_object(ext_pin)
            return ext_pin

        if type == GateNand:
            pos = Vector2.from_array(data['pos'])
            gate_nand = GateNand(simulator)

            if 'uid' in data:
                gate_nand.uid = data['uid']

            if 'p_i1' in data:
                gate_nand.i1.uid = data['p_i1']
            if 'p_i2' in data:
                gate_nand.i2.uid = data['p_i2']
            if 'p_q' in data:
                gate_nand.q.uid = data['p_q']

            gate_nand.position = pos
            simulator.scene.register_object(gate_nand)
            return gate_nand

        if type == GateOr:
            pos = Vector2.from_array(data['pos'])
            gate_or = GateOr(simulator)

            if 'uid' in data:
                gate_or.uid = data['uid']

            if 'p_i1' in data:
                gate_or.i1.uid = data['p_i1']
            if 'p_i2' in data:
                gate_or.i2.uid = data['p_i2']
            if 'p_q' in data:
                gate_or.q.uid = data['p_q']

            gate_or.position = pos
            simulator.scene.register_object(gate_or)
            return gate_or

        if type == GateXor:
            pos = Vector2.from_array(data['pos'])
            gate_xor = GateXor(simulator)

            if 'uid' in data:
                gate_xor.uid = data['uid']

            if 'p_i1' in data:
                gate_xor.i1.uid = data['p_i1']
            if 'p_i2' in data:
                gate_xor.i2.uid = data['p_i2']
            if 'p_q' in data:
                gate_xor.q.uid = data['p_q']

            gate_xor.position = pos
            simulator.scene.register_object(gate_xor)
            return gate_xor

        if type == GateNor:
            pos = Vector2.from_array(data['pos'])
            gate_nor = GateNor(simulator)

            if 'uid' in data:
                gate_nor.uid = data['uid']

            if 'p_i1' in data:
                gate_nor.i1.uid = data['p_i1']
            if 'p_i2' in data:
                gate_nor.i2.uid = data['p_i2']
            if 'p_q' in data:
                gate_nor.q.uid = data['p_q']

            gate_nor.position = pos
            simulator.scene.register_object(gate_nor)
            return gate_nor

        if type == GateXnor:
            pos = Vector2.from_array(data['pos'])
            gate_xnor = GateXnor(simulator)

            if 'uid' in data:
                gate_xnor.uid = data['uid']

            if 'p_i1' in data:
                gate_xnor.i1.uid = data['p_i1']
            if 'p_i2' in data:
                gate_xnor.i2.uid = data['p_i2']
            if 'p_q' in data:
                gate_xnor.q.uid = data['p_q']

            gate_xnor.position = pos
            simulator.scene.register_object(gate_xnor)
            return gate_xnor

        if type == GateNot:
            pos = Vector2.from_array(data['pos'])
            gate_not = GateNot(simulator)

            if 'uid' in data:
                gate_not.uid = data['uid']

            if 'p_i1' in data:
                gate_not.i1.uid = data['p_i1']
            if 'p_q' in data:
                gate_not.q.uid = data['p_q']

            gate_not.position = pos
            simulator.scene.register_object(gate_not)
            return gate_not

        if type == Switch:
            pos = Vector2.from_array(data['pos'])
            switch = Switch(simulator)

            if 'uid' in data:
                switch.uid = data['uid']

            if 'pin' in data:
                switch.pin.uid = data['pin']

            if 'state' in data:
                switch.refresh_state(True if data['state'] == 1 else False)

            switch.position = pos
            simulator.scene.register_object(switch)
            return switch

        if type == LightBulb:
            pos = Vector2.from_array(data['pos'])
            light = LightBulb(simulator)

            if 'uid' in data:
                light.uid = data['uid']

            if 'pin' in data:
                light.pin.uid = data['pin']

            light.position = pos
            simulator.scene.register_object(light)
            return light

        if type == LogicOne:
            pos = Vector2.from_array(data['pos'])
            logic0 = LogicOne(simulator)

            if 'uid' in data:
                logic0.uid = data['uid']

            if 'pin' in data:
                logic0.pin.uid = data['pin']

            logic0.position = pos
            simulator.scene.register_object(logic0)
            return logic0

        if type == Clock:
            pos = Vector2.from_array(data['pos'])
            clock = Clock(simulator)

            if 'uid' in data:
                clock.uid = data['uid']

            if 'pin' in data:
                clock.pin.uid = data['pin']

            if 'mode' in data:
                clock.mode = data['mode']

            clock.position = pos
            simulator.scene.register_object(clock)
            return clock
