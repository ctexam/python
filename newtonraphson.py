def f(x):
    return 2*x**2-3*x-5
def df(x):
    return 4*x-3
def sol(x):
    while True:
        h=-f(x)/df(x)
        if abs(h)<1.0e-4:
            break
        x=x+h
    return print(x)
sol(2)
