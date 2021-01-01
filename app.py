from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from forex_python import converter
from forex_python.converter import CurrencyCodes

#from forex_python.converter import CurrencyRates
#>>> c = CurrencyRates(force_decimal=True)
#>>> c.convert('USD', 'INR', Decimal('10.45'))
#Decimal('705.09')
#>>> c.convert('USD', 'INR', 10)
#DecimalFloatMismatchError: convert requires amount parameter is of type Decimal when use_decimal=True

app = Flask(__name__)
app.config["SECRET KEY"] = "IDIDIT"

@app.route("/")
def formpage():
    """Show homepage with conversion form"""
    return render_template("base.html")

@app.route("/results")
def results():
    """Displays results if correct information entered by user"""
    #takes the input values (CF, CT, A) and provides answer using forex_python
    return render_template("results.html", results = results) #with currency symbol and decimal place

@app.route("/results", methods=["POST"])
def collecting_data():
    """Collects data from form"""
    convert = request.form["conversions"]
    return convert