# ECE470_Project (The Ping-Pong Catcher)
 
In this project, we are going to build a ping-pong catcher with UR3. We will incorporate some machine learning and inverse kinematics to achieve our goals. More specific details will be updated later here.

## Installation & Setup
```sh
git clone https://github.com/sean94011/ECE470_Project.git

cd catkin_final_project/src

catkin_init_workspace

cd..

catkin_make
```

## Run the Project
```sh
cd catkin_final_project

source devel/setup.bash

catkin_make

roslaunch ur3_driver ur3_gazebo.launch
```
* Now open another new command prompt with "crtl+shift+N"
```sh
cd catkin_final_project/src/projectandDriver/project_py/scripts/

chmod +x project_exec.py

rosrun final_project fp_exec.py --simulator True
```
