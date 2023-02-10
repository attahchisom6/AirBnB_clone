#!usr/bin/python3
"""This module will create a storage system or database capable
of storing our data. It also serves as a source to provide
information for the user
"""
import os
import json
from models.user import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """This class serializes instances to a JSON file and deserializes
    JSON file to instances:
    """

    """private attributes

    Args:
        @__file_path: string - path to the JSON file
        @__objects: empty dictionary but will store all
        objects by <class name>.id
    """
    __file_path = "file.json"
    __objects = {}

    """public methods"""
    def all(self):
        return (self.__objects)

    def new(self, obj):
        """set's in __objects the obj with key <obj class name>.id
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """serializes objects to the json file
        """
        dictt = {}
        for key, value in self.__objects.items():
            dictt[key] = value.to_dict()

        with open(self.__file_path, mode="w+", encoding="utf-8") as f:
            json.dump(dictt, f)

    def reload(self):
        """deserializes json file to the inetances of the
        dictionary, '__objects'
        """
        if os.path.exists(self.__file_path) is False:
            return
        dictt = {}
        try:
            with open(self.__file_path, mode="r", encoding="utf-8") as f:
                dictt = json.load(f)
                for key, v in dictt.items():
                    value = eval("{}(**v)".format(v['__class__']))
                    self.__objects[key] = value
        except IOError:
            pass

    def data_classes(self):
        """returns a dictionary representation of our database
        classes"""

        data_classes = {
                "BaseModel": BaseModel,
                "User": User,
                "State": State,
                "City": City,
                "Place": Place,
                "Amenity": Amenity,
                "Review": Review
                }

        return (data_classes)
