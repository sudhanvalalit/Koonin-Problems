"""
Exercise 3: Apply the Taylor series method (2.10) and the implicit method (2.18) 
to the example of Eq. (2.7) and obtain the results shown in Table 2.1. Investigate 
the accuracy of integration to larger values of x.
"""
import numpy as np


def f(x):
    return -x[0]*x[1]


def partial_derivative(f, x, n, h):
    """
    Input:
        f   -   Function of N variables 
        x   -   An array of N values
        n   -   nth index for taking the partial derivative
        h   -   step size
    """
    x1 = x.copy()
    x2 = x.copy()
    x3 = x.copy()
    x4 = x.copy()
    x1[n] -= 2.0 * h
    x2[n] -= h
    x3[n] += h
    x4[n] += 2.0 * h
    dfdx = (f(x1) - 8.0 * f(x2) + 8.0 * f(x3) - f(x4)) / (
        12.0 * h
    )
    return dfdx


def taylor_series(f, x0, xe, y0, h):
    xvalues = np.arange(x0, xe+h, h)
    solutionx, solutiony = [], []
    y = y0
    nstep = 0
    for x in xvalues:
        solutionx.append(x)
        solutiony.append(y)
        x1 = np.array([x, y])
        fx = partial_derivative(f, x1, 0, h)
        fy = partial_derivative(f, x1, 1, h)
        y += h*f(x1) + 0.5*h**2*(fx + f(x1)*fy)
        if x == 3.0 or x == 1.0:
            exact = np.exp(-x**2/2)
            diff = exact - solutiony[nstep]
            print("step \t     x \t\t    y \t\t exact \t\t diff")
            print("{:3} \t {:.5f} \t {:.5E} \t {:.5E} \t {:.5E}".format(
                nstep, solutionx[nstep], solutiony[nstep], exact, diff))
        nstep += 1
    return np.array([solutionx, solutiony])


def implicit_method(f, x0, xe, y0, h):
    xvalues = np.arange(x0, xe+h, h)
    solutionx, solutiony = [], []
    y = y0
    nstep = 0
    for x in xvalues:
        solutionx.append(x)
        solutiony.append(y)
        x1 = np.array([x, 1])
        x2 = np.array([x+h, 1])
        y = ((1+0.5*f(x1)*h)/(1-0.5*f(x2)*h))*y
        if x == 3.0 or x == 1.0:
            exact = np.exp(-x**2/2)
            diff = exact - solutiony[nstep]
            print("step \t     x \t\t    y \t\t exact \t\t diff")
            print("{:3} \t {:.5f} \t {:.5E} \t {:.5E} \t {:.5E}".format(
                nstep, solutionx[nstep], solutiony[nstep], exact, diff))
        nstep += 1
    return np.array([solutionx, solutiony])


def main():
    h = 0.01
    x0 = 0.0
    y0 = 1.0
    xe = 3.0
    xed = 3.0
    while h > 0.0:
        h = float(
            input(f"\n Enter step size [h = {h:.2E}] (.le. 0 to stop): ") or h)
        if h <= 0.0:
            break
        print("Using Taylor Series (2.10) method:")
        solx, soly = taylor_series(f, x0, xe, y0, h)
        print()
        print("Using Implicit method (2.18):")
        sol4x, sol4y = implicit_method(f, x0, xe, y0, h)
        if xe > 3.0:
            x = np.arange(x0, xe+h, h)
            exact = np.exp(-x**2/2)
            diff = exact - sol4y
            print(f"\n The table for the values upto {xe:.4F}: ")
            print("\t     x \t\t    y \t\t exact \t\t diff")
            for i in range(len(x)):
                print("\t {:.5f} \t {:.5E} \t {:.5E} \t {:.5E}".format(
                    x[i], sol4y[i], exact[i], diff[i]))
        print()
        xe = float(
            input(f"If you want to check higher values of x [>{xed}], enter here: \n ") or xed)


if __name__ == "__main__":
    main()
