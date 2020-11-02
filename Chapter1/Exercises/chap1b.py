# Code for integration of a given function

import math
import numpy as np


def func(x):
    return np.exp(x)


def main():
    exact = np.exp(1.0) - 1.0
    N = 2
    while N >= 2:
        N = int(input("Enter N even ( .lt 2 to stop) : "))
        if N < 2:
            break
        if np.mod(N, 2) != 0:
            N += 1
        h = 1./N
        Sum = func(0.0)
        fac = 2
        for i in range(N):
            if fac == 2:
                fac = 4
            else:
                fac = 2
            x = i*h
            Sum += fac*func(x)

        Sum += func(1.0)
        xint = Sum*h/3
        diff = exact - xint
        print("N = {:.3e}, Difference = {:.3e}".format(N, diff))


if __name__ == "__main__":
    main()
