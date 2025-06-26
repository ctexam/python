from math import*
a=float(input("coeff of X^2="))
b=float(input("coeff of X="))
c=float(input("constant="))
print("qudratic equation is",a,"*X^2+",b,"*X+",c)
if a==0:
    print("Not a quadratic equation")
else:
    d=(-b+(((b**2)-(4*a*c))**0.5))/(2*a)
    e=(-b-(((b**2)-(4*a*c))**0.5))/(2*a)
    print(complex(round(d.real,4),round(d.imag,4)))
    print(complex(round(e.real,4),round(e.imag,4)))


    
