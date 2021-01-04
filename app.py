from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from forex_python import converter
from forex_python.converter import CurrencyCodes
from currency import Currency

#from forex_python.converter import CurrencyRates
#>>> c = CurrencyRates(force_decimal=True)
#>>> c.convert('USD', 'INR', Decimal('10.45'))
#Decimal('705.09')
#>>> c.convert('USD', 'INR', 10)
#DecimalFloatMismatchError: convert requires amount parameter is of type Decimal when use_decimal=True

app = Flask(__name__)
app.config["SECRET KEY"] = "IDIDIT"


rates = Currency()

@app.route("/")
def formpage():
    """Show homepage with conversion form"""
    return render_template("base.html")


@app.route("/", methods=["POST"])
def collecting_data():
    """Collects data from form"""
    convertfrom = request.form["from"]
    convertto = request.form["to"]
    amount = request.form["amount"]
    valid = rates.check_valid_currency(convertfrom)
    valid2 = rates.check_valid_currency(convertto)
    symbol = rates.find_symbol(valid2)
    results = rates.convert(valid, valid2, amount)

    return render_template("results.html", symbol = symbol, results = results)
    

