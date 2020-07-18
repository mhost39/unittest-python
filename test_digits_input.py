import unittest

from letters_mapped import convert_digits_input


class TestLetters(unittest.TestCase):
    def test_foo_bar(self):
        """
            test 333666 666022 2777 
        """
        data = "333666 666022 2777" 
        result = convert_digits_input(data)
        self.assertEqual(result, "foo bar")

    def test_more_digits(self):
        """
            test if user input 7 without space 
        """
        data = "7777777777777777" 
        result = convert_digits_input(data)
        self.assertEqual(result, "not supported")
    
    def test_case2(self):
        data = "7 77 777 7777" 
        result = convert_digits_input(data)
        self.assertEqual(result, "pqrs")

    def test_case3(self):
        """
            must be 222 2 because digit number 2 have 3 letters
        """
        data = "2222" 
        result = convert_digits_input(data)
        self.assertEqual(result, "not supported")

    def test_zero(self):
        """
            test spaces 
        """
        data = "0 0 0 0 0" 
        result = convert_digits_input(data)
        self.assertEqual(result, "     ")

    def test_zero_without_space(self):
        """
            fail because digit number 0 have 1 letter (space)
        """
        data = "00000" 
        result = convert_digits_input(data)
        self.assertEqual(result, "not supported")

    def test_input_1(self): # if user input 1
        """
            digit number 1 not have any letter
        """
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
    
    def test_long_input(self): 
        """
            test long input 
        """
        data = "2 2266688 802226663 337777222 255533777 7777" * 1000
        result = convert_digits_input(data)
        exp_result = "about codescalers" * 1000
        self.assertEqual(result, exp_result)

if __name__ == '__main__':
    unittest.main()