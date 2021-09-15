 #!/usr/bin/env python
import numpy as np
import rospy 
from task_three.msg import model_inp 
from task_three.msg import model_out

from time import sleep

class ref_cfg_model:
    def __init__(self,params,publisher):
        self.params= params
        self.pub  = publisher
        self.state = np.array([0,0,0,0], dtype='f') #State is [x,y,theta,headingAngle]
        self.x,self.y =[],[]
        
    def newState(self,model_inp):
        x_dot = model_inp.v*np.cos(self.state[2]+self.state[3])
        y_dot = model_inp.v*np.sin(self.state[2]+self.state[3])
        heading_angle = np.arctan(self.params['lr']*np.tan(model_inp.ster)/self.params['l'])
        theta_dot = model_inp.v*np.tan(model_inp.ster)*np.cos(heading_angle)/self.params['l']
        return np.array([x_dot,y_dot,theta_dot,heading_angle])
    
    def curState_and_pub(self,model_inp):
        cur_state = self.state + self.newState(model_inp)*self.params['delta']
        #To limit angle between pi and and -pi
        cur_state[2] = np.arctan2(np.sin(cur_state[2] ), np.cos(cur_state[2] ))
        self.state = cur_state
        self.pub.publish(model_out(self.state[0],self.state[1],self.state[2],model_inp.v))
        rospy.loginfo(self.state.tolist())
        
    
    
class ref_rear_model:
    def __init__(self,params,publisher):
        self.params= params
        self.pub  = publisher
        self.state = np.array([0,0,0], dtype='f') #State is [x,y,theta]
        self.x,self.y =[],[]
        
    def newState(self,model_inp):
        x_dot = model_inp.v*np.cos(self.state[2])
        y_dot = model_inp.v*np.sin(self.state[2])
        theta_dot = model_inp.v*np.tan(model_inp.ster)/self.params['l']
        return np.array([x_dot,y_dot,theta_dot])
    
    def curState_and_pub(self,model_inp):
        cur_state = self.state + self.newState(model_inp)*self.params['delta']
        #To limit angle between 0 and 360 and -1 turns to 359
        #cur_state[2] = (cur_state[2]+360)%360 
        cur_state[2] = np.arctan2(np.sin(cur_state[2] ), np.cos(cur_state[2] ))
        self.state = cur_state
        
        self.pub.publish(model_out(self.state[0],self.state[1],self.state[2],model_inp.v))
        rospy.loginfo(self.state.tolist())
        
    
    



    
    
def main():
    params = {
        "delta":0.5,
         "l" : 2,
         "lr":1,
         "refrencePoint" : "rear"
        } 
    rospy.init_node("simulation")
    pub = rospy.Publisher("states",model_out,queue_size=10)
    myModel = None
    if params["refrencePoint"] == "rear":
        myModel = ref_rear_model(params,pub)
    elif params["refrencePoint"] == "cfg" :
        myModel = ref_cfg_model(params,pub)

    sleep(params['delta'])
    myModel.curState_and_pub(model_inp(0,0))
    rospy.Subscriber("simulation_inputs",model_inp,myModel.curState_and_pub)
    rospy.spin()
    
if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass