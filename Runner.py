import math
from simple_pid import PID

from ikpy.chain import Chain
from ikpy.link import OriginLink, URDFLink
'''
armChain = Chain(name='armChain', links=[
    OriginLink(),
    URDFLink(
      name="Leg0",
      translation_vector=[0, 0, 0],
      orientation=[0, 0, 0],
      rotation=[0, 0, 1],
    ),
    URDFLink(
      name="Leg1",
      translation_vector=[10, 0, 0],
      orientation=[0, 0, 0],
      rotation=[0, 1, 0],
    ),
    URDFLink(
      name="Leg2",
      translation_vector=[20, 0, 0],
      orientation=[0, 1.5707, 0],
      rotation=[0, 1, 0],
    )
])
'''
'''
Created on Nov 25, 2018

@author: Mic
'''

class Runner(object):


    def __init__(self, constant1 , constant2 , constant3):
        
        
        #pid = PID(Pval, Ival, Dval, setpoint=1)
        #pid.output_limits = (0, 30000) 
        
        
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
     
     
        
     
        
    def update(self , position1 , position2 , position3):  
        
        self.pid1.setpoint = self.pos[0]
        self.pid2.setpoint = self.pos[1]
        self.pid3.setpoint = self.pos[2]
        
        
        control = []  
        control[0] = self.pid1(position1)
        control[1] = self.pid2(position2)
        control[2] = self.pid3(position3)
        return control
        
        
if __name__ == '__main__':
    m1 = Runner(100 , 100 , 100)
    print(m1.step(100, 100, 100))
  
         
         
         
         