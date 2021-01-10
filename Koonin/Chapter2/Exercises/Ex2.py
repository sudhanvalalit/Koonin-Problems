'''
Exercise 2: Apply the Adams-Bashforth two and four step algorithms to the example
defined by eq (2.7) using Euler's method (2.6) to generate the values of y needed to start
the recursion relation. Investigate the accuracy of y(x) for various values of h by 
comparing with the analytical results and by applying the reversibility test described
in Exercise 2.1

'''

import numpy as np
import matplotlib.pyplot as plt


def f(x, y):
    return -x*y


def ab_twoStep(f, x0, xe, y0, h):
    xvalues = np.arange(x0, xe+h, h)
    solutionx, solutiony = [], []
    y = y0
    yprev = 0
    nstep = 0
    for x in xvalues:
        solutionx.append(x)
        solutiony.append(y)
        yprev = solutiony[nstep-1]
        y += h*(1.5*f(x, y) - 0.5*f(x-h, yprev))
        if x == 3.0 or x == 1.0:
            exact = np.exp(-x**2/2)
            diff = exact - solutiony[nstep]
            print("step \t     x \t\t    y \t\t exact \t\t diff")
            print("{:3} \t {:.5f} \t {:.5E} \t {:.5E} \t {:.5E}".format(
                nstep, solutionx[nstep], solutiony[nstep], exact, diff))
        nstep += 1
    return np.array([solutionx, solutiony])


def ab_fourStep(f, x0, xe, y0, h):
    xvalues = np.arange(x0, xe+h, h)
    solutionx, solutiony = [], []
    y = y0
    nstep = 0
    for x in xvalues:
        solutionx.append(x)
        solutiony.append(y)
        yp1 = solutiony[nstep-1]
        if nstep - 2 < 0:
            yp2 = y0
        else:
            yp2 = solutiony[nstep-2]
        if nstep - 3 < 0:
            yp3 = y0
        else:
            yp3 = solutiony[nstep-3]
        y += (h/24)*(55*f(x, y) - 59*f(x-h, yp1) +
                     37*f(x-2*h, yp2)-9*f(x-3*h, yp3))
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
    while h > 0.0:
        h = float(
            input(f"\n Enter step size [h={h:.2E}] (.le. 0 to stop): ") or h)
        if h <= 0.0:
            break
        print("Using Adams Bashforth two step method:")
        solx, soly = ab_twoStep(f, x0, xe, y0, h)
        print()
        print("Using Adams Bashforth four step method:")
        sol4x, sol4y = ab_fourStep(f, x0, xe, y0, h)


if __name__ == "__main__":
    main()
