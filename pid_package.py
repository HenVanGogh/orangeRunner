
from simple_pid import PID

class pid_package(object):
    
    
    def __init__(self):
        pass
    
    
    
    def __call__(self):
        pass
    
    
    def keepSafe(self):
        pass
       ''' lenght = 3000
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
        plt.show()'''