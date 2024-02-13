#!/usr/bin/python3

import unittest
from models.amenity import Amenity
import datetime
from uuid import UUID

class TestAmenity(unittest.TestCase):
        """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = 'Amenity'
        self.value = Amenity

    def setUp(self):
        """
        Set up a fresh instance of Amenity for each test.
        """
        self.test_amenity = Amenity()

    def test_subclass(self):
        """
        Test if Amenity is a subclass of BaseModel.
        """
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_has_attributes(self):
        """
        Test if the Amenity instance has the expected attributes.
        """
        self.assertTrue(hasattr(self.test_amenity, 'name'))

    def test_id_is_valid_uuid(self):
        """
        Test if the 'id' attribute is a valid UUID.
        """
        self.assertTrue(UUID(self.test_amenity.id))

    def test_created_at_is_datetime(self):
        """
        Test if the 'created_at' attribute is of datetime type.
        """
        self.assertIsInstance(self.test_amenity.created_at, datetime.datetime)

    def test_updated_at_is_datetime(self):
        """
        Test if the 'updated_at' attribute is of datetime type.
        """
        self.assertIsInstance(self.test_amenity.updated_at, datetime.datetime)

    def test_to_dict_contains_correct_keys(self):
        """
        Test if the 'to_dict' method returns a dictionary with expected keys.
        """
        model_dict = self.test_amenity.to_dict()
        self.assertIn('name', model_dict)

    def test_str_representation(self):
        """
        Test if the string representation of Amenity contains expected information.
        """
        str_repr = str(self.test_amenity)
        self.assertIn("[Amenity]", str_repr)
        self.assertIn("id", str_repr)
        self.assertIn(str(self.test_amenity.id), str_repr)

if __name__ == '__main__':
    unittest.main()
