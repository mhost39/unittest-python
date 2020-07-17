import unittest

from letters_mapped import convert_digits_input


class TestLetters(unittest.TestCase):
    def test_foo_bar(self):
        data = "333666 666022 2777" 
        result = convert_digits_input(data)
        self.assertEqual(result, "foo bar")

    def test_more_digits(self):
        data = "7777777777777777" 
        result = convert_digits_input(data)
        self.assertEqual(result, "not supported")
    
    def test_case2(self):
        data = "7 77 777 7777" 
        result = convert_digits_input(data)
        self.assertEqual(result, "pqrs")

    def test_input_1(self): # if user input 1
        data = "111"
        result = convert_digits_input(data)
        self.assertEqual(result, "not supported")

    def test_spaces(self):
        data = "     "
        result = convert_digits_input(data)
        self.assertEqual(result, "not supported")

    def test_one_space(self): 
        data = " "
        result = convert_digits_input(data)
        self.assertEqual(result, "")
        
    def test_symbols(self):
        data = "+"
        result = convert_digits_input(data)
        self.assertEqual(result, "not supported")

    def test_letter_digits(self):
        data = "th258"
        result = convert_digits_input(data)
        self.assertEqual(result, "not supported")

    def test_empty_string(self): 
        data = ""
        result = convert_digits_input(data)
        self.assertEqual(result, "not supported")


if __name__ == '__main__':
    unittest.main()