from unittest import TestCase

from StringProcessor import StringProcessor

class TestStringProcessor(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.sp = StringProcessor()

    # Length

    def test_length_empty(self):
        self.assertEqual(self.sp.length(""), 0, "Length of empty string.")

    def test_length_one(self):
        self.assertEqual(self.sp.length("5"), 1, "Length of one number.")

    def test_length_two(self):
        self.assertEqual(self.sp.length("5,3"), 2, "Length of two numbers.")

    def test_length_n(self):
        self.assertEqual(self.sp.length("5,3,4,1,6,8"), 6, "Length of six numbers.")

    # Min

    def test_min_empty(self):
        self.assertEqual(self.sp.min(""), 0, "Min of empty string.")