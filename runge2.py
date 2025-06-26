def f(x, y):
    return x + y  # Define the function dy/dx = f(x, y)

def runge_kutta_2nd_order(x0, y0, x_end, h):
    x = x0
    y = y0
    print("x=",x ,"y=",y)
    
    while x < x_end:
        k1 = f(x, y)
        k2 = f(x + h, y + h * k1)
        y = y + (h / 2) * (k1 + k2)
        x = x + h
        print("x=",x ,"y=",y)

# Initial condition and step size
x0 = 0
y0 = 1
x_end = 0.2
h = 0.1
runge_kutta_2nd_order(x0, y0, x_end, h)
