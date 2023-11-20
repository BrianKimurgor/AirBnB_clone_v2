#!/usr/bin/python3
"""
""This module defines a base class for all models in our hbnb clone""
import uuid
from datetime import datetime


class BaseModel:
    ""A base class for all hbnb models""
    def __init__(self, *args, **kwargs):
        ""Initialize a new BaseModel.
        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        ""
        from models import storage

        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime
                            (value, "%Y-%m-%dT%H:%M:%S.%f"))
                if key != '__class__':
                    setattr(self, key, value)
                if 'id' not in kwargs:
                    self.id = str(uuid.uuid4())
                if 'created_at' not in kwargs:
                    self.created_at = datetime.now()
                if 'created_at' in kwargs and 'updated_at' not in kwargs:
                    self.updated_at = self.created_at
                else:
                    self.updated_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()

    def __str__(self):
        ""Returns a string representation of the instance""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        ""Updates updated_at with current time when instance is changed""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        ""Convert instance into dict format""

        dict_obj = self.__dict__.copy()
        dict_obj["__class__"] = self.__class__.__name__
        if isinstance(dict_obj["created_at"], datetime):
            dict_obj["created_at"] = dict_obj["created_at"].isoformat()
        if isinstance(dict_obj["updated_at"], datetime):
            dict_obj["updated_at"] = dict_obj["updated_at"].isoformat()

        return dict_obj
"""

#!/usr/bin/python3
"""
This module defines a base class for all models in our hbnb clone
"""
import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import models

Base = declarative_base()


class BaseModel:
    """
    A base class for all hbnb models
    """
    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """
        Initialize a new BaseModel.
        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        if not kwargs.get('id'):
            self.id = str(uuid.uuid4())
        if not kwargs.get('created_at'):
            self.created_at = datetime.utcnow()
        if not kwargs.get('updated_at'):
            self.updated_at = datetime.utcnow()

        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        """
        Returns a string representation of the instance
        """
        cls = self.__class__.__name__
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """
        Updates updated_at with the current time when the instance is changed
        """
        from models import storage
        self.updated_at = datetime.utcnow()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """
        Convert instance into dict format
        """
        dict_obj = self.__dict__.copy()
        dict_obj.pop('_sa_instance_state', None)

        for key, value in dict_obj.items():
            if isinstance(value, datetime):
                dict_obj[key] = value.isoformat()

        dict_obj["__class__"] = self.__class__.__name__

        return dict_obj

    def delete(self):
        """
        Delete the current instance from the storage (models.storage)
        """
        from models import storage
        storage.delete(self)
