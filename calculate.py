# MODULES


from flask import Flask
from flask import render_template
from flask import request
from flask import redirected

import dbFunctions as dbFunc


import formatInput as fi

# INITIATE FLASK APP

app = Flask(__name__)


# CALCULATE


def calculate(equation):

    # Check for variables, saved results, etc
    equation = fi.formatInputSaved(equation)
    equation = fi.formatInputVar(equation)
    ans = eval(equation)
    return ans


def postCalc(result):

    # Save as variable, assume yes for now:
    dbFunc.saveVar("placeholder", result)

    # Save to database, assume yes for now:
    dbFunc.insertTable("placeholder", result)


if __name__ == "__main__":
    app.config["TEMPLATES_AUTO__RELOAD"] = True