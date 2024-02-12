#!/usr/bin/python3
"""Unittest for BaseModel class"""
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        """Set up BaseModel instance for testing"""
        self.base_model = BaseModel()

    def test_init(self):
        """Test that the instances are properly initialized"""
        self.assertIsInstance(self.base_model, BaseModel)
        self.assertIsNotNone(self.base_model.id)
        self.assertIsNotNone(self.base_model.created_at)
        self.assertIsNotNone(self.base_model.updated_at)

    def test_str(self):
        """Test __str__ method"""
        expected_string = "[BaseModel] ({}) {}".format(
            self.base_model.id, self.base_model.__dict__)
        self.assertEqual(str(self.base_model), expected_string)

    def test_save(self):
        """Test save method"""
        prev_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(prev_updated_at, self.base_model.updated_at)

    def test_to_dict(self):
        """Test to_dict method"""
        base_model_dict = self.base_model.to_dict()
        self.assertIsInstance(base_model_dict, dict)
        self.assertEqual(base_model_dict['__class__'], 'BaseModel')
        self.assertEqual(base_model_dict['id'], self.base_model.id)
        self.assertEqual(
            base_model_dict['created_at'],
            self.base_model.created_at.isoformat()
        )
        self.assertEqual(
            base_model_dict['updated_at'],
            self.base_model.updated_at.isoformat()
        )


if __name__ == '__main__':
    unittest.main()
