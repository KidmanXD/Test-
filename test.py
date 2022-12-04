import unittest
from testkr.testkr.kr import *

class Testsnakecase(unittest.TestCase):

    def test_snake(self):
        s = NameConverterSnake('Bong-Doom')
        res = s.to_snake_case()
        self.assertEqual(res, 'bong__doom')

class Testcamelcase(unittest.TestCase):

    def test_camel(self):
        d = NameConverterCamel('Bong-Doom')
        res = d.to_camel_case()
        self.assertEqual(res, 'BongDoom')

if __name__ == '__main__':
    unittest.main()