#!/usr/bin/python3
"""
    Creating a BaseModel that defines all common
    attributes/methods for other classes
"""
import uuid
from datetime import datetime


class BaseModel:
    """Creating a BaseModel Class"""
    def __init__(self, *args, **kwargs):
        if kwargs:
            for k, v in kwargs.items():
                if k in ['created_at', 'updated_at']:
                    v = datetime.strptime(v, '%Y-%m-%dT%H:%M:%S.%f')
                if k is not '__class__':
                    setattr(self, k, v)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.today()
            self.updated_at = datetime.today()

    def __str__(self):
        """a string method for this class"""
        return "[{}] ({}) {}".format(
                __class__.__name__, self.id, self.__dict__)

    def save(self):
        """allows to save attributes"""
        self.updated_at = datetime.today()

    def to_dict(self):
        """creates a dictionary representation of instances"""
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = __class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict
