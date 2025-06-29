from math import*
def f(x):
	return (x*exp(x)-2)
a=float(input('Enter a value for which f(x) is negative(a):'))
b=float(input('Enter a value for which f(x) is positive(b):'))
while True:
	x=(a*f(b)-b*f(a))/(f(b)-f(a))
	if f(x)==0:
		print('The exact root is:',x)
		break
	elif abs(f(x))<0.0001:
		print('The root is:',x)
		break
	elif f(x) < 0:
		b = x
	else:
		a = x
print("value of f(x) is:",f(x))
