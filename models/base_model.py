#!/usr/bin/python3
"""This is a basemodel script."""

from uuid import uuid4
import datetime
from models import storage


class BaseModel:

    """Base class where all other classes will inherit from."""

    def __init__(self, *args, **kwargs):
        """Initialize instance attributes.

        Args:
        *args: list or arguments.
        **kwargs: dictionary of key-value args.
        """

        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.datetime.strptime
                    (kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.datetime.strptime
                    (kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]

        else:
            self.id = str(uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            storage.new(self)

    def __str__(self):
        """Return string representation of an object."""

        return "[{}] ({}) {}".\
            format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """Update the public instance attribute updated_at"""

        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        """Returns a dictionary rep. of all keys/values of __dict__"""

        obj_dict = self.__dict__.copy()
        if isinstance(obj_dict["created_at"], datetime.datetime):
            obj_dict["created_at"] = obj_dict["created_at"].isoformat()
        if isinstance(obj_dict["updated_at"], datetime.datetime):
            obj_dict["updated_at"] = obj_dict["updated_at"].isoformat()
        #obj_dict.pop("_sa_instance_state", None)    
        obj_dict["__class__"] = type(self).__name__
        '''obj_dict["created_at"] = obj_dict["created_at"].isoformat()
        obj_dict["updated_at"] = obj_dict["updated_at"].isoformat()'''
        return obj_dict
