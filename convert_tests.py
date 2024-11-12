import unittest

from convert import str_to_float


class test_str_to_float(unittest.TestCase):
        def test_one(self):
            input = '123.2'
            expected = 123.2
            result = str_to_float(input)
            self.assertEqual(expected,result)

        def test_one_2(self):
            input = 'xyz'
            expected = None
            result = str_to_float(input)
            self.assertEqual(expected, result)
