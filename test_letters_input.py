import unittest

from letters_mapped import convert_letters_input


class TestLetters(unittest.TestCase):
    def test_foo_bar(self):
        data = "foo bar"
        result = convert_letters_input(data)
        self.assertEqual(result, "333666 666022 2777")

    def test_letter_with_space(self):
        data = "a b c"
        result = convert_letters_input(data)
        self.assertEqual(result, "20220222")

    def test_spaces(self):
        data = "     "
        result = convert_letters_input(data)
        self.assertEqual(result, "0 0 0 0 0")

    def test_one_space(self): 
        data = " "
        result = convert_letters_input(data)
        self.assertEqual(result, "0")

    def test_email(self):
        data = "mhost39@gmail.com"
        result = convert_letters_input(data)
        self.assertEqual(result, "not supported")

    def test_letter_digits(self):
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


if __name__ == '__main__':
    unittest.main()