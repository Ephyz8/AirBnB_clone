#!/usr/bin/python3
"""A test module for the City class."""

from tests.test_models.test_base_model import test_basemodel
from models.city import City


class TestCity(test_basemodel):
    """
    Test class for the City model.

    This class contains unit tests for the attributes of the City model,
    specifically the 'state_id' and 'name' attributes.
    """

    def __init__(self, *args, **kwargs):
        """Initialize TestCity class."""
        super().__init__(*args, **kwargs)
        self.model_name = "City"
        self.city_class = City

    def test_state_id(self):
        """
        Test the state_id attribute of the City.

        This test checks whether the state_id attribute of a City instance
        is of type str.
        """
        new_city = self.city_class()
        self.assertEqual(type(new_city.state_id), str)

    def test_name(self):
        """
        Test the name attribute of the City.

        This test checks whether the name attribute of a City instance
        is of type str.
        """
        new_city = self.city_class()
        self.assertEqual(type(new_city.name), str)


# Example of how to use the TestCity class:
if __name__ == "__main__":
    test_city_instance = TestCity()
    test_city_instance.test_state_id()
    test_city_instance.test_name()
