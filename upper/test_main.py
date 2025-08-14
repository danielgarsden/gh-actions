import unittest
from main import UpperCaseConverter

class TestUpperCaseConverter(unittest.TestCase):
    def test_to_upper_with_lowercase(self):
        converter = UpperCaseConverter("hello")
        self.assertEqual(converter.to_upper(), "HELLO", "Should convert all letters to upper case.")

    def test_to_upper_with_mixed_case(self):
        converter = UpperCaseConverter("Hello World")
        self.assertEqual(converter.to_upper(), "HELLO WORLD", "Should convert all letters to upper case.")

    def test_to_upper_with_numbers_and_symbols(self):
        converter = UpperCaseConverter("abc123!@#")
        self.assertEqual(converter.to_upper(), "ABC123!@#", "Should leave numbers and symbols unchanged.")

if __name__ == '__main__':
    unittest.main()