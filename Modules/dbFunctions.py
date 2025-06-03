# MODULES

import sqlite3 as sql

import pandas as pd


from Modules import variables as var



# RETRIEVE RESULT
def queryResult(keyword):
    # INITIATE CONNECTION
    conn = sql.connect("DataBases/savedResults.db")

    #RETRIEVE
    query = (f'SELECT result FROM savedResults WHERE keyword="{keyword}"')
    retrievedResult = str(pd.read_sql_query(query, conn).to_numpy()[0, 0])

    # CLOSE CONNECTION
    conn.close()

    return retrievedResult

def insertTable(keyword, value):
    try:
        conn = sql.connect("Databases/savedResults.db")
        cursor = conn.cursor()
        query = 'INSERT OR REPLACE INTO savedResults (keyword, result) VALUES (?, ?)'
        values = (keyword, str(value))
        cursor.execute(query, values)
        conn.commit()
        conn.close()
    except Exception as e:
        print(f"[DB ERROR] Failed to insert: {e}")


def removeTable(keyword):
    # INITIATE CONNECTION

    conn = sql.connect("DataBases/savedResults.db")

    #CREATE A CURSOR
    cursor = conn.cursor()
    #A cursor allows for the execution of SQLite queries
    query = (f'DELETE FROM savedResults WHERE keyword="{keyword}"')
    cursor.execute(query)
    #Executes the query using the cursor
    conn.commit()
    #This ensures that the changes are made
    # CLOSE CONNECTION
    conn.close()


def saveVar(varName, result):
    for i in range(len(var.variables)):
        if varName == var.variables[i][0]:
            var.variables[i][1] = result
        else:
            pass