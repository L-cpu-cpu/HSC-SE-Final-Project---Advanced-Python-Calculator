import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np


def regressionLinear(x, y):
    model = LinearRegression()
    model.fit(x, y)
    score = model.score(x, y)
    formula = f"y = {model.coef_[0]:.4f}x + {model.intercept_:.4f} R² = {score:.4f}"
    return formula