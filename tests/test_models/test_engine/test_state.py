#!/usr/bin/python3
"""A test module for the State class."""

from tests.test_models.test_base_model import test_basemodel
from models.state import State


class TestState(test_basemodel):
    """
    Test class for the State model.

    This class contains unit tests for the attributes of the State model,
    specifically the 'name' attribute.
    """

    def __init__(self, *args, **kwargs):
        """Initialize TestState class."""
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.state_class = State

    def test_name(self):
        """
        Test the name attribute of the State.

        This test checks whether the name attribute of a State instance
        is of type str.
        """
        new_state = self.state_class()
        self.assertEqual(type(new_state.name), str)


# Example of how to use the TestState class:
if __name__ == "__main__":
    test_state_instance = TestState()
    test_state_instance.test_name()
