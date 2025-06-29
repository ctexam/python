from numpy import*
a=int(input("size of matrix="))
u=zeros((a,2*a),float)
for p in range(a):
    u[p][p+a]=1
    for l in range(a):
        b=float(input("enter values="))
        u[p][l]=b
u=array(u,float)
#print("orginal matrix",u[:,:a])
print("orginal matrix",u)

for i in range(a):
    j=0
    while u[i][i]==0:
        j=j+1
        u[[i,j]]=u[[j,i]]
        if j==a-1 :
            break
        print(u)
    u[i] = u[i]/u[i,i]
    for j in range(a):
        if j != i:
            u[j]=u[j]-u[j,i]*u[i]
print("inverse of matrix is=",round(u[:, a:],3))

