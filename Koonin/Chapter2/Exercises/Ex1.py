'''
Exercise 2.1: A simple and often stringent test of an accurate numerical
integration is to use the find value of y obtained as the initial condition
to integrate backward from the final value of x to the starting point. The
extent to which the resulting value of y differs from the original initial
condlition is then a measure of the inaccuracy. Apply this test to the
example above.
'''
import numpy as np


def f(x, y):
    return -x*y


def main():
    h = 0.01

    while h > 0.0:
        h = float(input("\n Enter step size (.le. 0 to stop): "))
        if h <= 0.0:
            break
        nstep = int(3.0/h)
        y = 1.0
        for i in range(nstep+1):
            x = i*h
            y += h*f(x, y)
        #    diff = np.exp(-0.5*(x+h)**2) - y
        #    print("{:3} \t {:.5f} \t {:.5E} \t {:.5E}".format(i, x+h, y, diff))
        print("Final y result: {:.5E} at x = {:.5f}".format(y, x))
        for i in range(nstep, 0, -1):
            x = i*h
            y += h*f(x, y)
            diff = np.exp(-0.5*(x)**2) - y
            if x == 3.0 or x == 1.0:
                exact = np.exp(-x**2/2)
                diff = exact - y
                print("step \t     x \t\t    y \t\t exact \t\t diff")
                print("{:3} \t {:.5f} \t {:.5E} \t {:.5E} \t {:.5E}".format(
                    nstep - i, x, y, exact, diff))


if __name__ == "__main__":
    main()
