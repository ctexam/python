from pylab import*
lx=[]
ly=[]
def f(x,y):
    return cos(x)
def e(xi,yi,xf,h=0.1):
    while xi<=xf:
        lx.append(xi)
        ly.append(yi)
        #print('xi=',xi,'/tyi=',yi)
        yi=yi+h*f(xi,yi)
        xi=xi+h
e(0,0,pi)
plot(lx,ly)
xlabel("x")
ylabel('y')
grid()
show()
