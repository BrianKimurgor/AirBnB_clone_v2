#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""
    id = Column(String(60), primary_key=True, nullable=False, unique=True)
    created_at = Column(DateTime, default=datetime.utcnow(), nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow(), nullable=False,
                        onupdate=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel.
        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        if 'id' not in kwargs:
            self.id = str(uuid.uuid4())
        if 'created_at' not in kwargs:
            self.created_at = datetime.utcnow()
        if 'updated_at' not in kwargs:
            self.updated_at = datetime.utcnow()

        for key, value in kwargs.items():
            if key != '__class__':
                setattr(self, key, value)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        self.updated_at = datetime.utcnow()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dict_obj = self.__dict__.copy()
        dict_obj.pop('_sa_instance_state', None)

        dict_obj["__class__"] = self.__class__.__name__
        if isinstance(dict_obj.get("created_at"), datetime):
            dict_obj["created_at"] = dict_obj["created_at"].isoformat()

        if 'updated_at' in dict_obj and isinstance(dict_obj["updated_at"], datetime):
            dict_obj["updated_at"] = dict_obj["updated_at"].isoformat()

        return dict_obj

    def delete(self):
        """Deletes the current instance from the storage (models.storage)"""
        storage.delete(self)
