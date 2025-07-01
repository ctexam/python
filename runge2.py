import matplotlib.pyplot as plt

def f(x, y):
    return x + y  # Define the function dy/dx = f(x, y)

def runge_kutta_2nd_order(x0, y0, x_end, h):
    x = x0
    y = y0
    x_values = [x]
    y_values = [y]
    print("x=", x, "y=", y)
    
    while x < x_end:
        k1 = f(x, y)
        k2 = f(x + h, y + h * k1)
        y = y + (h / 2) * (k1 + k2)
        x = x + h
        x_values.append(x)
        y_values.append(y)
        print("x=", x, "y=", y)
    
    # Plotting the results
    plt.plot(x_values, y_values, 'o-', label='RK2 Approximation')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('2nd Order Runge-Kutta Method')
    plt.grid(True)
    plt.legend()
    plt.show()

# Initial condition and step size
x0 = 0
y0 = 1
x_end = 1.6
h = 0.1
runge_kutta_2nd_order(x0, y0, x_end, h)