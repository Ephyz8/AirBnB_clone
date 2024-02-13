import unittest
from models.place import Place
import datetime
from uuid import UUID

class TestPlace(unittest.TestCase):
        """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = 'Place'
        self.value = Place

    def setUp(self):
        """
        Set up a fresh instance of Place for each test.
        """
        self.test_place = Place()

    def test_subclass(self):
        """
        Test if Place is a subclass of BaseModel.
        """
        self.assertTrue(issubclass(Place, BaseModel))

    def test_has_city_id_attribute(self):
        """
        Test if Place instance has 'city_id' attribute.
        """
        self.assertTrue(hasattr(self.test_place, 'city_id'))

    def test_has_description_attribute(self):
        """
        Test if Place instance has 'description' attribute.
        """
        self.assertTrue(hasattr(self.test_place, 'description'))

    def test_has_user_id_attribute(self):
        """
        Test if Place instance has 'user_id' attribute.
        """
        self.assertTrue(hasattr(self.test_place, 'user_id'))

    def test_has_name_attribute(self):
        """
        Test if Place instance has 'name' attribute.
        """
        self.assertTrue(hasattr(self.test_place, 'name'))

    def test_has_number_rooms_attribute(self):
        """
        Test if Place instance has 'number_rooms' attribute.
        """
        self.assertTrue(hasattr(self.test_place, 'number_rooms'))

    def test_has_number_bathrooms_attribute(self):
        """
        Test if Place instance has 'number_bathrooms' attribute.
        """
        self.assertTrue(hasattr(self.test_place, 'number_bathrooms'))

    def test_has_price_by_night_attribute(self):
        """
        Test if Place instance has 'price_by_night' attribute.
        """
        self.assertTrue(hasattr(self.test_place, 'price_by_night'))

    def test_has_max_guest_attribute(self):
        """
        Test if Place instance has 'max_guest' attribute.
        """
        self.assertTrue(hasattr(self.test_place, 'max_guest'))

    def test_has_latitude_attribute(self):
        """
        Test if Place instance has 'latitude' attribute.
        """
        self.assertTrue(hasattr(self.test_place, 'latitude'))

    def test_has_longitude_attribute(self):
        """
        Test if Place instance has 'longitude' attribute.
        """
        self.assertTrue(hasattr(self.test_place, 'longitude'))

    def test_has_amenity_ids_attribute(self):
        """
        Test if Place instance has 'amenity_ids' attribute.
        """
        self.assertTrue(hasattr(self.test_place, 'amenity_ids'))

    def test_id_is_valid_uuid(self):
        """
        Test if the 'id' attribute is a valid UUID.
        """
        self.assertTrue(UUID(self.test_place.id))

    def test_created_at_is_datetime(self):
        """
        Test if the 'created_at' attribute is of datetime type.
        """
        self.assertIsInstance(self.test_place.created_at, datetime.datetime)

    def test_updated_at_is_datetime(self):
        """
        Test if the 'updated_at' attribute is of datetime type.
        """
        self.assertIsInstance(self.test_place.updated_at, datetime.datetime)

    def test_to_dict_contains_correct_keys(self):
        """
        Test if the 'to_dict' method returns a dictionary with expected keys.
        """
        model_dict = self.test_place.to_dict()
        self.assertIn('city_id', model_dict)
        self.assertIn('description', model_dict)
        self.assertIn('user_id', model_dict)
        self.assertIn('name', model_dict)
        self.assertIn('number_rooms', model_dict)
        self.assertIn('number_bathrooms', model_dict)
        self.assertIn('price_by_night', model_dict)
        self.assertIn('max_guest', model_dict)
        self.assertIn('latitude', model_dict)
        self.assertIn('longitude', model_dict)
        self.assertIn('amenity_ids', model_dict)

    def test_str_representation(self):
        """
        Test if the string representation of Place contains expected information.
        """
        str_repr = str(self.test_place)
        self.assertIn("[Place]", str_repr)
        self.assertIn("id", str_repr)
        self.assertIn(str(self.test_place.id), str_repr)

if __name__ == '__main__':
    unittest.main()
