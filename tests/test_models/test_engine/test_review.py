#!/usr/bin/python3
"""A test module for the Review class."""

from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class TestReview(test_basemodel):
    """
    Test class for the Review model.

    This class contains unit tests for the attributes of the Review model,
    such as place_id, user_id, and text.
    """

    def __init__(self, *args, **kwargs):
        """Initialize TestReview class."""
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.review_class = Review

    def test_place_id(self):
        """
        Test the place_id attribute of the Review.

        This test checks whether the place_id attribute of a Review instance
        is of type str.
        """
        new_review = self.review_class()
        self.assertEqual(type(new_review.place_id), str)

    def test_user_id(self):
        """
        Test the user_id attribute of the Review.

        This test checks whether the user_id attribute of a Review instance
        is of type str.
        """
        new_review = self.review_class()
        self.assertEqual(type(new_review.user_id), str)

    def test_text(self):
        """
        Test the text attribute of the Review.

        This test checks whether the text attribute of a Review instance
        is of type str.
        """
        new_review = self.review_class()
        self.assertEqual(type(new_review.text), str)


# Example of how to use the TestReview class:
if __name__ == "__main__":
    test_review_instance = TestReview()
    test_review_instance.test_place_id()
    test_review_instance.test_user_id()
    test_review_instance.test_text()
