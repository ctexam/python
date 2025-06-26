def f(x, y):
    return x + y  # Define the function dy/dx = f(x, y)

def runge_kutta_4th_order(x0, y0, x_end, h):
    x = x0
    y = y0
    print("X=",round(x,2) ,"Y=",round(y,2))
    
    while x < x_end:
        k1 = f(x, y)
        k2 = f(x + h/2, y + h/2 * k1)
        k3 = f(x + h/2, y + h/2 * k2)
        k4 = f(x + h, y + h * k3)
        
        y = y + (h / 6) * (k1 + 2*k2 + 2*k3 + k4)
        x = x + h
        print("X=",round(x,2) ,"Y=",round(y,2))

# Initial conditions and step size
x0 = 0
y0 = 1
x_end = 1
h = 0.1

runge_kutta_4th_order(x0, y0, x_end, h)
