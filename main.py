import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np
import math
import var 

def Q(t):
    return var.Qm*math.exp(-var.R/2*var.L) * math.cos(var.w * t + var.phi)

def dI(I,t):
    return I * math.sin(t*var.dt)

def dU(U,t):
    return U * math.cos(t*var.dt)

def getIfromR(U,R):
    return U/R

def getRfromUI(U,I):
    return U/I

xl = []
yl = []

def simulateRLC(time):
    for t in range(0,time):
        xl.append(t)
        yl.append(getIfromR(dU(var.U,t),var.R))

simulateRLC(100)

plt.plot(xl,yl)

#plt.scatter(xl,yl)
#plt.plot(xl,yl)
plt.show()