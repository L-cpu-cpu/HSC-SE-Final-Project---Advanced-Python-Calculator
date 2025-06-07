import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np
from flask import session
import matplotlib.pyplot as plt
import os
import uuid
import matplotlib
matplotlib.use("Agg")


def regressionLinear(x, y):
    model = LinearRegression()
    model.fit(x, y)
    score = model.score(x, y)
    rounding = session.get("rounding", 2)
    formula = f"y = {round(model.coef_[0], rounding)}x + {round(model.intercept_, rounding)} R² = {round(score, rounding)}"

    # Generate the regression line
    x_range = np.linspace(min(x)[0], max(x)[0], 100).reshape(-1, 1)
    y_pred_line = model.predict(x_range)

    # Create plot
    plt.figure()
    plt.scatter(x, y, color="blue", label="Data Points")
    plt.plot(x_range, y_pred_line, color="red", label="Regression Line")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Linear Regression")
    plt.legend()

    # Save plot to static folder with unique filename
    unique_filename = f"regression_plot_{uuid.uuid4().hex}.png"
    plot_path = os.path.join("static", unique_filename)
    plt.savefig(plot_path)
    plt.close()

    return formula, unique_filename