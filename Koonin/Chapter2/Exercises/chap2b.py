import numpy as np


def main():
    h = 0.1
    while h > 0.0:
        h = float(
            input(f"\n Enter step size [h= {h:.2E}] (.le. 0 to stop): ") or h)
        if h <= 0.0:
            break
        yminus = 1.0
        yzero = 1 - h + h**2/2
        nstep = int(6/h)
        for i in range(1, nstep):
            x = i*h
            yplus = yminus-2*h*yzero
            exact = np.exp(-x)
            diff = exact - yzero
            yminus = yzero
            yzero = yplus
            print(f"\t {x:.4E} \t {exact:.4E} \t {diff:.4E}")


if __name__ == "__main__":
    main()
