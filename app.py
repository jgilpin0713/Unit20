from flask import Flask, render_template, request, flash, redirect, session
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
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False
app.secret_key = "I DID IT"
rates = Currency()

@app.route("/")
def formpage():
    """Show homepage with conversion form"""
    return render_template("base.html")


@app.route("/", methods=["POST"])
def is_it_valid():
    """Collects data from form and determine if it's part of dictionary"""
    convertfrom = request.form["from"]
    convertto = request.form["to"]
    amount = request.form["amount"]
    
    valid = rates.check_valid_currency(convertfrom)
    if valid is False:
        flash("Not Valid Code:")
        flash(convertfrom)
    valid2 = rates.check_valid_currency(convertto)
    if valid2 is False:
        flash("Not a Valid Code:")
        flash(convertto)
    if not amount.isdigit():
        flash("Not a valid amount")
    if valid is True and valid2 is True and amount.isdigit():
        symbol = rates.find_symbol(convertto)
        results = rates.convert(convertfrom, convertto, amount)
        return render_template("results.html", symbol = symbol, results = results)
    else:
        return redirect("/")
    

