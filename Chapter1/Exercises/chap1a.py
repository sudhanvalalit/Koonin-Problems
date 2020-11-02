# The following code evaluates equation 1.3b in the text for the value of h input

import numpy as np


def main():
    x = 1.0
    exact = np.cos(x)
    h = 0.1
    while h > 0:
        h = float(input("Enter value of h (.LE. 0 to STOP) :"))
        if h <= 0:
            break
        fprime = (np.sin(x+h)-np.sin(x-h))/(2.0*h)
        diff = exact - fprime
        print("H = {:.5f}, Error = {:.8f}".format(h, diff))
        print("h = {:.5f}, Exact = {:.5f}, Calculated = {:.5f}".format(
            h, exact, fprime))


if __name__ == "__main__":
    main()
