r"""
Exercise 1.2: Using any function whose definite integral you can compute analytically, 
investigate the accuracy of the various quadrature methods discussed above for 
different values of h.

"""
import math
import numpy as np


def f(x):
    return np.exp(x)


def Simpson13(f, x0, xn, h):
    N = int((xn-x0)/h)
    Sum = f(x0)
    fac = 2
    for i in range(1, N):
        if (fac == 2):
            fac = 4.0
        else:
            fac = 2.0
        x = x0 + i*h
        Sum += fac*f(x)
    Sum += f(xn)
    xint = Sum*h/3
    return xint


def Simpson38(f, x0, xn, h):
    N = int((xn-x0)/h)
    Sum = f(x0)
    for i in range(1, N):
        if (i % 3 == 1 or i % 3 == 2):
            fac = 3.0
        else:
            fac = 2.0
        x = x0 + i*h
        Sum += fac*f(x)
    Sum += f(xn)
    xint = Sum*3*h/8
    return xint


def BooleRule(f, x0, xn, h):
    N = int((xn-x0)/h)
    Sum = 0.0
    for i in range(N):
        if (i == 0):
            fac = 7.0
        elif i % 4 == 1 or i % 4 == 3:
            fac = 32.0
        elif i % 4 == 2:
            fac = 12.0
        else:
            fac = 14.0
        x = x0 + i*h
        Sum += fac*f(x)
    Sum += f(xn)
    xint = 2*h*Sum/45
    return xint


def main():
    exact = np.exp(1.0) - 1.0
    x0 = 0.0
    xn = 1.0
    h = float(input("Enter h: "))
    Result1 = Simpson13(f, x0, xn, h)
    Result2 = Simpson38(f, x0, xn, h)
    Result3 = BooleRule(f, x0, xn, h)
    diff1 = exact - Result1
    diff2 = exact - Result2
    diff3 = exact - Result3
    print("The value of the integral for")
    print(
        "Exact Value: {: .5E} \n Simpson 1/3 Method: {: .5E}  Error: {:.5E}".format(exact, Result1, diff1))
    print("Simpson 3/8 Method: {:.5E} Error: {:.5E}".format(Result2, diff2))
    print("Boole Method: {:.5E} Error: {:.5E}".format(Result3, diff3))


if __name__ == "__main__":
    main()
