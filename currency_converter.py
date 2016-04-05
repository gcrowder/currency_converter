from currency import *

class UnknownCurrencyCodeError(Exception):
    pass

class CurrencyConverter:

    def __init__(self, conversion_rates={'USD' : 1.0, 'EUR' : 0.878, 'GBP' : 0.701, 'JPY' : 110.947}):
        self.conversion_rates = conversion_rates

    def convert(self, currency_object, destination_currency_code='USD'):
        if destination_currency_code in self.conversion_rates:
            total = currency_object.amount * (self.conversion_rates[destination_currency_code] / self.conversion_rates[currency_object.currency_code])
            total = round(total, 2)
            new_currency_object = Currency(total, destination_currency_code)
            return new_currency_object
        else:
            raise UnknownCurrencyCodeError("That currency code is not recognized. Please add it to conversion_rates and try again.")
