from src.types.typing import *
from json import loads,dumps


class JsonObject(DataObject):
    def parse(self,data:str):
        self.__dict__=loads(data)
    def dump(self):
        return dumps(self.__dict__)
