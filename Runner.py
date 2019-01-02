import math
from simple_pid import PID

'''
Created on Nov 25, 2018

@author: Mic
'''

class Runner(object):


    def __init__(self, constant1 , constant2 , constant3):
        

        self.constant1 = constant1
        self.constant2 = constant2
        self.constant3 = constant3
                                          
        
       
    def step(self , X , Y , Z):
        L0 = 56
        L1 = 202.240
        L2 = 173.215
        
        radian = 57.2958;
        
        sqrtZX = (Z*Z) + (X*X)
        T1 = math.atan (Z/X);
        
        X0 = math.sin(T1) * L0
        Z0 = math.cos(T1) * L0     
        X = X - X0
        Z = Z - Z0
        L5 = math.sqrt(sqrtZX);
        L4 = math.sqrt((Y*Y) + (L5*L5));
        K1 = math.acos(L5/L4);
        PowL2L4 = ((L2*L2)+(L4*L4));
        PowL1 = L1*L1;
        subL2L4L1 = PowL2L4 - PowL1;
        K2 = math.acos(subL2L4L1 /(2*L4*L2));
        K3 = K1+K2;
        K5 = math.acos(((L1*L1)+ (L2*L2)- (L4*L4))/(2*L1*L2))
        K6 = K3
        T2 = 3.14159-(K5+ K6)
        T3 = 3.14159- K5
        
        TD1 = T1*radian*4.166
        TD2 = T2*radian*4.166
        TD3 = T3*radian*4.166
        
        self.pos = [None] * 3
        self.pos[0] = self.constant1 + TD1
        self.pos[1] = self.constant2 + TD2
        self.pos[2] = self.constant3 + TD3

        return self.pos
     
        
if __name__ == '__main__':
    m1 = Runner(100 , 100 , 100)
    print(m1.step(100, 100, 100))
  
         
         
         
         