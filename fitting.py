from pylab import*
x_data=[1,2,3,4,6,8]
y_data=[2,3,4,6,5,6]

n=int(input("enter the degree of polynomial="))
#print(x_data) 
#print(y_data)
sum_matrix=zeros((n+1,n+1),int)
sum_yx=zeros((n+1,1))
print(sum_yx)
for i in range(n+1):
    for j in range(n+1):
        sum_matrix[i][j]=sum(x**(i+j) for x in x_data)
print(sum_matrix)

for j in range(n+1):
    sum_yx[j]=sum(y * x**j for x, y in zip(x_data, y_data))
invmat=(linalg.inv(sum_matrix))
print((sum_matrix))
print(sum_yx)
print(invmat)
ans=dot(invmat,sum_yx)
print(ans)
po=len(ans)
x =linspace(1, 8, 256)

coefficents= ans.flatten()
polyn=poly1d(coefficents[::-1])
print(polyn)
y=polyn(x)

plot(x,y)
plot(x_data,y_data,':dg')
show()
