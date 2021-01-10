"""
Exercise 4: Try out the second-, third- and fourth-order Runge-Kutta methods discussed above
on the problem defined by Eq. (2.7). Compare the computational effort for a given accuracy
with that of other methods.
"""
import numpy as np


def f(x, y):
    return -x*y


def RK2(f, x0, xe, y0, h):
    times = np.arange(x0, xe + h, h)
    solutionx, solutiony = [], []
    y = y0
    nstep = 0
    for x in times:
        solutionx.append(x)
        solutiony.append(y)
        k = h * f(x, y)
        y += h * f(x + 0.5 * h, y + 0.5 * k)
        if x == 3.0 or x == 1.0:
            exact = np.exp(-x**2/2)
            diff = exact - solutiony[nstep]
            print("step \t     x \t\t    y \t\t exact \t\t diff")
            print("{:3} \t {:.5f} \t {:.5E} \t {:.5E} \t {:.5E}".format(
                nstep, solutionx[nstep], solutiony[nstep], exact, diff))
        nstep += 1
    return times, np.array([solutionx, solutiony], float)


def RK3(f, x0, xe, y0, h):
    times = np.arange(x0, xe + h, h)
    solutionx, solutiony = [], []
    y = y0
    x = x0
    nstep = 0
    for x in times:
        solutionx.append(x)
        solutiony.append(y)
        k1 = h * f(x, y)
        k2 = h * f(x + 0.5 * h, y + 0.5 * k1)
        k3 = h * f(x + 0.5 * h, y + 0.5 * k2)
        k4 = h * f(x + h, y + k3)
        y += (k1 + 2 * (k2 + k3) + k4) / 6
        if x == 3.0 or x == 1.0:
            exact = np.exp(-x**2/2)
            diff = exact - solutiony[nstep]
            print("step \t     x \t\t    y \t\t exact \t\t diff")
            print("{:3} \t {:.5f} \t {:.5E} \t {:.5E} \t {:.5E}".format(
                nstep, solutionx[nstep], solutiony[nstep], exact, diff))
        nstep += 1
    return times, np.array([solutionx, solutiony], float)


def RK4(f, x0, xe, y0, h):
    times = np.arange(x0, xe + h, h)
    solutionx, solutiony = [], []
    x = x0
    y = y0
    nstep = 0
    for x in times:
        solutionx.append(x)
        solutiony.append(y)
        k1 = h * f(x, y)
        k2 = h * f(x + 0.5 * h, y + 0.5 * k1)
        k3 = h * f(x + 0.5 * h, y + 0.5 * k2)
        k4 = h * f(x + h, y + k3)
        y += (k1 + 2 * (k2 + k3) + k4) / 6
        if x == 3.0 or x == 1.0:
            exact = np.exp(-x**2/2)
            diff = exact - solutiony[nstep]
            print("step \t     x \t\t    y \t\t exact \t\t diff")
            print("{:3} \t {:.5f} \t {:.5E} \t {:.5E} \t {:.5E}".format(
                nstep, solutionx[nstep], solutiony[nstep], exact, diff))
        nstep += 1
    return times, np.array([solutionx, solutiony], float)


def main():
    h = 0.01
    x0 = 0.0
    y0 = 1.0
    xe = 3.0
    xed = 3.0
    while h > 0.0:
        h = float(
            input(f"\n Enter step size [h= {h:.2E}] (.le. 0 to stop): ") or h)
        if h <= 0.0:
            break
        print("Using Runge-Kutta Second order method:")
        times, soly = RK2(f, x0, xe, y0, h)
        print()
        print("Using Runge-Kutta Third order method:")
        times, sol1y = RK3(f, x0, xe, y0, h)
        print()
        print("Using Runge-Kutta Fourth order method:")
        times, sol2y = RK4(f, x0, xe, y0, h)
        if xe > 3.0:
            x = np.arange(x0, xe+h, h)
            exact = np.exp(-x**2/2)
            diff = exact - sol2y[1]
            print(f"\n The table for the values upto {xe:.4F} using RK4: ")
            print("\t     x \t\t    y \t\t exact \t\t diff")
            for i in range(len(x)):
                print("\t {:.5f} \t {:.5E} \t {:.5E} \t {:.5E}".format(
                    sol2y[0][i], sol2y[1][i], exact[i], diff[i]))
        print()
        xe = float(
            input("If you want to check higher values of x, enter here: \n ") or xed)


if __name__ == "__main__":
    main()
