#first we party with Midpoint Rule then we party with Gaussian Quadrature


import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

############INPUT ##############
startpoint=-10
endpoint=10
numberofpoints=[]



# define the cosine function
def function(x):
    return np.cos(x)+2



#calculate interval
for i in range(0,50):
    numberofpoints.append(int(i+6))
    
numberofpoints=np.array(numberofpoints)





######## MIDPOINT RULE ################





midpoint_integral=[]
for j in numberofpoints:
    step=(endpoint-startpoint)/j
    integral_mid=0
    for i in range(j):
        integral_mid += step * function((startpoint + (2*i+1 ) * step/2))
    midpoint_integral.append(integral_mid)


######### GAUSSIAN QUADRATURE ##########

#integral_quad,difference=integrate.quadrature(function, startpoint, endpoint,args=(2))
quadrature_integral=[]    
for j in numberofpoints:

    integral_quad,difference=integrate.fixed_quad(function, startpoint,endpoint , n=j)
    quadrature_integral.append(integral_quad)
    


#plotting Stuff
fig,ax=plt.subplots()

ax.plot(numberofpoints, quadrature_integral, label='Gaussian Quadrature')
ax.plot(numberofpoints, midpoint_integral, label='Midpoint Formula')

plt.xlabel('n')
plt.ylabel('True value - Integral estimate')
plt.legend()

plt.title('Difference between Analytical value and Estimate')
    
plt.savefig('Numerical_Integration.pdf')

plt.show()

