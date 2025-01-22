from collections import abc
import keyword

class FrozenJSON:
    #1
    def __init__(self, mapping:abc.Mapping):
        self.__data = {}
        for key, value in mapping.items():
            if keyword.iskeyword(key):
                key += '_'
            self.__data[key] = value

    
    #2
    def __getattr__(self, name):
    #3 
        try:
            return getattr(self.__data, name)
    #4
        except AttributeError:
            return FrozenJSON.build(self.__data[name])

    #5
    def __dir__(self): 
        return self.__data.keys()
    

    @classmethod
    def build(cls, obj):
        #6
        if isinstance(obj, abc.Mapping):
            return cls(obj)

        #7
        elif isinstance(obj, abc.MutableSequence):
            return [cls.build(item) for item in obj]
        #8
        else:
            return obj
        

python_dict = {
    'class': {
        'time': 4.4,
        'code': 1324
    },
    'venue': ['tehran', 'marzdaran', '22shahrivar blvd']
}
obj = FrozenJSON(python_dict)
print(obj.class_.code)