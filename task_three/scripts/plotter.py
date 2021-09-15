
 #!/usr/bin/env python
 
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import rospy 
from task_three.msg import curState_and_target

fig = plt.figure()
ax = fig.add_subplot(111)


i = 0
xs = []
ys = []
tx = []
ty = []
time = []

#def callback0(msg):

def plot(msg):
    global i
    time.append(i)
    xs.append(msg.x)
    ys.append(msg.y)
    tx.append(msg.tx)
    ty.append(msg.ty)
    ax.plot(xs, ys)
    ax.plot(tx, ty)
    plt.legend(["cur", "target"])
    ax.set_xlim(left= max(0, i-50), right= i+50)
    plt.draw()
    plt.pause(0.05) 
    i += 1
    plt.savefig('test.png')

if __name__ == '__main__':
    rospy.init_node('plotter' ,anonymous=True)

    rospy.Subscriber('targets', curState_and_target, plot)
    rospy.spin()