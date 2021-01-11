"""
Exercise 5: The two coupled differential equations
    dy/dt = p ; dp/dt = -4pi^2 y

define simple harmonic motion with period 1. By generalizing one of the single variable
formulas given above to this two variable case, integrate these equations with any particular
initial conditions you choose aand investigate the accuracy with which the system
returns to its initial state at integral values of t.
"""
import numpy as np
import matplotlib.pyplot as plt


def f(x, yvec):
    y, p = yvec[0], yvec[1]
    f1 = p
    f2 = -4 * np.pi**2*y
    return np.array([f1, f2], float)


def RK4(f, x0, xe, y0, h):
    times = np.arange(x0, xe + h, h)
    solutionx, solutiony = [], []
    x = x0
    y = y0
    for x in times:
        solutionx.append(y[0])
        solutiony.append(y[1])
        k1 = h * f(x, y)
        k2 = h * f(x + 0.5 * h, y + 0.5 * k1)
        k3 = h * f(x + 0.5 * h, y + 0.5 * k2)
        k4 = h * f(x + h, y + k3)
        y += (k1 + 2 * (k2 + k3) + k4) / 6
    return times, np.array([solutionx, solutiony], float)


def main():
    h = 0.1
    t0 = 0.0
    te = 1.0
    # Inside the trapped region
    xInput = np.array([.10, .1])
    while h > 0.0:
        h = float(
            input(f"\n Enter step size [h= {h:.2E}] (.le. 0 to stop): ") or h)
        if h <= 0.0:
            break
        print("Using Runge-Kutta Fourth order method:")
        times, result = RK4(f, t0, te, xInput, h)
        print()
        print("\t times \t\t     x \t\t    y")
        for i in range(len(times)):
            print("\t{:.3E}\t {:.5E} \t {:.5E} ".format(times[i],
                                                        result[0][i], result[1][i]))
        plt.plot(result[0, :], result[1, :])
        plt.show()


if __name__ == "__main__":
    main()
