from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from forex_python import converter
from forex_python.converter import CurrencyCodes, CurrencyRates, Decimal
import math

class Currency():

    def __init__(self):

        self.currency = self.read_dict("currency.txt")

    def read_dict(self, dict_path):
        """Read and return all currencies in dictionary."""

        dict_file = open(dict_path) # opens dict_path and labels the results as dict_file
        currency = [c.strip() for c in dict_file] #strips the currency of any spacing from the words in dict_file
        dict_file.close() #closes the file
        return currency #returns currency with no spacing from the dict_file
        
    def check_valid_currency(self, abb):
        """Check if the currency is found in the dictionary"""
        currency_exists = abb.upper() in self.currency

        if currency_exists:
            return abb.upper()
        else:
            return "Invalid Currency"

    def find_symbol(self, cf):
        """ Finds the symbol of the converting to variable"""
        c = CurrencyCodes()
        symbol = c.get_symbol(cf)
        return symbol

    def convert(self, cf, ct, amt):
        c = CurrencyRates(force_decimal=True)
        result = c.convert(cf, ct, Decimal(amt))
        return round(result, 2)