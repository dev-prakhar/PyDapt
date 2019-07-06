from pydapt.constants import INVALID_ARGS_ERROR
from pydapt.exceptions import InvalidArgumentException


class PyFlex(object):
    """
    PyFlex converts a dictionary to object
    """

    def __init__(self, dictionary=None, **kwargs):
        dictionary = dictionary or {}
        if isinstance(dictionary, dict):
            attributes_dict = {**dictionary, **kwargs}
            self.set_attributes(attributes_dict)
        else:
            raise InvalidArgumentException(INVALID_ARGS_ERROR)

    def set_attributes(self, attributes_dict):
        """
        This method set the attributes present in kwargs to the self
        """
        for key, value in attributes_dict.items():
            setattr(self, key, PyFlex(value)) if isinstance(value, dict) else setattr(self, key, value)


    def drop(self, key):
        """
        Delete given attribute from object
        """
        return self.__dict__.pop(key, None)

    def __str__(self):
        """
        Representation of object
        """
        return str(self.__dict_repr())

    def __dict_repr(self):
        """
        Returns the dictionary representation of the object
        """
        return {
            key: value.__dict_repr() if isinstance(value, PyFlex) else value
            for key, value in self.__dict__.items()
        }
