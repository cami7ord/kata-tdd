from unittest import TestCase

import StringProcessor

class TestStringProcessor(TestCase):
    def test_length(self):
        self.assertEqual(StringProcessor.length(""), 0, "Length of empty string.")
