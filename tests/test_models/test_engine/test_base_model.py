#!/usr/bin/python3

from models.base_model import BaseModel
import unittest
import datetime
from uuid import UUID
import json
import os

class TestBaseModel(unittest.TestCase):
        """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """
        Set up a fresh instance of BaseModel for each test.
        """
        self.test_instance = BaseModel()

    def test_has_attributes(self):
        """
        Test if the BaseModel instance has the expected attributes.
        """
        self.assertTrue(hasattr(self.test_instance, 'id'))
        self.assertTrue(hasattr(self.test_instance, 'created_at'))
        self.assertTrue(hasattr(self.test_instance, 'updated_at'))

    def test_id_is_string(self):
        """
        Test if the 'id' attribute is of string type.
        """
        self.assertIsInstance(self.test_instance.id, str)

    def test_id_is_valid_uuid(self):
        """
        Test if the 'id' attribute is a valid UUID.
        """
        self.assertTrue(UUID(self.test_instance.id))

    def test_created_at_is_datetime(self):
        """
        Test if the 'created_at' attribute is of datetime type.
        """
        self.assertIsInstance(self.test_instance.created_at, datetime.datetime)

    def test_updated_at_is_datetime(self):
        """
        Test if the 'updated_at' attribute is of datetime type.
        """
        self.assertIsInstance(self.test_instance.updated_at, datetime.datetime)

    def test_save_updates_updated_at(self):
        """
        Test if the 'save' method updates the 'updated_at' attribute.
        """
        old_updated_at = self.test_instance.updated_at
        self.test_instance.save()
        new_updated_at = self.test_instance.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)

    def test_to_dict_contains_correct_keys(self):
        """
        Test if the 'to_dict' method returns a dictionary with expected keys.
        """
        model_dict = self.test_instance.to_dict()
        self.assertIn('id', model_dict)
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)
        self.assertIn('__class__', model_dict)

    def test_to_dict_datetime_format(self):
        """
        Test if the 'to_dict' method returns datetime attributes in ISO format.
        """
        model_dict = self.test_instance.to_dict()
        self.assertEqual(model_dict['created_at'], self.test_instance.created_at.isoformat())
        self.assertEqual(model_dict['updated_at'], self.test_instance.updated_at.isoformat())

    def test_str_representation(self):
        """
        Test if the string representation of BaseModel contains expected information.
        """
        str_repr = str(self.test_instance)
        self.assertIn("[BaseModel]", str_repr)
        self.assertIn("id", str_repr)
        self.assertIn(str(self.test_instance.id), str_repr)

if __name__ == '__main__':
    unittest.main()
