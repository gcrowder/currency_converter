from currency import Currency, DifferentCurrencyCodeError
from currency_converter import CurrencyConverter, UnknownCurrencyCodeError

def greeting():
    print("Welcome to the Currency Convertatorium!")
    print("Come to the Convertatorium for all your currency converting needs.")

def make_currency():
    while True:
        try:
            amount = float(input("Please enter an amount:"))
            currency_code = input("Please enter a currency code. Your options are USD, EUR, GBP, and JPY: ").upper()
            return Currency(amount, currency_code)
        except ValueError:
            print("Only numbers will be accepted as amounts. Please try again.")
            continue

def make_conversion(currency_object):
    while True:
        converter_object = CurrencyConverter()
        destination_currency = input("Please enter your destination currency code. Your options are USD, EUR, GBP, and JPY: ").upper()
        try:
            new_destination_currency_object = converter_object.convert(currency_object, destination_currency)
            return new_destination_currency_object
        except UnknownCurrencyCodeError:
            print("We are unfamilar with that currency and it's exchange rate. Please try again.")
            continue

def show_converted_currency(currency_object):
    print("After conversion, you have ", "{}{}".format(currency_object.currency_dict[currency_object.currency_code], currency_object.amount))


def main():
    greeting()
    starting_currency = make_currency()
    converted_currency = make_conversion(starting_currency)
    show_converted_currency(converted_currency)

if __name__ == '__main__':
    main()
