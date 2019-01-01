import keyboard


import math




import PyInstaller

import matplotlib.pyplot as plt
import time

from simple_pid import PID
from Runner import Runner
from Overlord import Overlord
from gyroscope import gyro
from PVector import PVector
import serial
from time import sleep

from LX16A import LX16A
'''
Created on Nov 25, 2018

@author: Mic
'''

if __name__ == '__main__':
    data_b = [0 , 0]
    
    blackBox = []
    
    def move1(x , y , z , spedo = 1000):
        poseList = Leg1.step(x , y , z)
        m1.moveServo(1  , int(poseList[0]) , spedo)
        m1.moveServo(13 , int(poseList[1]) , spedo)
        m1.moveServo(3  , int(poseList[2]) , spedo)
        
    def move2(x , y , z , spedo = 1000):
        poseList = Leg2.step(x , y , z)
        m1.moveServo(31 , int(poseList[0]) , spedo)
        m1.moveServo(22 , int(poseList[1]) , spedo)
        m1.moveServo(23 , int(poseList[2]) , spedo)
        
    def move3(x , y , z , spedo = 1000):
        poseList = Leg3.step(x , y , z)
        m1.moveServo(21 , int(poseList[0]) , spedo)
        m1.moveServo(32 , int(poseList[1]) , spedo)
        m1.moveServo(33 , int(poseList[2]) , spedo)
        
    def move4(x , y , z , spedo = 1000):
        poseList = Leg4.step(x , y , z)
        m1.moveServo(11 , int(poseList[0]) , spedo)
        m1.moveServo(12 , int(poseList[1]) , spedo)
        m1.moveServo(2  , int(poseList[2]) , spedo)
    def moveAll(x , y ,z , speed = 0):
        move1(162.079+x, 123.215+y, -162.079+z , speed)
        move2(162.079-x, 123.215+y, 162.079-z , speed)
        move3(162.079-x, 123.215+y, -162.079-z , speed)
        move4(162.079+x, 123.215+y, 162.079+z , speed)
        
    def executeBase(base):
        #print(base)
        #print(-1 *(-base[0][2]+   (126.8095 / math.sqrt(2))))
        #print(-base[0][0]-  (126.8095 / math.sqrt(2)))
        #sleep(200000)
        move1(  -base[0][0]-  (126.8095 / math.sqrt(2)) , base[0][1] , -base[0][2]+   (126.8095 / math.sqrt(2)) , 0)
        move2(  base[1][0]-   (126.8095 / math.sqrt(2)),   base[1][1] ,    base[1][2]-  (126.8095 / math.sqrt(2)) , 0)
        move3(  base[2][0]-  (126.8095 / math.sqrt(2)) ,  base[2][1] ,  base[2][2]+  (126.8095 / math.sqrt(2)) , 0)
        move4(  -base[3][0]-   (126.8095 / math.sqrt(2)) , base[3][1] , -base[3][2]-   (126.8095 / math.sqrt(2)), 0)
    
    
    ser = serial.Serial()
    m1 = LX16A()
    robot = Overlord(126.8095)
    gyro = gyro()
    
    Leg1 = Runner( 611 + 187.5 , 634 , 500 )
    Leg2 = Runner( 347 - 187.5 , 549 , 340 )
    Leg3 = Runner( 273 + 187.5 , 489 , 440 )
    Leg4 = Runner( 500 , 405 , 325 )
    
    literation = 800
    cordinate = [None] * 2
    radiusInfinite = [30 , 30]
    print(m1.readVoltage(31))
    '''
    while(1):
        for i in range(0 , 500):
            moveAll(0 , i/10 , 0)
            print(i)
            
        for i in range(0 , 500):
            moveAll(0 , 1000-(i/10) , 0)
            print(i)
    
    '''
    '''
    while(1):
        moveAll(0 , -20 , 0 , 500)
        sleep(0.5)
        moveAll(0 , -20 , -80, 500)
        sleep(0.5)
        moveAll(0 , -20 , 80, 500)
        sleep(0.5)
        
        moveAll(0 , -20 , 0, 500)
        sleep(0.5)
        moveAll(80 , -20 , 0, 500)
        sleep(0.5)
        moveAll(-80 , -20 , 0, 500)
        sleep(0.5)
        
        moveAll(0 , -20 , 0, 500)
        sleep(0.5)
        moveAll(0 , 150 , 0, 500)
        sleep(0.5)
        moveAll(0 , -50 , 0, 500)
        sleep(0.5)
    
    
    '''
    xBias = 120
    zBias = 160
    yBias = 0
    
    yMove = 110
    aMove = 100
    bMove = aMove / math.sqrt(2)
    
    #xposStatic = 0
    #yposStatic = 0
    #zposStatic = 0
    
    radiusInfinite = [1 , 1]     
    speed = 6
    def addRecord(list):
        global blackBox
        blackBox.append(list)
    
    def rotate_counter_clockwise():
        pose = robot.midPointGrinderZ(robot.addSpeed(robot.makeAllMoves2(robot.universal_StepList_rotary(170 , 30, 110 , 1)) , speed) , radiusInfinite)
        for step in range(0 , speed * 16):
            move1(pose[0][1][step]  , pose[0][0][step] + yBias , -pose[0][2][step] , 0)
            move2(-pose[3][1][step] , pose[3][0][step]+ yBias , pose[3][2][step] , 0)
            move3(-pose[2][1][step] , pose[2][0][step]+ yBias , -pose[2][2][step] , 0)
            move4( pose[1][1][step] , pose[1][0][step]+ yBias , pose[1][2][step] , 0)
    
    def rotate_clockwise():
        pose = robot.midPointGrinderZ(robot.addSpeed(robot.makeAllMoves2(robot.universal_StepList_rotary(170 , 30, 110 , 0)) , speed) , radiusInfinite)
        for step in range(0 , speed * 16):
            move1(pose[0][1][step] + xBias , pose[0][0][step] + yBias , pose[0][2][step] - zBias , 0)
            move2(-pose[3][1][step]+ xBias , pose[3][0][step]+ yBias , -pose[3][2][step] + zBias , 0)
            move3(-pose[2][1][step]+ xBias , pose[2][0][step]+ yBias , -pose[2][2][step] - zBias , 0)
            move4( pose[1][1][step]+ xBias , pose[1][0][step]+ yBias , pose[1][2][step] +  zBias , 0)
            
    
            
    def left_front():
        tempList = []
        pose = robot.midPointGrinderZ(robot.addSpeed(robot.makeAllMoves2(robot.universal_StepList(-bMove, yMove, bMove)) , speed) , radiusInfinite)
        for step in range(0 , speed * 16):
            move1(pose[0][1][step] + xBias , pose[0][0][step] + yBias , pose[0][2][step] - zBias , 0)
            move2(-pose[3][1][step]+ xBias , pose[3][0][step]+ yBias , -pose[3][2][step] + zBias , 0)
            move3(-pose[2][1][step]+ xBias , pose[2][0][step]+ yBias , -pose[2][2][step] - zBias , 0)
            move4( pose[1][1][step]+ xBias , pose[1][0][step]+ yBias , pose[1][2][step] +  zBias , 0)
            tempList.append(gyro.receivePacket)
            
        for step in range(0 , speed * 16):
            move1(pose[0][1][step] + xBias , pose[0][0][step] + yBias , pose[0][2][step] - zBias , 0)
            move2(-pose[3][1][step]+ xBias , pose[3][0][step]+ yBias , -pose[3][2][step] + zBias , 0)
            move3(-pose[2][1][step]+ xBias , pose[2][0][step]+ yBias , -pose[2][2][step] - zBias , 0)
            move4( pose[1][1][step]+ xBias , pose[1][0][step]+ yBias , pose[1][2][step] +  zBias , 0)
            tempList.append(gyro.receivePacket)
        addRecord(tempList)

    def true_front():
        global data_b
        tempList = []
        pose = robot.midPointGrinderZ(robot.addSpeed(robot.makeAllMoves2(robot.universal_StepList(0, yMove, aMove)) , speed) , radiusInfinite)
        for step in range(0 , speed * 16):
            move1(pose[0][1][step] + xBias , pose[0][0][step] + yBias , pose[0][2][step] - zBias , 0)
            move2(-pose[3][1][step]+ xBias , pose[3][0][step]+ yBias , -pose[3][2][step] + zBias , 0)
            move3(-pose[2][1][step]+ xBias , pose[2][0][step]+ yBias , -pose[2][2][step] - zBias , 0)
            move4( pose[1][1][step]+ xBias , pose[1][0][step]+ yBias , pose[1][2][step] +  zBias , 0)
            tempList.append([data_b[0] , data_b[1]])
        for step in range(0 , speed * 16):
            move1(pose[0][1][step] + xBias , pose[0][0][step] + yBias , pose[0][2][step] - zBias , 0)
            move2(-pose[3][1][step]+ xBias , pose[3][0][step]+ yBias , -pose[3][2][step] + zBias , 0)
            move3(-pose[2][1][step]+ xBias , pose[2][0][step]+ yBias , -pose[2][2][step] - zBias , 0)
            move4( pose[1][1][step]+ xBias , pose[1][0][step]+ yBias , pose[1][2][step] +  zBias , 0)
            tempList.append([data_b[0] , data_b[1]])
        addRecord(tempList)
    
    def right_front():
        tempList = []
        pose = robot.midPointGrinderZ(robot.addSpeed(robot.makeAllMoves2(robot.universal_StepList(bMove, yMove, bMove)) , speed) , radiusInfinite)
        for step in range(0 , speed * 16):
            move1(pose[0][1][step] + xBias , pose[0][0][step] + yBias , pose[0][2][step] - zBias , 0)
            move2(-pose[3][1][step]+ xBias , pose[3][0][step]+ yBias , -pose[3][2][step] + zBias , 0)
            move3(-pose[2][1][step]+ xBias , pose[2][0][step]+ yBias , -pose[2][2][step] - zBias , 0)
            move4( pose[1][1][step]+ xBias , pose[1][0][step]+ yBias , pose[1][2][step] +  zBias , 0)
            tempList.append(gyro.receivePacket)
        for step in range(0 , speed * 16):
            move1(pose[0][1][step] + xBias , pose[0][0][step] + yBias , pose[0][2][step] - zBias , 0)
            move2(-pose[3][1][step]+ xBias , pose[3][0][step]+ yBias , -pose[3][2][step] + zBias , 0)
            move3(-pose[2][1][step]+ xBias , pose[2][0][step]+ yBias , -pose[2][2][step] - zBias , 0)
            move4( pose[1][1][step]+ xBias , pose[1][0][step]+ yBias , pose[1][2][step] +  zBias , 0)
            tempList.append(gyro.receivePacket)
        addRecord(tempList)
    
    def true_left():
        tempList = []
        pose = robot.midPointGrinderZ(robot.addSpeed(robot.makeAllMoves2(robot.universal_StepList(-aMove, yMove, 0)) , speed) , radiusInfinite)
        for step in range(0 , speed * 16):
            move1(pose[0][1][step] + xBias , pose[0][0][step] + yBias , pose[0][2][step] - zBias , 0)
            move2(-pose[3][1][step]+ xBias , pose[3][0][step]+ yBias , -pose[3][2][step] + zBias , 0)
            move3(-pose[2][1][step]+ xBias , pose[2][0][step]+ yBias , -pose[2][2][step] - zBias , 0)
            move4( pose[1][1][step]+ xBias , pose[1][0][step]+ yBias , pose[1][2][step] +  zBias , 0)
            tempList.append(gyro.receivePacket)
        for step in range(0 , speed * 16):
            move1(pose[0][1][step] + xBias , pose[0][0][step] + yBias , pose[0][2][step] - zBias , 0)
            move2(-pose[3][1][step]+ xBias , pose[3][0][step]+ yBias , -pose[3][2][step] + zBias , 0)
            move3(-pose[2][1][step]+ xBias , pose[2][0][step]+ yBias , -pose[2][2][step] - zBias , 0)
            move4( pose[1][1][step]+ xBias , pose[1][0][step]+ yBias , pose[1][2][step] +  zBias , 0)
            tempList.append(gyro.receivePacket)
        addRecord(tempList)
    
    def stay():
        move1(162.079, 173.215, -162.079)
        move2(162.079, 173.215, 162.079)
        move3(162.079, 173.215, -162.079)
        move4(162.079, 173.215, 162.079)
        sleep(1.0)
        move1(162.079, 103.215, -162.079)
        move2(162.079, 103.215, 162.079)
        move3(162.079, 103.215, -162.079)
        move4(162.079, 103.215, 162.079)
        
        
         
        
        
    
    def true_right():
        tempList = []
        pose = robot.midPointGrinderZ(robot.addSpeed(robot.makeAllMoves2(robot.universal_StepList(aMove, yMove, 0)) , speed) , radiusInfinite)
        for step in range(0 , speed * 16):
            move1(pose[0][1][step] + xBias , pose[0][0][step] + yBias , pose[0][2][step] - zBias , 0)
            move2(-pose[3][1][step]+ xBias , pose[3][0][step]+ yBias , -pose[3][2][step] + zBias , 0)
            move3(-pose[2][1][step]+ xBias , pose[2][0][step]+ yBias , -pose[2][2][step] - zBias , 0)
            move4( pose[1][1][step]+ xBias , pose[1][0][step]+ yBias , pose[1][2][step] +  zBias , 0)
            tempList.append(gyro.receivePacket)
        for step in range(0 , speed * 16):
            move1(pose[0][1][step] + xBias , pose[0][0][step] + yBias , pose[0][2][step] - zBias , 0)
            move2(-pose[3][1][step]+ xBias , pose[3][0][step]+ yBias , -pose[3][2][step] + zBias , 0)
            move3(-pose[2][1][step]+ xBias , pose[2][0][step]+ yBias , -pose[2][2][step] - zBias , 0)
            move4( pose[1][1][step]+ xBias , pose[1][0][step]+ yBias , pose[1][2][step] +  zBias , 0)
            tempList.append(gyro.receivePacket)
        addRecord(tempList)
    
    def left_back():
        tempList = []
        pose = robot.midPointGrinderZ(robot.addSpeed(robot.makeAllMoves2(robot.universal_StepList(-bMove, yMove, -bMove)) , speed) , radiusInfinite)
        for step in range(0 , speed * 16):
            move1(pose[0][1][step] + xBias , pose[0][0][step] + yBias , pose[0][2][step] - zBias , 0)
            move2(-pose[3][1][step]+ xBias , pose[3][0][step]+ yBias , -pose[3][2][step] + zBias , 0)
            move3(-pose[2][1][step]+ xBias , pose[2][0][step]+ yBias , -pose[2][2][step] - zBias , 0)
            move4( pose[1][1][step]+ xBias , pose[1][0][step]+ yBias , pose[1][2][step] +  zBias , 0)
            tempList.append(gyro.receivePacket)
        for step in range(0 , speed * 16):
            move1(pose[0][1][step] + xBias , pose[0][0][step] + yBias , pose[0][2][step] - zBias , 0)
            move2(-pose[3][1][step]+ xBias , pose[3][0][step]+ yBias , -pose[3][2][step] + zBias , 0)
            move3(-pose[2][1][step]+ xBias , pose[2][0][step]+ yBias , -pose[2][2][step] - zBias , 0)
            move4( pose[1][1][step]+ xBias , pose[1][0][step]+ yBias , pose[1][2][step] +  zBias , 0)
            tempList.append(gyro.receivePacket)
        addRecord(tempList)
    
    def true_back():
        tempList = []
        pose = robot.midPointGrinderZ(robot.addSpeed(robot.makeAllMoves2(robot.universal_StepList(0, yMove, -aMove)) , speed) , radiusInfinite)
        for step in range(0 , speed * 16):
            move1(pose[0][1][step] + xBias , pose[0][0][step] + yBias , pose[0][2][step] - zBias , 0)
            move2(-pose[3][1][step]+ xBias , pose[3][0][step]+ yBias , -pose[3][2][step] + zBias , 0)
            move3(-pose[2][1][step]+ xBias , pose[2][0][step]+ yBias , -pose[2][2][step] - zBias , 0)
            move4( pose[1][1][step]+ xBias , pose[1][0][step]+ yBias , pose[1][2][step] +  zBias , 0)
            tempList.append(gyro.receivePacket)
        for step in range(0 , speed * 16):
            move1(pose[0][1][step] + xBias , pose[0][0][step] + yBias , pose[0][2][step] - zBias , 0)
            move2(-pose[3][1][step]+ xBias , pose[3][0][step]+ yBias , -pose[3][2][step] + zBias , 0)
            move3(-pose[2][1][step]+ xBias , pose[2][0][step]+ yBias , -pose[2][2][step] - zBias , 0)
            move4( pose[1][1][step]+ xBias , pose[1][0][step]+ yBias , pose[1][2][step] +  zBias , 0)
            tempList.append(gyro.receivePacket)
        addRecord(tempList)
    
    def right_back():
        tempList = []
        pose = robot.midPointGrinderZ(robot.addSpeed(robot.makeAllMoves2(robot.universal_StepList(bMove, yMove, -bMove)) , speed) , radiusInfinite)
        for step in range(0 , speed * 16):
            move1(pose[0][1][step] + xBias , pose[0][0][step] + yBias , pose[0][2][step] - zBias , 0)
            move2(-pose[3][1][step]+ xBias , pose[3][0][step]+ yBias , -pose[3][2][step] + zBias , 0)
            move3(-pose[2][1][step]+ xBias , pose[2][0][step]+ yBias , -pose[2][2][step] - zBias , 0)
            move4( pose[1][1][step]+ xBias , pose[1][0][step]+ yBias , pose[1][2][step] +  zBias , 0)
            tempList.append(gyro.receivePacket)
        for step in range(0 , speed * 16):
            move1(pose[0][1][step] + xBias , pose[0][0][step] + yBias , pose[0][2][step] - zBias , 0)
            move2(-pose[3][1][step]+ xBias , pose[3][0][step]+ yBias , -pose[3][2][step] + zBias , 0)
            move3(-pose[2][1][step]+ xBias , pose[2][0][step]+ yBias , -pose[2][2][step] - zBias , 0)
            move4( pose[1][1][step]+ xBias , pose[1][0][step]+ yBias , pose[1][2][step] +  zBias , 0)
            tempList.append(gyro.receivePacket)
        addRecord(tempList)
        
        
        
    def customMade(xMove , zMove):
        tempList = []
        pose = robot.midPointGrinderZ(robot.addSpeed(robot.makeAllMoves2(robot.universal_StepList(xMove, yMove, zMove)) , speed) , radiusInfinite)
        for step in range(0 , speed * 16):
            move1(pose[0][1][step] + xBias , pose[0][0][step] + yBias , pose[0][2][step] - zBias , 0)
            move2(-pose[3][1][step]+ xBias , pose[3][0][step]+ yBias , -pose[3][2][step] + zBias , 0)
            move3(-pose[2][1][step]+ xBias , pose[2][0][step]+ yBias , -pose[2][2][step] - zBias , 0)
            move4( pose[1][1][step]+ xBias , pose[1][0][step]+ yBias , pose[1][2][step] +  zBias , 0)
            tempList.append(gyro.receivePacket)
        for step in range(0 , speed * 16):
            move1(pose[0][1][step] + xBias , pose[0][0][step] + yBias , pose[0][2][step] - zBias , 0)
            move2(-pose[3][1][step]+ xBias , pose[3][0][step]+ yBias , -pose[3][2][step] + zBias , 0)
            move3(-pose[2][1][step]+ xBias , pose[2][0][step]+ yBias , -pose[2][2][step] - zBias , 0)
            move4( pose[1][1][step]+ xBias , pose[1][0][step]+ yBias , pose[1][2][step] +  zBias , 0)
            tempList.append(gyro.receivePacket)
        addRecord(tempList)
        
    def testTrend():
        global blackBox
        true_front()
        true_front()
        sleep(10) 
        true_front()
        true_front()
        sleep(10) 
        true_front()
        true_front()
        sleep(10) 
        true_front()
        true_front()
        sleep(10) 
        true_front()
        true_front()
        sleep(10) 
        
        true_front()
        true_front()
        sleep(10) 
        true_front()
        true_front()
        sleep(10) 
        true_front()
        true_front()
        sleep(10) 
        true_front()
        true_front()
        sleep(10) 
        true_front()
        true_front()
        #sleep(10) 
        
        print(blackBox)
        
        listA = []
        listB = []
        list0 = produceTrend(blackBox)
        for a in list0:
            listA.append(a[0])
            listB.append(a[1])
            
        plt.plot(listA , 'r')
        plt.plot(listB , 'b')

            
        plt.xlabel('time (s)')
        plt.ylabel('pose (mm)')
        plt.title('we will rise folks')
        plt.grid(True)
        plt.savefig("test.png")
        plt.show()
    
        
    def produceTrend(list0):
        lenghtA = 0
        lenghtB = 0
        readOne = True
        
        trend = []
        
        for a in list0:
            if readOne:
                for n in a:
                    lenghtB += 1
                readOne = False
            lenghtA += 1
            
        for i in range(0 , lenghtB):
            
            tempSumA = 0
            tempSumB = 0
            for n in range(0 , lenghtA):
                tempSumA += list0[n][i][0]
                tempSumB += list0[n][i][1]
                
            tempSumA = tempSumA / lenghtA
            tempSumB = tempSumB / lenghtA
            
            trend.append([tempSumA , tempSumB])
            
        return trend
            
        
    
    incresementInMove = 10
    
    xposStatic = 0
    yposStatic = 0
    zposStatic = 0
    
    
    def upper_move():
        global yposStatic
        yposStatic = yposStatic + incresementInMove
        moveAll(xposStatic , yposStatic , zposStatic)
    
    def move_down():
        global yposStatic
        yposStatic = yposStatic -incresementInMove
        moveAll(xposStatic , yposStatic , zposStatic)
    
    def move_left():
        global zposStatic
        zposStatic = zposStatic +incresementInMove
        moveAll(xposStatic , yposStatic , zposStatic)
    
    def move_right_():
        global zposStatic
        zposStatic = zposStatic -incresementInMove
        moveAll(xposStatic , yposStatic , zposStatic)
    
    def move_forvard():
        global xposStatic
        xposStatic = xposStatic +incresementInMove
        moveAll(xposStatic , yposStatic , zposStatic)
    
    def move_back():
        global xposStatic
        xposStatic = xposStatic -incresementInMove
        moveAll(xposStatic , yposStatic , zposStatic)
        
        
    Xrotation = 0
    Yrotation = 0
    Zrotation = 0
    
    val_34 = 126.8095 / math.sqrt(2)
    
    base = [[-150 - val_34 , 150 ,  150 + val_34] ,
            [ 150 + val_34 , 150 ,  150 + val_34] ,
            [ 150 + val_34 , 150 , -150 - val_34] ,
            [-150 - val_34 , 150 , -150 - val_34] ]
    
    vector = PVector(base , 126.8095)
    
    incresementInRotation = 5 / 57.2958
        
    def rotateX_C():
        global Xrotation
        global Yrotation
        global Zrotation
        Xrotation = Xrotation + incresementInRotation
        vector.rotateX(Xrotation)
        vector.rotateY(Yrotation)
        vector.rotateZ(Zrotation)
        executeBase(vector.result())
        print("Xrotation")
        print(Xrotation * 57.2958)
        print("Yrotation")
        print(Yrotation * 57.2958)
        print("Zrotation")
        print(Zrotation * 57.2958)
    
    def rotateX_O():
        global Xrotation
        global Yrotation
        global Zrotation
        Xrotation = Xrotation - incresementInRotation
        vector.rotateX(Xrotation)
        vector.rotateY(Yrotation)
        vector.rotateZ(Zrotation)
        executeBase(vector.result())
        print("Xrotation")
        print(Xrotation * 57.2958)
        print("Yrotation")
        print(Yrotation * 57.2958)
        print("Zrotation")
        print(Zrotation * 57.2958)
    
    def rotateY_C():
        global Xrotation
        global Yrotation
        global Zrotation
        Yrotation = Yrotation + incresementInRotation
        vector.rotateX(Xrotation)
        vector.rotateY(Yrotation)
        vector.rotateZ(Zrotation)
        executeBase(vector.result())
        print("Xrotation")
        print(Xrotation * 57.2958)
        print("Yrotation")
        print(Yrotation * 57.2958)
        print("Zrotation")
        print(Zrotation * 57.2958)
    
    def rotateY_O():
        global Xrotation
        global Yrotation
        global Zrotation
        Yrotation = Yrotation - incresementInRotation
        vector.rotateX(Xrotation)
        vector.rotateY(Yrotation)
        vector.rotateZ(Zrotation)
        executeBase(vector.result())
        print("Xrotation")
        print(Xrotation * 57.2958)
        print("Yrotation")
        print(Yrotation * 57.2958)
        print("Zrotation")
        print(Zrotation * 57.2958)
    
    def rotateZ_C():
        global Xrotation
        global Yrotation
        global Zrotation
        Zrotation = Zrotation + incresementInRotation
        vector.rotateX(Xrotation)
        vector.rotateY(Yrotation)
        vector.rotateZ(Zrotation)
        executeBase(vector.result())
        print("Xrotation")
        print(Xrotation * 57.2958)
        print("Yrotation")
        print(Yrotation * 57.2958)
        print("Zrotation")
        print(Zrotation * 57.2958)
    
    def rotateZ_O():
        global Xrotation
        global Yrotation
        global Zrotation
        Zrotation = Zrotation - incresementInRotation
        vector.rotateX(Xrotation)
        vector.rotateY(Yrotation)
        vector.rotateZ(Zrotation)
        executeBase(vector.result())
        print("Xrotation")
        print(Xrotation * 57.2958)
        print("Yrotation")
        print(Yrotation * 57.2958)
        print("Zrotation")
        print(Zrotation * 57.2958)
    
    
    spedowagonVal = 8
    def testX():
        lenght = int((300 / spedowagonVal) * 16 * 3)
        tableInput = [0 for x in range(lenght)]
        tableOutput = [0 for x in range(lenght)]
        n = 0
        previousData = 0
        '''
        accualTime_if = time.time()* 1000
        accualTime = time.time()* 1000
        for j in range(0 , 1000):
            sleep(0.01)
            if(time.time()* 1000 - accualTime_if > 6.0):
                accualTime_if = time.time()* 1000
                data = gyro.receivePacket()
                print(data)
                #if(data != None)
        '''
        for i in range(0 , 8):
            for Xrotation in range(int(-300 / spedowagonVal) , int(300/ spedowagonVal)):
                Xrotation = Xrotation / (57.2958 * 10/ spedowagonVal)
                vector.rotateX(Xrotation)
                vector.rotateY(0)
                vector.rotateZ(0)
                executeBase(vector.result())
                
                tableInput[n] = -Xrotation* 40 * 1.12
                data_p = gyro.receivePacket()
                if(data_p != None):
                    tableOutput[n] = data_p[1]
                    previousData = tableOutput[n]
                    
                else:
                    tableOutput[n] = previousData
                    print("NULL")
                    
                    
                n += 1
            for Xrotation in range(int(-300/ spedowagonVal) , int(300/ spedowagonVal)):
                Xrotation = Xrotation / (57.2958 * 10/ spedowagonVal)
                vector.rotateX(-Xrotation)
                vector.rotateY(0)
                vector.rotateZ(0)
                executeBase(vector.result())
                
                tableInput[n] = Xrotation * 40* 1.12
                data_p = gyro.receivePacket()
                if(data_p != None):
                    tableOutput[n] = data_p[1]
                    previousData = tableOutput[n]
                else:
                    tableOutput[n] = previousData
                    print("NULL")
                    
                    
                n += 1
                
        for i in range(0 , 500):
            tableInput[n] = 0
            data_p = gyro.receivePacket()
            if(data_p != None):
                tableOutput[n] = data_p[1]
                previousData = tableOutput[n]
                
            else:
                tableOutput[n] = previousData
                print("NULL")
                
            n += 1
        
        for o in tableInput:
            print(o)
            
        print("*********")
        
        for o in tableOutput:
            print(o)
            
        plt.plot(tableInput , 'r')
        plt.plot(tableOutput , 'b')

            
        plt.xlabel('time (s)')
        plt.ylabel('pose (mm)')
        plt.title('we will rise folks')
        plt.grid(True)
        plt.savefig("test.png")
        plt.show()

    
    def testZ():
        for i in range(0 , 4):
            for Zrotation in range(int(-300/ spedowagonVal) , int(300/ spedowagonVal)):
                Zrotation = Zrotation / (57.2958 * (10/ spedowagonVal))
                vector.rotateX(0)
                vector.rotateY(0)
                vector.rotateZ(Zrotation)
                executeBase(vector.result())
            for Zrotation in range(int(-300/ spedowagonVal) , int(300/ spedowagonVal)):
                Zrotation = Zrotation / (57.2958 * (10/ spedowagonVal))
                vector.rotateX(0)
                vector.rotateY(0)
                vector.rotateZ(-Zrotation)
                executeBase(vector.result())
                
    def testY():
        for i in range(0 , 4):
            for Zrotation in range(int(-150/ spedowagonVal) , int(150/ spedowagonVal)):
                Zrotation = Zrotation / (57.2958 * (10/ spedowagonVal))
                vector.rotateZ(0)
                vector.rotateX(0)
                vector.rotateY(Zrotation)
                executeBase(vector.result())
            for Zrotation in range(int(-300/ spedowagonVal) , int(300/ spedowagonVal)):
                Zrotation = Zrotation / (57.2958 * (10/ spedowagonVal))
                vector.rotateZ(0)
                vector.rotateX(0)
                vector.rotateY(-Zrotation)
                executeBase(vector.result())
        
    
    def keepSafe():
        global data_b
        
        lenght = 3000
        table1 = [0 for x in range(lenght)]
        table2 = [0 for x in range(lenght)]
        
        table1b = [0 for x in range(lenght)]
        table2b = [0 for x in range(lenght)]
        
        
        vector.rotateX(0)
        vector.rotateY(0)
        vector.rotateZ(0)
        executeBase(vector.result())
        sleep(2.0)
        
        
        pidX = PID(0.04, 0, 0.02, setpoint=0 , sample_time=0.005)
        pidZ = PID(0.04, 0, 0.02, setpoint=0 , sample_time=0.005)
        
        #pidX = PID(0.009, 0.35, 0.03, setpoint=0 , sample_time=0.005)
        #pidZ = PID(0.009, 0.35, 0.03, setpoint=0 , sample_time=0.005)
        
        
        
        pidX.output_limits = (-35 / 57.2958, 35 / 57.2958) 
        pidZ.output_limits = (-35 / 57.2958, 35 / 57.2958) 
        
        pidX.proportional_on_measurement = True
        pidZ.proportional_on_measurement = True
        
        
        #data_p = gyro.receivePacket()
        try:
            vZ = data_b[0]
        except TypeError:
            print("ni")
            vZ = 0
           
        try:
            vX = data_b[1]
        except TypeError:
            print("ni")
            vX = 0
        
        
        for i in range(0 , lenght):

            controlX = -pidX(vX)
            controlZ = -pidZ(vZ)
            
            #print(controlX)
            table1[i] = controlZ * 10
            table1b[i] = controlX * 10
            
            
            vector.rotateZ(controlZ)
            vector.rotateX(controlX)
            vector.rotateY(0)
            executeBase(vector.result())
            
            
            #data_p = gyro.receivePacket()
            try:
                if(data_b[0] < 25):
                    if(data_b[0] != 0):
                        vZ = data_b[0]

            except TypeError:
                print("I po h mi to")
                
            table2[i] = vZ
               
            try:
                vX = data_b[1]
            except TypeError:
                print("I po h mi to")
                
            table2b[i] = vX
            
        plt.plot(table1 , '#b30000')
        plt.plot(table1b , '#660000')
        plt.plot(table2 , '#0066ff') 
        plt.plot(table2b , '#002966') 
        
        for i in table1:
            print(i)
        print("*****")
        for i in table2:
            print(i)

            
        plt.xlabel('time (s)')
        plt.ylabel('pose (mm)')
        plt.title('we will rise folks')
        plt.grid(True)
        plt.savefig("test.png")
        plt.show()
            
        
               
    
    
    
    
    keyboard.add_hotkey('Q', testTrend)
    keyboard.add_hotkey('W', true_front)
    keyboard.add_hotkey('E', right_front)
    keyboard.add_hotkey('A', true_left)
    keyboard.add_hotkey('S', stay)
    keyboard.add_hotkey('D', true_right)
    keyboard.add_hotkey('Z', left_back)
    keyboard.add_hotkey('X', true_back)
    keyboard.add_hotkey('C', right_back)
    
    keyboard.add_hotkey('f', upper_move)
    keyboard.add_hotkey('v', move_down)
    keyboard.add_hotkey('g', move_left)
    keyboard.add_hotkey('b', move_right_)
    keyboard.add_hotkey('h', move_forvard)
    keyboard.add_hotkey('n', move_back)
    
    keyboard.add_hotkey('u', rotateX_C)
    keyboard.add_hotkey('j', rotateX_O)
    keyboard.add_hotkey('i', rotateY_C)
    keyboard.add_hotkey('k', rotateY_O)
    keyboard.add_hotkey('o', rotateZ_C)
    keyboard.add_hotkey('l', rotateZ_O)
    
    keyboard.add_hotkey('R', testX)
    keyboard.add_hotkey('T', testZ)
    keyboard.add_hotkey('P', testY)
    
    keyboard.add_hotkey('m', keepSafe)
        
    while True:
        tempR = gyro.receivePacket()
        if(tempR != None):
            try:
                ifffr = tempR[1]
                data_b = tempR 
            except IndexError:
                print("lol kek")
            
        
        
        
        
        
        
        
        
        
        
        
    
    move1(162.079, 123.215, -162.079)
    move2(162.079, 123.215, 162.079)
    move3(162.079, 123.215, -162.079)
    move4(162.079, 123.215, 162.079)
    
    sleep(1.0) 
    move1(162.079, 173.215, -162.079)
    move2(162.079, 173.215, 162.079)
    move3(162.079, 173.215, -162.079)
    move4(162.079, 173.215, 162.079)
 
    
    
    print(m1.readVoltage(31))
    sleep(100000.0) 
    
    radiusInfinite = [1 , 1]     
    speed = 4
    
    '''
    while(1):
        pose = robot.midPointGrinderZ(robot.addSpeed(robot.makeAllMoves2(robot.universal_StepList_rotary(170, 110 , 1)) , speed) , radiusInfinite)
        for step in range(0 , speed * 16):
            move1(pose[0][1][step] + 60 , pose[0][0][step] + 20 , pose[0][2][step] - 60 , 0)
            move2(-pose[3][1][step]+ 60 , pose[3][0][step]+ 20 , -pose[3][2][step] + 60 , 0)
            move3(-pose[2][1][step]+ 60 , pose[2][0][step]+ 20 , -pose[2][2][step] - 60 , 0)
            move4( pose[1][1][step]+ 60 , pose[1][0][step]+ 20 , pose[1][2][step] +  60 , 0)
            
        pose = robot.midPointGrinderZ(robot.addSpeed(robot.makeAllMoves2(robot.universal_StepList_rotary(170, 110 , 0)) , speed) , radiusInfinite)
        for step in range(0 , speed * 16):
            move1(pose[0][1][step] + 60 , pose[0][0][step] + 20 , pose[0][2][step] - 60 , 0)
            move2(-pose[3][1][step]+ 60 , pose[3][0][step]+ 20 , -pose[3][2][step] + 60 , 0)
            move3(-pose[2][1][step]+ 60 , pose[2][0][step]+ 20 , -pose[2][2][step] - 60 , 0)
            move4( pose[1][1][step]+ 60 , pose[1][0][step]+ 20 , pose[1][2][step] +  60 , 0)
            
    '''
    
    
    
    
    
    
    
    while(1):
        pose = robot.midPointGrinderZ(robot.addSpeed(robot.makeAllMoves2(robot.universal_StepList(0, 110, 70)) , speed) , radiusInfinite)
        for step in range(0 , speed * 16):
            move1(pose[0][1][step] + 120 , pose[0][0][step] + 20 , pose[0][2][step] - 160 , 0)
            move2(-pose[3][1][step]+ 120 , pose[3][0][step]+ 20 , -pose[3][2][step] + 160 , 0)
            move3(-pose[2][1][step]+ 120 , pose[2][0][step]+ 20 , -pose[2][2][step] - 160 , 0)
            move4( pose[1][1][step]+ 120 , pose[1][0][step]+ 20 , pose[1][2][step] +  160 , 0)
        for step in range(0 , speed * 16):
            move1(pose[0][1][step] + 120 , pose[0][0][step] + 20 , pose[0][2][step] - 160 , 0)
            move2(-pose[3][1][step]+ 120 , pose[3][0][step]+ 20 , -pose[3][2][step] + 160 , 0)
            move3(-pose[2][1][step]+ 120 , pose[2][0][step]+ 20 , -pose[2][2][step] - 160 , 0)
            move4( pose[1][1][step]+ 120 , pose[1][0][step]+ 20 , pose[1][2][step] +  160 , 0)
            
        pose = robot.midPointGrinderZ(robot.addSpeed(robot.makeAllMoves2(robot.universal_StepList(50, 110, 50)) , speed) , radiusInfinite)
        for step in range(0 , speed * 16):
            move1(pose[0][1][step] + 120 , pose[0][0][step] + 20 , pose[0][2][step] - 160 , 0)
            move2(-pose[3][1][step]+ 120 , pose[3][0][step]+ 20 , -pose[3][2][step] + 160 , 0)
            move3(-pose[2][1][step]+ 120 , pose[2][0][step]+ 20 , -pose[2][2][step] - 160 , 0)
            move4( pose[1][1][step]+ 120 , pose[1][0][step]+ 20 , pose[1][2][step] +  160 , 0)
        for step in range(0 , speed * 16):
            move1(pose[0][1][step] + 120 , pose[0][0][step] + 20 , pose[0][2][step] - 160 , 0)
            move2(-pose[3][1][step]+ 120 , pose[3][0][step]+ 20 , -pose[3][2][step] + 160 , 0)
            move3(-pose[2][1][step]+ 120 , pose[2][0][step]+ 20 , -pose[2][2][step] - 160 , 0)
            move4( pose[1][1][step]+ 120 , pose[1][0][step]+ 20 , pose[1][2][step] +  160 , 0)
            
        pose = robot.midPointGrinderZ(robot.addSpeed(robot.makeAllMoves2(robot.universal_StepList(-50, 110, -50)) , speed) , radiusInfinite)
        for step in range(0 , speed * 16):
            move1(pose[0][1][step] + 120 , pose[0][0][step] + 20 , pose[0][2][step] - 160 , 0)
            move2(-pose[3][1][step]+ 120 , pose[3][0][step]+ 20 , -pose[3][2][step] + 160 , 0)
            move3(-pose[2][1][step]+ 120 , pose[2][0][step]+ 20 , -pose[2][2][step] - 160 , 0)
            move4( pose[1][1][step]+ 120 , pose[1][0][step]+ 20 , pose[1][2][step] +  160 , 0)
        for step in range(0 , speed * 16):
            move1(pose[0][1][step] + 120 , pose[0][0][step] + 20 , pose[0][2][step] - 160 , 0)
            move2(-pose[3][1][step]+ 120 , pose[3][0][step]+ 20 , -pose[3][2][step] + 160 , 0)
            move3(-pose[2][1][step]+ 120 , pose[2][0][step]+ 20 , -pose[2][2][step] - 160 , 0)
            move4( pose[1][1][step]+ 120 , pose[1][0][step]+ 20 , pose[1][2][step] +  160 , 0)
            
        pose = robot.midPointGrinderZ(robot.addSpeed(robot.makeAllMoves2(robot.universal_StepList(-50, 110, 50)) , speed) , radiusInfinite)
        for step in range(0 , speed * 16):
            move1(pose[0][1][step] + 120 , pose[0][0][step] + 20 , pose[0][2][step] - 160 , 0)
            move2(-pose[3][1][step]+ 120 , pose[3][0][step]+ 20 , -pose[3][2][step] + 160 , 0)
            move3(-pose[2][1][step]+ 120 , pose[2][0][step]+ 20 , -pose[2][2][step] - 160 , 0)
            move4( pose[1][1][step]+ 120 , pose[1][0][step]+ 20 , pose[1][2][step] +  160 , 0)
        for step in range(0 , speed * 16):
            move1(pose[0][1][step] + 120 , pose[0][0][step] + 20 , pose[0][2][step] - 160 , 0)
            move2(-pose[3][1][step]+ 120 , pose[3][0][step]+ 20 , -pose[3][2][step] + 160 , 0)
            move3(-pose[2][1][step]+ 120 , pose[2][0][step]+ 20 , -pose[2][2][step] - 160 , 0)
            move4( pose[1][1][step]+ 120 , pose[1][0][step]+ 20 , pose[1][2][step] +  160 , 0)
            
        pose = robot.midPointGrinderZ(robot.addSpeed(robot.makeAllMoves2(robot.universal_StepList(50, 110, -50)) , speed) , radiusInfinite)
        for step in range(0 , speed * 16):
            move1(pose[0][1][step] + 120 , pose[0][0][step] + 20 , pose[0][2][step] - 160 , 0)
            move2(-pose[3][1][step]+ 120 , pose[3][0][step]+ 20 , -pose[3][2][step] + 160 , 0)
            move3(-pose[2][1][step]+ 120 , pose[2][0][step]+ 20 , -pose[2][2][step] - 160 , 0)
            move4( pose[1][1][step]+ 120 , pose[1][0][step]+ 20 , pose[1][2][step] +  160 , 0)
        for step in range(0 , speed * 16):
            move1(pose[0][1][step] + 120 , pose[0][0][step] + 20 , pose[0][2][step] - 160 , 0)
            move2(-pose[3][1][step]+ 120 , pose[3][0][step]+ 20 , -pose[3][2][step] + 160 , 0)
            move3(-pose[2][1][step]+ 120 , pose[2][0][step]+ 20 , -pose[2][2][step] - 160 , 0)
            move4( pose[1][1][step]+ 120 , pose[1][0][step]+ 20 , pose[1][2][step] +  160 , 0)
            
        pose = robot.midPointGrinderZ(robot.addSpeed(robot.makeAllMoves2(robot.universal_StepList(0, 110, -70)) , speed) , radiusInfinite)
        for step in range(0 , speed * 16):
            move1(pose[0][1][step] + 120 , pose[0][0][step] + 20 , pose[0][2][step] - 160 , 0)
            move2(-pose[3][1][step]+ 120 , pose[3][0][step]+ 20 , -pose[3][2][step] + 160 , 0)
            move3(-pose[2][1][step]+ 120 , pose[2][0][step]+ 20 , -pose[2][2][step] - 160 , 0)
            move4( pose[1][1][step]+ 120 , pose[1][0][step]+ 20 , pose[1][2][step] +  160 , 0)
        for step in range(0 , speed * 16):
            move1(pose[0][1][step] + 120 , pose[0][0][step] + 20 , pose[0][2][step] - 160 , 0)
            move2(-pose[3][1][step]+ 120 , pose[3][0][step]+ 20 , -pose[3][2][step] + 160 , 0)
            move3(-pose[2][1][step]+ 120 , pose[2][0][step]+ 20 , -pose[2][2][step] - 160 , 0)
            move4( pose[1][1][step]+ 120 , pose[1][0][step]+ 20 , pose[1][2][step] +  160 , 0)
            
        pose = robot.midPointGrinder(robot.addSpeed(robot.makeAllMoves2(robot.universal_StepList(70, 110, 0)) , speed) , radiusInfinite)
        for step in range(0 , speed * 16):
            move1(pose[0][1][step] + 120 , pose[0][0][step] + 20 , pose[0][2][step] - 160 , 0)
            move2(-pose[3][1][step]+ 120 , pose[3][0][step]+ 20 , -pose[3][2][step] + 160 , 0)
            move3(-pose[2][1][step]+ 120 , pose[2][0][step]+ 20 , -pose[2][2][step] - 160 , 0)
            move4( pose[1][1][step]+ 120 , pose[1][0][step]+ 20 , pose[1][2][step] +  160 , 0)
        for step in range(0 , speed * 16):
            move1(pose[0][1][step] + 120 , pose[0][0][step] + 20 , pose[0][2][step] - 160 , 0)
            move2(-pose[3][1][step]+ 120 , pose[3][0][step]+ 20 , -pose[3][2][step] + 160 , 0)
            move3(-pose[2][1][step]+ 120 , pose[2][0][step]+ 20 , -pose[2][2][step] - 160 , 0)
            move4( pose[1][1][step]+ 120 , pose[1][0][step]+ 20 , pose[1][2][step] +  160 , 0)
            
        pose = robot.midPointGrinder(robot.addSpeed(robot.makeAllMoves2(robot.universal_StepList(-70, 110, 0)) , speed) , radiusInfinite)
        for step in range(0 , speed * 16):
            move1(pose[0][1][step] + 120 , pose[0][0][step] + 20 , pose[0][2][step] - 160 , 0)
            move2(-pose[3][1][step]+ 120 , pose[3][0][step]+ 20 , -pose[3][2][step] + 160 , 0)
            move3(-pose[2][1][step]+ 120 , pose[2][0][step]+ 20 , -pose[2][2][step] - 160 , 0)
            move4( pose[1][1][step]+ 120 , pose[1][0][step]+ 20 , pose[1][2][step] +  160 , 0)
        for step in range(0 , speed * 16):
            move1(pose[0][1][step] + 120 , pose[0][0][step] + 20 , pose[0][2][step] - 160 , 0)
            move2(-pose[3][1][step]+ 120 , pose[3][0][step]+ 20 , -pose[3][2][step] + 160 , 0)
            move3(-pose[2][1][step]+ 120 , pose[2][0][step]+ 20 , -pose[2][2][step] - 160 , 0)
            move4( pose[1][1][step]+ 120 , pose[1][0][step]+ 20 , pose[1][2][step] +  160 , 0)
            
            
    
    
    
    radiusInfinite = [1 , 1]     
    speed = 5
    while(1):
        pose = robot.midPointGrinder(robot.addSpeed(robot.makeAllMoves2(robot.makeStepList(70, 110, 170)) , speed) , radiusInfinite)
        for step in range(0 , speed * 16):
            move1(pose[0][1][step] + 120 , pose[0][0][step] + 20 , pose[0][2][step] - 160 , 0)
            move2(-pose[3][1][step]+ 120 , pose[3][0][step]+ 20 , -pose[3][2][step] + 160 , 0)
            move3(-pose[2][1][step]+ 120 , pose[2][0][step]+ 20 , -pose[2][2][step] - 160 , 0)
            move4( pose[1][1][step]+ 120 , pose[1][0][step]+ 20 , pose[1][2][step] +  160 , 0)
    
    
    
    radiusInfinite = [30 , 30]
    speed = 6
    while(1):
        pose = robot.midPointGrinder(robot.addSpeed(robot.makeAllMoves(robot.makeStepList(70, 110, 170)) , speed) , radiusInfinite)
        for step in range(0 , speed * 16):
            move1(pose[0][1][step] + 120 , pose[0][0][step] + 20 , pose[0][2][step] - 160 , 0)
            move2(-pose[3][1][step]+ 120 , pose[3][0][step]+ 20 , -pose[3][2][step] + 160 , 0)
            move3(-pose[2][1][step]+ 120 , pose[2][0][step]+ 20 , -pose[2][2][step] - 160 , 0)
            move4( pose[1][1][step]+ 120 , pose[1][0][step]+ 20 , pose[1][2][step] +  160 , 0)
        
            
        
    
    
    while(1):
        moveAll(0 , -20 , -50)
        sleep(2.0)
        moveAll(0 , -20 , 50)
        sleep(2.0)
    
    
    
    while(1):
        for i in range(0 , literation):
            n = 0
            for a in(robot.moveForInfinity(radiusInfinite, i/literation)):
                cordinate[n] = a
                n = n + 1
            moveAll(cordinate[0] , -20 , cordinate[1])
            
      
            
      
    
    
    
    while(1):
        move1(110, 250, -110)
        move2(110, 250, 110)
        move3(110, 250, -110)
        move4(110, 250, 110)
        
        sleep(1.0)
        
        move1(110, 120, -110)
        move2(110, 120, 110)
        move3(110, 120, -110)
        move4(110, 120, 110)
        
        sleep(1.0)
        
        
       
        
    while(1):
        print(m1.readPosition(1))
        print(m1.readPosition(13))
        print(m1.readPosition(3))
        print("---")
        
        print(m1.readPosition(31))
        print(m1.readPosition(22))
        print(m1.readPosition(23))
        print("---")
        
        print(m1.readPosition(21))
        print(m1.readPosition(32))
        print(m1.readPosition(33))
        print("---")
        
        print(m1.readPosition(11))
        print(m1.readPosition(12))
        print(m1.readPosition(2))
        
        m1.moveServo(1 , 611 , 500)
        m1.moveServo(13 , 694 , 500)
        m1.moveServo(3 , 500+325 , 500)
        
        m1.moveServo(31 , 347 , 500)
        m1.moveServo(22 , 549 , 500)
        m1.moveServo(23 , 340+325 , 500)
        
        m1.moveServo(21 , 373 , 500)
        m1.moveServo(32 , 489 , 500)
        m1.moveServo(33 , 440+325 , 500)
        
        m1.moveServo(11 , 560 , 500)
        m1.moveServo(12 , 408 , 500)
        m1.moveServo(2 , 360+325 , 500)
        
        
        sleep(2000.0)
    
    
    
    while(1):
        poseList = Leg1.step(182.6032 , 173.215 , 182.6032)
        m1.moveServo(11 , int(poseList[0]) , 500)
        m1.moveServo(12 , int(poseList[1]) , 500)
        m1.moveServo(2  , int(poseList[2]) , 500)
        print(poseList)
        sleep(1.0)
        poseList = Leg1.step(100.6032 , 173.215 , 182.6032)
        m1.moveServo(11 , int(poseList[0]) , 500)
        m1.moveServo(12 , int(poseList[1]) , 500)
        m1.moveServo(2  , int(poseList[2]) , 500)
        print(poseList)
        sleep(2.0)
        poseList = Leg1.step(100.6032 , 173.215 , -100.6032)
        m1.moveServo(11 , int(poseList[0]) , 500)
        m1.moveServo(12 , int(poseList[1]) , 500)
        m1.moveServo(2  , int(poseList[2]) , 500)
        print(poseList)
        sleep(2.0)
        poseList = Leg1.step(182.6032 , 173.215 , -100.6032)
        m1.moveServo(11 , int(poseList[0]) , 500)
        m1.moveServo(12 , int(poseList[1]) , 500)
        m1.moveServo(2  , int(poseList[2]) , 500)
        print(poseList)
        sleep(2.0)
    
    
    
    
        poseList = Leg1.step(182.6032 , 173.215 , 182.6032)
        m1.moveServo(11 , int(poseList[0]) , 100)
        m1.moveServo(12 , int(poseList[1]) , 100)
        m1.moveServo(2  , int(poseList[2]) , 100)
        print(poseList)
        sleep(2.0)
        
        poseList = Leg1.step(182.6032 , 173.215 , 222.6032)
        m1.moveServo(11 , int(poseList[0]) , 100)
        m1.moveServo(12 , int(poseList[1]) , 100)
        m1.moveServo(2  , int(poseList[2]) , 100)
        print(poseList)
        sleep(2.0)
        
        poseList = Leg1.step(222.6032 , 173.215 , 182.6032)
        m1.moveServo(11 , int(poseList[0]) , 100)
        m1.moveServo(12 , int(poseList[1]) , 100)
        m1.moveServo(2  , int(poseList[2]) , 100)
        print(poseList)
        sleep(2.0)
        
        poseList = Leg1.step(182.6032 , 130.215 , 222.6032)
        m1.moveServo(11 , int(poseList[0]) , 100)
        m1.moveServo(12 , int(poseList[1]) , 100)
        m1.moveServo(2  , int(poseList[2]) , 100)
        print(poseList)
        sleep(2.0)
    
    pass









