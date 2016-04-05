# Currency Converter
##currency.py
class Currency takes an amount and a currency code as arguments. Equal, not equal, add, subtract, and multiply are all overloaded so that Currency objects may use those operators. In non-Boolean cases, a Currency object is returned.

##currency_test.py
unittest suite for class Currency. At present, all tests report success.

##currency_converter.py
class CurrencyConverter takes a dictionary of conversion rates as an argument. the convert(self, currency_object, currency_code) method converts one currency object into another. The default currency code is 'USD'.

##currency_converter_test.py
unittest suite for class CurrencyConverter. At present, all tests report success.
