 #!/usr/bin/env python
import rospy
import re
from std_msgs.msg import String,Int64 

name,age,height = None,None,None 
pubName,pubAge,pubHeight = None,None,None
def callBack(msg):
    global name,age,height #Just in case we needed to use these values in the rest of the scirpt
    global pubName,pubAge,pubHeight 
    Data = msg.data
    splitted = re.split(": |, ",Data)
    name = splitted[1]
    age = int(splitted[3])
    height = float(splitted[-1])
    pubName.publish(String(name))
    pubAge.publish(Int64(int(age)))
    pubHeight.publish(Int64(int(height)))
    
def main ():
    global pubName,pubAge,pubHeight 
    rospy.init_node("data_processsing")
    rospy.Subscriber("raw_data",String,callBack)
    pubName = rospy.Publisher("name",String,queue_size=10)
    pubAge = rospy.Publisher("age",Int64,queue_size=10)
    pubHeight = rospy.Publisher("height",Int64,queue_size=10)
    rospy.spin()
    
if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass