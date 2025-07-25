from typing import Any
from src.types.typing import *
import builtins as bt

def infer_field(field_name:str,data:Any):
    match type(data):
        case bt.int:
            return IntField(field_name,data)
        case bt.str:
            return StringField(field_name,data)
        case bt.bool:
            return BooleanField(field_name,data)
        case bt.list:
            #recursive solution
            return ListField(field_name,data)
        case bt.dict:
            #recursive solution
            return ObjectField(field_name,data)
