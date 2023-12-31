# test_my_module.py
import unittest
from my_module import add_numbers

class TestAddNumbers(unittest.TestCase):

    def w_add_numbers1(self):
        # Test the add_numbers function
        result = add_numbers(2, 3)
        self.assertEqual(result, 5)
    def test_add_numbers2(self):
        # Test the add_numbers function result = add_numbers(2, 5)
        self.assertEqual(result, 7)
        result = add_numbers(3, 3)
    def test_add_numbers3(self):
        # Test the add_numbers functionassert result == 6
        result = add_numbers(55, 99)
        self.assertEqual(result, 154)
    def test_add_numbers4(self):
        # Test the add_numbers functionassert result == 6
        result = add_numbers(4, 99)
        self.assertEqual(result, 103)
          # Assert that the result is equal to 5

if __name__ == '__main__':
    unittest.main()
