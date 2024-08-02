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

    def test_custom_delimiter(self):
        self.assertEqual(add("//;\n1;2"), 3)
        self.assertEqual(add("//|\n1|2|3"), 6)
        
    def test_multiple_delimiters(self):
        self.assertEqual(add("//[*][%]\n1*2%3"), 6)
        self.assertEqual(add("//[\\n]\n1\n2\n3"), 6)
        
    def test_ignore_numbers_greater_than_1000(self):
        self.assertEqual(add("2,1001"), 2)
        self.assertEqual(add("1000,1001,2"), 1002)

    def test_edge_cases(self):
        self.assertEqual(add("//;\n"), 0)    # No numbers after delimiter specification
        self.assertEqual(add("//;\n1;"), 1)  # Trailing delimiter without a number
        self.assertEqual(add("1\n,\n2"), 3)  # Irregular input format
        self.assertEqual(add("\n1,2\n"), 3)  # Leading and trailing newlines
        self.assertEqual(add("//\n"), 0)

    def test_no_delimiters(self):
        self.assertEqual(add("1\n2,3"), 6)
        self.assertEqual(add("1\n2\n3\n4"), 10)
    
    def test_negative_numbers(self):
        with self.assertRaises(ValueError) as context:
            add("1,-2,3")
        self.assertIn("Negative numbers not allowed", str(context.exception))
        self.assertIn("-2", str(context.exception))

        with self.assertRaises(ValueError) as context:
            add("-1,-2,-3")
        self.assertIn("Negative numbers not allowed", str(context.exception))
        self.assertIn("-1", str(context.exception))
        self.assertIn("-2", str(context.exception))
        self.assertIn("-3", str(context.exception))

if __name__ == "__main__":
    unittest.main()