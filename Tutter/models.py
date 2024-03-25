import json
from perks import Header, tutstr
from typing import Union, get_args


class BaseModel(object):

    '''
        From this model extends other models. This is basement of Tutter logic;

        If frozen is True it means that you cannot add new attributes to those that have already been created in the class;

        If convert is True then the data types you are looking for do not matter
    '''

    __slots__ = ['__primary_annotations']

    __builtin_types: dict = {
        'int': int,
        'str': str,
        'bool': bool,
        'float': float,
        'list': list,
        'dict': dict,
        'tuple': tuple,
        'set': set,
        'bytes': bytes
    }

    def __fromJSON(self, filename) -> None:

        j = json.loads(open('wg_configs.json', 'r').read())

        for key, value in j.items():

            if type(value) == dict:
                value = BaseModel(**value)

            setattr(self, key, value)

    def __parse(self, data: tuple) -> None:

        '''
            TODO: Types handler
        '''

        filename, separator = data

        file_data: str

        with open(file=filename, mode='r') as f:

            file_data = f.read()

        file_key_value: dict = dict(tuple(data.split(sep=separator)) for data in [line for line in file_data.split(sep='\n')] if separator in data)

        for key, value in file_key_value.items():

            if key in self.__annotations__.keys():

                setattr(self, key, value)

            else:

                raise ValueError(f'Field \'{key}\' from parsed file doesn\'t exists in model')

    def toJSONString(self, indent: int = 4) -> str:

        '''
            indent - count tabs; 4 by default
        '''


        header = [key for key, k_type in self.__primary_annotations.items() if 'Header' in str(k_type)]

        json_dict = dict()

        if header:

            header = ''.join(header)

            json_dict[header] = dict()

            json_items = {k:v for k, v in self.__dict__.items() if k != header}

            for key, value in json_items.items():

                json_dict[header][key] = value

        else:

            json_items = {k:v for k, v in self.__dict__.items()}

            for key, value in json_items.items():

                json_dict[key] = value

        return json.dumps(json_dict, indent=4)


    def __annotations_validation(self):

        a = [str(annotation) for key, annotation in self.__primary_annotations.items()]
        print(a)

        if 'tutstr' in [str(annotation) for key, annotation in self.__primary_annotations.items()]:

            print('OK')

    def __init__(
            self,
            frozen: bool = False,
            convert: bool = False,
            file: bool | tuple = False,
            **fields
            ):

        self.__primary_annotations = {}

        print(self.__annotations__)
         
        for field, f_type in self.__annotations__.items():
             
            self.__primary_annotations[field] = f_type


        for key in fields.keys():

            if file:

                raise AttributeError(f'Arguments \'file\' and \'**fields\' is incompatible')

            if key not in self.__annotations__.keys() and frozen:

                raise ValueError(f'Field \'{key}\' doesn\'t exists in frozen model')    
                
            else:

                if convert == True:

                    setattr(self, key, fields[key])

                else:

                    if isinstance(fields[key], self.__annotations__[key]):

                        setattr(self, key, fields[key])

                    else:

                        raise TypeError(
                            f'Argument \'{key}\' has type {type(fields[key])} (value = {fields[key]}), but field \'{key}\' has type {self.__annotations__[key]}')


        if file:

            self.__parse(data=file)

        #print(dir(self))
        self.__annotations_validation()

    def __repr__(self):

        key_value_str = ', '.join([f'{key}={value}' for key, value in self.__dict__.items()])

        return f'{self.__class__.__name__}({key_value_str})'
    
        
    
#class TestModel(BaseModel):
#
#    Address: str
#    DNS: str
#    PrivateKey: str
#    MTU: int | str
#
#    PublicKey: str
#    PresharedKey: str
#    AllowedIPs: str
#    Endpoint: str
#    PersistentKeepalive: int | str

class TestModel(BaseModel):

    a: int


test = TestModel(frozen=True, a=1)
#print(test)
#print(test.a)

