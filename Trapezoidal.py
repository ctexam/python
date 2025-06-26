from numpy import*
a=int(input("upper limit:"))
b=int(input("lower limit:"))
n=int(input("n="))
h=(a-b)/n
print(h)
x=linspace(b,a,n+1)
y=1/(1+x**2)
print(x)
print(y)
sol=(h/2)*(2*sum(y)-(y[0]+y[n]))
print(sol)
