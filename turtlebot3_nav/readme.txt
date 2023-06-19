conda activate py27
rosclean purge
roslaunch turtlebot3_nav stage.launch
conda env list
roslaunch turtlebot3_nav dqn_train.launch
roslaunch turtlebot3_nav result_graph.launch



