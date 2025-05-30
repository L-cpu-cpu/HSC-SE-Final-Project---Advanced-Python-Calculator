# MODULES

import sqlite3 as sql

import pandas as pd

import dbFunctions as rR

import variables as vars


#Replaces saved results with their values

def formatInputSaved(input):
    # INITIATE CONNECTION

    conn = sql.connect("DataBases/savedResults.db")

    # RETRIEVE KEYWORDS

    query = ('SELECT keyword FROM savedResults')
    retrievedKeywords = pd.read_sql_query(query, conn).to_numpy()


    #FORMAT ARRAY

    keywordArray = []
    for i in range(len(retrievedKeywords)):
        keywordArray.append(str(retrievedKeywords[i]).replace("[","").replace("]","").replace("'",""))
    newInput = input
    for i in range(len(keywordArray)):
        if keywordArray[i] in input:
            newInput = newInput.replace(str(keywordArray[i]), rR.queryResult(keywordArray[i]))
        else:
            pass

    # CLOSE CONNECTION
    conn.close()

    return newInput


#Replaces session variables with their values

def formatInputVar(EQinput):
    newInput = EQinput
    #FORMAT ARRAY
    for i in range(len(vars.variables)):
        if vars.variables[i][0] in EQinput:
            newInput = newInput.replace(vars.variables[i][0], str(vars.variables[i][1]))
        else:
            pass

    return newInput