from pytest import mark,param
from src.types.utils import *
@mark.parametrize("type,object,strict,expected",[
    param(str,"test",True,True),
    param(str,12,True,False,marks=mark.xfail),
    param(int,"test",True,False,marks=mark.xfail),
    param(str,"test",False,True),
    param(int,"test",False,False),
    param(str,13,False,False),
])
def test_type_checker(type,object,strict,expected):
    assert check_type(type,object,strict)==expected