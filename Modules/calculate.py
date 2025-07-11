# MODULES

from Modules import dbFunctions as dbFunc


from Modules import formatInput as fi


from flask import session

import math as mt
# CALCULATE


def calculate(equation, ans):
    # Check for variables, saved results, python math functions, '^'
    equation = fi.formatInputAns(equation, ans)
    equation = fi.replacePower(equation)
    equation = fi.formatInputSaved(equation)
    equation = fi.formatInputVar(equation)
    equation = fi.addMT(equation)
    ans = eval(str(equation))
    rounding = session.get("rounding", 2)
    return round(ans, rounding)


def postCalcVar(result, varName):
    # Save as variable, assume yes for now:
    dbFunc.saveVar(varName, result)

def postCalcTable(result, keyword):
    # Save to database, assume yes for now:
    dbFunc.insertTable(keyword, result)
