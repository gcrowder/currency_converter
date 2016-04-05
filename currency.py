class DifferentCurrencyCodeError(Exception):
    pass

class Currency:
    currency_dict = {'USD' : '$', 'EUR' : '€', 'GBP' : '£', 'JPY' : '¥'}
    def __init__(self, amount, currency_code='USD'):
        try:
            self.amount = float(amount)
            self.currency_code = currency_code
        except:
            for key in self.currency_dict:
                if self.currency_dict[key] == amount[0]:
                    self.currency_code = key
            self.amount = float(amount[1:])

    def __eq__(self, currency_object):
        return self.amount == currency_object.amount and self.currency_code == currency_object.currency_code

    def __ne__(self, currency_object):
        return self.currency_code != currency_object.currency_code or self.amount != currency_object.amount

    def __add__(self, currency_object):
        total = 0
        if self.currency_code == currency_object.currency_code:
            total = self.amount + currency_object.amount
            new_currency_object = Currency(currency_code=self.currency_code, amount=round(total, 2))
            return new_currency_object
        else:
            raise DifferentCurrencyCodeError("You can't add two different currencies.")

    def __sub__(self, currency_object):
        total = 0
        if self.currency_code == currency_object.currency_code:
            total = self.amount - currency_object.amount
            new_currency_object = Currency(currency_code=self.currency_code, amount=round(total, 2))
            return new_currency_object
        else:
            raise DifferentCurrencyCodeError("You can't subtract two different currencies.")

    def __mul__(self, currency_object):
        total = 0
        try:
            if self.currency_code == currency_object.currency_code:
                total = self.amount * currency_object.amount
                new_currency_object = Currency(currency_code=self.currency_code, amount=round(total, 2))
                return new_currency_object
            else:
                raise DifferentCurrencyCodeError("You can't multiply two different currencies.")
        except AttributeError:
            total = self.amount * currency_object
            new_currency_object = Currency(currency_code=self.currency_code, amount=round(total, 2))
            return new_currency_object
