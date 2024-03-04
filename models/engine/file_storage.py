#!/usr/bin/python3
"""FileStorage class module"""

import datetime
import json
import os
'''from models.base_model import BaseModel
from models.state import State
from models.amenity import Amenity
from models.city import City
from models.review import Review
from models.place import Place
from models.user import User'''


class FileStorage:
    """Class to handle serialization and deserialisation of
    instances to and fro JSON file.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(type(obj.__class__.__name__), obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        with open(FileStorage.__file_path, "w", encoding="utf-8") as files:
            docm = {ky: vl.to_dict()
                    for ky, vl in FileStorage.__objects.items()}
            json.dump(docm, files, default=self.custom_json_serializer)

    def custom_json_serializer(self, obj):
        """Custom JSON serializer for handling non-serializable objects."""
        if isinstance(obj, (datetime.datetime)):
            return obj.isoformat()
        return None

    def classes(self):
        """Returns a dict of valid classes and their references"""
        from models.base_model import BaseModel
        from models.state import State
        from models.amenity import Amenity
        from models.city import City
        from models.review import Review
        from models.place import Place
        from models.user import User

        return {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review,
            }

    def reload(self):
        """Module to reload the stored objects."""
        if not os.path.isfile(FileStorage.__file_path):
            return
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as files:
                new_dict = json.load(files)
                new_dict = {ky: self.classes()[vl["__class__"]](**vl)
                            for ky, vl in new_dict.items()
                            if vl.get("__class__") in self.classes()}
                FileStorage.__objects = new_dict
        except Exception as e:
            pass

    def attributes(self):
        """Returns the attrs. and their types for classname."""
        attributes = {
            "BaseModel":
                     {"id": str,
                      "created_at": datetime.datetime,
                      "updated_at": datetime.datetime},
            "User":
                     {"email": str,
                      "password": str,
                      "first_name": str,
                      "last_name": str},
            "State":
                     {"name": str},
            "City":
                     {"state_id": str,
                      "name": str},
            "Amenity":
                     {"name": str},
            "Place":
                     {"city_id": str,
                      "user_id": str,
                      "name": str,
                      "description": str,
                      "number_rooms": int,
                      "number_bathrooms": int,
                      "max_guest": int,
                      "price_by_night": int,
                      "latitude": float,
                      "longitude": float,
                      "amenity_ids": list},
            "Review":
            {"place_id": str,
                         "user_id": str,
                         "text": str}
        }
        return attributes
