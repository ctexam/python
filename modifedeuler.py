from pylab import*
def f(x, y):
    return (-2*x-y)  # Example: dy/dx = (x-y)/2

def euler_method(x0, y0, x_end, h):
    x = x0
    y = y0
    x_data=[x]
    y_data=[y]
    print("x=",x, "y=",y)
    
    while x < x_end:
        y = y + h * f(x+(h/2), y+(h/2)*f(x,y))  # Euler's formula
        x = x + h
        print("x=",x, "y=",y)
        x_data.append(x)
        y_data.append(y)
    print(x_data)
    print(y_data)
    plot(x_data,y_data)
    plot(x_data,y_data ,'o')
    show()



# Initial conditions and step size
x0 = 0
y0 = -1
x_end = 0.5
h = 0.1

euler_method(x0, y0, x_end, h)