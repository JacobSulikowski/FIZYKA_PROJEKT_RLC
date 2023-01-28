import matplotlib.pyplot as plt
import numpy as np


R = 200
L = 20
C = 10

U = 3
I = 2
dt = 0.001

def getIfromR(U,R):
    return U/R

def getRfromUI(U,I):
    return U/I

xl = []
yl = []



for t in range(0,2):
    xl.append(U+t)
    yl.append(getIfromR(U+t,R))

x = np.array(xl)
y = np.array(yl)

plt.xlabel("U")
plt.ylabel("I")
plt.plot(x,y)
plt.show()