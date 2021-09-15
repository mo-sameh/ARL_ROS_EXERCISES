 #!/usr/bin/env python

import numpy as np
import rospy 

from task_three.msg import curState_and_target
from task_three.msg import model_out
path = []
k = 1
lfc = 3.0
no_points = 100
delta = 0.05
def generate_sample_path():
    for i in np.linspace(0,no_points,1000):
        y = 2*np.sin(0.1*i)*np.exp(0.01*i)
        path.append(np.array([i,y]))

    
        
def getDistance(p1,p2):
    return np.hypot(p1[0]-p2[0],p1[1]-p2[1])

def getNearestIdx(p):
    temp = path - p
    dis = np.hypot(temp[:,0],temp[:,1])
    return np.argmin(dis)
    
        
def get_lookahead(cur,ld):
    idx = getNearestIdx(cur)
    
    while ld > getDistance(path[idx],cur):
        
        if idx +1 >=len(path):
            break
        idx = idx+1
    return path[idx]

#Initial_state
cur_target = curState_and_target(0,0,0,0,0,0)
def lookahead_callback(msg):
    global cur_target
    state = np.array([msg.x,msg.y])
    ld = msg.v * k + lfc
    lookahead = get_lookahead(state,ld)
    cur_target = curState_and_target(msg.x,msg.y,msg.theta,lookahead[0],lookahead[1],5)
    
def main():
    global cur_target
    generate_sample_path()
    rospy.init_node("path_generation")
    pub = rospy.Publisher("targets",curState_and_target,queue_size=10)
    rospy.Subscriber("states",model_out,lookahead_callback)
    rate = rospy.Rate(0.5)
    while not rospy.is_shutdown():
        pub.publish(cur_target)
        rate.sleep()

    
    
    
if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass