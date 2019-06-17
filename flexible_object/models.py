from flexible_object.constants import INVALID_ARGS_ERROR
from flexible_object.exceptions import InvalidArgumentException


class FlexibleObject(object):
    """
    Flexible Object converts a dictionary to object
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
            if isinstance(value, dict):
                flexible_object = FlexibleObject(value)
                setattr(self, key, flexible_object)
            else:
                setattr(self, key, value)

    def drop(self, key):
        """
        Delete given attribute from object
        :param key:
        """
        self.__dict__.pop(key)

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
            key: value.__dict_repr() if isinstance(value, FlexibleObject) else value
            for key, value in self.__dict__.items()
        }
