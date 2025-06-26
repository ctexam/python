def f(x, y):
    return ((x-y)/2)  # Example: dy/dx = (x-y)/2

def euler_method(x0, y0, x_end, h):
    x = x0
    y = y0
    print("x=",x, "y=",y)
    
    while x < x_end:
        y = y + h * f(x, y)  # Euler's formula
        x = x + h
        print("x=",x, "y=",y)

# Initial conditions and step size
x0 = 0
y0 = 1
x_end = 0.2
h = 0.1

euler_method(x0, y0, x_end, h)