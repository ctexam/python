from math import*
def f(x):
	return (1/sin(x+2)-2.5)
a=float(input('Enter a value for which f(x) is negative(a):'))
b=float(input('Enter a value for which f(x) is positive(b):'))
while True:
	x=(a+b)/2
	print('x=',x)
	if f(x)==0:
		print('The exact root is:',x)
		break
	elif abs(f(x))<0.0001:
		print('The root is:',x)
		break
	elif f(x)>0:
		b=x  #if f(x) is +ve, replace b by x
	else:
		a=x  