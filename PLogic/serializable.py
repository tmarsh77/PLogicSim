from abc import ABCMeta, abstractmethod, abstractstaticmethod
import json


class Serializable(metaclass=ABCMeta):
    json_dumps = json.dumps
    json_loads = json.loads

    @abstractmethod
    def to_json(self):
        pass
