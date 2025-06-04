from flask import Flask, url_for
from flask import redirect
from flask import render_template
from flask import request
from flask import jsonify
from flask import session
import requests
from flask_wtf import CSRFProtect
from flask_csp.csp import csp_header
import sqlite3 as sql
import numpy as np
from flask import url_for
from Modules import calculate as calc
from Modules import formulae as form
from Modules.variables import variables
from Modules import regression as reg
import reprlib
import logging


app_log = logging.getLogger(__name__)
logging.basicConfig(
    filename="security_log.log",
    encoding="utf-8",
    level=logging.DEBUG,
    format="%(asctime)s %(message)s",
)

# Unique basic 16 key
app = Flask(__name__)
app.secret_key = b"_53oi3uriq9pifpff;apl"
csrf = CSRFProtect(app)


# CSP header
@csp_header(
    {
        "base-uri": "self",
        "default-src": "'self'",
        "style-src": "'self'",
        "script-src": "'self'",
        "img-src": "*",
        "media-src": "'self'",
        "font-src": "self",
        "object-src": "'self'",
        "child-src": "'self'",
        "connect-src": "'self'",
        "worker-src": "'self'",
        "report-uri": "/csp_report",
        "frame-ancestors": "'none'",
        "form-action": "'self'",
        "frame-src": "'none'",
    }
)

@app.route("/index", methods=["GET"])
@app.route("/index.html", methods=["GET"])
@app.route("/index.asp", methods=["GET"])
@app.route("/index.php", methods=["GET"])
@app.route("/index.html", methods=["GET"])
def root():
    return redirect("/", 302)

@app.before_request
def set_default_ans():
    session.setdefault('ans', 0)

@app.route("/", methods=["POST", "GET"])
@csp_header(
    {
        # Server Side CSP is consistent with meta CSP in layout.html
        "base-uri": "'self'",
        "default-src": "'self'",
        "style-src": "'self'",
        "script-src": "'self'",
        "img-src": "'self' data:",
        "media-src": "'self'",
        "font-src": "'self'",
        "object-src": "'self'",
        "child-src": "'self'",
        "connect-src": "'self'",
        "worker-src": "'self'",
        "report-uri": "/csp_report",
        "frame-ancestors": "'none'",
        "form-action": "'self'",
        "frame-src": "'none'",
    }
)
def index():
    return render_template("/index.html")
    


@app.route('/displayResult.html')
def results():
    conn = sql.connect("Databases/savedResults.db")
    conn.row_factory = sql.Row
    savedResults = conn.execute('SELECT * FROM savedResults').fetchall()
    conn.close()
    return render_template('displayResult.html', results=savedResults)


# example CSRF protected form
@app.route("/formCalcMode.html", methods=["POST", "GET"])
def calculation():
    if request.method == "POST":
        equationInput = request.form["input"]
        session['result'] = calc.calculate(equationInput, session['ans'])
        session['equation'] = equationInput
        session['ans'] = session['result']
        return redirect("/answer.html")
    else:
        return render_template("/formCalcMode.html")


@app.route("/answer.html", methods=["GET"])
def answerDisplay():
    answer = session.get('result')
    EQinput = session.get('equation')
    save_status = session.pop('save_status', None)
    return render_template("/answer.html", answer=answer, EQinput=EQinput, save_status=save_status, variables=variables)

# Save result to variable
@app.route("/save-variable", methods=["POST"])
def save_variable():
    var_name = request.form.get("varName")
    result = session.get("result")

    if var_name and result:
        calc.postCalcVar(result, var_name)
        session['save_status'] = f"Saved result to variable '{var_name}'"
        return "Success"
    return "Fail"


# Save result to table/database
@app.route("/save-result", methods=["POST"])
def save_result():
    keyword = request.form.get("keyword")
    result = session.get("result")
    if keyword and result:
        calc.postCalcTable(result, keyword)
        session['save_status'] = f"Saved result under keyword '{keyword}'"
        return "Success"
    return "Fail"

# Placeholder. answer.html will have 2 buttons that allow the user to save the result
# A button that will bring the user back to the homepage
# and a button that will redirect the user back to the form

@app.route("/calculateFormula.html", methods=["POST", "GET"])
def calculateFormula():
    if request.method == "POST":
        selected_formula = request.form.get("specificFormula")
        equation = request.form.get("equation")
        session['equation'] = equation
        dynamic_inputs = request.form.getlist("dynamicInput")

        # You can then pass this into your calculation logic or just store it
        session['inputs'] = dynamic_inputs
        session['selected_formula'] = selected_formula
        # Use explicit session key access and defaults
        formula_name = session.get('selected_formula', '').strip()
        inputs = session.get('inputs', [])
        ans = session.get('ans')
        session['result'] = form.run_formula(formula_name, inputs, ans)
        session.pop('save_status', None)
        return redirect(url_for('answerDisplay'))
    else:
        return render_template("/calculateFormula.html")
    

@app.route("/regression.html", methods=["GET", "POST"])
def regressionCalc():
    formula = None
    if request.method == "POST":
        try:
            x_vals = []
            y_vals = []
            i = 0
            while True:
                x = request.form.get(f"x{i}")
                y = request.form.get(f"y{i}")
                if x is None or y is None:
                    break
                x_vals.append(float(x))
                y_vals.append(float(y))
                i += 1

            x_array = np.array(x_vals).reshape(-1, 1)
            y_array = np.array(y_vals)
            formula = reg.regressionLinear(x_array, y_array)
        except Exception as e:
            formula = f"Error: {e}"

    return render_template("regression.html", formula=formula)

# New route for settings page to set rounding
@app.route("/settings.html", methods=["GET", "POST"])
def set_rounding():
    confirmation = None
    if request.method == "POST":
        try:
            rounding = int(request.form.get("rounding"))
            session['rounding'] = rounding
            confirmation = f"Rounding set to {rounding} decimal places."
        except:
            confirmation = "Invalid rounding value."

    return render_template("settings.html", confirmation=confirmation)

# Endpoint for logging CSP violations
@app.route("/csp_report", methods=["POST"])
@csrf.exempt
def csp_report():
    app.logger.critical(request.data.decode())
    return "done"


if __name__ == "__main__":
    app.config["TEMPLATES_AUTO_RELOAD"] = True
    app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0
    app.run(debug=True, host="0.0.0.0", port=4000)