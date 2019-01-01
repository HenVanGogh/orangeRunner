'''
Created on Nov 26, 2018

@author: Mic
'''
import serial
import time
class comm(object):
    '''
    classdocs
    '''
    

    def __init__(self,baundRate = 115200 ,name = 'COM8'):
        self.ser = serial.Serial(name, baundRate, timeout=0, parity=serial.PARITY_EVEN, rtscts=1)
        self.ser.open()
        
        
        
    def sendRaw(self , message , Lenght):
        key = bytes([  0x00, 0x00, 0x00, 0x00, 0x00
                     , 0x00, 0x00, 0x00, 0x00, 0x00
                     , 0x00, 0x00, 0x00, 0x00, 0x00
                     , 0x00, 0x00, 0x00, 0x00, 0x00
                     , 0x00, 0x00, 0x00, 0x00, 0x00
                     , 0x00, 0x00, 0x00, 0x00, 0x00
                     , 0x00, 0x00, 0x00, 0x00, 0x00
                     , 0x00, 0x00, 0x00, 0x00, 0x00
                     , 0x00, 0x00, 0x00, 0x00, 0x00
                     , 0x00, 0x00, 0x00, 0x00, 0x00
                     , 0x00, 0x00, 0x00, 0x00, 0x00
                     , 0x00, 0x00, 0x00, 0x00, 0x00])
        message = str(message)
        n = 0
        while(Lenght != n):
            for i in message:
                key[n] = i
                n = n + 1
            
        self.ser.write(key)
        
        
    def send(self , ID , cmd , lenght , *elements):
        n = 0
        
        
        
        message = [0] * (len + 6)
        
        message[0] = 0x55
        message[1] = 0x55
        message[2] = ID
        message[3] = lenght + 3
        message[4] = cmd
        
        chcecksum = message[2] + message[3] + message[4]
        
        for i in elements:
            message[5 + n] = i
            chcecksum = chcecksum + i
            n = n + 1
            
        
        
        
        
        
        
    def recv_raw(self , timeout):
        starttime  = int(round(time.time() * 1000))
        
        while(int(round(time.time() * 1000)) - starttime < timeout):
            
            if(self.ser.available()):
                self.messageReceived = self.ser.read(size=1)
                
                    
    def recv(self):
        n = 0
        i = 0
        len = 0
        
        self.ser.reset_input_buffer()
        
        while(1):
            self.recv_raw(5)
                    
            n = n + 1
            
            if(i >= 3):
                self.data[n-3] = self.messageReceived
                    
            if(i == 2):
                len = self.messageReceived[n] + 3
                i = 3
            
            if(self.messageReceived == 0x55):
                i = i + 1
                
            if(len == n):
                break
        
        for i in self.messageReceived:
            print(i)
        
        
        
        
        
        
        
            