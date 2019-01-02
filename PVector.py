'''
Created on Dec 14, 2018

@author: Mic
'''

import matplotlib.pyplot as plt
import numpy as np
from time import sleep

from mpl_toolkits.mplot3d import Axes3D
import math
class PVector(object):
    def __init__(self, Base , radius):
        self.base = self.copy(Base)
        
        self.baseOutput = [[0 for x in range(6)] for y in range(4)]
        self.baseStatic = [[0 for x in range(6)] for y in range(4)]
        
        leg_0 = 0
        for i in self.base:
            leg_1 = 0
            for n in i:
                self.baseStatic[leg_0][leg_1] = n
                leg_1 = leg_1 + 1
            leg_0 = leg_0 + 1
            
            
            
        self.radius = radius / math.sqrt(2)
        self.base[0][2]
        
    def baseUpdate(self , base):
        self.base = self.copy(base)
        self.baseStatic = self.copy(base)
    
    def copy(self , table):
        returnTable = [[0 for x in range(6)] for y in range(4)]
        leg_0 = 0
        for i in table:
            leg_1 = 0
            for n in i:
                returnTable[leg_0][leg_1] = n
                leg_1 = leg_1 + 1
            leg_0 = leg_0 + 1
        return returnTable
        
    def rotateX(self , angle):

        #print(angle)
        for i in range(0 , 4):
            cosa = math.cos(angle)
            sina = math.sin(angle)
            tempy = self.base[i][1]
            self.base[i][1] = cosa * self.base[i][1] - sina * self.base[i][2]
            self.base[i][2] = (cosa * self.base[i][2] + sina * tempy)# - self.radius
    
    def rotateY(self , angle):

        #self.base = self.baseStatic
        for i in range(0 , 4):
            cosa = math.cos(angle)
            sina = math.sin(angle)
            z = self.base[i][2] 
            x = self.base[i][0] 
            tempz = self.base[i][2]            
            self.base[i][2] = ((cosa * z) - (sina * x))# - self.radius
            self.base[i][0] = ((cosa * x) + (sina * tempz))# - self.radius

    def rotateZ(self , angle):

        #print(angle)
        for i in range(0 , 4):
            cosa = math.cos(angle)
            sina = math.sin(angle)
            tempx = self.base[i][0]
            
            self.base[i][0] = (cosa * self.base[i][0] - sina * self.base[i][1])# - self.radius
            self.base[i][1] = cosa * self.base[i][1] + sina * tempx
            
            
    def rotateX_onlyY(self ,angle):
        RZ = []
        for i in range(0 , 4):
            RZ.append(self.base[i][2] + self.radius)
            
        yMode = []    
        for i in range(0 , 4):
            yMode.append(RZ[i] / (math.tan(math.atan(RZ[i] / self.base[i][1]) + angle)))
        
        self.base[0][1] = self.base[0][1] + yMode[0]
        self.base[1][1] = self.base[1][1] + yMode[1]
        self.base[2][1] = self.base[2][1] - yMode[2]
        self.base[3][1] = self.base[3][1] - yMode[3]
    
    
    def rotateZ_onlyY(self ,angle):
        RX = []
        for i in range(0 , 4):
            RX.append(self.base[i][0] + self.radius)
            
        yMode = []    
        for i in range(0 , 4):
            yMode.append(RX[i] / (math.tan(math.atan(RX[i] / self.base[i][1]) + angle)))
        
        self.base[0][1] = self.base[0][1] - yMode[0]
        self.base[1][1] = self.base[1][1] + yMode[1]
        self.base[2][1] = self.base[2][1] + yMode[2]
        self.base[3][1] = self.base[3][1] - yMode[3]
        
        
    def findPointUnderneathMainPlane(self):
        Pes = []
        res = []
        for i in self.base:
            Pes.append(i)
            
        res.append(self.pointUderPlane(Pes[0] , Pes[1] , Pes[2] , Pes[3]))
        res.append(self.pointUderPlane(Pes[1] , Pes[2] , Pes[3] , Pes[0]))
        res.append(self.pointUderPlane(Pes[2] , Pes[3] , Pes[0] , Pes[1]))
        res.append(self.pointUderPlane(Pes[3] , Pes[0] , Pes[1] , Pes[2])) 
        
        return res
            
    def pointUderPlane(self , P1 , P2 , P3 , S):

        p1 = np.array([P1[0], P1[1], P1[2]])
        p2 = np.array([P2[0], P2[1], P2[2]])
        p3 = np.array([P3[0], P3[1], P3[2]])
        
        v1 = p3 - p1
        v2 = p2 - p1
        
        cp = np.cross(v1, v2)
        a, b, c = cp
        
        d = np.dot(cp, p3)

        yb = -(a * S[0] + c * S[2] - d) / b
        if(S[1] < yb):
            return True
        else:
            return False
        
    def loverBase(self , val):
        for i in range(0 , 4):
            self.base[i][1] += val
        
        
            
    def result(self):
        self.baseOutput = self.copy(self.base)
        self.base = self.copy(self.baseStatic)
        return self.baseOutput
    
    
if __name__ == '__main__':
    
    rangeOf_A = 9000
    rangeOf = 18000
    
    val_34 = 126.8095 / math.sqrt(2)
    
    base = [[-150 - val_34 , 100 ,  150 + val_34 , 0, 0] ,
            [ 150 + val_34 , 100 ,  150 + val_34, 0, 0] ,
            [ 150 + val_34 , 100 , -150 - val_34, 0, 0] ,
            [-150 - val_34 , 100 , -150 - val_34, 0, 0] ]
    
    vector = PVector(base , 126.8095)
    
    vector.findPointUnderneathMainPlane()
    stepListX = [0 for x in range(rangeOf)]
    stepListZ = [0 for x in range(rangeOf)]
    
    stepListS = [0 for x in range(rangeOf)]
    stepListC = [0 for x in range(rangeOf)]
    
    stepList1 = [0 for x in range(rangeOf)]
    
    stepListA = [0 for x in range(rangeOf)]
    
    n = 0
    for i in range(int(-rangeOf_A) , int(rangeOf_A)):
        vector.rotateX((i/ (57.2958 * 100))) #+ 1.5706212322718245))
        vector.rotateZ(0)
        vector.rotateY(0)
        s = vector.result()
        legCount = 0
        
        
        stepListX[n] = s[0][2] #-  2* (126.8095 / math.sqrt(2))
        stepListZ[n] =  s[1][2] #    
        stepListS[n] =  -s[2][2] #
        stepListC[n] = -s[3][2] #-  2* (126.8095 / math.sqrt(2))
        
        
        '''
        stepListX[n] = s[0][0]
        stepListZ[n] = s[1][0]     
        stepListS[n] = -s[2][0]-  2* (126.8095 / math.sqrt(2))
        stepListC[n] = -s[3][0]-  2* (126.8095 / math.sqrt(2))
        '''
        
        stepListA[n] = (i / (57.2958 * 10))*100
        n = n + 1
        
    plt.plot(stepListX , 'r')
    plt.plot(stepListZ , 'g')
    plt.plot(stepListS , 'b')
    plt.plot(stepListC , 'm')
    
    
    plt.xlabel('time (s)')
    plt.ylabel('pose (mm)')
    plt.title('we will rise folks')
    plt.grid(True)
    plt.savefig("test.png")
    plt.show()
    
    
    
    

    
    
    
    
    
    
    
    
    