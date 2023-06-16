# Mobile Robot Navigation with Deep Reinforcement Learning
Autonomous Movement with Deep Reinforcement Learning in Mobile Robots

Derin Pekiştirmeli Öğrenme ile Mobil Robotlarda Otonom Hareket

Bu çalışma da, Derin Pekiştirmeli Öğrenme (DQN) ile mobil robotlarda otonom hareket planlaması ele alınmaktadır.
<h3>Kullanılan Araçlar:</h3>
<ul>
  <li>Ubuntu 18.04 LTS</li>
  <li>Anaconda python 2.7</li>
  <li>catkin-pkg 0.5.2 (for ROS)</li>
  <li>tensorflow 1.15.0</li>
  <li>keras 2.2.4</li>
  <li>numpy 1.16.5</li>
  <li>pyqt 5.9.2</li>
  <li>ROS Melodic</li>
  <li>Gazebo</li>
  <li>TurtleBot3 Package</li>
  <li>Pekiştirmeli Öğrenme ROS&Gazebo çerçevesi için "<a href="">ROBOTIS Official GitHub</a>" teşekkürler</li>
</ul>
<h3>Ros Kurulumu:</h3>
<p>sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'</p>
<p>sudo apt install curl</p>
<p>curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -</p>
<p>sudo apt update</p>
<p>sudo apt install ros-melodic-desktop-full</p>
<br>
<p><b>Her yeni kabuk başlatıldığında, ROS ortam değişkenlerinin bash oturumunuza otomatik olarak eklenmesi için</b></p>
<p>echo "source /opt/ros/melodic/setup.bash" >> ~/.bashrc</p>
<p>source ~/.bashrc</p>
<br>
<p><b>Bağımlıklları kurun</b></p>
<p>sudo apt install python-rosdep python-rosinstall python-rosinstall-generator python-wstool build-essential</p>
<p>sudo apt install python-rosdep</p>
<p>sudo rosdep init</p>
<p>rosdep update</p>
<h3>TurtleBot3 Paketlerini Kurun</h3>
<p>$ sudo apt-get install ros-melodic-turtlebot3-msgs</p>
<p>$ sudo apt-get install ros-melodic-turtlebot3</p>
<p>$ echo "export TURTLEBOT3_MODEL=burger" >> ~/.bashrc</p>
<p>mkdir -p ~/catkin_ws/src</p>
<p>cd ~/catkin_ws/src/</p>
<p>
  $ git clone -b melodic-devel https://github.com/ROBOTIS-GIT/DynamixelSDK.git<br>
  $ git clone -b melodic-devel https://github.com/ROBOTIS-GIT/turtlebot3_msgs.git<br>
  $ git clone -b melodic-devel https://github.com/ROBOTIS-GIT/turtlebot3.git<br>
  $ cd ~/catkin_ws && catkin_make<br>
  $ echo "source ~/catkin_ws/devel/setup.bash" >> ~/.bashrc
</p>



