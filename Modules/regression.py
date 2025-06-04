import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np
from flask import session


def regressionLinear(x, y):
    model = LinearRegression()
    model.fit(x, y)
    score = model.score(x, y)
    rounding = session.get("rounding", 2)
    formula = f"y = {round(model.coef_[0], rounding)}x + {round(model.intercept_, rounding)} R² = {round(score, rounding)}"
    return formula