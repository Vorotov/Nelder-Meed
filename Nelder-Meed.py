import numpy as np


def f(x):
    return 3*(x[0]-3)**2+(2*x[1]+3)**2+3*x[0]*x[1]


a, b, c = 1, 0.5, 2
x1 = np.array([0,0])
x2 = np.array([0.965, 0.259])
x3 = np.array([0.259, 0.965])
for i in range(1,21):
    f1 = f(x1)
    f2 = f(x2)
    f3 = f(x3)
    print("Шаг №", i)
    print(x1, x2, x3)
    print(f1, f2, f3,"\n")
    fh = max(f1, f2, f3)
    fl = min(f1, f2, f3)
    xh = x1
    xl = x1
    if f2 == fh:
        xh = x2
    elif f3 == fh:
        xh = x3
    if f2 == fl:
        xl = x2
    elif f3 == fl:
        xl = x3
    #x5 = x1 + x2 + x3 - 2 * xh
    x4 = (x1 + x2 + x3 - xh)/2
    x5 = x4 + a * (x4 - xh)
    f5 = f(x5)
    #print(x5, f5)
    if f5 > fh:
        x1 = (x1 + xl) / 2
        x2 = (x2 + xl) / 2
        x3 = (x3 + xl) / 2
    else:
        if ((f5 > f1) + (f5 >f2) + (f5 > f3)) == 2:
            xh = x4 + (xh - x4) * b
        else:
            x6 = x4 + c * (x5 - x4)
            if f(x6) <= fl:
                xh = x6
            else:
                xh = x5
        if fh == f1:
            x1 = xh
        elif fh == f2:
            x2 = xh
        else:
            x3 = xh

res = (x1 + x2 + x3)/3
print(res, "\n", f(res))
