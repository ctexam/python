from numpy import*
n=int(input('size of the matrix=' ))
u=zeros((n,2*n),float)
for p in range(n):
    u[p][p+n]=1
    for l in range(n):
        b=(float(input("enter the number=" )))
        u[p][l]=b
print("original matrix",u[:,:n])
print("augmented matrix",u)

for i in range(n):
    while u[i][i]==0:
        u[[i,i+1]]=u[[i+1,i]]
        print(u)
    u[i]=u[i]/u[i,i]
    for j in range(n):
        if j!=i:
            u[j]=u[j]-u[j,i]*u[i]
print("inverse of the matrix is =",round(u[:,n:],3))

