# MODULES

import math as mt


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


def rightAngleTriangleArea():
    value1Name = "base"
    value2Name = "height"
    base = inputLengthPositive(value1Name)
    height = inputLengthPositive(value2Name)
    ans = base * height * 0.5
    return ans


def nonRightAngleTriangleArea():
    value1Name = "adjacent side 1"
    value2Name = "adjacent side 2"
    side1 = inputLengthPositive(value1Name)
    side2 = inputLengthPositive(value2Name)
    angle = inputAngleAcuObt("None")
    ans = 0.5 * side1 * side2 * mt.sin(angle)
    return ans


# quadrilaterals


def rectangleAndParallelogramArea():
    value1Name = "side 1"
    value2Name = "side 2"
    a = inputLengthPositive(value1Name)
    b = inputLengthPositive(value2Name)
    ans = a * b
    return ans


def rhombusAndKiteArea():
    value1Name = "first diagonal"
    value2Name = "second diagonal"
    diag1 = inputLengthPositive(value1Name)
    diag2 = inputLengthPositive(value2Name)
    ans = (diag1 * diag2) / 2
    return ans


# circles


def circleArea():
    choice = int(input("1.Radius 2.Diameter - "))
    while choice < 1 or choice > 2:
        print("Input value is invalid, please reinput")
        choice = int(input("1.Radius 2.Diameter - "))
    match choice:
        case 1:
            valueName = "radius"
            radius = inputLengthPositive(valueName)
            ans = (radius ^ 2) * mt.pi
        case 2:
            valueName = "diameter"
            diameter = inputLengthPositive(valueName)
            ans = ((diameter / 2) ^ 2) * mt.pi
    return ans


def circleCircumference():
    choice = int(input("1.Radius 2.Diameter - "))
    while choice < 1 or choice > 2:
        print("Input value is invalid, please reinput")
        choice = int(input("1.Radius 2.Diameter - "))
    match choice:
        case 1:
            valueName = "radius"
            radius = inputLengthPositive(valueName)
            ans = 2 * radius * mt.pi
        case 2:
            valueName = "diameter"
            diameter = inputLengthPositive(valueName)
            ans = diameter * mt.pi
    return ans


def sectorArea():
    valueName = "radius"
    radius = inputLengthPositive(valueName)
    angle = float(input("Input angle - "))
    angle = inputAngleAcuObt("None")
    ratio = angle / 360
    ans = ratio * mt.pi * (radius ^ 2)
    return ans


def arcLength():
    valueName = "radius"
    radius = inputLengthPositive(valueName)
    angle = float(input("Input angle - "))
    angle = inputAngleAcuObt("None")
    ratio = angle / 360
    ans = 2 * mt.pi * radius * ratio
    return ans


# Trigonometry


# pythagoras
def findHypotPythag():
    value1Name = "opposite side"
    value2Name = "adjacent side"
    a = inputLengthPositive(value1Name)
    b = inputLengthPositive(value2Name)
    ans = mt.sqrt((a ** 2) + (b ** 2))
    return ans


def findHypotSine():
    valueName = "opposite side"
    oppSide = inputLengthPositive(valueName)
    angle = inputAngleAcuObt("None")
    ans = oppSide / mt.sin(angle)
    return ans


def findHypotCosine():
    valueName = "adjacent side"
    adjSide = inputLengthPositive(valueName)
    angle = inputAngleAcuObt("None")
    ans = adjSide / mt.cos(angle)
    return ans


def findSideSineOpp():
    valueName = "hypoteneuse"
    hypot = inputLengthPositive(valueName)
    angle = inputAngleAcuObt("None")
    ans = hypot * mt.sin(angle)
    return ans


def findSideCosineAdj():
    valueName = "hypoteneuse"
    hypot = inputLengthPositive(valueName)
    angle = inputAngleAcuObt("None")
    ans = hypot * mt.cos(angle)
    return ans


def findSideTangentOpp():
    valueName = "adjacent side"
    adjSide = inputLengthPositive(valueName)
    angle = inputAngleAcuObt("None")
    ans = adjSide * mt.tan(angle)
    return ans


def findSideTangentAdj():
    valueName = "opposite side"
    oppSide = inputLengthPositive(valueName)
    angle = inputAngleAcuObt("None")
    ans = oppSide / mt.tan(angle)
    return ans


def findAngleTangent():
    value1Name = "adjacent side"
    adjSide = inputLengthPositive(value1Name)
    value2Name = "opposite side"
    oppSide = inputLengthPositive(value2Name)
    ans = mt.atan(adjSide / oppSide)
    return ans


# rules


def sineRuleAngle(pair1Angle, pair1Side, pair2Side):
    value1Name = "pair 1 side"
    pair1Side = inputLengthPositive(value1Name)
    value2Name = "pair 2 side"
    pair2Side = inputLengthPositive(value2Name)
    value3Name = "pair 1 angle"
    pair1Angle = inputAngleAcuObt(value3Name)
    ans = pair2Side * (mt.sin(pair1Angle) / pair1Side)
    return ans


def sineRuleSide(pair1Angle, pair1Side, pair2Angle):
    value1Name = "pair 1 side"
    pair1Side = inputLengthPositive(value1Name)
    value2Name = "pair 1 angle"
    pair1Angle = inputAngleAcuObt(value2Name)
    value3Name = "pair 2 angle"
    pair2Angle = inputAngleAcuObt(value3Name)
    componentA = pair1Side / mt.sin(pair1Angle)
    ans = mt.sin(pair2Angle) * componentA
    return ans


def cosineRuleSide(oppAngle, side1, side2):
    value1Name = "adjacent side 1"
    side1 = inputLengthPositive(value1Name)
    value2Name = "adjacent side 2"
    side2 = inputLengthPositive(value2Name)
    value3Name = "opposite angle"
    oppAngle = inputAngleAcuObt(value3Name)
    componentA = (side1 ** 2) * (side2 ** 2)
    componentB = side1 * side2 * mt.cos(oppAngle)
    ans = mt.sqrt(componentA - componentB)
    return ans


def cosineRuleAngle(side1, side2, oppSide):
    value1Name = "adjacent side 1"
    side1 = inputLengthPositive(value1Name)
    value2Name = "adjacent side 2"
    side2 = inputLengthPositive(value2Name)
    value3Name = "opposite side"
    oppSide = inputLengthPositive(value3Name)
    componentA = ((side1 ** 2) + (side2 ** 2)) - (oppSide ** 2)
    componentB = 2 * side1 * side2
    componentC = componentA / componentB
    ans = mt.acos(componentC)
    return ans


# Polynomials


# quadratics


def quadraticInput():
    a = float(input("Input x^2 coefficient - "))
    b = float(input("Input x coefficient - "))
    c = float(input("Input constant - "))
    x = float(input("Input x - "))
    componentA = a * (x ** 2)
    componentB = b * x
    ans = componentA + componentB + c
    return ans


def quadraticInput2(a, b, c, x):
    componentA = a * (x ** 2)
    componentB = b * x
    ans = componentA + componentB + c
    return ans


def quadraticRoots():
    a = float(input("Input x^2 coefficient - "))
    b = float(input("Input x coefficient - "))
    c = float(input("Input constant - "))
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


def quadraticVertexX():
    a = float(input("Input x^2 coefficient - "))
    b = float(input("Input x coefficient - "))
    ans = -b / (2 * a)
    return ans


def quadraticVertexY():
    a = float(input("Input x^2 coefficient - "))
    b = float(input("Input x coefficient - "))
    c = float(input("Input constant - "))
    componentA = -b / (2 * a)
    ans = quadraticInput2(a, b, c, componentA)
    return ans


def quadraticFirstDerivValue():
    a = float(input("Input x^2 coefficient - "))
    b = float(input("Input x coefficient - "))
    x = float(input("Input x - "))
    a = 2 * a
    ans = (a * x) + b
    return ans


def quadraticSecondDerivValue():
    a = float(input("Input x^2 coefficient - "))
    x = float(input("Input x - "))
    a = 2 * a
    ans = a * x
    return ans


# cubics


def cubicInput():
    a = float(input("Input x^3 coefficient - "))
    b = float(input("Input x^2 coefficient - "))
    c = float(input("Input x coefficient - "))
    d = float(input("Input constant"))
    x = float(input("Input x - "))
    componentA = a * (x ** 3)
    componentB = b * (x ** 2)
    componentC = c * x
    ans = componentA + componentB + componentC + d
    return ans


def cubicFirstDerivValue():
    a = float(input("Input x^3 coefficient - "))
    b = float(input("Input x^2 coefficient - "))
    c = float(input("Input x coefficient - "))
    x = float(input("Input x - "))
    a = 3 * a
    b = 2 * b
    ans = ((a ** 2) * x) + (b * x) + c
    return ans


def cubicSecondDerivValue():
    a = float(input("Input x^3 coefficient - "))
    b = float(input("Input x^2 coefficient - "))
    x = float(input("Input x - "))
    a = 6 * a
    b = 2 * b
    ans = (a * x) + b
    return ans


def cubicThirdDerivValue():
    a = float(input("Input x^3 coefficient - "))
    x = float(input("Input x - "))
    a = 6 * a
    ans = a * x
    return ans


# quartics


def quarticInput():
    a = float(input("Input x^4 coefficient - "))
    b = float(input("Input x^3 coefficient - "))
    c = float(input("Input x^2 coefficient - "))
    d = float(input("Input x coefficient - "))
    e = float(input("Input constant"))
    x = float(input("Input x - "))
    componentA = a * (x ** 4)
    componentB = b * (x ** 3)
    componentC = c * (x ** 2)
    componentD = d * x
    ans = componentA + componentB + componentC + componentD + e
    return ans


def quarticFirstDerivValue():
    a = float(input("Input x^4 coefficient - "))
    b = float(input("Input x^3 coefficient - "))
    c = float(input("Input x^2 coefficient - "))
    d = float(input("Input x coefficient - "))
    x = float(input("Input x - "))
    a = 4 * a
    b = 3 * b
    c = 2 * c
    ans = ((a ** 3) * x) + (b * (x ** 2)) + (c * x) + d
    return ans


def quarticSecondDerivValue():
    a = float(input("Input x^4 coefficient - "))
    b = float(input("Input x^3 coefficient - "))
    c = float(input("Input x^2 coefficient - "))
    x = float(input("Input x - "))
    a = 12 * a
    b = 6 * b
    c = 2 * c
    ans = (a * (x ** 2)) + (b * x) + c
    return ans


def quarticThirdDerivValue():
    a = float(input("Input x^4 coefficient - "))
    b = float(input("Input x^3 coefficient - "))
    x = float(input("Input x - "))
    a = 24 * a
    b = 6 * b
    ans = (a * x) + b
    return ans


def quarticFourthDerivValue():
    a = float(input("Input x^3 coefficient - "))
    x = float(input("Input x - "))
    a = 24 * a
    ans = a * x
    return ans


# Physics


def newtonSecondLawForce():
    valueName = "mass"
    mass = inputLengthPositive(valueName)
    valueName = "acceleration"
    acceleration = inputLengthPositive(valueName)
    ans = mass * acceleration
    return ans


def newtonSecondLawMass():
    valueName = "force"
    force = inputLengthPositive(valueName)
    valueName = "acceleration"
    acceleration = inputLengthPositive(valueName)
    ans = force / acceleration
    return ans


def newtonSecondLawAcc():
    valueName = "force"
    force = inputLengthPositive(valueName)
    valueName = "mass"
    mass = inputLengthPositive(valueName)
    ans = force * mass
    return ans


# Others


def factorial():
    valueName = "a positive number"
    number = inputLengthPositive(valueName)
    ans = mt.factorial(number)
    return ans