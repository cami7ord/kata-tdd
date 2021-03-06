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

    def test_min_one(self):
        self.assertEqual(self.sp.min("5"), 5, "Min of one number.")

    def test_min_two(self):
        self.assertEqual(self.sp.min("5,3"), 3, "Min of two numbers.")

    def test_min_n(self):
        self.assertEqual(self.sp.min("5,3,4,1,6,8"), 1, "Length of six numbers.")

    # Max

    def test_max_empty(self):
        self.assertEqual(self.sp.max(""), 0, "Max of empty string.")

    def test_max_one(self):
        self.assertEqual(self.sp.max("5"), 5, "Max of one number.")

    def test_max_two(self):
        self.assertEqual(self.sp.max("5,3"), 5, "Max of two numbers.")

    def test_max_n(self):
        self.assertEqual(self.sp.max("5,3,4,1,6,8"), 8, "Max of six numbers.")

    # Average

    def test_avg_empty(self):
        self.assertEqual(self.sp.avg(""), 0, "Average of empty string.")

    def test_avg_one(self):
        self.assertEqual(self.sp.avg("5"), 5, "Average of one number.")

    def test_avg_two(self):
        self.assertEqual(self.sp.avg("5,3"), 4, "Average of two numbers.")

    def test_avg_n(self):
        self.assertEqual(self.sp.avg("5,3,4,1,6,8"), 4.5, "Average of six numbers.")


    # Process String

    def test_process_string(self):
        self.assertEqual(self.sp.process(""), [0, 0, 0, 0], "Process an empty string.")

    def test_process_one(self):
        self.assertEqual(self.sp.process("5"), [1, 5, 5, 5], "Process of one number.")

    def test_process_two(self):
        self.assertEqual(self.sp.process("5,3"), [2, 3, 5, 4], "Process of two numbers.")

    def test_process_n(self):
        self.assertEqual(self.sp.process("5,3,4,1,6,8"), [6, 1, 8, 4.5], "Process of six numbers.")