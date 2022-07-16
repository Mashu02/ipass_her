import unittest
from algo import data_check

class TestData(unittest.TestCase):
    def test_data(self):
        result = data_check()
        self.assertTrue(result)