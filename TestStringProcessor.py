from unittest import TestCase

from StringProcessor import StringProcessor

class TestStringProcessor(TestCase):

    def test_length_empty(self):
        self.assertEqual(StringProcessor().length(""), 0, "Length of empty string.")

    def test_length_one(self):
        self.assertEqual(StringProcessor().length("5"), 1, "Length of one number.")

    def test_length_two(self):
        self.assertEqual(StringProcessor().length("5,3"), 2, "Length of two numbers.")
