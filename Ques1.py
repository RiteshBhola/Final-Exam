from scipy import  integrate
import numpy as np
import math as m
import matplotlib.pyplot as plt
"""
Ritesh Kr. Bhola
10 Dec. 2019

Integrals in all three coordinates are independent of each other
and are done separately.
"""

rho =10
def f(r):
	return r*r
	
"performing angular integrals"
def ftheta(x):
	return m.sin(x)

def fphi(x):
	return 1

phi_integral	=integrate.quad(fphi,0,2*m.pi)[0]
theta_integral	=integrate.quad(ftheta,0,m.pi)[0]

print()
print()
def mass(r):
	return rho*phi_integral*theta_integral*integrate.quad(f,0,r)[0]
	
x=np.linspace(0,10,100)
f2=np.vectorize(mass)
y=f2(x)
print(y)
plt.plot(x,y,'r',ms=5)
plt.xlabel('r')
plt.ylabel('mass(r)')
plt.title("Mass as a function of r")
plt.show()
