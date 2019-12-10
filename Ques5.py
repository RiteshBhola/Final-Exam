import numpy as np
import math as m
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange
from scipy import optimize

#data loaded
theta=np.loadtxt('data.txt',usecols=0)
d=np.loadtxt('data.txt',usecols=1)

#print(theta)
#print(d)
"""
y_lagrange is the interpolated function.
"""
y_lagrange=lagrange(theta,d)


user_input = float(input('Enter value of theta (b/w 0 to 10) at which d is required:'))
print ("Your input",user_input)
print("Corresponding Value of d is ",y_lagrange(user_input))

x = int(input('Want to see plots? (1=yes,any other number=no)'))
if(x==1):
	plt.plot(theta, y_lagrange(theta), 'c', lw=2,label="Interpolated lagrange Polynomial")
	plt.plot(theta,d,'r*',ms=5,label="Data points")
	plt.legend()
	plt.show()


print(
"""
*************************
Finding theta at d=370.4
*************************
""")
def f(x):
	return y_lagrange(x)-370.4
	
root=optimize.bisect(f,0.2,2)
print("Value of root i.e theta for d=370.4 is",root)
print("Function value at root",f(root))
	
	
