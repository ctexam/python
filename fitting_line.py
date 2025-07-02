from pylab import*
x=array([1,2,3,4,6,8])
y=array([14,27,40,55,68,90])
sum_matrix=array([[len(x),sum(x),sum(x**2)],[sum(x),sum(x**2),sum(x**3)],[sum(x**2),sum(x**3),sum(x**4)]] )
sum_yx=array([[sum(y)],[sum(x*y)],[sum((x**2)*y)]] )
print("Sum Matrix:", sum_matrix)
print("Sum YX:", sum_yx)
invmat=(linalg.inv(sum_matrix))

ans=dot(invmat,sum_yx)
xc =linspace(x[0], x[len(x)-1], 256)

coefficents= ans.flatten()

polyn=poly1d(coefficents[::-1])
print(polyn)
yc=polyn(xc)

plot(xc,yc)
plot(x,y ,'bo')
show()