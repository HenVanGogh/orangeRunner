'''
Created on Dec 17, 2018

@author: Mic
'''

import serial
import struct
from time import sleep
import time
#from adodbapi.examples.xls_write import data

class gyro(object):
    '''
    classdocs
    '''


    def __init__(self,Port="COM6",Baudrate=1000000, Timeout= 0.001):
        self.serial = serial.Serial(Port,baudrate=Baudrate,timeout=Timeout)
        #self.serial.setDTR(1)
        #self.TX_DELAY_TIME = 0.000001
    
                
                
    def receivePacket(self):
        self.serial.flushInput()
        for i in range(0 , 9):
            data = self.serial.read()
            #print(data)
            if(data == b'm'):  
                parsed = 0
                data = self.serial.read(8)
                #print(data)
                if(data != None):
                    parsed = struct.unpack('<ff' , data)
                    return parsed
                
            if(data == b'r'):  
                parsed = 0
                while(self.serial.in_waiting < 2):
                    pass
                data = self.serial.read(2)
                #print(data)
                if(data != None):
                    parsed = struct.unpack('<h' , data)
                    return parsed
                
    
                
            
    def testSpeed(self):      
        n = 0
        someTime = time.time()
        while True:
            if(time.time() - someTime < 1):
            
                gyro.receivePacket_float()
                n += 1
                
            else:
                someTime = time.time()
                print(n)
                n = 0
            
            
            
            
        '''
            command = self.serial.read(1)
            if(command == 'm'):
                if(self.serial.inWaiting() > 7):
                    package = self.serial.readline()
                    print(package)
                    parsed = struct.unpack('<ff' , package)
                    return parsed
        '''
                
            
    
if __name__ == '__main__':
    gyro = gyro()

    while True:
        data = gyro.receivePacket()
        if(data != None):
            print(data)

        
        
        
        
        
        