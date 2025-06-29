from numpy import*
n=int(input("size of matrix=")) #n is the size of the matrix
u=zeros((n,2*n),float)  # u is the augmented matrix
for p in range(n): # p is the row number
    u[p][p+n]=1 # make the identity matrix in the right half
    for l in range(n): # l is the column number
        b=float(input("enter values="))  #input value in order
        u[p][l]=b    #assign the value to the matrix

#print("orginal matrix",u[:,:a])
print("orginal matrix",u)

for i in range(n):
    while u[i][i]==0:  # if the diagonal element is zero
        u[[i,i+1]]=u[[i+1,i]] # swap the row with the next row
        print(u) # print the matrix after swapping
    u[i] = u[i]/u[i,i] 
    for j in range(n):
        if j != i:
            u[j]=u[j]-u[j,i]*u[i]
print("inverse of matrix is=",round(u[:, n:],3))

