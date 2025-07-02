from pylab import*
from math import*
x_val=[1891,1901,1911,1921,1931]
y_val=[46,66,81,93,101]
n=len(x_val)

print(x_val);print(y_val)
diff=[[0]*i for i in range(n-1,0,-1)]
for i in range(n-1):   
    diff[0][i]=y_val[i+1]-y_val[i]
for k in range(1,n-1):
     for j in range(0,n-1-k):
        diff[k][j]=diff[k-1][j+1]-diff[k-1][j]               
print("difference table=",(diff))
#xi=float(input("enter x to find y="))
xi =linspace((x_val[0])-5,(x_val[n-1])+5, 256)

p=((xi-x_val[0])/(x_val[1]-x_val[0]))

a=1
y=y_val[0]
for i in range(n-1):
    a=(a*(p-i))/(i+1)
    y=y+a*diff[i][0]
plot(xi,y,label="interpolated curve")
plot(x_val,y_val,'o',label="orginal data")
xlabel("x")
ylabel("f(x)")
legend()
show()
