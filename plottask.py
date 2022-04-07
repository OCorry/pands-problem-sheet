#program called plottask.py that displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] 
#on the one set of axes
#Author: Orla Corry 


import numpy as np 
import matplotlib.pyplot as plt
xpoints = np.array(range(0,5)) #making this 0,5 so that the x axis contains 0 through to 4 
ypointsA = xpoints #the function of x is y: f(x)=y    
ypointsB = xpoints*xpoints #g(x)=x2 ie: y=x*x
ypointsC = xpoints**3 #h(x)=x3 ie: y= x*x*x

plt.title("Plot of Functions", color= "purple")
plt.xlabel("Range 0-4", color = "red")
plt.ylabel("Function", color ="red")

plt.plot(xpoints, ypointsA, label = "f(x)=x", color= "purple", ls =":", marker = "H")
plt.plot(xpoints, ypointsB, label = "g(x) = x2", color = "blue", ls = "--", marker = "H")
plt.plot(xpoints, ypointsC, label = "h(x) = x3", color = "green", marker= "H")
plt.legend()
plt.grid()

#plt.show()
plt.savefig("Plot Task.png")




