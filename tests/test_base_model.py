#!/usr/bin/python3
"""
Unit tests for BaseModel class.
"""
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """
    Test cases for BaseModel class.
    """
    def test_instance_creation(self):
        """
        Test creation of BaseModel instance.
        """
        my_model = BaseModel()
        self.assertIsInstance(my_model, BaseModel)
        self.assertIsInstance(my_model.created_at, datetime)
        self.assertIsInstance(my_model.updated_at, datetime)
        self.assertIsNotNone(my_model.id)

    def test_to_dict(self):
        """
        Test to_dict() method.
        """
        my_model = BaseModel()
        my_model.name = "Test Model"
        my_model.my_number = 123
        my_model_dict = my_model.to_dict()
        self.assertEqual(my_model_dict['__class__'], 'BaseModel')
        self.assertEqual(my_model_dict['name'], 'Test Model')
        self.assertEqual(my_model_dict['my_number'], 123)

    def test_str_representation(self):
        """
        Test __str__() method.
        """
        my_model = BaseModel()
        my_model.name = "Test Model"
        my_model.my_number = 123
        self.assertEqual(str(my_model),
                         "[BaseModel] ({}) {}".format(
                             my_model.id, my_model.__dict__))


if __name__ == '__main__':
    unittest.main()
