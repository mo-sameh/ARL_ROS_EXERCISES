 #!/usr/bin/env python
import rospy
from std_msgs.msg import String
import sys
def driver(name, age, height):
    rospy.init_node("user_info_driver")
    pub = rospy.Publisher("raw_data",String,queue_size=10)
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        msg = String("name: {}, age: {}, heigh: {}".format(name,str(age),str(height)))
        pub.publish(msg)
        rospy.loginfo(msg)
        rate.sleep()
if __name__ == '__main__':
    try:
        if len(sys.argv) < 4 :
            print("usge : user_driver_info_b.py name age height")
        else:
            driver(sys.argv[1],sys.argv[2],sys.argv[3])
    except rospy.ROSInterruptException:
        pass