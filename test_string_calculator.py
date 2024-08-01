import unittest
from string_calculator import add

class TestStringCalculator(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(add(""), 0)

    def test_single_number(self):
        self.assertEqual(add("1"), 1)
        self.assertEqual(add("5"), 5)
    
    def test_two_numbers(self):
        self.assertEqual(add("1,2"), 3)

    def test_multiple_numbers(self):
        self.assertEqual(add("1,2,3"), 6)
        self.assertEqual(add("4,5,6,7"), 22)
    
    def test_new_line_delimiter(self):
        self.assertEqual(add("1\n2,3"), 6)

    
if __name__ == "__main__":
    unittest.main()