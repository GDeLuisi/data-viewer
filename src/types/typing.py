from typing import Any
from .utils import check_type
from exceptions import *

class Field():
    def __init__(self,name:str,value:Any):
        self.name=name
        self.value=value
    def __eq__(self, value):
        check_type(self.__class__,value)
        eq=(value.name==self.name and self.value==self.value)
        return eq
    def __str__(self):
        return f"Type: {self.__class__.__name__} name: {self.name} value: {self.value}"
    
class IntField(Field):
    pass
class StringField(Field):
    pass
class BooleanField(Field):
    pass
class ObjectField(Field):
    pass
class ListField(Field):
    pass


class DataObject():
    def __init__(self,data:str):
        self.parse(data)

    def parse(self,data:str):
        raise NotImplementedError()
    
    def get_fields(self)->set[str]:
        return set(self.__dict__.keys())
    
    def get(self,field:str)->Field:
        item=self.__dict__.get(field,None)
        if item == None:
            raise FieldNotFound(f"Field {field} not found")
        return item

    def set(self,field:str,value:Field):
        check_type(Field,field)
        self.__dict__[field]=value

    def dump(self):
        raise NotImplementedError()