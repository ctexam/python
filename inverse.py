from numpy import*
def determinant(a):
    n=len(a)
    if n==1:
        return(a[0][0])
    if n==2:
        return (a[0][0]*a[1][1])-(a[0][1]*a[1][0])
    det=0
    for i in range(n):
        b=delete(a,0,0)
        b=delete(b,i,1)
        det+=a[0][i]*(-1)**i*determinant(b)
    return(det)


def inv(f):
    y=determinant(f)
    k=len(f)
    t=zeros((k,k),float)
    for i in range(k):
        for j in range(k):
            b=delete(f,j,0)
            b=delete(b,i,1)
            t[i][j]=(((-1)**(i+j))*determinant(b))
    s=t/y
    return(s)
m=[[2,4,6,16],[2,12,4,6],[1,10,5,8],[1,3,2,8]]
print(inv(m))