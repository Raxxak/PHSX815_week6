import scipy.integrate as integrate
from scipy.integrate import quad

import random

import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

############INPUT ##############
startpoint=0
endpoint=1
numberofpoints=[]



# define the cosine function
def function(x):
    return np.cos(x)


#calculate interval
for i in range(1,20):
    numberofpoints.append(int(i**3+100))
    
numberofpoints=np.array(numberofpoints)


########Quadrature
quadrature_integral=[]    
for j in numberofpoints:

    integral_quad,difference=integrate.fixed_quad(function, startpoint,endpoint , n=j)
    quadrature_integral.append(integral_quad)









######## Monte Carlo Integration ################


i=0
integral=[]
for i in range(len(numberofpoints)):
    temp=[]
    num=0
    for j in range(0,numberofpoints[i]):
        num=num+function(random.uniform(0,1))
    integral.append(num/numberofpoints[i])    
     
     
               
     




#actual value
actualvalue,error=quad(function, 0, 1) 

######### plotting Stuff ###########
fig,ax=plt.subplots()

ax.plot(numberofpoints, integral, label='MC Integration')

plt.axhline(y=actualvalue, color='r', label='Analytical value' )
ax.plot(numberofpoints, quadrature_integral, label='Gaussian Quadrature')


plt.xlabel('n')
plt.ylabel('True value - Integral estimate')
plt.legend()

plt.title('Difference between Analytical value and Estimate')
    
plt.savefig('Numerical_Integration_MonteCarlo.pdf')

plt.show()

               #create n random numbers



