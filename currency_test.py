import unittest
import currency

first_currency_object = currency.Currency('£5.25')
second_currency_object = currency.Currency(currency_code='GBP', amount=5.25)
third_currency_object = currency.Currency(amount=5.25, currency_code='EUR')
fourth_currency_object = currency.Currency('£10.50')

class TestCurrency(unittest.TestCase):

    def test_assert_equal(self):
        self.assertEqual(first_currency_object, second_currency_object)

    def test_assert_not_equal_currency_code(self):
        self.assertNotEqual(second_currency_object, third_currency_object)

    def test_assert_not_equal_amount(self):
        self.assertNotEqual(first_currency_object, fourth_currency_object)

    def test_assert_equal_add(self):
        self.assertEqual(first_currency_object + second_currency_object, fourth_currency_object)

    def test_assert_not_equal_add(self):
        self.assertNotEqual(first_currency_object + currency.Currency('£8.75'), fourth_currency_object)

    def test_assert_raises_add(self):
        self.assertRaises(currency.DifferentCurrencyCodeError, lambda: first_currency_object + third_currency_object)

    def test_assert_equal_sub(self):
        self.assertEqual(fourth_currency_object - first_currency_object, second_currency_object)

    def test_assert_not_equal_sub(self):
        self.assertNotEqual(second_currency_object - first_currency_object, fourth_currency_object)

    def test_assert_raises_sub(self):
        self.assertRaises(currency.DifferentCurrencyCodeError, lambda: fourth_currency_object - third_currency_object)

    def test_assert_equal_mul(self):
        self.assertEqual(first_currency_object * second_currency_object, currency.Currency('£27.56'))

    def test_assert_not_equal_mul(self):
        self.assertNotEqual(first_currency_object * second_currency_object, currency.Currency('£900'))

    def test_assert_raises_mul(self):
        self.assertRaises(currency.DifferentCurrencyCodeError, lambda: first_currency_object * third_currency_object)

if __name__ == '__main__':
    unittest.main()
