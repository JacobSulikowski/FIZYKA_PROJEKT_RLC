import math
import var
class Kondensator:
    def __init__(self,capacity):
        self.capacity = capacity
        self.current = 0
        self.voltage = 0
        self.power = 0
        self.frequency = 0


    def getQ(self,t):
        return var.Qm*math.exp(-var.R/2*var.L) * math.cos(var.w * t + var.phi)
    
    def getU(self,t):
        return var.Qm*math.exp(-var.R/2*var.L) * math.cos(var.w * t + var.phi)/var.C  