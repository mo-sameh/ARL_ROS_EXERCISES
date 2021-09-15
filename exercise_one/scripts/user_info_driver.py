 #!/usr/bin/env python
import rospy
from std_msgs.msg import String

def driver():
    rospy.init_node("user_info_driver")
    pub = rospy.Publisher("raw_data",String,queue_size=10)
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        msg = String("name: Rose, age: 20, heigh: 170")
        pub.publish(msg)
        rospy.loginfo(msg)
        rate.sleep()
if __name__ == '__main__':
    try:
        driver()
    except rospy.ROSInterruptException:
        pass