#!/usr/bin/python3
""" Tests for database"""
import unittest
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models.user import User
from models.engine.db_storage import DBStorage
from models.base_model import BaseModel


class TestDBStorage(unittest.TestCase):
    """ Tests for DBStorage class"""
    
    @classmethod
    def setUpClass(cls):
        """ Set up for the test suite """
        
        cls.db_storage = DBStorage()
        cls.db_storage.reload()
        
    @classmethod
    def tearDownClass(cls):
        """ Tear down after all tests """
        cls.db_storage.close()
        
    def test_all_methods(self):
        """ Check if all methods are working correctly """
        
        users = self.db_storage.all(User)
        self.assertIsInstance(users, dict)
        
        states = self.db_storage.all(State)
        self.assertIsInstance(states, dict)
        
        citites = self.db_storage.all(City)
        self.assertIsInstance(citites, dict)
        
        places = self.db_storage.all(Place)
        self.assertIsInstance(places, dict)
        
        amenities = self.db_storage.all(Amenity)
        self.assertIsInstance(amenities, dict)
        reviews = self.db_storage.all(Review)
        self.assertIsInstance(reviews, dict)
        
    
if __name__ == "__main__":
    unittest.main()
