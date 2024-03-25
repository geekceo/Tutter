from pydantic import constr, BaseModel, validator
from typing import Final
from types import FunctionType

class Header(dict):


    def __repr__(self):

        return self.__class__.__name__

#def validator(func): ...

def tutstr(
        max_length: int
        ):
    
    def validate(obj: str):

        if len(obj) > max_length:

            raise ValueError('Value greater then max_length')
        


    