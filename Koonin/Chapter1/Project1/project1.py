'''

Project 1:

'''

import numpy as np

# Constants
V0 = 1.0
a = 1.0
tolr = 1e-6


def V(x):
    return 4*V0*((x)**(-12) - (x)**(-6))


def theta1(r, b):
    term = 1/r**2/np.sqrt(1-(b/r)**2)
    return term


def theta2(r, b, E):
    return 1.0/np.sqrt(1.0 - (b/r)**2 - V(r)/E)/r**2


def integration(b, rmax, E):
    # Inward search for turning point
    dr = 0.2
    rmin = rmax
    while (dr > tolr):
        rmin = rmin - dr
        if ((1.0 - (b/rmin)**2 - V(rmin)/E)) < 0.0:
            rmin += dr
            dr /= 2

    # do the integration
    sum1 = 0.0
    N = 100
    umax = np.sqrt(rmax - b)
    h = umax/N
    for i in range(N):
        u = h*(i + 0.5)
        r = u**2 + b
        sum1 += u*theta1(r, b)
    int1 = 2*h*sum1

    # second integral
    sum2 = 0
    umax = np.sqrt(rmax - rmin)
    h = umax/N
    for i in range(N):
        u = h*(i + 0.5)
        r = u**2 + rmin
        sum2 += u*theta2(r, b, E)

    int2 = 2*h*sum2
    return 2*b*(int1 - int2), rmin


def main():

    #rmin = 2**(1/6)*a
    rmax = 2.4
    E = float(input("Input the value of E: "))
    N = 10
    h = (rmax)/N

    for i in range(N+1):
        b = i*h
        result, rmin = integration(b, rmax, E)
        diff = 2.0*(np.arccos(b/rmax) - np.pi/2.0) - result
        print("b = {:.4f}, I = {:.5f}, Radius = {:.5f}".format(b, result, rmin))


if __name__ == "__main__":
    main()
