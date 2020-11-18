#
import numpy as np


def f(x, y):
    return -x*y


def main():
    h = 0.01
    while h > 0:
        h = float(input("Enter step size (.le. 0 to stop): "))
        if (h <= 0.0):
            break
        nstep = int(3.0/h)
        y = 1.0
        for i in range(nstep):
            x = i*h
            y += h*f(x, y)
            diff = np.exp(-0.5*(x+h)**2) - y
            print("{:3} \t {:.5f} \t {:.5E} \t {:.5E}".format(i, x+h, y, diff))


if __name__ == "__main__":
    main()
