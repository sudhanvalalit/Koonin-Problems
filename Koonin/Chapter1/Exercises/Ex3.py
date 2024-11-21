r""" Exercise 1.3:  Write a program to calculate 

.. math::
    $\int_0^1 t^{-2/3}(1-t)^{-1/3} dt = 2\pi/3^{1/2}$
 
using one of the quadrature formulas discussed above and investigate its accuracy for
various values of h. (Hint: Split the range of integration into two parts and make a
different change of variable in each integral to handle the singularities.)
"""

import numpy as np
from Ex2 import Simpson13


def f(x):
    return x**(-2/3)*(1-x)**(-1/3)


def main():
    pass


if __name__ == "__main__":
    main()
