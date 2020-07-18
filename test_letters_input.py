import unittest

from letters_mapped import convert_letters_input


class TestLetters(unittest.TestCase):
    def test_foo_bar(self):
        """
            test foo bar input 
        """
        data = "foo bar"
        result = convert_letters_input(data)
        self.assertEqual(result, "333666 666022 2777")

    def test_letter_with_space(self):
        """
            test input with space
        """
        data = "a b c"
        result = convert_letters_input(data)
        self.assertEqual(result, "20220222")

    def test_spaces(self):
        """
            test all input is space 
        """
        data = "     "
        result = convert_letters_input(data)
        self.assertEqual(result, "0 0 0 0 0")

    def test_one_space(self): 
        """
            test one space
        """
        data = " "
        result = convert_letters_input(data)
        self.assertEqual(result, "0")

    def test_email(self):
        """
            test if input is contain symbols like @ and . in email
        """
        data = "mhost39@gmail.com"
        result = convert_letters_input(data)
        self.assertEqual(result, "not supported")

    def test_letter_digits(self):
        """
            test input letter and digits
        """
        data = "th258"
        result = convert_letters_input(data)
        self.assertEqual(result, "not supported")
    def test_symbols(self): # symbols like *, #, $ ..
        data = "*#"
        result = convert_letters_input(data)
        self.assertEqual(result, "not supported")

    def test_empty_string(self): 
        data = ""
        result = convert_letters_input(data)
        self.assertEqual(result, "not supported")
    def test_capital_letters(self):
        """
            test if user input is capital letters
        """ 
        data = "HELLO"
        result = convert_letters_input(data)
        self.assertEqual(result, "not supported")

    def test_long_letters(self):
        """
            test long letters
        """ 
        data = "hello world" * 1000
        exp_result = "4433555 555666096667775553" * 1000
        result = convert_letters_input(data)
        self.assertEqual(result, exp_result)


if __name__ == '__main__':
    unittest.main()