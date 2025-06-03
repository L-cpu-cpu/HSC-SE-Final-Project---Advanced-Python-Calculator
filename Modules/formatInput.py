# MODULES

import sqlite3 as sql

import pandas as pd

from Modules import dbFunctions as rR

from Modules import variables as varis

from flask import session

# Replaces saved results with their values

def formatInputSaved(input):
    # INITIATE CONNECTION

    conn = sql.connect("DataBases/savedResults.db")

    # RETRIEVE KEYWORDS
    query = ('SELECT keyword FROM savedResults')
    retrievedKeywords = pd.read_sql_query(query, conn).to_numpy()


    # FORMAT ARRAY
    keywordArray = []
    for i in range(len(retrievedKeywords)):
        keywordArray.append(str(retrievedKeywords[i]).replace("[","").replace("]","").replace("'",""))
    newInput = input
    for i in range(len(keywordArray)):
        if keywordArray[i] in input:
            newInput = newInput.replace(str(keywordArray[i]), str(rR.queryResult(keywordArray[i])))
        else:
            pass

    # CLOSE CONNECTION
    conn.close()

    return newInput


# Replaces session variables with their values

def formatInputVar(EQinput):
    newInput = EQinput
    # FORMAT ARRAY
    for i in range(len(varis.variables)):
        if varis.variables[i][0] in EQinput:
            newInput = newInput.replace(varis.variables[i][0], str(varis.variables[i][1]))
        else:
            pass

    return newInput


# Replaces '^' with ** so eval() works

def replacePower(EQinput):
    newInput = EQinput
    newInput = newInput.replace("^", "**")
    return newInput


# Adds 'mt.' to math module functions so eval() works

def addMT(EQinput):
    newInput = EQinput
    mtFunctions = [["SIN", "mt.sin"], ["COS", "mt.cos"], ["TAN", "mt.tan"], ["SQRT", "mt.sqrt"], ["PI", "mt.pi"], ["CBRT", "mt.cbrt"], ["EXP", "mt.exp"], ["LOG", "mt.log"], ["DEGREES", "mt.degrees"], ["RADIANS", "mt.radians"], ["ACOS", "mt.acos"], ["ASIN", "mt.asin"], ["ATAN", "mt.atan"], ["E", "mt.e"], ["FACTORIAL", "mt.factorial"]]
    for i in range(len(mtFunctions)):
        if mtFunctions[i][0] in newInput:
            newInput = newInput.replace(str(mtFunctions[i][0]), mtFunctions[i][1])
        else:
            pass
    return newInput


# Replaces ans with the last result
def formatInputAns(EQinput, ans):
    newInput = EQinput
    ans = session.get('ans', ans)  # Get the last result from session or use provided ans
    newInput = newInput.replace("ans", str(ans))
    return newInput