#!/usr/bin/python3
"""defining a base class, which will be a parent of all
subsequent classes"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """this class define the basic characteristics of all child classes"""

    def __init__(self, *args, **kwargs):
        """initialize public mwthods and and attribute"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            self.__dict__ = kwargs
            date_format = "%Y-%m-%dT%H:%M:%S.%f"

            self.created_at = datetime.strptime(self.created_at, date_format)
            self.updated_at = datetime.strptime(self.updated_at, date_format)

    def __str__(self):
        """return a string representation of objects"""
        strr = "[{}] ({}) ({})".format(
                self.__class__.__name__, self.id, self.__dict__)
        return (strr)

    """pubic instances"""
    def save(self):
        """updates the pubic instance attribute 'update_at' with the
        current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a key value pairs of all instances of the
        dictionary __dict__"""
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return (new_dict)
