'''
Created on Dec 4, 2018

@author: Mic
'''
import math
import sys

import matplotlib.pyplot as plt
import numpy as np
from time import sleep

class Overlord(object):
    '''
    classdocs
    '''


    def __init__(self, radius):
        self.radius = radius
      
      
    def compute(self ,xPos , yPos , zPos , azymuth , increase , valZero , valZero1):
        absoluteRadius = self.radius / math.sqrt(2)
        
        A1 = azymuth + 0.785398
        A2 = 0.785398 - azymuth
        a =  absoluteRadius * math.sin(A1)
        c = -absoluteRadius * math.sin(A2)
        vRu = math.sqrt((xPos*xPos)+(zPos*zPos)) + absoluteRadius
        vR = math.sqrt((vRu*vRu)+(yPos*yPos))
        vRk = math.asin(yPos / vR)
        Kx1 = (math.sin(increase)*a) / 2
        Kx2 = (math.sin(increase)*c) / 2
        increaseBis1 = math.acos(1 - (Kx1 * Kx1) / (self.radius^2))
        increaseBis2 = math.acos(1 - (Kx2 * Kx2) / (self.radius^2))
        K1 = vRk + increaseBis1 * valZero
        K2 = vRk + increaseBis2 * valZero
        K3 = vRk - increaseBis2 * valZero
        K4 = vRk - increaseBis1 * valZero
        L1 = math.cos(K1)*vR
        L2 = math.cos(K2)*vR
        L3 = math.cos(K3)*vR
        L4 = math.cos(K4)*vR
        newXZ1 = L1 - absoluteRadius
        newXZ2 = L2 - absoluteRadius
        newXZ3 = L3 - absoluteRadius
        newXZ4 = L4 - absoluteRadius
        yBis1 = math.sqrt((vR*vR)-(L1*L1))
        yBis2 = math.sqrt((vR*vR)-(L2*L2))
        yBis3 = math.sqrt((vR*vR)-(L3*L3))
        yBis4 = math.sqrt((vR*vR)-(L4*L4))
        xBis1 = newXZ1 / math.sqrt(2)
        xBis2 = newXZ2 / math.sqrt(2)
        xBis3 = newXZ3 / math.sqrt(2)
        xBis4 = newXZ4 / math.sqrt(2)
        zBis1 = newXZ1 / math.sqrt(2)
        zBis2 = newXZ2 / math.sqrt(2)
        zBis3 = newXZ3 / math.sqrt(2)
        zBis4 = newXZ4 / math.sqrt(2)
        
        posList = [[0 for x in range(4)] for y in range(3)]
        posList[0][0] = xBis1
        posList[0][1] = xBis2
        posList[0][2] = xBis3
        posList[0][3] = xBis4
        
        posList[1][0] = yBis1
        posList[1][1] = yBis2
        posList[1][2] = yBis3
        posList[1][3] = yBis4
        
        posList[2][0] = zBis1
        posList[2][1] = zBis2
        posList[2][2] = zBis3
        posList[2][3] = zBis4
        
        return posList
        
    def moveForInfinity(self , radius , progress ):
        valX = progress
        
        if(progress > 0.50):
            valX = -math.pow((4 * (progress - 0.5)) - 1 , 2) + 1
        else:
            valX = -(-math.pow((4 * progress) - 1 , 2) + 1)
        
        
        
        if(progress > 0.75):
            progress = 1 - ((progress - 0.75) * 4)
            valY = -math.sqrt((math.pow(progress , 4) * 2) * (((-math.pow(progress , 4)* 2) + 2)))
            #valX = -math.pow((progress + 0.25) - 1 , 2) + 1
        elif(progress > 0.5):
            progress = (progress - 0.5) * 4
            valY = math.sqrt((math.pow(progress , 4) * 2) * (((-math.pow(progress , 4)* 2) + 2)))
            #valX = -math.pow((progress) - 1 , 2) + 1
        elif(progress > 0.25):
            progress = 1 - ((progress - 0.25) * 4)
            valY = -math.sqrt((math.pow(progress , 4) * 2) * (((-math.pow(progress , 4)* 2) + 2)))
            #valX = -math.pow((progress + 0.25) - 1 , 2) + 1
        else: 
            progress = progress * 4
            valY = math.sqrt((math.pow(progress , 4) * 2) * (((-math.pow(progress , 4)* 2) + 2)))
            #valX = -math.pow((progress) - 1 , 2) + 1
            
        pos = [None] * 2
        
        pos[0] = valX * radius[0]
        pos[1] = valY * radius[1]
        
        return pos
     
     
     
     
    
    def makeStepList(self , lenght , yheight , windth):
        stepList = [[0 for x in range(16)] for y in range(3)]
        stepList[1][0]  = lenght * 0.83
        stepList[1][1]  = lenght * 0.66
        stepList[1][2]  = lenght * 0.5
        stepList[1][3]  = lenght * 0.33
        stepList[1][4]  = lenght * 0.16
        stepList[1][5]  = 0
        stepList[1][6]  = -lenght * 0.16
        stepList[1][7]  = -lenght * 0.33
        stepList[1][8]  = -lenght * 0.5
        stepList[1][9]  = -lenght * 0.66
        stepList[1][10] = -lenght * 0.83
        stepList[1][11] = -lenght 
        stepList[1][12] = -lenght * 0.5
        stepList[1][13] =  0
        stepList[1][14] = lenght * 0.5
        stepList[1][15] = lenght
        
        stepList[0][0]  = yheight
        stepList[0][1]  = yheight
        stepList[0][2]  = yheight
        stepList[0][3]  = yheight
        stepList[0][4]  = yheight
        stepList[0][5]  = yheight
        stepList[0][6]  = yheight
        stepList[0][7]  = yheight
        stepList[0][8]  = yheight
        stepList[0][9]  = yheight
        stepList[0][10] = yheight
        stepList[0][11] = yheight
        stepList[0][12] = yheight*0.23
        stepList[0][13] = 0
        stepList[0][14] = yheight*0.23
        stepList[0][15] = yheight
        
        stepList[2][0]  = windth
        stepList[2][1]  = windth
        stepList[2][2]  = windth
        stepList[2][3]  = windth
        stepList[2][4]  = windth
        stepList[2][5]  = windth
        stepList[2][6]  = windth
        stepList[2][7]  = windth
        stepList[2][8]  = windth
        stepList[2][9]  = windth
        stepList[2][10] = windth
        stepList[2][11] = windth
        stepList[2][12] = windth
        stepList[2][13] = windth
        stepList[2][14] = windth
        stepList[2][15] = windth
        
        return stepList
    
    
    
    def universal_StepList(self , lenghtx , yheight , lenghtz):
        stepList = [[0 for x in range(16)] for y in range(3)]
        stepList[1][0]  = lenghtx * 0.83
        stepList[1][1]  = lenghtx * 0.66
        stepList[1][2]  = lenghtx * 0.5
        stepList[1][3]  = lenghtx * 0.33
        stepList[1][4]  = lenghtx * 0.16
        stepList[1][5]  = 0
        stepList[1][6]  = -lenghtx * 0.16
        stepList[1][7]  = -lenghtx * 0.33
        stepList[1][8]  = -lenghtx * 0.5
        stepList[1][9]  = -lenghtx * 0.66
        stepList[1][10] = -lenghtx * 0.83
        stepList[1][11] = -lenghtx 
        stepList[1][12] = -lenghtx * 0.5
        stepList[1][13] =  0
        stepList[1][14] = lenghtx * 0.5
        stepList[1][15] = lenghtx
        
        stepList[0][0]  = yheight
        stepList[0][1]  = yheight
        stepList[0][2]  = yheight
        stepList[0][3]  = yheight
        stepList[0][4]  = yheight
        stepList[0][5]  = yheight
        stepList[0][6]  = yheight
        stepList[0][7]  = yheight
        stepList[0][8]  = yheight
        stepList[0][9]  = yheight
        stepList[0][10] = yheight
        stepList[0][11] = yheight
        stepList[0][12] = yheight*0.23
        stepList[0][13] = 0
        stepList[0][14] = yheight*0.23
        stepList[0][15] = yheight
        
        stepList[2][0]  = lenghtz * 0.83
        stepList[2][1]  = lenghtz * 0.66
        stepList[2][2]  = lenghtz * 0.5
        stepList[2][3]  = lenghtz * 0.33
        stepList[2][4]  = lenghtz * 0.16
        stepList[2][5]  = 0
        stepList[2][6]  = -lenghtz * 0.16
        stepList[2][7]  = -lenghtz * 0.33
        stepList[2][8]  = -lenghtz * 0.5
        stepList[2][9]  = -lenghtz * 0.66
        stepList[2][10] = -lenghtz * 0.83
        stepList[2][11] = -lenghtz 
        stepList[2][12] = -lenghtz * 0.5
        stepList[2][13] =  0
        stepList[2][14] = lenghtz * 0.5
        stepList[2][15] = lenghtz
        
        return stepList
    
    
    def universal_StepList_rotary(self , radius , angle, yheight , direction):
        stepList = [[0 for x in range(16)] for y in range(3)]
        
        angle = angle / 57.2958
        
        if(direction):
            n = 0
            for i in range(0 , 12):
                val = i * 0.833 *angle + ((3.14 - angle) / 2)
                stepList[1][n] = (math.sin(val) * radius) - (self.radius / math.sqrt(2))
                stepList[2][n] = (math.cos(val) * radius) - (self.radius / math.sqrt(2))
                n = n + 1
                
            for i in range(4 , 0):
                val = i * 0.25*angle + ((3.14 - angle) / 2)
                stepList[1][n] = (math.sin(val) * radius) - (self.radius / math.sqrt(2))
                stepList[2][n] = (math.cos(val) * radius) - (self.radius / math.sqrt(2))
                n = n + 1
        else:
            n = 0
            for i in range(0 , 12):
                val = (i * 0.833*angle) + ((3.14 - angle) / 2)
                stepList[1][n] = (math.sin(val) * radius) - (self.radius / math.sqrt(2))
                stepList[2][n] = (math.cos(val) * radius) - (self.radius / math.sqrt(2))
                n = n + 1
                
            for i in range(4 , 0):
                val = i * 0.25*angle + ((3.14 - angle) / 2)
                stepList[1][n] = (math.sin(val) * radius) - (self.radius / math.sqrt(2))
                stepList[2][n] = (math.cos(val) * radius) - (self.radius / math.sqrt(2))
                n = n + 1
        
        stepList[0][0]  = yheight
        stepList[0][1]  = yheight
        stepList[0][2]  = yheight
        stepList[0][3]  = yheight
        stepList[0][4]  = yheight
        stepList[0][5]  = yheight
        stepList[0][6]  = yheight
        stepList[0][7]  = yheight
        stepList[0][8]  = yheight
        stepList[0][9]  = yheight
        stepList[0][10] = yheight
        stepList[0][11] = yheight
        stepList[0][12] = yheight*0.23
        stepList[0][13] = 0
        stepList[0][14] = yheight*0.23
        stepList[0][15] = yheight
        
        return stepList
    
    
        
    def makeAllMoves(self , stepSample):
        m = 0
        n = 0
        o = 0
        stepList = [[[0 for x in range(18)] for y in range(3)]for z in range(4)]
        
        
        for o in range(0 , 4):
            if(o == 0):
                for i in stepSample:
                    m = 0
                    for a in i:
                        if(m == 16):
                            m = 0
                        stepList[o][n][m] = a
                        m = m + 1
                    n = n + 1
            
            if(o == 1):
                n = 0
                for i in stepSample:
                    m = 0
                    t = 0
                    for a in i:
                        if(m == 16):
                            m = 0
                        if(m + 4 != 16):   
                            stepList[o][n][m+4] = a
                            m = m + 1
                        else:
                            stepList[o][n][t] = a
                            t = t +1
                    n = n + 1   
            
            if(o == 2):
                n = 0
                for i in stepSample:
                    m = 0
                    t = 0
                    for a in i:
                        if(m == 16):
                            m = 0
                        if(m + 8 != 16):   
                            stepList[o][n][m+8] = a
                            m = m + 1
                        else:
                            stepList[o][n][t] = a
                            t = t +1
                    n = n + 1
     
            if(o == 3):
                n = 0
                for i in stepSample:
                    m = 0
                    t = 0
                    for a in i:
                        if(m == 16):
                            m = 0
                        if(m + 12 != 16):   
                            stepList[o][n][m+12] = a
                            m = m + 1
                        else:
                            stepList[o][n][t] = a
                            t = t +1
                    n = n + 1
                   
        return stepList
    
    def makeAllMoves2(self , stepSample):
        m = 0
        n = 0
        o = 0
        stepList = [[[0 for x in range(18)] for y in range(3)]for z in range(4)]
        
        
        for o in range(0 , 4):
            if(o == 0):
                for i in stepSample:
                    m = 0
                    for a in i:
                        if(m == 16):
                            m = 0
                        stepList[o][n][m] = a
                        m = m + 1
                    n = n + 1
            
            if(o == 1):
                n = 0
                for i in stepSample:
                    m = 0
                    t = 0
                    for a in i:
                        if(m == 16):
                            m = 0
                        if(m + 8 != 16):   
                            stepList[o][n][m+8] = a
                            m = m + 1
                        else:
                            stepList[o][n][t] = a
                            t = t +1
                    n = n + 1 
            
            if(o == 3):
                n = 0
                for i in stepSample:
                    m = 0
                    t = 0
                    for a in i:
                        if(m == 16):
                            m = 0
                        if(m + 8 != 16):   
                            stepList[o][n][m+8] = a
                            m = m + 1
                        else:
                            stepList[o][n][t] = a
                            t = t +1
                    n = n + 1
     
            if(o == 2):
                n = 0
                for i in stepSample:
                    m = 0
                    for a in i:
                        if(m == 16):
                            m = 0
                        stepList[o][n][m] = a
                        m = m + 1
                    n = n + 1
                   
        return stepList
    
    
     
    def addSpeed(self , movesList , speed):
        self.speed = speed
        stepList = [[[0 for x in range(speed * 16)] for y in range(4)]for z in range(4)]
        leg = 0
        for i in movesList:
            xyzPose = 0
            t = 0
            for n in i:
                for r in range(0 , 16):
                    if(xyzPose == 15):
                        for step in range(0 , speed):
                            delta = n[15] - n[0]
                            stepList[leg][t][step + (speed * xyzPose)] = ((-delta/speed) * step) + n[15]
                        xyzPose = 0
                        
                    else:
                        for step in range(0 , speed):
                            delta = n[xyzPose] - n[xyzPose + 1]
                            stepList[leg][t][step + (speed * xyzPose)] = ((-delta/speed) * step) + n[xyzPose]
                        xyzPose = xyzPose + 1
                t = t +1
            leg = leg + 1
        
        #self.debugPlotline(stepList) 
        return stepList
            
            
    def midPointGrinder(self ,moveList ,  radius):
        stepList = [[[0 for x in range(self.speed * 16)] for y in range(4)]for z in range(4)]
        
        pointLeg = 0
        for leg in moveList:
            xyzPoint = 0
            for sign in leg:
                if(xyzPoint == 2):
                    for step in range(0 , len(sign)):
                        elipse = self.moveForInfinity(radius , step / len(sign))
                        #stepList[pointLeg][xyzPoint][step] = sign[step] - elipse[0]
                        stepList[pointLeg][xyzPoint][step] =  - elipse[0]
                        
                if(xyzPoint == 0):
                    for step in range(0 , len(sign)):
                        stepList[pointLeg][xyzPoint][step] = sign[step]
                
                if(xyzPoint == 1):
                    for step in range(0 , len(sign)):
                        elipse = self.moveForInfinity(radius , step / len(sign))
                        stepList[pointLeg][xyzPoint][step] = sign[step] + elipse[1]
                        
                xyzPoint = xyzPoint + 1
            pointLeg = pointLeg + 1
        #self.debugPlotline(stepList)
        
        return stepList
    
    
    def midPointGrinderZ(self ,moveList ,  radius):
        stepList = [[[0 for x in range(self.speed * 16)] for y in range(4)]for z in range(4)]
        
        pointLeg = 0
        for leg in moveList:
            xyzPoint = 0
            for sign in leg:
                if(xyzPoint == 2):
                    for step in range(0 , len(sign)):
                        stepList[pointLeg][xyzPoint][step] = sign[step]
                        
                if(xyzPoint == 0):
                    for step in range(0 , len(sign)):
                        stepList[pointLeg][xyzPoint][step] = sign[step]
                
                if(xyzPoint == 1):
                    for step in range(0 , len(sign)):
                        stepList[pointLeg][xyzPoint][step] = sign[step]
                        
                xyzPoint = xyzPoint + 1
            pointLeg = pointLeg + 1
        #self.debugPlotline(stepList)
        #sleep(20000.0)
        
        return stepList
    
    def debugPlotline(self , moveList):
        literation = 16 * self.speed 
        stepList = [0 for x in range(literation)]
        stepList2 = [0 for x in range(literation)]
        stepList3 = [0 for x in range(literation)]
        stepList4 = [0 for x in range(literation)]
        
        leg = 0
        sign = 2
        step = 0
        for i in range(0 , literation):
            stepList[i] = moveList[leg][sign][i]
        for i in range(0 , literation):
            stepList2[i] = moveList[leg+1][sign][i]
        for i in range(0 , literation):
            stepList3[i] = moveList[leg+2][sign][i]
        for i in range(0 , literation):
            stepList4[i] = moveList[leg+3][sign][i]
            
        plt.plot(stepList)
        plt.plot(stepList2)
        plt.plot(stepList3)
        plt.plot(stepList4)
        plt.xlabel('time (s)')
        plt.ylabel('voltage (mV)')
        plt.title('About as simple as it gets, folks')
        plt.grid(True)
        plt.savefig("test.png")
        plt.show()
        
        
        
        
        
    
        
    
        
if __name__ == '__main__':
    robot = Overlord(100)
    radius = [None] * 2
    radius[0] = 100
    radius[1] = 100 
    print("start")
    
    radiusInfinite = [50 , 50]
    robot.midPointGrinder(robot.addSpeed(robot.makeAllMoves(robot.makeStepList(50, 50, 110)) , 200) , radiusInfinite)
    sleep(2000.0)
    while(1):
        for i in range(0 , 1000):
            print("")
            for a in robot.moveForInfinity(radius, i / 1000):
                sys.stdout.write(str(a))
                sys.stdout.write(' ')
            
        
        
        
        