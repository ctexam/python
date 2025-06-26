from pylab import*
a=int(input("upper limit:"))
b=int(input("lower limit:"))
n=int(input("n="))
h=(a-b)/n
print(h)
x=linspace(b,a,n+1)
y=((2*x**3)-(4*x)+1)
sum=y[0]+y[n]
for i in range(1,n):
    print(i)
    if i%3==0:
        sum+=2*y[i]
    else:
        sum+=3*y[i]
sol=(3*h/8)*sum
print(sol)

    