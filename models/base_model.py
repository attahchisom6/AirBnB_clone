#!/usr/bin/python3
"""Defining the base class for every model class"""
import uuid
from datetime import datetime
from models import storage

class BaseModel:
    """This class will serve as database or backened for our
    frontend files"""

    def __init__(self, *args, **kwargs):
        """initializing public attributes"""
        if not kwargs:
            id = str(uuid.uuid4())

            created_at = datetime.now()

            updated_at = created_at
            storage.new(self)
        else:
            self.__dict__ = kwargs
            date_format = "%Y-%m-%dT%H:%M:%S.%f"

            self.created_at = datetime.strptime(self.created_at, date_format)
            self.updated_at = datetime.strptime(self.updated_at, date_format)

    def __str__(self):
        """return a string representation of instance attributes"""
        strr = "[{}] ({}) {}".format(self.__class__.__name__,
                                         self.id, self.__dict__)
            return (strr)

    """public instances"""
    def save(self):
        """update the public instance attrubute updated_at
        with current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """return all the key, value pairs of instanxes of the
        dictionary __dict__"""
        database_dict = ___dictionary.copy()
        data_base['__class__'] = self.__class__.__name
