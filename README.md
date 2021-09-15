# ARL_workshop

This is the current src folder for the ROS workspace. It contains 5 different packages.

# Ros mini-project

Exercise_one, exercise_two, exercise_three, are the three tasks for the ROS module.

# Navigation mini-project

The package named task-three contains 5 python files:
1. Kinematic model is an implementation for the bicycle kinematic model for both(Rear-axile and CFG refrence points), which is currently used for simulation. 
2. Path_generation is responsible for generating a simple path described by the following function (y = 2*sin(0.1*x)*exp(0.01*x)),
also it is resbonsible for determining the lookahead point based on the current position and propgate the lookahead point to the pure pursuit controller.
3. Pure_pursuit_controller is an implementation of the pure pursuit for controlling the stering angle.(currently the velocity is constant)
4. Plotter is just a simple node to visualize the target trajectory and the actual one, it saves an image file in directory ws/image_name.

# Control and simulation loop architecture
![alt text](https://github.com/mo-sameh/ARL_workshop/blob/master/imgs/arch.png)


# Results 
The following graph shows the target trajectory and how the pure pursuit controller performed with sharp curves.
![alt text](https://github.com/mo-sameh/ARL_workshop/blob/master/imgs/test.png)
