 #!/usr/bin/env python
import rospy
import re
from std_msgs.msg import String,Int64 
from exercise_three.msg import UserInfo

name,age,height = None,None,None 
pub= None
def callBack(msg):
    global name,age,height #Just in case we needed to use these values in the rest of the scirpt
    global pub
    Data = msg.data
    splitted = re.split(": |, ",Data)
    name = splitted[1]
    age = int(splitted[3])
    height = float(splitted[-1])
    pub.publish(UserInfo(name,age,height))
    
def main ():
    global pub
    rospy.init_node("data_processsing")
    rospy.Subscriber("raw_data",String,callBack)
    pub = rospy.Publisher("user_info",UserInfo,queue_size=10)

    rospy.spin()
    
if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass