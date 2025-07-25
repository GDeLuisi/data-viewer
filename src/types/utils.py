from typing import Type,Any
def check_type(t:Type,object:Any,strict:bool=True)->bool:
    """Checks object's type

    Args:
        t (Type): expected type
        object (Any): object to check
        strict (bool, optional): whether the function fails on wrong type. Defaults to True.

    Raises:
        TypeError:

    Returns:
        bool: returns true if the object's type is the one expected
    """
    is_correct=isinstance(object,t)
    if strict and not is_correct:
        raise TypeError(f"Object {type(object)} is not of type {t}")
    elif not is_correct:
        return False
    return True
