import unittest
from currency import *
from currency_converter import *

currency_converter = CurrencyConverter({'USD' : 1.0, 'EUR' : 0.878})


class TestCurrencyConverter(unittest.TestCase):

    def test_assert_equal_convert_1(self):
        self.assertEqual(currency_converter.convert(Currency(1, 'USD'), 'USD'), Currency(1, 'USD'))

    def test_assert_not_equal_convert(self):
        self.assertNotEqual(currency_converter.convert(Currency(1, 'USD'), 'USD'), Currency(1, 'EUR'))

    def test_assert_equal_convert_2(self):
        self.assertEqual(currency_converter.convert(Currency(1, 'USD'), 'EUR'), Currency(0.88, 'EUR'))

if __name__ == '__main__':
    unittest.main()
