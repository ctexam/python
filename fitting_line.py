from pylab import*
x=[1,2,3,4,6,8]
y=[14,27,40,55,68,90]
sum_matrix=array([[len(x),sum(x)],[sum(x),sum(x1**2 for x1 in x)]] )
sum_yx=array([[sum(y)],[sum(x1*y1 for x1, y1 in zip(x, y))]] )
print("Sum Matrix:", sum_matrix)
print("Sum YX:", sum_yx)
invmat=(linalg.inv(sum_matrix))

ans=dot(invmat,sum_yx)
print(ans)
po=len(ans)
xc =linspace(1, 8, 256)

coefficents= ans.flatten()
polyn=poly1d(coefficents[::-1])
print(polyn)
yc=polyn(xc)

plot(xc,yc)
plot(x,y ,'o')
show()