 #!/usr/bin/env python
import rospy
import re
from std_msgs.msg import String 

name,age,height = None,None,None 
def callBack(msg):
    global name
    global age
    global height
    Data = msg.data
    splitted = re.split(": |, ",Data)
    name = splitted[1]
    age = splitted[3]
    height = splitted[-1]
    rospy.loginfo("Name:" + name)
    rospy.loginfo("Age:" + age)
    rospy.loginfo("Height:" + height)
    
def main ():
    rospy.init_node("data_processsing")
    rospy.Subscriber("raw_data",String,callBack)
    rospy.spin()
    
if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass