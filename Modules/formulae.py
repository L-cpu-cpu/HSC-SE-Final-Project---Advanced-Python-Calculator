# MODULES

import math as mt


from Modules import formatInput as fi


from flask import session
# INPUTS


def inputLengthPositive(inputWord):
    length = float(input(f"Input {inputWord} - "))
    while length <= 0:
        print("Input value is negative, please reinput")
        length = float(input(f"Input {inputWord} - "))
    return length


def inputAngleAcuObt(inputWordOverride):
    if inputWordOverride == "None":
        angle = float(input("Input angle - "))
        while angle <= 0 or angle >= 180:
            print("Input value is outside range, please reinput")
            angle = float(input("Input angle - "))
    else:
        angle = float(input(f"Input {inputWordOverride} - "))
        while angle <= 0 or angle >= 180:
            print("Input value is outside range, please reinput")
            angle = float(input(f"Input {inputWordOverride} - "))
    return angle


# FORMULAE


# Areas and Perimeters


# triangles


def rightAngleTriangleArea(base, height):
    ans = base * height * 0.5
    return ans


def nonRightAngleTriangleArea(side1, side2, angle):
    ans = 0.5 * side1 * side2 * mt.sin(angle)
    return ans


# quadrilaterals


def rectangleAndParallelogramArea(side1, side2):
    ans = side1 * side2
    return ans


def rhombusAndKiteArea(diag1, diag2):
    ans = (diag1 * diag2) / 2
    return ans


# circles


def circleArea(radius):
    ans = (radius ^ 2) * mt.pi
    return ans


def circleCircumference(radius):
    ans = 2 * radius * mt.pi
    return ans


def sectorArea(radius, angle):
    ratio = angle / 360
    ans = ratio * mt.pi * (radius ^ 2)
    return ans


def arcLength(radius, angle):
    ratio = angle / 360
    ans = 2 * mt.pi * radius * ratio
    return ans


# Trigonometry


# pythagoras
def findHypotPythag(oppSide, adjSide):
    ans = mt.sqrt((oppSide ** 2) + (adjSide ** 2))
    return ans


def findHypotSine(oppSide, angle):
    ans = oppSide / mt.sin(angle)
    return ans


def findHypotCosine(adjSide, angle):
    ans = adjSide / mt.cos(angle)
    return ans


def findSideSineOpp(hypot, angle):
    ans = hypot * mt.sin(angle)
    return ans


def findSideCosineAdj(hypot, angle):
    ans = hypot * mt.cos(angle)
    return ans


def findSideTangentOpp(adjSide, angle):
    ans = adjSide * mt.tan(angle)
    return ans


def findSideTangentAdj(oppSide, angle):
    ans = oppSide / mt.tan(angle)
    return ans


def findAngleTangent(adjSide, oppSide):
    ans = mt.atan(adjSide / oppSide)
    return ans


# rules


def sineRuleAngle(angleA, sideA, sideB):
    ans = sideB * (mt.sin(angleA) / sideA)
    return ans


def sineRuleSide(angleA, sideA, angleB):
    componentA = sideA / mt.sin(angleA)
    ans = mt.sin(angleB) * componentA
    return ans


def cosineRuleSide(oppAngle, sideA, sideB):
    componentA = (sideA ** 2) * (sideB ** 2)
    componentB = 2 * sideA * sideB * mt.cos(oppAngle)
    ans = mt.sqrt(componentA - componentB)
    return ans


def cosineRuleAngle(sideA, sideB, oppSide):
    componentA = ((sideA ** 2) + (sideB ** 2)) - (oppSide ** 2)
    componentB = 2 * sideA * sideB
    componentC = componentA / componentB
    ans = mt.acos(componentC)
    return ans


# Polynomials


# quadratics


def quadraticInput(a, b, c, x):
    componentA = a * (x ** 2)
    componentB = b * x
    ans = componentA + componentB + c
    return ans


def quadraticRoots(a, b, c):
    delta = b ** 2 - (4 * a * c)
    if delta < 0:
        ans = "No real solutions"
    elif delta == 0:
        ans = -b / (2 * a)
    else:
        choice = int(input("1.x (1) 2.x (2) - "))
        while choice < 1 or choice > 2:
            print("Input value is invalid, please reinput")
            choice = int(input("1.x (1) 2.x (2) - "))
        match choice:
            case 1:
                componentA = -b + mt.sqrt(delta)
                ans = componentA / (2 * a)
            case 2:
                componentA = -b - mt.sqrt(delta)
                ans = componentA / (2 * a)
    return ans


def quadraticVertexX(a, b):
    ans = -b / (2 * a)
    return ans


def quadraticVertexY(a, b, c):
    componentA = -b / (2 * a)
    ans = quadraticInput(a, b, c, componentA)
    return ans


def quadraticFirstDerivValue(a, b, x):
    a = 2 * a
    ans = (a * x) + b
    return ans


def quadraticSecondDerivValue(a, x):
    a = 2 * a
    ans = a * x
    return ans


# cubics


def cubicInput(a, b, c, d, x):
    componentA = a * (x ** 3)
    componentB = b * (x ** 2)
    componentC = c * x
    ans = componentA + componentB + componentC + d
    return ans


def cubicFirstDerivValue(a, b, c, x):
    a = 3 * a
    b = 2 * b
    ans = ((a ** 2) * x) + (b * x) + c
    return ans


def cubicSecondDerivValue(a, b, x):
    a = 6 * a
    b = 2 * b
    ans = (a * x) + b
    return ans


def cubicThirdDerivValue(a, x):
    a = 6 * a
    ans = a * x
    return ans


# quartics


def quarticInput(a, b, c, d, e, x):
    componentA = a * (x ** 4)
    componentB = b * (x ** 3)
    componentC = c * (x ** 2)
    componentD = d * x
    ans = componentA + componentB + componentC + componentD + e
    return ans


def quarticFirstDerivValue(a, b, c, d, x):
    a = 4 * a
    b = 3 * b
    c = 2 * c
    ans = ((a ** 3) * x) + (b * (x ** 2)) + (c * x) + d
    return ans


def quarticSecondDerivValue(a, b, c, x):
    a = 12 * a
    b = 6 * b
    c = 2 * c
    ans = (a * (x ** 2)) + (b * x) + c
    return ans


def quarticThirdDerivValue(a, b, x):
    a = 24 * a
    b = 6 * b
    ans = (a * x) + b
    return ans


def quarticFourthDerivValue(a, x):
    a = 24 * a
    ans = a * x
    return ans


# Physics


def newtonSecondLawForce(mass, acceleration):
    ans = mass * acceleration
    return ans


def newtonSecondLawMass(force, acceleration):
    ans = force / acceleration
    return ans


def newtonSecondLawAcc(force, mass):
    ans = force * mass
    return ans


# Formula dictionary
formula_map = {
    'Right angle Triangles': rightAngleTriangleArea,
    'Non-right angle Triangles': nonRightAngleTriangleArea,
    "Rectangles and Parallelograms": rectangleAndParallelogramArea,
    "Rhombuses and Kites": rhombusAndKiteArea,
    "Area": circleArea,
    "Circumference": circleCircumference,
    "Sector Area": sectorArea,
    "Arc Length": arcLength,
    "Hypotenuse": findHypotPythag,
    "Hypotenuse (Sine)": findHypotSine,
    "Hypotenuse (Cosine)": findHypotCosine,
    "Opposite": findSideSineOpp,
    "Adjacent": findSideCosineAdj,
    "Tangent (Opposite)": findSideTangentOpp,
    "Tangent (Adjacent)": findSideTangentAdj,
    "Angle (Tangent)": findAngleTangent,
    "Sine Rule (Angle)": sineRuleAngle,
    "Sine Rule (Side)": sineRuleSide,
    "Cosine Rule (Side)": cosineRuleSide,
    "Cosine Rule (Angle)": cosineRuleAngle,
    "Find y (quadratic)": quadraticInput,
    "Quadratic Formula": quadraticRoots,
    "Vertex (x)": quadraticVertexX,
    "Vertex (y)": quadraticVertexY,
    "First derivative (quadratic)": quadraticFirstDerivValue,
    "Second derivative (quadratic)": quadraticSecondDerivValue,
    "Find y (cubic)": cubicInput,
    "First derivative (cubic)": cubicFirstDerivValue,
    "Second derivative (cubic)": cubicSecondDerivValue,
    "Third derivative (cubic)": cubicThirdDerivValue,
    "Find y (quartic)": quarticInput,
    "First derivative (quartic)": quarticFirstDerivValue,
    "Second derivative (quartic)": quarticSecondDerivValue,
    "Third derivative (quartic)": quarticThirdDerivValue,
    "Fourth derivative": quarticFourthDerivValue,
    "Second Law (Force)": newtonSecondLawForce,
    "Second Law (Mass)": newtonSecondLawMass,
    "Second Law (Acceleration)": newtonSecondLawAcc,
}


# Run forumla
def run_formula(formula_name, input_list, ans):
    try:
        ans = session.get('ans', ans)  # Get the last result from session or use provided ans
        inputs = [fi.formatInputAns(x, ans) for x in input_list]
        inputs = [fi.formatInputSaved(x) for x in inputs]
        inputs = [fi.formatInputVar(x) for x in inputs]
        inputs = [fi.addMT(x) for x in inputs]
        # Convert all inputs to float
        inputs = [float(x) for x in inputs]

        # Look up the right function
        func = formula_map.get(formula_name)

        if not func:
            return "Formula not found."

        # Call the function with unpacked inputs
        result = func(*inputs)
        rounding = session.get("rounding", 2)
        return round(result, rounding)

    except Exception as e:
        return f"Error: {str(e)}"